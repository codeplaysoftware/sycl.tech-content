# Contributing News

If you would like to create a new news item, that will show on sycl.tech and also our feeds, please create a new 
markdown file the named with the format `YYYY-MM-DD-slugified-event-name-here.md` and place it within the 
`/content/news/YYYY/` directory.

Once you have created your file, copy and paste the contents below, replacing all the details with your own.

```markdown
---
contributor: anonymous
date: '2024-01-31T11:11:59'
external_url: https://www.mywebsite.com/news-post.html
title: Example Title Here
image: ../../../static/images/news/2024-01-01-slugified-event-name-here.webp
tags:
  - oneapi
  - performance
  - nvidia
  - a100
---

Some content describing the news post here.
```

Once you have done all the above, create a pull request to the repository.

## Notes

* `contributor: anonymous` should refer to a contributor stored within the [contributors directory](../contributors)
* `external_url:` should point to a website URL that the user can follow to read the full post
* `tags:` a YAML list of tags to best describe the item

## Support

Please use the issues section if you need support.
