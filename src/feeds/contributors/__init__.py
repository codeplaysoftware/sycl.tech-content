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

from markdownfeeds.Generators.Default.DefaultFeedGenerator import DefaultFeedGenerator
from markdownfeeds.Generators.Json.Models.Author import Author
from markdownfeeds.MarkdownFile import MarkdownFile

from src import get_collection_path


CACHE: {str: Author} = {}


def get_contributor_as_author(
    username: str | None = None,
    markdown_file: MarkdownFile | None = None
) -> Author:
    """
    Create an author instance from either a markdown file or a username.
    """
    if not username and not markdown_file:
        raise ValueError('You must specify either a username or a markdown file.')

    if not markdown_file:
        markdown_file = get_markdown_file_by_username(username)

    username = os.path.basename(markdown_file.file_path).replace('.md', '')

    if username in CACHE:
        return CACHE[username]

    author = Author()
    author.inject_dict(markdown_file.front_matter)
    author.set('id', markdown_file.id)
    author.set('date_published', markdown_file.date.isoformat() if markdown_file.date else None)
    author.set('summary', markdown_file.summary)
    author.set('username', username)
    author.set('content_html', markdown_file.html)
    author.set('contribution_counts', {
        'events': count_collection_contributions_by_username('events', username),
        'projects': count_collection_contributions_by_username('projects', username),
        'news': count_collection_contributions_by_username('news', username),
        'research_papers': count_collection_contributions_by_username('research_papers', username),
        'videos': count_collection_contributions_by_username('videos', username),
    })

    author.remove('date')

    if author.has('links'):
        author.set('url', author.get('links')[0])

    CACHE[username] = author
    return author


def get_markdown_file_by_username(
    username: str
):
    """
    Get a markdown file by username.
    """
    full_path = os.path.join(get_collection_path('contributors'), username + '.md')

    if not os.path.exists(full_path):
        raise ValueError(f'No contributor with username "{username}" exists.')

    return MarkdownFile.load(full_path)


def count_collection_contributions_by_username(collection: str, username: str) -> int:
    """
    Quickly search markdown files for the contributor and return the count.
    """
    markdown_files = DefaultFeedGenerator.discover_markdown_file_paths(
        get_collection_path(collection))

    found_count = 0
    for markdown_file_path in markdown_files:
        with open(markdown_file_path) as file:
            if f'contributor: {username}' in file.read():
                found_count += 1

    return found_count
