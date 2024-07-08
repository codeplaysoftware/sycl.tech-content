---
contributor: max
date: '2017-11-20T13:07:17+01:00'
external_url: https://www.codeplay.com/portal/10-13-17-managed-virtual-pointers-with-sycl
image: ../../../static/images/news/2017-11-20-managed-virtual-pointers-with-sycl.webp
title: Managed Virtual Pointers With SYCL
tags:
  - SYCL
  - c++11
---

In this post we will present a utility that facilitates integrating SYCL into existing codebases that are not C++11
friendly. If your application uses malloc and frees for allocation, or has some existing CUDA®-based memory management,
the "Legacy Pointer" and/or the "Managed Virtual Pointer" utilities can help you to integrate your code with SYCL.
