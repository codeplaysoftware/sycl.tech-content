---
contributor: anonymous
date: '2022-02-08T10:27:22.090000+00:00'
external_url: https://medium.com/intel-tech/oneapi-as-a-catalyst-for-open-innovation-59904a602e
image: ../../../static/images/news/2022-02-08-sycl-the-heart-of-oneapi.webp
title: SYCL - the heart of oneAPI
tags:
  - oneapi
  - dpc++
---

SYCL is the heart of oneAPI, enabling cross-platform data parallel programming in modern C++. SYCL is a Khronos standard
with broad participation across research institutions and companies. Intel contributes to the development of SYCL by
participating in the SYCL standard committee and
contributing [SYCL support to the LLVM](https://github.com/intel/llvm/tree/sycl)project. The SYCL support, combined with
LLVM’s SPIR-V, PTX, and CPU backends enable targeting SYCL programs to a wide variety of CPUs and accelerators. SYCL is
augmented with the [oneAPI DPC++ Library (oneDPL)](https://github.com/oneapi-src/oneDPL), which provides STL-like
capabilities for programming accelerators. When you need high performance math,
the [oneAPI Math Kernel Library (oneMKL)](https://github.com/oneapi-src/onemkl)includes BLAS, LAPACK, FFTs, and random
number generation. There are many good math libraries out there already, and open source oneMKL provides a common
SYCL-based interface that lets you integrate low-level proprietary and open-source libraries.
