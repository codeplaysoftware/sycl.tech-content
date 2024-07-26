---
contributor: scott
date: '2023-12-21T08:08:10.490000+00:00'
title: 'Evaluating Performance Portability of SYCL and Kokkos: A Case Study on LBM Simulations'
external_url: https://ieeexplore.ieee.org/document/10491773
authors:
  - Yue Ding
  - Chuanfu Xu
  - Haozhong Qiu
  - Qingsong Wang
  - Weixi Dai
  - Yongzhen Lin
  - Yonggang Che
tags:
  - kokkos
  - performance
  - portability
  - cross-platform
  - lbm
  - simulations
---

Since modern high performance computing systems are evolving towards diverse and heterogeneous architectures, the
emergence of high-level portable programming models leads to a particular focus on performance portability. In this
paper, we evaluate the performance portability and explore performance optimization methods for two portable programming
models SYCL and Kokkos. We take an open-source multi-phase Lattice Boltzmann Method (LBM) flow simulation code as a case
study and implement portable versions with different optimizations. Then we compare our portable implementations with
engineer-tuned OpenMP and CUDA versions on Intel CPUs and NVIDIA GPUs. Experimental results show that both SYCL and
Kokkos can deliver superior performance than traditional programming models, but the best performance of the portable
versions depends heavily on platform-specific optimizations. There is no single implementation that can achieve the best
performance on both CPUs and GPUs. Consequently, we conclude that the performance portability still needs to be further
improved for both SYCL and Kokkos. In addition, we present a comparative analysis of different optimization methods that
qualify the performance enhancement when using SYCL and Kokkos on CPUs and GPUs. Our work offers valuable references for
the development of both portable programming models and applications.
