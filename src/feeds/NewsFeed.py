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

from markdownfeeds.Generators.Default.Models.FeedItem import FeedItem
from markdownfeeds.Generators.Json.Models.JsonFeedItem import JsonFeedItem
from markdownfeeds.MarkdownFile import MarkdownFile

from slugify import slugify

from src.feeds import BaseJsonFeed


class NewsFeed(BaseJsonFeed):
    """
    Class builds a feed for news collection files.
    """

    def _check_feed_item(
        self,
        feed_item: JsonFeedItem
    ):
        """
        Check if a feed item is valid or not.
        """
        super()._check_feed_item(feed_item)

        if not feed_item.has('image') or feed_item.get('image') is None:
            raise ValueError(f'Missing an image for on news feed item "{feed_item.markdown_file.file_path}".')

    def _inject_feed_item_details(
        self,
        feed_item: JsonFeedItem,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        """
        Inject any additional feed item details.
        """
        feed_item.set(
            'tag', slugify(markdown_file.date.strftime('%Y-%m-%d') + '-' + markdown_file.title))

        feed_item.set(
            'content_html', markdown_file.html)

        feed_item.remove('date')

        return super()._inject_feed_item_details(feed_item, markdown_file)

    def _sort_feed_items(
        self,
        feed_items: [FeedItem]
    ) -> [FeedItem]:
        """
        Sort a list of feed items. Override this to provided custom sorting.
        """
        feed_items.sort(key=lambda feed_item: feed_item.get('date_published'), reverse=True)
        return feed_items
