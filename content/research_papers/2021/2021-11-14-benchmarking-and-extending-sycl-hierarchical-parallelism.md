---
contributor: scott
date: '2021-11-14T08:08:10.490000+00:00'
title: 'Benchmarking and Extending SYCL Hierarchical Parallelism'
external_url: https://ieeexplore.ieee.org/document/9654235
authors:
  - name: Tom Deakin
    affiliation: University of Bristol
  - name: Simon McIntosh-Smith
    affiliation: University of Bristol
  - name: Aksel Alpay
    affiliation:  Universität Heidelberg
  - name: Vincent Heuveline
    affiliation: Universität Heidelberg
tags:
  - benchmarks
  - extending
  - parallelism
---

SYCL is an open-standard, parallel programming model for programming heterogeneous devices from Khronos. It allows
single-source programming of diverse attached devices in a cross-platform manner in modern C++. SYCL provides different
layers of parallel abstractions, including Same Instruction Multiple Thread (SIMT) kernels, data-parallel loop
concurrency and hierarchical parallelism. We discuss Scoped Parallelism as an extension to the existing Hierarchical
Parallelism in SYCL, and highlight the advantages and disadvantages of these models from the perspective of the
programmer and an implementer of SYCL. In this paper, we compare writing benchmark programs using SIMT kernel,
hierarchical parallelism and scoped parallelism paradigms, and present results running on a high-performance CPU and
GPU.
