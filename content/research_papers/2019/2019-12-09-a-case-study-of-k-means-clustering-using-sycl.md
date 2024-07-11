---
contributor: scott
date: '2019-12-09T10:57:29+01:00'
title: A Case Study of k-means Clustering using SYCL
external_url: https://ieeexplore.ieee.org/document/9005555
authors:
  - name: Zheming Jin
    affiliation: Argonne National Laboratory
  - name: Hal Finkel
    affiliation: Argonne National Laboratory
tags:
  - benchmark
  - energy-consumption
  - programming-language
  - gpu
  - lowest-consumption
  - rodinia
  - minimum-distance
  - data-transfer
  - api
  - means-clustering
  - fuzzy-clustering
  - haswell
  - broadwell
  - skywell
---

As opposed to the OpenCL programming model in which host and device codes are written in two programming languages, the
SYCL programming model combines them for an application in a type-safe way to improve development productivity. As a
popular cluster analysis algorithm, k-means has been implemented using programming models such as OpenMP, OpenCL, and
CUDA. Developing a SYCL implementation of k-means as a case study allows us to have a better understanding of
performance portability and programming productivity of the SYCL programming model. Specifically, we explained the
k-means benchmark in Rodinia, described our efforts of porting the OpenCL k-means benchmark, and evaluated the
performance of the OpenCL and SYCL implementations on the Intel ® Haswell, Broadwell, and Skylake processors. We
summarized the migration steps from OpenCL to SYCL, compiled the SYCL program using Codeplay and Intel ® SYCL compilers,
analyzed the SYCL and OpenCL programs using an open-source profiling tool which can intercept OpenCL runtime calls, and
compared the performance of the implementations on Intel ® CPUs and integrated GPU. The experimental results show that
the SYCL version in which the kernels run on the GPU is 2% and 8% faster than the OpenCL version for the two large
datasets. However, the OpenCL version is still much faster than the SYCL version on the CPUs. Compared to the Intel ®
Haswell and Skylake CPUs, running the k-means benchmark on the Intel ® Broadwell low-power processor with a CPU and an
integrated GPU can achieve the lowest energy consumption. In terms of programming productivity, the lines of code of the
SYCL program are 51% fewer than those of the OpenCL program.