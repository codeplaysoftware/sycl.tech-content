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
import hashlib
import logging

import bs4
from markdownfeeds.Generators.Default.Models.FeedItem import FeedItem
from markdownfeeds.Generators.Json.Models.JsonFeedItem import JsonFeedItem
from markdownfeeds.MarkdownFile import MarkdownFile
from slugify import slugify

from src import safe_read_from_url
from src.feeds import BaseJsonFeed


class AcademyLessonFeed(BaseJsonFeed):
    """
    Class builds a feed for academy lessons, pulled from GitHub.
    """
    ACADEMY_BASE_URL = 'https://github.com/codeplaysoftware/syclacademy/blob/main/'
    ACADEMY_RAW_URL = 'https://raw.githubusercontent.com/codeplaysoftware/syclacademy/main/'
    FOUND_LESSONS = []

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
            'feed/academy_lessons',
            'Academy Lessons Feed'
        )

    def _inject_feed_item_details(
        self,
        feed_item: JsonFeedItem,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        """
        Inject any additional feed item details.
        """
        feed_item.set(
            'tag', slugify(f"{feed_item.get('number')}-{feed_item.title}"))

        feed_item.set(
            'content_html', markdown_file.body)

        return super()._inject_feed_item_details(feed_item, markdown_file)

    def _sort_feed_items(
        self,
        feed_items: [FeedItem]
    ) -> [FeedItem]:
        """
        Sort by name.
        """
        feed_items.sort(key=lambda feed_item: feed_item.get('number'), reverse=False)
        return feed_items

    def _process_file_path_list(
        self,
        file_paths: list
    ) -> list:
        """
        Override this method to find all the lessons we need.
        """
        url_result = safe_read_from_url(
            AcademyLessonFeed.ACADEMY_RAW_URL + '/README.md')

        soup = bs4.BeautifulSoup(
            MarkdownFile.markdown_to_html(
                url_result.content.decode('utf-8')), 'html.parser')

        for tr in soup.find('table').find_all('tr'):
            tds = tr.find_all('td')

            if len(tds) == 0:
                continue

            read_me_link = tds[3].find('a')

            if not read_me_link:
                logging.warning(f'Could not parse lesson from lesson table.')
                continue

            AcademyLessonFeed.FOUND_LESSONS.append({
                'number':
                    int(tds[0].text),
                'title':
                    tds[1].text,
                'url':
                    AcademyLessonFeed.ACADEMY_RAW_URL + str(read_me_link['href']),
                'lesson_home':
                    AcademyLessonFeed.ACADEMY_BASE_URL + str(read_me_link['href']),
            })

        return [u['url'] for u in AcademyLessonFeed.FOUND_LESSONS]

    def _process_file_path_to_markdown_file(
        self,
        file_path: str
    ) -> MarkdownFile:
        """
        Convert a file path to a markdown file.
        """
        markdown_file_path_base = file_path.replace('README.md', '')

        logging.info(f'Loading contents for lesson "{markdown_file_path_base}"..')

        read_me_contents = safe_read_from_url(file_path).content.decode('utf-8')
        source_contents = solution_contents = None

        try:
            source_contents = safe_read_from_url(markdown_file_path_base + 'source.cpp').content.decode('utf-8')
        except ConnectionError:
            logging.warning(f'Could not load source.cpp for lesson {markdown_file_path_base}, skipping it.')

        try:
            solution_contents = safe_read_from_url(markdown_file_path_base + 'solution.cpp').content.decode('utf-8')
        except ConnectionError:
            logging.warning(f'Could not load solution.cpp for lesson {markdown_file_path_base}, skipping it.')

        lesson_info = AcademyLessonFeed.__get_lesson_by_readme_url(file_path)

        markdown_file = MarkdownFile()
        markdown_file.body = read_me_contents
        markdown_file.front_matter['id'] = hashlib.sha1(lesson_info['title'].encode('utf-8')).hexdigest()
        markdown_file.front_matter['title'] = lesson_info['title']
        markdown_file.front_matter['number'] = lesson_info['number']
        markdown_file.front_matter['source'] = source_contents
        markdown_file.front_matter['solution'] = solution_contents
        markdown_file.front_matter['lesson_home'] = lesson_info['lesson_home']
        markdown_file.body = self.__clean_html(markdown_file.html)
        return markdown_file

    @staticmethod
    def __clean_html(
        html: str
    ) -> str:
        """
        Clean up a lesson's HTML as much as possible.
        """
        soup = bs4.BeautifulSoup(html, 'html.parser')

        h1s = soup.find_all('h1')
        h2s = soup.find_all('h2')
        hrs = soup.find_all('hr')

        if len(h2s) > 0:
            h2s[0].decompose()

        if len(h1s) > 0:
            h1s[0].decompose()

        if len(hrs) > 0:
            hrs[0].decompose()

        return str(soup).strip('\n')

    @staticmethod
    def __get_lesson_by_readme_url(
        readme_url: str
    ) -> dict:
        """
        Get a lesson by its README.md URL.
        """
        for x in AcademyLessonFeed.FOUND_LESSONS:
            if x['url'] == readme_url:
                return x

        raise ValueError(f'No lesson with README.md URL "{readme_url}" found.')
