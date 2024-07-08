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
import os
import logging
import requests

from markdownfeeds.Generators.Default.Models.FeedItem import FeedItem
from markdownfeeds.Generators.Json.Models.Author import Author
from markdownfeeds.Generators.Json.Models.JsonFeedItem import JsonFeedItem
from markdownfeeds.MarkdownFile import MarkdownFile

from src.feeds import BaseJsonFeed, Filters, get_contributor_as_author


class VideoFeed(BaseJsonFeed):
    """
    Class builds a feed for video collection files.
    """

    def _sort_feed_items(
            self, feed_items: [FeedItem]) -> [FeedItem]:
        """
        Sort by name.
        """
        feed_items.sort(key=lambda feed_item: feed_item.get('date_published'), reverse=True)
        return feed_items

    def _check_feed_items(
        self,
        feed_items: [FeedItem]
    ):
        super()._check_feed_items(feed_items)
        BaseJsonFeed._check_for_duplicates(feed_items, 'external_url')

    def _check_feed_item(
        self,
        feed_item: JsonFeedItem
    ):
        """
        Check if a feed item is valid or not.
        """
        super()._check_feed_item(feed_item)

        if not feed_item.has('image') or feed_item.get('image') is None:
            raise ValueError(f'Missing an image for on news feed item at path "{feed_item}".')

        if not feed_item.has('type'):
            raise ValueError(f'Missing a value for "type" on video feed item at path "{feed_item}".')

    def _inject_feed_item_details(
        self,
        feed_item: JsonFeedItem,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        """
        Inject any additional feed item details.
        """
        feed_item = self._inject_youtube_thumbnail(feed_item)
        feed_item = self._inject_authors_into_featured(feed_item)
        return super()._inject_feed_item_details(feed_item, markdown_file)

    def _inject_authors_into_featured(
        self,
        feed_item: JsonFeedItem
    ) -> JsonFeedItem:
        """
        This function replaces any "featuring" list items that reference a contributor using their username with
        their contributor profile.
        """
        if not feed_item.has('featuring'):
            return feed_item

        featuring = feed_item.get('featuring')
        for key, value in enumerate(featuring):
            if isinstance(value, dict) and 'username' in value:
                featuring[key] = get_contributor_as_author(
                    value['username'])
            else:
                author = Author()
                author.inject_dict(value)
                featuring[key] = author

        feed_item.set('featuring', featuring)
        return feed_item

    @staticmethod
    def _inject_youtube_thumbnail(
        feed_item: JsonFeedItem
    ) -> JsonFeedItem:
        """
        This function injects a thumbnail value for YouTube videos using the YouTube API.
        """
        # Skip if feed item already has an image
        if feed_item.has_value('image'):
            return feed_item

        url = str(feed_item.get('external_url'))

        if 'youtube.com/watch' in url:
            video_id = url.split('?v=')[1].split('&')[0]
            youtube_thumbnail_url = f'https://img.youtube.com/vi/{video_id}/mqdefault.jpg'
            target_directory = os.path.dirname(os.path.join(os.getcwd(), 'static/images/videos/'))
            target_file_name = feed_item.markdown_file.file_name.replace('.md', '.jpg')

            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            target_thumbnail_path = os.path.join(target_directory, target_file_name)

            if os.path.exists(target_thumbnail_path):
                os.unlink(target_thumbnail_path)

            with open(target_thumbnail_path, 'wb') as handler:
                # Don't need to do any status code checking, API will ALWAYS return an image, even if 404 for video
                request = requests.get(youtube_thumbnail_url)

                logging.info(f'Downloaded YouTube thumbnail "{youtube_thumbnail_url}" to {target_thumbnail_path}.')

                handler.write(request.content)

                feed_item.set('image', f'../../../static/images/videos/{target_file_name}')

        return feed_item

    def _generate_filters(
        self,
        feed_items: [JsonFeedItem]
    ) -> Filters:
        filters = Filters()

        for feed_item in feed_items:
            if feed_item.has_value('type'):
                filters.add_filter('type', feed_item.get('type'))

            if feed_item.has_value('tags'):
                [filters.add_filter('tags', tag) for tag in feed_item.get('tags')]

            if feed_item.has_value('featuring'):
                [filters.add_filter('featuring', featured.name) for featured in feed_item.get('featuring')]

            filters.add_filter('year', feed_item.markdown_file.date.year)

        return filters
