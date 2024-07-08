---
contributor: rod
date: '2020-09-02T08:28:48.960000+00:00'
title: A Comparison of Programming Models with SYCL
external_url: https://www.youtube.com/watch?v=x-z0I858mMc
type: presentation
featuring:
  - username: tom
---

In the Exascale era, high-performance scientific codes will be required to run on both homogeneous and heterogeneous
systems made from hardware by different vendors. The supercomputers are constructed from CPUs with lots of cores, and in
many cases with multiple GPU accelerators. Having a parallel programming model to support all these systems is key to
having a code that is flexible and performance portable. In this talk, I’ll show the similarities and differences of
implementing some simple typical computational patterns in three heterogeneous parallel programming models: OpenCL,
OpenMP and SYCL. I’ll show performance results for each on a range of hardware from different vendors, focussing on
performance portability.
