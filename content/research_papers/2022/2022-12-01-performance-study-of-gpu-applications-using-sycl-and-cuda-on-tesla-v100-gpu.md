---
contributor: scott
date: '2022-12-01T08:08:10.490000+00:00'
title: 'Performance Study of GPU applications using SYCL and CUDA on Tesla V100 GPU'
external_url: https://ieeexplore.ieee.org/document/9622813
authors:
  - name: Goutham Kalikrishna Reddy Kuncham
  - name: Rahul Vaidya
  - name: Mahesh Barve
tags:
  - performance
  - runtime
  - conferences
  - gpu
  - ram
  - throughput
  - hardware
---

SYCL standard enables single-source programs to run on heterogeneous platforms consisting of CPUs, GPUs, FPGAs across
different hardware vendors. SYCL combines modern C++ features along with OpenCL’s portability. SYCL runtime is also
capable of targeting the CUDA backend directly on NVIDIA GPUs. This approach can potentially improve the performance of
SYCL on NVIDIA devices. Although NVIDIA GPUs can be targeted via OpenCL backend, their features and capabilities are
limited, and the performance is inadequate.In this study, we compare the performance of the Nvidia V100 GPU using SYCL
and CUDA. For performance evaluation, we selected three GPU applications: BabelStream, Mixbench, and Tiled
Matrix-Multiplication. We conducted extensive tests to understand the performance in terms of DRAM bandwidth, kernel
execution time, compilation time, and throughput. As per our study, the performance of SYCL and CUDA were found to be
similar. However, in some cases, CUDA outperformed SYCL.