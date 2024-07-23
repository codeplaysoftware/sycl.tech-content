---
contributor: max
date: '2024-01-05T08:08:10.490000+00:00'
title: 'Preliminary report: Initial evaluation of StdPar implementations on AMD GPUs for HPC'
external_url: https://arxiv.org/pdf/2401.02680
authors:
  - name: Wei-Chen Lin
  - name: Simon McIntosh-Smith
  - name: Tom Deakin
tags:
  - sycl
  - gpu
  - hip
---

Recently, AMD platforms have not supported offloading C++17 PSTL (StdPar) programs to the GPU. Our previous work highlights
how StdPar is able to achieve good performance across NVIDIA and Intel GPU platforms. In that work, we acknowledged AMD’s past 
effort such as HCC, which unfortunately is deprecated and does not support newer hardware platforms. Recent developments by AMD, Codeplay, 
and AdaptiveCpp (previously known as hipSYCL or OpenSYCL) have enabled multiple paths for StdPar programs to run on AMD GPUs. 
This informal report discusses our experiences and evaluation of currently available StdPar implementations for AMD GPUs. 
We conduct benchmarks using our suite of HPC mini-apps with ports in many heterogeneous programming models, including StdPar. 
We then compare the performance of StdPar, using all available StdPar compilers, to contemporary heterogeneous programming models
supported on AMD GPUs: HIP, OpenCL, Thrust, Kokkos, OpenMP, SYCL. Where appropriate, we discuss issues encountered and workarounds
applied during our evaluation. Finally, the StdPar model discussed in this report largely depends on Unified Shared Memory (USM) performance
and very few AMD GPUs have proper support for this feature. As such, this report demonstrates a proof-of-concept host-side userspace pagefault
solution for models that use the HIP API. We discuss performance improvements achieved with our solution using the same set of benchmarks.
