---
contributor: rod
date: '2021-05-13T16:00:41.424000+00:00'
external_url: https://hgpu.org/?p=24964
image: ../../../static/images/news/2021-05-13-sylkan-towards-a-vulkan-compute-target-platform-for-sycl.webp
title: 'Sylkan: Towards a Vulkan Compute Target Platform for SYCL'
tags:
  - sylkan
  - vulkan
  - compute
  - opencl
---

In this paper, we discuss the opportunities and challenges of mapping SYCL to Vulkan, a low-level explicit programming
model for GPUs. This includes an analysis of the potential semantic mismatch between each respective standard, as well
as approaches to work around some of these issues. Additionally, we present a prototype research implementation of
Sylkan, a SYCL compiler and runtime targeting Vulkan. In order to evaluate our prototype qualitatively and
quantitatively, we chose a variety of functional tests as well as three performance benchmarks. For the functional
tests, we discuss and categorize the failures of the current prototype, noting which semantic mismatch or missing
implementation causes them. For the performance benchmarks, we compare execution times against a OpenCL-based SYCL
implementation and a native Vulkan version of each benchmark, on two hardware platforms.
