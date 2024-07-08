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

from src.feeds import BaseJsonFeed, get_contributor_as_author


class EventFeed(BaseJsonFeed):
    """
    Class builds a feed for event collection files.
    """

    def _check_feed_item(
        self,
        feed_item: JsonFeedItem
    ):
        """
        Check if a feed item is valid or not.
        """
        super()._check_feed_item(feed_item)

        if feed_item.get('starts') > feed_item.get('ends'):
            raise ValueError(f'Start datetime cannot be greater than end datetime in file {feed_item}.')

    def _inject_feed_item_details(
        self,
        feed_item: JsonFeedItem,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        """
        Inject any additional feed item details.
        """
        if feed_item.has('attendees'):
            attendees = feed_item.get('attendees')
            feed_item.set(
                'attendees', [
                    get_contributor_as_author(attendee) for attendee in attendees
                ])

        feed_item.set(
            'content_html', markdown_file.html)

        return super()._inject_feed_item_details(feed_item, markdown_file)

    def _sort_feed_items(
        self,
        feed_items: [FeedItem]
    ) -> [FeedItem]:
        """
        Sort by name.
        """
        feed_items.sort(key=lambda feed_item: feed_item.get('starts'), reverse=True)
        return feed_items
