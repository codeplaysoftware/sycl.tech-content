---
contributor: max
date: '2023-10-01T08:08:10.490000'
title: 'Open SYCL on heterogeneous GPU systems: A case of study'
external_url: https://arxiv.org/ftp/arxiv/papers/2310/2310.06947.pdf
authors:
  - Rocío Carratalá-Sáez
  - Francisco J. Andújar
  - Yuri Torres
  - Arturo Gonzalez-Escribano
  - Diego R. Llanos
tags:
  - gpu
  - cuda
  - hpc
  - hip
---

Computational platforms for high-performance scientific applications are becoming more heterogeneous, including hardware
accelerators such as multiple GPUs. Applications in a wide variety of scientific fields require an efficient and careful
management of the computational resources of this type of hardware to obtain the best possible performance. However,
there are currently different GPU vendors, architectures and families that can be found in heterogeneous clusters or
machines. Programming with the vendor provided languages or frameworks, and optimizing for specific devices, may become
cumbersome and compromise portability to other systems. To overcome this problem, several proposals for high-level
heterogeneous programming have appeared, trying to reduce the development effort and increase functional and performance
portability, specifically when using GPU hardware accelerators. This paper evaluates the SYCL programming model, using
the Open SYCL compiler, from two different perspectives: The performance it offers when dealing with single or multiple
GPU devices from the same or different vendors, and the development effort required to implement the code. We use as
case of study the Finite Time Lyapunov Exponent calculation over two real-world scenarios and compare the performance
and the development effort of its Open SYCL-based version against the equivalent versions that use CUDA or HIP. Based on
the experimental results, we observe that the use of SYCL does not lead to a remarkable overhead in terms of the GPU
kernels execution time. In general terms, the Open SYCL development effort for the host code is lower than that observed
with CUDA or HIP. Moreover, the SYCL version can take advantage of both CUDA and AMD GPU devices simultaneously much
easier than directly using the vendor-specific programming solutions.
