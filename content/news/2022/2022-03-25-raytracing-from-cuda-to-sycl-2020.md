---
contributor: scott
date: '2022-03-25T10:43:40.017000+00:00'
external_url: https://www.codeproject.com/Articles/5292398/Raytracing-From-CUDA-to-SYCL-2020-via-DPCplusplus
image: ../../../static/images/news/2022-03-25-raytracing-from-cuda-to-sycl-2020.webp
title: Raytracing From CUDA to SYCL 2020
tags:
  - raytracing
  - guide
  - cuda
  - nvidia
  - dpc++
  - intel
  - oneapi
---

A walkthrough of converting a code from parallel C++ ray-tracing code to CUDA, and the work needed to make that CUDA
code run on CPU using parallel `for_each()` and then converted the code to SYCL 2020.

In this article, we will port [Raytracing in One Weekend](https://raytracing.github.io/), the already converted parallel
code to CUDA, make CUDA run on CPU and then port again to SYCL 2020
via [Intel® Data-Parallel C++ (DPC++)](https://software.intel.com/content/www/us/en/develop/tools/oneapi/data-parallel-c-plus-plus.html)
toolkit. DPC++ is ISO C++ plus Khronos SYCL with community extensions eventually making their way into the final
standard. As time of article writing, the SYCL 2020 specification has been released for public review as a provisional
specification for developers to provide their valuable feedback before the final version is published and ratified.
