---
contributor: scott
date: '2021-11-14T08:08:10.490000+00:00'
title: 'Case Study of Using Kokkos and SYCL as Performance-Portable Frameworks for Milc-Dslash Benchmark on NVIDIA, AMD and Intel GPUs'
external_url: https://ieeexplore.ieee.org/document/9652859
authors:
  - name: Amanda S. Dufek
  - name: Rahulkumar Gayatri
  - name: Neil Mehta
  - name: Douglas Doerfler
  - name: Brandon Cook
  - name: Yasaman Ghadar
  - name: Carleton DeTar
tags:
  - kokkos
  - milc-dslash
  - performance
  - portability
  - nvidia
  - intel
  - amd
---

Six of the top ten supercomputers in the TOP500 list from June 2021 rely on NVIDIA GPUs to achieve their peak compute
bandwidth. With the announcement of Aurora, Frontier, and El Capitan, Intel and AMD have also entered the domain of
providing GPUs for scientific computing. A consequence of the increased diversity in the GPU landscape is the emergence
of portable programming models such as Kokkos, SYCL, OpenCL, and OpenMP, which allow application developers to maintain
a single-source code across a diverse range of hardware architectures. While the portable frameworks try to optimize the
compute resource usage on a given architecture, it is the programmers responsibility to expose parallelism in an
application that can take advantage of thousands of processing elements available on GPUs. In this paper, we introduce a
GPU-friendly parallel implementation of Milc-Dslash that exposes multiple hierarchies of parallelism in the algorithm.
Milc-Dslash was designed to serve as a benchmark with highly optimized matrix-vector multiplications to measure the
resource utilization on the GPU systems. The parallel hierarchies in the Milc-Dslash algorithm are mapped onto a target
hardware using Kokkos and SYCL programming models. We present the performance achieved by Kokkos and SYCL
implementations of Milc-Dslash on NVIDIA A100 GPU, AMD MI100 GPU, and Intel Gen9 GPU. Additionally, we compare the
Kokkos and SYCL performances with those obtained from the versions written in CUDA and HIP programming models on NVIDIA
A100 GPU and AMD MI100 GPU, respectively.
