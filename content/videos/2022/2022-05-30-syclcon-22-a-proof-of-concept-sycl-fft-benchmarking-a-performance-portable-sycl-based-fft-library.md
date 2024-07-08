---
contributor: max
date: '2022-05-30T10:57:44.284000+00:00'
title: "SYCLcon 2022 - A Proof-of-Concept SYCL FFT Benchmarking a Performance Portable SYCL-based FFT Library"
external_url: https://www.youtube.com/watch?v=eynIjKrzXds
type: presentation
tags: 
  - syclcon
  - iwocl
  - ftt
featuring:
  - name: Vincent R. Pascuzzi
    affiliation_at_video_production_time: Brookhaven National Laboratory
  - name: Mehdi Goli
    affiliation_at_video_production_time: Codeplay Software
---

In this paper, we present an early version of a SYCL-based FFT library, capable of running on all major vendor hardware,
including CPUs and GPUs from AMD, ARM, Intel and NVIDIA. Although preliminary, the aim of this work is to seed further
developments for a diverse and rich set of features for calculating FFTs. It has the advantage over existing portable
FFT libraries in that it is single-source, and therefore removes the complexities that arise due to abundant use of
pre-process macros and auto-generated kernels to target different architectures. We exercise two SYCL-enabled compilers,
Codeplay ComputeCpp and Intel’s open-source LLVM project, to evaluate performance portability of our SYCL-based FFT on
various heterogeneous architectures. The current limitations of our library is it supports single-dimension FFTs up to
$2^{11}$ in length and base-2 input sequences. We compare our results with highly optimized vendor specific FFT
libraries and provide a detailed analysis to demonstrate a fair level of performance, and highlight sources of
performance bottlenecks in SYCL runtimes.
