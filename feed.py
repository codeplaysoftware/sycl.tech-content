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
import time

from argparse import ArgumentParser
from markdownfeeds.Gatherer import Gatherer

from src.feeds.AcademyLessonFeed import AcademyLessonFeed
from src.feeds.EventFeed import EventFeed
from src.feeds.ImplementationActivityFeed import ImplementationActivityFeed
from src.feeds.NewsFeed import NewsFeed
from src.feeds.PlaygroundSampleFeed import PlaygroundSampleFeed
from src.feeds.ProjectFeed import ProjectFeed
from src.feeds.ResearchPaperFeed import ResearchPaperFeed
from src.feeds.VideoFeed import VideoFeed
from src.feeds.contributors.ContributorFeed import ContributorFeed


def load_command_line_args():
    """
    Load the relevant command line arguments
    :return:
    """
    argument_parser = ArgumentParser()

    argument_parser.add_argument('-s',
                                 '--siteUrl',
                                 dest='site_url',
                                 help='The site URL.',
                                 required=True)

    argument_parser.add_argument('-a',
                                 '--assetUrl',
                                 dest='asset_base_url',
                                 help='The static asset base URL.',
                                 required=True)

    argument_parser.add_argument('-b',
                                 '--feedBaseUrl',
                                 dest='feed_base_url',
                                 help='The base feed URL.',
                                 required=True)

    argument_parser.add_argument('-g',
                                 '--githubApiKey',
                                 dest='github_api_key',
                                 help='A GitHub API key, used to pull information from API.',
                                 required=True)

    argument_parser.add_argument('-i',
                                 '--itemsPerFeedPage',
                                 dest='items_per_feed_page',
                                 help='Maximum items per feed page.',
                                 default=100,
                                 required=False)

    argument_parser.add_argument('-d',
                                 '--debug',
                                 dest='debug_mode',
                                 help='Enable debug mode, will cause stack trace to print.',
                                 required=False,
                                 default=False,
                                 action='store_true')

    return argument_parser.parse_args()


if __name__ == '__main__':
    debug = False

    try:
        # Parse arguments
        args = load_command_line_args()
        debug = args.debug_mode

        logging.basicConfig(level=logging.INFO if debug else logging.WARNING)

        # Start time
        start_time = round(time.time() * 1000)

        # Vars
        print('Generating feeds....')

        # Set some require attributes
        ImplementationActivityFeed.GITHUB_API_KEY = args.github_api_key
        ProjectFeed.GITHUB_API_KEY = args.github_api_key

        # Files to skip when looking for feed markdown files
        skip_files = ['README.md']

        contributions = ContributorFeed(args, 'contributors').run_standalone()

        Gatherer([
            EventFeed(args, 'events'),
            NewsFeed(args, 'news'),
            PlaygroundSampleFeed(args, 'playground_samples'),
            ResearchPaperFeed(args, 'research_papers'),
            VideoFeed(args, 'videos'),
            AcademyLessonFeed(args),
            ImplementationActivityFeed(args),
            ProjectFeed(args, 'projects')
        ]).generate()

        # Print success and time took
        time_diff_in_seconds = (round(time.time() * 1000) - start_time) / 1000

        print(f'Success, took {time_diff_in_seconds}s.')
        exit(0)
    except Exception as e:
        if debug:
            raise e

        print('Error: ' + str(e.__str__().encode('ascii', errors='ignore').decode('ascii')))
        exit(1)
