---
contributor: scott
date: '2020-01-16T08:00:07+02:00'
external_url: https://www.codeplay.com/portal/01-09-20-sycl-performance-post-choosing-a-good-work-group-size-for-sycl
title: Choosing a Good Work Group Size for SYCL
image: ../../../static/images/news/2020-01-16-choosing-a-good-work-group-size-for-sycl.webp
tags:
  - work-groups
  - tutorial
  - opencl
---

" A "work group" is a 1, 2 or 3 dimensional set of threads within the thread hierarchy and contains a set of "work
items," and each of these work items maps to a "core" in a GPU.

When using SYCL with an OpenCL device, the "work group" size often dictates the occupancy of the compute units. In order
to achieve the best performance, we need to try to match the work group size to the size of the compute units on the
hardware. Too large and the computations won't fit on the core, and too small the full capabilities of the core are not
being used. Both of these scenarios are likely to reduce the performance of the code. Software can only achieve 100%
utilization of an OpenCL device (e.g. a GPU) if it can fully occupy the hardware resources."
