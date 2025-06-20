import os
import urllib.request
import json
from datetime import datetime

from pathlib import Path

import yaml
from markdownfeeds.MarkdownFile import MarkdownFile
from slugify import slugify

projects_path = os.path.join(os.getcwd(), '../content/projects')
url = 'https://api.github.com/search/repositories?q=topic:sycl&per_page=100'


def create_project_file(repo):
    date = datetime.fromisoformat(repo['created_at'])
    title = slugify(repo['name'])
    file_path = os.path.join(
        projects_path,
        str(date.year),
        f'{date.year}-{date.strftime("%m")}-{date.strftime("%d")}-{title}.md')

    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    license = 'Unspecified'

    if 'license' in repo and repo['license'] is not None and 'name' in repo['license']:
        license = repo['license']['name']

    with open(file_path, mode='w') as file:
        front_matter = {
            'date': datetime.today().strftime('%Y-%m-%dT%H:%M:%S'),
            'creation_date': repo['created_at'],
            'title': repo['name'],
            'license': license,
            'contributor': 'anonymous',
            'external_url': repo['html_url'],
            'tags': repo['topics']
        }

        contents = '---\n'
        contents += yaml.dump(front_matter)
        contents += '---\n\n'
        contents += repo['description'] if repo['description'] is not None else repo['name']
        contents += '\n'

        print(f'Wrote new project file to {file_path}')
        file.write(contents)


# Fetch and load JSON data
page = 1
total_repos_to_fetch = 0
repos = []

while len(repos) < total_repos_to_fetch or total_repos_to_fetch == 0:
    with urllib.request.urlopen(url + f'&page={page}') as response:
        result = json.loads(response.read().decode())
        total_repos_to_fetch = result['total_count']
        repos = repos + result['items']
        page += 1

# Get all the project URLs we currently have
project_urls = []
for markdown_file in list(Path(projects_path).rglob('*.md')):
    contents = MarkdownFile.load(str(markdown_file))
    project_urls.append(str(contents.front_matter.get('external_url')).lower())

# Loop all the repos we have found from API and ensure we have a project file for them
for repo in repos:
    needle = str(repo['html_url']).lower()

    if needle not in project_urls:
        print(f'Project not found: ' + repo['html_url'])
        create_project_file(repo)
