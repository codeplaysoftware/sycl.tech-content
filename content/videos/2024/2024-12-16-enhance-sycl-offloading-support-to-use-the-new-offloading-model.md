---
contributor: scott
date: '2024-12-16T12:11:00'
title: '2024 LLVM Dev Mtg - Enhance SYCL offloading support to use the new offloading model'
external_url: 'https://www.youtube.com/watch?v=4Qof7vtfhuk'
type: presentation
tags:
  - sycl
  - offload
  - intel
  - clang
featuring:
  - name: Ravi Narayanaswamy
    affiliation_at_video_production_time: Unknown
---

Driven by Intel, SYCL compiler is an LLVM-based project that implements support for the SYCL language. In our downstream
implementation, We (Intel) have made several changes to the clang-linker-wrapper tool to support SYCL device code
linking and wrapping. This talk includes discussion of key changes to clang-linker-wrapper tool to enable JIT/AOT
compilation flow for SYCL offloading, addition of a new sycl-post-link library, SYCL specific options passed to
clang-linker-wrapper, and use of existing mechanism for propagating SYCL specific metadata from the compiler to SYCL
runtime library.
