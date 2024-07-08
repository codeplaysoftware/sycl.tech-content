---
contributor: anonymous
date: '2019-04-29T12:18:06+02:00'
title: "2019 EuroLLVM Meeting: SYCL compiler: zero-cost abstraction and type...\u201D"
external_url: https://www.youtube.com/watch?v=rfg19iODkhI
type: presentation
featuring:
  - name: Andrew Savonichev (Intel)
    affiliation_at_video_production_time: Intel Corporation
---

SYCL is an abstraction layer for C++, that allows a developer to write heterogeneous programs in a "single source"
model, where host and device code are written in the same file. Utilizing modern C++ features, SYCL provides a way to
develop type-safe and efficient programs for various accelerator devices.

This talk will go over technical details of the SYCL compiler, and the changes we need to make in order to bring full
support for SYCL into upstream LLVM and Clang as described in the RFC
