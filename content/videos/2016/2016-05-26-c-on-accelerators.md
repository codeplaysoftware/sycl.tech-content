---
contributor: max
date: '2016-05-26T14:39:36+02:00'
title: C++ on Accelerators
external_url: https://www.youtube.com/watch?v=YKX6EMEib4g
type: presentation
tags:
  - tutorial
  - c++
  - accelerators
  - presentation
featuring:
  - name: Victor Lomüller
    affiliation_at_video_production_time: Codeplay Software
---

Recent initiatives attempt to bring modern C++ applications to heterogeneous devices. The Khronos Group published SYCL
in mid-2015. SYCL offers a single-source C++ programming environment built on top of OpenCL. Codeplay and the University
of Bath are currently collaborating on a C++ front-end for HSAIL (HSA Intermediate Language) from the HSA Foundation.
Both models use a similar single-source C++ approach, in which the host and device kernel C++ code is interleaved. A
kernel always starts using specific function calls, which take a functor object. To support the compilation of these two
high-level programming models, Codeplay's compilers rely on a common engine based on Clang and LLVM to extract and
manipulate those kernels.
