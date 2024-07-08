# Contributing Events

If you would like to create a new event that will show on sycl.tech and also our feeds, please create a new  
markdown file the named with the format `YYYY-MM-DD-slugified-event-name-here.md` and place it within the 
`/content/events/YYYY/` directory.

Once you have created your file, copy and paste the contents below, replacing all the details with your own.

```markdown
---
contributor: anonymous
date: '2023-11-02T14:52:03'
ends: '2024-05-11T00:00:00'
starts: '2024-05-08T00:00:00'
title: IWOCL 2024 - 12th International Workshop on OpenCL and SYCL
external_url: 'https://www.iwocl.org'
attendees:
  - max
  - scott
  - rod
---

Some content describing the event here.
```

Once you have done all the above, create a pull request to the repository.

## Notes

* `contributor: anonymous` should refer to a contributor stored within the [contributors directory](../contributors)
* `attendees:` should be a YAML list, with [contributor](../contributors) usernames
* `starts:` should never be after `before:`

## Support

Please use the issues section if you need support.
