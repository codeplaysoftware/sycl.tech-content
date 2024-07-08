---
contributor: max
date: '2022-12-19T14:52:49.222000+00:00'
title: GPU Performance Portability Using Standard C++ with SYCL
external_url: https://www.youtube.com/watch?v=8Cs_uI-O51s
type: presentation
featuring:
  - name: Hugh Delaney 
    affiliation_at_video_production_time: Codeplay Software
---

The proliferation of accelerators, in particular GPUs, over the past decade is impacting the way software is being
developed. Most developers who have been using CPU based machines are now considering how it's possible to improve the
performance of applications by offloading execution to many core processors. Many emerging disciplines including AI,
deep neural networks and machine learning have shown that GPUs can increase performance by many times compared to
CPU-only architectures. New hardware features such as "tensor cores" are also starting to emerge to address specific
problems including mixed precision computing. The new challenge for developers is figuring out how to develop for
heterogeneous architectures that include GPUs made by different companies. Currently, the most common way to develop
software for GPUs is using the CUDA programming model but this has pitfalls. CUDA uses non-standard C++ syntax and
semantics, is a proprietary interface, and can only be used to target Nvidia GPUs. Alternatives include HIP which offers
another proprietary programming interface only capable of targeting AMD GPUs.

This presentation will demonstrate how standard C++ code with SYCL can be used to achieve performance portability on
processors from multiple vendors including Nvidia GPUs, AMD GPUs and Intel GPUs. The SYCL programming interface is a
royalty free and industry defined open standard designed to enable the latest features of accelerators. Using an open
source project, we'll show how standard C++ syntax and semantics are used to define the SYCL kernel and memory
management code required to offload parallel execution to a range of GPUs. Further to this, we'll explain how easy it is
to compile this C++ code using a SYCL compiler so that it can be run on Nvidia, AMD and Intel GPUs and compare this
execution performance with the same code written using proprietary CUDA and HIP environments. Lastly we'll share our
tips for achieving the best performance on different processor architectures, including dealing with varying memory
resources, using the most appropriate memory access patterns, using hardware specific features such as "tensor cores"
and ensuring high utilization of the processor cores.
