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
from markdownfeeds.Generators.Json.Models.Author import Author
from markdownfeeds.Generators.Json.Models.JsonFeedItem import JsonFeedItem
from markdownfeeds.MarkdownFile import MarkdownFile

from src.feeds import BaseJsonFeed, Filters


class ResearchPaperFeed(BaseJsonFeed):
    """
    Class builds a feed for research paper collection files.
    """

    def _check_feed_items(
        self,
        feed_items: [FeedItem]
    ):
        super()._check_feed_items(feed_items)
        BaseJsonFeed._check_for_duplicates(feed_items, 'external_url')

    def _inject_feed_item_details(
            self, feed_item: JsonFeedItem, markdown_file: MarkdownFile) -> JsonFeedItem:
        """
        Inject any additional feed item details.
        """
        feed_item = self._inject_authors_into_featured(feed_item)
        return super()._inject_feed_item_details(feed_item, markdown_file)

    def _sort_feed_items(
            self, feed_items: [FeedItem]) -> [FeedItem]:
        """
        Sort by name.
        """
        feed_items.sort(key=lambda feed_item: feed_item.get('date_published'), reverse=True)
        return feed_items

    @staticmethod
    def _inject_authors_into_featured(
        feed_item: JsonFeedItem
    ) -> JsonFeedItem:
        """
        This function replaces any "authors" list items that reference a contributor using their username with
        their contributor profile.
        """
        if not feed_item.has('authors'):
            return feed_item

        authors = feed_item.get('authors')
        for key, value in enumerate(authors):
            author = Author()
            author.inject_dict(value)
            authors[key] = author

        feed_item.set('authors', authors)
        return feed_item

    def _generate_filters(
        self,
        feed_items: [JsonFeedItem]
    ) -> Filters:
        filters = Filters(1)

        for feed_item in feed_items:
            if feed_item.has_value('tags'):
                [filters.add_filter('tags', tag) for tag in feed_item.get('tags')]

            filters.add_filter('year', feed_item.markdown_file.date.year)

        return filters
