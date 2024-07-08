---
contributor: max
date: '2023-02-24T08:57:40.423000+00:00'
external_url: https://www.intel.com/content/www/us/en/developer/videos/the-evolution-of-different-sycl-implementations.html
image: ../../../static/images/news/2023-02-24-the-evolution-of-different-sycl-trade-implementations.webp
title: The Evolution of Different SYCL Implementations
tags:
  - plssvm
  - implementations
  - cuda
  - hip
  - nvidia
  - amd
  - intel
  - openmp
  - opencl
---

A GPU-accelerated Parallel Least Squares Support Vector Machine (PLSSVM) was developed to classify dense datasets
with hundreds of thousands data points and more than a thousand features. It beats the state-of-the-art sequential
minimal optimization (SMO) implementations like LIBSVM.

PLSSVM supports many different hardware architectures that include any Intel CPU and GPUs, and NVIDIA and AMD
GPUs that use different back ends written in OpenMP, CUDA, HIP, OpenCL™ code, and SYCL. This talk compares
these back ends on different architectures in relation to their implementation and performance characteristics.
