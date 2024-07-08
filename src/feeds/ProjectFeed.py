#
#   Copyright (C) Codeplay Software Limited.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use these files except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   For your convenience, a copy of the License has been included in this
#   repository.
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

import json
import logging
import time
from urllib.parse import urlparse

from markdownfeeds.Generators.Default.Models.FeedItem import FeedItem
from markdownfeeds.Generators.Json.Models.JsonFeedItem import JsonFeedItem
from markdownfeeds.MarkdownFile import MarkdownFile

from src import similar, safe_read_from_url
from src.feeds import BaseJsonFeed, Filters


class ProjectFeed(BaseJsonFeed):
    """
    Class builds a feed for project collection files.
    """

    # To avoid throttling, we will use API key which has a pretty flexible rate limit
    GITHUB_API_KEY = None

    # We will try and guess the best category based on tags
    CATEGORIES = {
        'Animation':
            ['blender', '3dmax'],
        'Neural Networks':
            ['deep', 'learning', 'neural', 'tensorflow'],
        'Library':
            ['libraries', 'lib', 'library'],
        'Benchmarks':
            ['benchmark', 'profiling', 'performance'],
        'Mathematical':
            ['math', 'mathematical', 'eigen'],
        'Graphics':
            ['opengl', 'directx', 'opencl'],
        'Image Processing':
            ['image', 'gfx'],
        'ROCm':
            ['rocm'],
        'CUDA&reg;':
            ['cuda'],
        'Simulators':
            ['simulators', 'simulations', 'simulation'],
        'Science':
            ['physics', 'chemistry'],
        'Hashing Libraries':
            ['sha1', 'sha224', 'sha256', 'sha3', 'sha3-256', 'sha3-512', 'sha384', 'sha512',
             'sha512-224', 'sha512-256'],
        'oneAPI&trade;':
            ['oneapi', 'dpc++', 'dpcpp', 'icx'],
        'hipSYCL':
            ['hipsycl', 'hip'],
        'C++':
            ['cpp', 'c++'],
    }

    def _check_feed_items(
        self,
        feed_items: [FeedItem]
    ):
        super()._check_feed_items(feed_items)
        BaseJsonFeed._check_for_duplicates(feed_items, 'external_url')

    def _sort_feed_items(
            self, feed_items: [FeedItem]) -> [FeedItem]:
        """
        Sort by name.
        """
        feed_items.sort(key=lambda feed_item: feed_item.get('date_published'), reverse=True)
        return feed_items

    def _inject_feed_item_details(
        self,
        feed_item: JsonFeedItem,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        """
        Inject any additional feed item details.
        """
        feed_item = self._inject_repository_information(feed_item, markdown_file)
        feed_item = self.__inject_categories(feed_item)

        return super()._inject_feed_item_details(feed_item, markdown_file)

    def _inject_repository_information(
        self,
        json_feed_item: JsonFeedItem,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        """
        Using GitHub, GitLab, Other APIs, load in more useful repository information.
        """
        if 'github.com' in markdown_file.front_matter['external_url']:
            return self._inject_github_repository_information(
                json_feed_item, markdown_file)
        elif 'gitlab_project_id' in markdown_file.front_matter:
            return self._inject_gitlab_repository_information(
                json_feed_item, markdown_file)

        return json_feed_item

    def _inject_github_repository_information(
        self,
        json_feed_item: JsonFeedItem,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        """
        Load in GitHub repository information.
        """
        repo_details = {}

        api_base_url = self.to_github_api_url(markdown_file.front_matter['external_url'])

        # Slow things down a bit to avoid being throttled by GitHub's API
        time.sleep(1)

        logging.info(f'Loading GitHub.com repo data from URL "{api_base_url}"...')

        # Load the defaults
        api_result = json.loads(
            safe_read_from_url(api_base_url, ProjectFeed.GITHUB_API_KEY).content)

        repo_details['stars'] = api_result['stargazers_count']
        repo_details['forks'] = api_result['forks']
        repo_details['clone_url'] = api_result['clone_url']
        repo_details['owner'] = {
            'name': api_result['owner']['login'],
            'avatar': api_result['owner']['avatar_url'],
            'url': api_result['owner']['html_url'],
        }

        # Load contributor information
        api_result = safe_read_from_url(api_base_url + '/contributors', ProjectFeed.GITHUB_API_KEY)

        contributors = []
        for contributor in json.loads(api_result.content):
            contributors.append({
                'username': contributor['login'],
                'avatar': contributor['avatar_url'],
                'github_url': contributor['html_url'],
            })

            repo_details['contributors'] = contributors

        json_feed_item.set('repo_details', repo_details)
        return json_feed_item

    @staticmethod
    def _inject_gitlab_repository_information(
        json_feed_item: JsonFeedItem,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        """
        Load in Gitlab repository information.
        """
        repo_details = {}

        domain = urlparse(markdown_file.front_matter['external_url']).netloc

        api_base_url = f'https://{domain}/api/v4/projects/{markdown_file.front_matter["gitlab_project_id"]}'

        # Slow things down a bit to avoid being throttled by GitHub's API
        time.sleep(1)

        logging.info(f'Loading Gitlab.com repo data from URL "{api_base_url}"...')

        # Load the repo details
        api_result = json.loads(
            safe_read_from_url(api_base_url).content)

        repo_details['stars'] = api_result['star_count']
        repo_details['forks_count'] = api_result['forks_count']
        repo_details['clone_url'] = api_result['ssh_url_to_repo']
        repo_details['owner'] = {
            'name': api_result['namespace']['name'],
            'avatar': api_result['avatar_url'],
            'url': api_result['namespace']['web_url'],
        }

        repo_details['contributors'] = [{
            'username': api_result['namespace']['name'],
            'avatar': api_result['avatar_url'],
            'github_url': api_result['namespace']['web_url'],
        }]

        json_feed_item.set('repo_details', repo_details)
        return json_feed_item

    def _generate_filters(
        self,
        feed_items: [JsonFeedItem]
    ) -> Filters:
        filters = Filters(1)

        for feed_item in feed_items:
            if feed_item.has_value('categories'):
                [filters.add_filter('categories', category) for category in feed_item.get('categories')]

            if feed_item.has_value('license'):
                filters.add_filter('license', feed_item.get('license'))

            filters.add_filter('year', feed_item.markdown_file.date.year)

        return filters

    @staticmethod
    def __inject_categories(
        feed_item: JsonFeedItem
    ) -> JsonFeedItem:
        if not feed_item.has_value('tags'):
            return feed_item

        matched_categories = ['Miscellaneous']
        for tag in feed_item.get('tags'):
            for tag_group in ProjectFeed.CATEGORIES.items():
                if similar(tag, tag_group[1]) or similar(tag, tag_group[0]):
                    matched_categories.append(tag_group[0])

        feed_item.set('categories', list(set(matched_categories)))
        return feed_item

    @staticmethod
    def to_github_api_url(
        html_url: str
    ):
        """
        Convert a GitHub URL into an GitHub API request url.
        """
        return (
            html_url
            .replace('https://github.com/', 'https://api.github.com/repos/')
            .replace('https://www.github.com/', 'https://api.github.com/repos/')
            .rstrip('/'))
