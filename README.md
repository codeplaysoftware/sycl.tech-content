# SYCL.tech Content

[![Scorecard supply-chain security](https://github.com/codeplaysoftware/sycl.tech-content/actions/workflows/scorecard.yml/badge.svg)](https://github.com/codeplaysoftware/sycl.tech-content/actions/workflows/scorecard.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/codeplaysoftware/sycl.tech-content/badge)](https://scorecard.dev/viewer/?uri=github.com/codeplaysoftware/sycl.tech-content)

## About The Project

This repository contains all the content (news, videos, projects etc.) that is shown on [sycl.tech](https://sycl.tech).
Anyone is free to contributor sycl based material by creating pull requests. 

## Contribute SYCL Related Content

To get you information on contributing to the right place, please use the links shown in the table below.

| Collection / Type                                          | Info                                                                     |
|------------------------------------------------------------|--------------------------------------------------------------------------|
| [Contributors](content/contributors/README.md)             | If you would like to create a contributor profile.                       |
| [Events](content/events/README.md)                         | If you have an event that has sycl based on interesting to sycl devs.    |
| [News](content/news/README.md)                             | If you have a news item, update or something else to share sycl related. |
| [Playground Samples](content/playground_samples/README.md) | If you have a sample of SYCL code to share with others.                  |
| [Projects](content/projects/README.md)                     | If you have a sycl based project to share.                               |
| [Research Papers](content/research_papers/README.md)       | If you have a research paper that covers SYCL.                           |
| [Videos](content/videos/README.md)                         | If you have a video to share that discusses SYCL.                        |

## JSON Feeds

You can subscribe to our [JSON feeds](https://www.jsonfeed.org/version/1/) and consume our content using your own 
feed reader. Below is a list of our JSON feeds.

* [Contributors Feed](https://feeds.sycl.tech/contributors/feed.json)
* [Events Feed](https://feeds.sycl.tech/events/feed.json)
* [News Feed](https://feeds.sycl.tech/news/feed.json)
* [Playground Samples Feed](https://feeds.sycl.tech/playground_samples/feed.json)
* [Projects Feed](https://feeds.sycl.tech/projects/feed.json)
* [Research Papers Feed](https://feeds.sycl.tech/research_papers/feed.json)
* [Videos Feed](https://feeds.sycl.tech/videos/feed.json)

## Getting Started

You can build the json feeds using the following command:

1) Install dependencies:

```shell
pip install -r requirements.txt
```

2) Run the feed generator:

```shell
python feed.py
    -a "https://feed.mywebsite.com/static/"
    -b "https://feed.mywebsite.com"
    -s "https://mywebsite.com"
    -g "github_api_token_here"
```

## Flags

* `-s` The URL for the front-end website
* `-a` The asset URL, pointing to the static assets
* `-b` The base URL to which the feed lives at
* `-g` A GitHub API key, used to pull project and other information
* `-i` The number of items to render per feed page
* `-d` To show debug output

## Contributing

Please see the `CONTRIBUTING.md` file for details.

## License

Distributed under the Apache 2.0 License. See `LICENSE.txt` file for more information.

## Contact

<dev-rel@codeplay.com>
