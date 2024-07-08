# Contributing Research Papers

If you would like to create a new playground sample, that will show on sycl.tech and also our feeds, please create a new 
markdown file the named with the format `YYYY-MM-DD-slugified-event-name-here.md` and place it within the 
`/content/research_papers/YYYY/` directory.

Once you have created your file, copy and paste the contents below, replacing all the details with your own.

```markdown
---
contributor: anonymous
date: '2022-04-14T08:08:10'
title: My Research Paper
external_url: https://link-to-paper.com/research-paper-1
authors:
  - name: John Smith
    affiliation: University of Sycl
  - name: Alice Ryan
    affiliation: University of Space
---

Your description of the research paper here.
```

Once you have done all the above, create a pull request to the repository.

## Notes

* `contributor: anonymous` should refer to a contributor stored within the [contributors directory](../contributors)
* `authors:` a YAML list of authors of the paper

## Support

Please use the issues section if you need support.
