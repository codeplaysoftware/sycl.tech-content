---
contributor: max
date: '2016-10-26T10:57:29+01:00'
title: 'A Comparative Study of SYCL, OpenCL, and OpenMP'
external_url: https://ieeexplore.ieee.org/document/7803697
authors:
  - name: Hércules Cardoso da Silva
    affiliation: Inst. of Comput
  - name: Flávia Pisani
    affiliation: Institute of Computing,
  - name: Edson Borin
    affiliation: Institute of Computing
tags:
  - opencl
  - openmp
  - parallel
  - performance
  - evaluation
---

Recent trends indicate that future computing systems will be composed by a group of heterogeneous computing devices,
including CPUs, GPUs, and other hardware accelerators. These devices provide increased processing performance, however,
creating efficient code for them may require that programmers manage memory assignments and use specialized APIs,
compilers, or runtime systems, thus making their programs dependent on specific tools. In this scenario, SYCL is an
emerging C++ programming model for OpenCL that allows developers to write code for heterogeneous computing devices that
are compatible with standard C++ compilation frameworks. In this paper, we analyze the performance and programming
characteristics of SYCL, OpenMP, and OpenCL using both a benchmark and a real-world application. Our performance results
indicate that programs that rely on available SYCL runtimes are not on par with the ones based on OpenMP and OpenCL yet.
Nonetheless, the gap is getting smaller if we consider the results reported by previous studies. In terms of
programmability, SYCL presents itself as a competitive alternative to OpenCL, requiring fewer lines of code to implement
kernels and also fewer calls to essential API functions and methods.