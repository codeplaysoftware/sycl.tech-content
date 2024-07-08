---
contributor: max
date: '2022-09-06T16:29:39.348000+00:00'
title: 'C++ on Sea SYCL: Open Your Code to More Hardware Choices - Igor Vorobtsov'
external_url: https://www.youtube.com/watch?v=hIEBWdwxo6g
type: workshop
featuring:
  - name: Igor Vorobtsov
    affiliation_at_video_production_time: Intel Corporation
---

SYCL is a Khronos standard that introduces support for fully heterogeneous data parallelism to C++ and a solution to one
aspect of a larger problem: How do we enable full heterogeneous programming given the emerging explosion in hardware
diversity?

SYCL uses generic programming with templates and generic lambda functions to enable higher-level application software to
be cleanly coded with optimized acceleration of kernel code across the extensive range of various acceleration APIs,
e.g. OpenCL. Developers program at a higher level than the native acceleration API, but always have access to
lower-level code through seamless integration with the native acceleration API. We will talk on SYCL basics and show the
case of the successful tsunami simulation code migration to SYCL and new opportunities it may bring to developers by
unlocking other hardware vendors and architectures with reasonable performance.
