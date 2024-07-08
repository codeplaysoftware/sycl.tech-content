---
contributor: rod
date: '2019-10-24T09:31:36+02:00'
title: 'CppCon 2019: Efficient GPU Programming with Modern C++'
external_url: https://www.youtube.com/watch?v=8pJS3n4MITM
type: presentation
featuring:
  - username: gordon
---

This talk uses SYCL as a programming model for demonstrating the concepts being presented, however, the concepts can be
applied to any other heterogeneous programming model such as OpenCL or CUDA. SYCL allows users to write standard C++
code which is then executed on a range of heterogeneous architectures including CPUs, GPUs, DSPs, FPGAs and other
accelerators. On top of this SYCL also provides a high-level abstraction which allows users to describe their
computations as a task graph with data dependencies, while the SYCL runtime performs data dependency analysis and
scheduling. SYCL also supports a host device which will execute on the host CPU with the same execution and memory model
guarantees as OpenCL for debugging purposes, and a fallback mechanism which allows an application to recover from
failure.
