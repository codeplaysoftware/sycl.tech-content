---
contributor: anonymous
creation_date: '2024-06-07T09:04:19Z'
date: '2025-06-20T12:22:10'
external_url: https://github.com/habalasub/sycl_math_library_bug
license: Unspecified
tags:
- intel
- sycl
title: sycl_math_library_bug
---

When using Intel icpx to run both a sycl kernel and a sequential loop, there are differences in the
pow and the exp functions. The following example is a reproducer of these errors.
