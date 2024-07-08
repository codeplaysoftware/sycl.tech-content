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

import logging

from markdownfeeds.Generators.Json.Models.JsonFeedItem import JsonFeedItem
from markdownfeeds.MarkdownFile import MarkdownFile

from src.feeds import BaseJsonFeed
from src.feeds.contributors import get_contributor_as_author


class ContributorFeed(BaseJsonFeed):
    """
    Class builds a feed for contributor collection files.
    """

    def process_markdown_file_to_feed_item(
        self,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        """
        Convert a markdown file to a feed item.
        """
        logging.info(f'Successfully converted markdown file "{markdown_file}" to feed item.')
        return get_contributor_as_author(None, markdown_file)

    def _sort_feed_items(
        self,
        feed_items: [JsonFeedItem]
    ) -> [JsonFeedItem]:
        """
        Sort by name.
        """
        feed_items.sort(key=lambda feed_item: feed_item.get('name'))
        return feed_items
