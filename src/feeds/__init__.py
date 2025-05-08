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
import os
import re

from markdownfeeds.Generators import GeneratorSettings
from markdownfeeds.Generators.Default.Models.Feed import Feed
from markdownfeeds.Generators.Default.Models.FeedItem import FeedItem
from markdownfeeds.Generators.Json.JsonFeedGenerator import JsonFeedGenerator
from markdownfeeds.Generators.Json.Models.JsonFeed import JsonFeed
from markdownfeeds.Generators.Json.Models.JsonFeedItem import JsonFeedItem
from markdownfeeds.MarkdownFile import MarkdownFile

from src import get_collection_path
from src.feeds.contributors import get_contributor_as_author


class Filters:
    """
    Class that represents filters to provided in the JSON feed. This allows feed consumers to know what values within
    each feed item can be filtered based on a series of values.
    """

    def __init__(
        self,
        min_occurrence: int = 2
    ):
        self.filters = {}
        self.min_occurrence = min_occurrence

    def set_min_occurrence(
        self,
        value: int
    ):
        self.min_occurrence = value

    def add_filter(
        self,
        group: str,
        value: any
    ):
        value = str(value)

        if len(value) == 0:
            logging.warning(f'Skipping adding filter "{group}" as it has no value.')
            return

        if group not in self.filters:
            self.filters[group] = {}

        if value in self.filters[group]:
            self.filters[group][value] = self.filters[group][value] + 1
        else:
            self.filters[group][value] = 1

    def collect(
        self
    ):
        found_filters = {}

        for group in self.filters:
            found_filters[group] = list({
                k: v for k, v in self.filters[group].items() if v >= self.min_occurrence
            })

        return found_filters


class BaseJsonFeed(JsonFeedGenerator):
    """
    Class is base class for all our collection JSON feeds. Provides handy functionality such as author injection,
    converting relative asset paths to absolute etc.
    """

    def __init__(
        self,
        args: any,
        collection_dir_name: str | None = None,
        target_directory: str | None = None,
        title: str | None = None
    ):
        """
        Constructor.
        """
        if not collection_dir_name:
            collection_dir_name = 'news'  # This will not be used, it's just to pass exists validation

        if not target_directory:
            target_directory = f'feed/{collection_dir_name}'

        if not title:
            title = f'{collection_dir_name.replace("_", " ").title()} Feed'

        JsonFeedGenerator.__init__(
            self,
            JsonFeed(title=title),
            GeneratorSettings(
                source_directory=get_collection_path(collection_dir_name),
                target_directory=target_directory,
                feed_items_per_export=args.items_per_feed_page,
                feed_base_url=f'{args.feed_base_url}/{collection_dir_name}',
                assets_base_url=args.asset_base_url,
                skip_files=['README.md']
            )
        )

    def _generate_filters(
        self,
        feed_items: [JsonFeedItem]
    ) -> Filters:
        """
        Override to provide custom filters.
        """
        return Filters()

    def _inject_feed_item_details(
        self,
        feed_item: JsonFeedItem,
        markdown_file: MarkdownFile
    ) -> JsonFeedItem:
        """
        Base feed generator.
        """
        if feed_item.has_value('contributor'):
            feed_item.set(
                'author', get_contributor_as_author(feed_item.get('contributor')))

            feed_item.remove('contributor')

        if feed_item.has_value('date'):
            feed_item.replace('date', 'date_published')

        return feed_item

    def _replace_asset_paths_in_string(
        self,
        input_string: str
    ) -> str:
        """
        Replace relative asset paths in a string with and absolute version.
        """
        asset_base_url = self.generator_settings.get('assets_base_url') \
            if self.generator_settings.has('assets_base_url') else ''

        if '../static/' in input_string:
            return re.sub(r"[./]+/static/", f'{asset_base_url.rstrip("/")}/', input_string)

        return input_string

    def _verify_asset_exists(
        self,
        feed_item: FeedItem,
        asset_path: str
    ):
        """
        Ensure an asset path exists, relative to the markdown file its referenced from.
        """
        asset_image_path = os.path.abspath(
            os.path.join(
                os.path.dirname(feed_item.markdown_file.file_path), asset_path))

        if not os.path.exists(asset_image_path):
            raise ValueError(f'Asset for feed item "{feed_item.markdown_file.file_path}" does not exist.')

    async def _export_feed(
        self,
        feed: Feed
    ):
        feed.set('filters', self._generate_filters(feed.items).collect())
        await super()._export_feed(feed)

    def _dump_feed(self, feed: Feed):
        """
        Dump a feed, replacing relative asset paths.
        """
        return self._replace_asset_paths_in_string(
            json.dumps(
                feed.dump(), indent=JsonFeedGenerator.JSON_INDENTATION))

    @staticmethod
    def _check_for_duplicates(
        feed_items: [FeedItem],
        feed_item_key: str
    ):
        """
        This function attempts to check for duplicates within the feed_item list using a specific key.
        """
        duplicate_tracker = {}

        for feed_item in feed_items:
            if feed_item.get(feed_item_key) in duplicate_tracker:
                raise ValueError(
                    f'The feed item "{feed_item}" is attempting to set an value for "{feed_item_key} that is '
                    f'already used by "{duplicate_tracker[feed_item.get(feed_item_key)]}".')
            else:
                duplicate_tracker[feed_item.get(feed_item_key)] = feed_item
