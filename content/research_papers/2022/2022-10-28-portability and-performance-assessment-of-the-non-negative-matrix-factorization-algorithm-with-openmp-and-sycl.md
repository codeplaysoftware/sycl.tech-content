---
contributor: scott
date: '2022-10-28T08:08:10.490000+00:00'
title: 'Portability and Performance Assessment of the Non-Negative Matrix Factorization Algorithm with OpenMP and SYCL'
external_url: https://ieeexplore.ieee.org/document/9959906
authors:
  - Youssef Faqir-Rhazoui
  - Carlos García
  - Francisco Tirado
tags:
  - openmp
  - sycl
  - dpc++
  - oneapi
  - matrix
  - hpc
---

The SYCL standard was released to improve code portability across heterogeneous environments. Intel released the oneAPI
toolkit, which includes the Data-Parallel C++ (DPC++) compiler which is the Intel’s SYCL implementation. SYCL is
designed to use a single source code to target multiple accelerators such as: multi-core CPUs, GPUs and even FPGAs.
Additionally, the C/C++ compiler provided in the oneAPI toolkit supports OpenMP which also allows targeting codes on
both CPU and GPU devices. In this paper, the performance of SYCL and OpenMP is evaluated using the well-known
non-negative matrix factorization (NMF) algorithm. Three different NMF implementations are developed: baseline, SYCL and
OpenMP versions to analyze the acceleration on CPU and GPU. Experimental results show that while the two programming
models perform almost identically on CPU, on GPU, SYCL outperforms its OpenMP counterpart slightly.
