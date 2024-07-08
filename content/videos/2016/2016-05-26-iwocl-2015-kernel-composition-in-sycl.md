---
contributor: anonymous
date: '2016-05-26T14:39:36+02:00'
title: 'IWOCL 2015: Kernel Composition In SYCL'
external_url: https://www.youtube.com/watch?v=dO_4pn8YkKQ
type: presentation
tags:
  - composition
  - opencl
  - kernels
featuring:
  - name: Ralph Potter
    affiliation_at_video_production_time: Codeplay Software
---

Parallel primitives libraries reduce the burden of knowledge required for developers to begin developing parallel
applications and accelerating them with OpenCL. Unfortunately some current implementations implement primitives as
individual kernels and so incur a high performance cost in off-chip memory operations for intermediate variables. We
describe a methodology for creating efficient domain specific embedded languages on top of the SYCL for OpenCL standard
for parallel programming. Using this approach, a small example language was developed which provides an environment for
composing image processing pipelines from a library of more primitive operations, while retaining the capability to
generate a single kernel from a complex expression, and so eliminate unnecessary intermediate loads and stores to global
memory. This elimination of global memory accesses leads to a 2.75x speedup over implementing an unsharp mask in
OpenCLIPP. We give details of our domain specific embedded language, and provide experimental performance measurements
of both primitive performance and an unsharp mask operation composed of multiple primitives.
