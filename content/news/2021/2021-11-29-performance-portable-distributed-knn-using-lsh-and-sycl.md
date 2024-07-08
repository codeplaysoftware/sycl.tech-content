---
contributor: scott
date: '2021-11-29T12:10:39.251000+00:00'
external_url: https://www.intel.com/content/www/us/en/developer/videos/performance-portable-distributed-k-nn-lsh-sycl.html
image: ../../../static/images/news/2021-11-29-performance-portable-distributed-knn-using-lsh-and-sycl.webp
title: Performance-Portable Distributed KNN Using LSH and SYCL
tags:
  - ai
  - artificial-intelligence
  - library
  - hipsycl
  - dpc++
  - oneapi
  - intel
  - algorithm
  - mpi
---

In the age of artificial intelligence, algorithms must efficiently cope with vast datasets. We propose a
performance-portable implementation of locality-sensitive hashing (LSH), which is an approximate k-nearest neighbor (
KNN) algorithm to speed up the classification on heterogeneous hardware.

Our new library provides a hardware independent, yet efficient and distributed implementation of the LSH algorithm using
SYCL and message passing interface (MPI).

The results show that our library can scale on multiple GPUs, achieving a speedup of up to 7.6x on eight GPUs. It
supports different SYCL implementations—ComputeCpp, hipSYCL, DPC++—to target different hardware.
