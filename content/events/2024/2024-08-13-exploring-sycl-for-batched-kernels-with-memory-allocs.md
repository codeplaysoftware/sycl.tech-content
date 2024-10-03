---
contributor: rod
date: '	2024-07-05T14:46:00'
starts: '2024-08-13T13:00:10-05:00'
ends: '2024-08-13T14:00:10-05:00'
title: 'Exploring SYCL for Batched Kernels with Memory Allocations'
external_url: 'https://www.alcf.anl.gov/events/exploring-sycl-batched-kernels-memory-allocations'
---

Batched parallelism with local allocations is an extremely common pattern in HPC, appearing in multi-dimensional FFTs,
neural networks processing, or split computation of numerical operators. Its efficient support is especially complex on
GPU where memory per thread is limited and dynamic memory allocations are challenging. This study investigates whether
the native abstractions of SYCL can support performance portability for this pattern. We implement versions of a batched
semi-Lagrangian advection kernel using each parallel construct of SYCL. We evaluate them in terms of maintainability,
performance portability and memory footprint on CPUs and GPUs (AMD, Intel, NVIDIA), with two distinct SYCL
implementations (AdaptiveCpp and DPC++). Our results demonstrate that no single parallel construct of SYCL emerges as
best solution and that a construct offering a higher level of abstraction would be required to support this common
pattern.
