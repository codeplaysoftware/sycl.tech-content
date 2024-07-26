---
contributor: scott
date: '2022-11-13T08:08:10.490000+00:00'
title: 'Towards Cross-Platform Portability of Coupled-Cluster Methods with Perturbative Triples using SYCL'
external_url: https://ieeexplore.ieee.org/document/10024604
authors:
  - Abhishek Bagusetty
  - Ajay Panyala
  - Gordon Brown
  - Jack Kirk
tags:
  - performance
  - nvidia
  - perturbation
  - triples
  - coupled-cluster
  - portability
---

Tensor contractions form the fundamental computational operation of computational chemistry, and these contractions
dictate the performance of widely used coupled-cluster (CC) methods in computational chemistry. In this work, we study a
single-source, cross-platform C++ abstraction layer programming model, SYCL, for applications related to the
computational chemistry methods such as CCSD(T) coupled-cluster formalism. An existing optimized CUDA implementation was
migrated to SYCL to make use of the novel algorithm that provides tractable GPU memory needs for solving
high-dimensional tensor contractions for accelerating CCSD(T). We present the cross-platform performance achieved using
SYCL implementations for the non-iterative triples contribution of the CCSD(T) formalism which is considered as the
performance bottle neck on NVIDIA A100 and AMD Instinct MI250X. Additionally, we also draw comparisons of similar
performance metrics from vendor-based native programming models such as CUDA and ROCm HIP. Our results indicate that the
performance of SYCL measured at-scale was on-par with the code written in HIP for AMD MI250X GPUs while the performance
is slightly lacking on NVIDIA A100 GPUs in comparison to CUDA.
