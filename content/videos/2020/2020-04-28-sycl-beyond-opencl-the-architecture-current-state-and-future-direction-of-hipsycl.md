---
contributor: rod
date: '2020-04-28T11:31:36+02:00'
title: 'SYCL beyond OpenCL: The architecture, current state and future direction of hipSYCL'
external_url: https://www.youtube.com/watch?v=kYrY80J4ZAs
type: presentation
featuring:
  - name: Aksel Alpay
    affiliation_at_video_production_time: Heidelberg University
---

The SYCL ecosystem currently contains four major SYCL implementations: Codeplay’s ComputeCpp, Intel’s LLVM/clang
implementation, triSYCL led by Xilinx and hipSYCL led by Heidelberg University. HipSYCL, an open source project
available at https://github.com/illuhad/hipSYCL, is the first SYCL implementation that does not build on OpenCL,
providing instead CUDA/HIP and OpenMP backends that allow it to target CPUs, NVIDIA GPUs and AMD GPUs. Since hipSYCL
builds on the CUDA/HIP clang frontend, augmented with a clang plugin to add support for SYCL constructs, it is
inherently interoperable with existing CUDA or HIP codebases, vendor-optimized libraries, and can expose latest hardware
features such as intrinsics as soon as they become available in the clang CUDA/HIP toolchain.
