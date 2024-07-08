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

from markdownfeeds.Generators.Default.Models.FeedItem import FeedItem
from markdownfeeds.Generators.Json.Models.Author import Author
from markdownfeeds.Generators.Json.Models.JsonFeedItem import JsonFeedItem
from markdownfeeds.MarkdownFile import MarkdownFile

from src import safe_read_from_url
from src.feeds import BaseJsonFeed


class ImplementationActivityFeed(BaseJsonFeed):
    """
    Class builds a feed for implementations, pulled from various public repositories.
    """

    ACTIVITY = []
    GITHUB_API_KEY = None

    def __init__(
        self,
        args: any
    ):
        """
        Constructor.
        """
        super().__init__(
            args,
            'news',
            'feed/implementation_activity',
            'Implementation Activity Feed'
        )

    def _inject_feed_item_details(
        self,
        feed_item: JsonFeedItem,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        """
        Inject any additional feed item details.
        """
        feed_item.set('content_html', markdown_file.html)
        return super()._inject_feed_item_details(feed_item, markdown_file)

    def _process_file_path_list(
        self,
        file_paths: list
    ) -> list:
        ImplementationActivityFeed.ACTIVITY += ImplementationActivityFeed.fetch_github_activity(
            'intel', 'llvm', 'sycl')

        ImplementationActivityFeed.ACTIVITY += ImplementationActivityFeed.fetch_github_activity(
            'AdaptiveCpp',
            'AdaptiveCpp',
            'master'
        )

        ImplementationActivityFeed.ACTIVITY += ImplementationActivityFeed.fetch_github_activity(
            'codeplaysoftware',
            'oneapi-construction-kit'
        )

        return [a['url'] for a in ImplementationActivityFeed.ACTIVITY]

    def _sort_feed_items(
        self,
        feed_items: [FeedItem]
    ) -> [FeedItem]:
        """
        Sort by name.
        """
        feed_items.sort(key=lambda feed_item: feed_item.get('date_published'), reverse=True)
        return feed_items

    def _process_file_path_to_markdown_file(
        self,
        file_path: str
    ) -> MarkdownFile:
        """
        Load markdown file contents.
        """
        activity_item = ImplementationActivityFeed.__get_activity_by_id(file_path)

        markdown_file = MarkdownFile()
        markdown_file.front_matter = activity_item
        markdown_file.body = activity_item['title']
        return markdown_file

    @staticmethod
    def fetch_github_activity(
        organization: str,
        repo: str,
        branch: str = 'main',
        max_results: int = 50
    ):
        """
        Fetch commit and release information from the GitHub API.
        """
        commit_data = safe_read_from_url(
            f'https://api.github.com/repos/{organization}/{repo}/commits?sha={branch}',
            ImplementationActivityFeed.GITHUB_API_KEY)

        release_data = safe_read_from_url(
            f'https://api.github.com/repos/{organization}/{repo}/releases',
            ImplementationActivityFeed.GITHUB_API_KEY)

        logging.info(f'Loading GitHub repo data for for "{organization}/{repo}"..')

        activity = []

        # Load commit activity
        for c in json.loads(commit_data.content.decode('utf-8')):
            activity.append({
                'title': f"{c['author']['login']} created a new commit to {repo}.",
                'repository': f'{organization}/{repo}', 'type': 'commit',
                'author': ImplementationActivityFeed.__create_author(c['author']), 'url': c['html_url'],
                'date': c['commit']['author']['date'], }
            )

        # Load releases activity
        for r in json.loads(release_data.content.decode('utf-8')):
            activity.append({
                'title': f"{r['name']} has been released.", 'type': 'release',
                'author': ImplementationActivityFeed.__create_author(r['author']), 'url': r['html_url'],
                'date': r['published_at'], }
            )

        activity.sort(key=lambda a: a['date'], reverse=True)
        return activity[:max_results]

    @staticmethod
    def __create_author(
        values: dict
    ) -> Author:
        """
        Create an author object.
        """
        author = Author()
        author.name = values['login']
        author.avatar = values['avatar_url']
        author.url = values['avatar_url']
        return author

    @staticmethod
    def __get_activity_by_id(
        activity_id: str
    ) -> dict:
        """
        Get a bit of activity by its id (url).
        """
        for a in ImplementationActivityFeed.ACTIVITY:
            if a['url'] == activity_id:
                return a

        raise ValueError(f'No activity item with provided id "{activity_id}" was found.')
