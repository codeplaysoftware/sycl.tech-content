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

from markdownfeeds import read_from_url
from requests import Response


def get_collection_path(collection_name: str) -> str:
    """
    Get an absolute path to a collection.
    """
    return os.path.join(os.getcwd(), 'content', collection_name)


def similar(value_one: any, value_two: any) -> bool:
    """
    Attempts to check if one value is similar in some way to another value.
    """
    value_one_str = str(value_one).lower()
    value_two_str = str(value_two).lower()

    if value_one == value_two:
        return True

    if value_one_str in value_two_str or value_two_str in value_one_str:
        return True

    if isinstance(value_one, list):
        for x in value_one:
            if x in value_two:
                return True

    if isinstance(value_two, list):
        for x in value_two:
            if x in value_one:
                return True

    return False


def safe_read_from_url(
    url: str,
    bearer_token: str = None,
    expected_status_code: int = 200
) -> Response:
    """
    Read from url and raise an exception if the returned status code does not match the expected.
    """
    response = read_from_url(url, bearer_token)

    if response.status_code != expected_status_code:
        raise ConnectionError(
            f'Reading from the URL "{url}" likely failed due to the returned status code. '
            f'Expected code: {expected_status_code}, actual code: {response.status_code}.')

    return response
