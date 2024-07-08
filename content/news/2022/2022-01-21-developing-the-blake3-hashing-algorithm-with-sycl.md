---
contributor: max
date: '2022-01-21T09:14:04.755000+00:00'
external_url: https://itzmeanjan.in/pages/blake3-on-gpgpu.html
image: ../../../static/images/news/2022-01-21-developing-the-blake3-hashing-algorithm-with-sycl.webp
title: Developing the BLAKE3 hashing algorithm with SYCL
tags:
  - blake3
  - cryptographic
  - opencl
---

Last week I implemented multiple variants of highly parallelizable cryptographic hash function BLAKE3 using SYCL and
today I'd like to present my collective understanding, which I gained while implementing/benchmarking BLAKE3, targeting
heterogeneous accelerator platform(s). BLAKE3 cryptographic hash function easily lends itself well to data parallel
execution environments like SYCL/ OpenCL.
