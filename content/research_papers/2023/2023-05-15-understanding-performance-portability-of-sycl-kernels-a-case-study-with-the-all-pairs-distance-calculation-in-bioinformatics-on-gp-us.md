---
contributor: scott
date: '2023-05-15T08:08:10.490000+00:00'
title: 'Understanding Performance Portability of SYCL Kernels: A Case Study with the All-Pairs Distance Calculation in Bioinformatics on GPUs'
external_url: https://ieeexplore.ieee.org/document/10196541
authors:
  - name: Zheming Jin
    affiliation: Oak Ridge National Laboratory
  - name: Jeffrey S. Vetter
    affiliation: Oak Ridge National Laboratory
tags:
  - portability
  - performance
  - bioinformatics
---

SYCL is a portable programming model. Toward the goal of a better understanding of performance portability of SYCL
kernels on GPUs, we select a bioinformatics kernel for computing the all-pairs distance as a case study. After migrating
the kernel from CUDA to HIP and SYCL, we evaluate the performance of the CUDA, HIP, and SYCL kernels on NVIDIA V100 and
AMD MI210 GPUs. We analyze the GPU instructions from the kernels to explain performance gaps between SYCL and CUDA/HIP.
We hope that the findings are valuable for improving performance portability of SYCL.
