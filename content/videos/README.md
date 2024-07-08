# Contributing Videos

If you would like to create a new playground sample, that will show on sycl.tech and also our feeds, please create a new 
markdown file the named with the format `YYYY-MM-DD-slugified-event-name-here.md` and place it within the 
`/content/videos/YYYY/` directory.

Once you have created your file, copy and paste the contents below, replacing all the details with your own.

```markdown
---
contributor: anonymous
date: '2023-04-03T13:23:23.11'
title: Example Video Title
external_url: https://www.youtube.com/watch?v=dQw4w9WgXcQ
type: presentation
tags:
  - sycl
  - presentation
  - syclcon
featuring:
  - name: John Smith
    affiliation_at_video_production_time: Sycl University
---

Your same SYCL (C++) code can now run not only on CPU but also (same code) on GPUs by Nvidia® and AMD® with the new
plugins from Codeplay®.
```

Once you have done all the above, create a pull request to the repository.

## Notes

* `contributor: anonymous` should refer to a contributor stored within the [contributors directory](../contributors)
* `featuring:` a YAML list of people appearing in the video
* `affiliation` should refer to the company or institute at the time of the video creation

## Support

Please use the issues section if you need support.
