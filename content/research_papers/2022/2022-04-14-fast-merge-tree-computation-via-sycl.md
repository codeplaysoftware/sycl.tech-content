---
contributor: max
date: '2022-04-14T08:08:10.490000+00:00'
title: Fast Merge Tree Computation via SYCL
external_url: https://arxiv.org/pdf/2301.10838.pdf
authors:
  - name: Arnur Nigmetov
  - name: Dmitriy Morozov
tags:
  - merge-tree
  - benchmarking
---

A merge tree is a topological descriptor of a real-valued function. Merge trees are used in visualization and
topological data analysis, either directly or as a means to another end:computing a 0-dimensional persistence diagram,
identifying connected components, performing topological simplification, etc. Scientific computing relies more and more
on GPUs to achieve fast, scalable computation. For efficiency, data analysis should take place at the same location as
the main computation, which motivates interest in parallel algorithms and portable software for merge trees that can run
not only on a CPU, but also on a GPU, or other types of accelerators. The SYCL standard defines a programming model that
allows the same code, written in standard C++, to compile targets for multiple parallel backends (CPUs via OpenMP or
TBB, NVIDIA GPUs via CUDA, AMD GPUs via ROCm, Intel GPUs via Level Zero, FPGAs). In this paper, we adapt the triplet
merge tree algorithm to SYCL and compare our implementation with the VTK-m implementation, which is the only
