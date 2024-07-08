# Contributing Playground Samples

If you would like to create a new playground sample, that will show on sycl.tech and also our feeds, please create a new 
markdown file the named with the format `slugified-event-name-here.md` and place it within the 
`/content/playground_samples/` directory.

Once you have created your file, copy and paste the contents below, replacing all the details with your own.

```markdown
---
contributor: anonymous
title: "Hello World! (on device)"
summary: "Learn the basics with classic Hello World! sample, run on device."
---

#include <sycl/sycl.hpp>

class hello_world;

int main(int, char**) {
    std::cout << "Hello World!";
}
```

Once you have done all the above, create a pull request to the repository.

## Notes

* `contributor: anonymous` should refer to a contributor stored within the [contributors directory](../contributors)

## Support

Please use the issues section if you need support.
