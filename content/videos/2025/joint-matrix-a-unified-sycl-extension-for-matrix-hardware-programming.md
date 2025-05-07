---
contributor: max
date: '2025-05-07T12:11:00'
title: 'Joint Matrix: A Unified SYCL Extension for Matrix Hardware Programming'
external_url: 'https://www.youtube.com/watch?v=BBESHzVVDYo'
type: presentation
tags:
  - sycl
  - oneapi
---

Joint Matrix: A Unified SYCL Extension for Matrix Hardware Programming

Joint matrix is a new SYCL extension for matrix hardware programming. It unifies 
targets like Intel Advanced Matrix Extensions (Intel AMX), Intel Xe Matrix Extensions
(Intel XMX), NVIDIA* Tensor Cores, AMD* Matrix Cores, etc. In general, ML frameworks
like Tensorflow and libraries like oneAPI Deep Neural Network Library (oneDNN) are capable
of heavily utilizing matrix hardware acceleration, and are the answer for many types
of users and applications who want high performance from such hardware. However,
for users who want to build their own neural network applications, these libraries
and frameworks become too high-level, because users cannot do custom optimizations,
and too heavyweight, because the size of libraries is large. Moreover, new operations
are often introduced in the machine learning domain for which frameworks and libraries
do not provide timely and performant solutions. For such cases, APIs are needed to
write custom workload-specific optimizations and this is where joint matrix can help.
Joint matrix has a lower level of abstraction than these frameworks and libraries,
enabling it to provide performance, productivity, and fusion capabilities but, at the
same time, offers portability by using one code to target different matrix hardware.

In this talk, we present (1) the main APIs introduced as part of SYCL joint matrix extension,
(2) tuning techniques to fully utilize Intel hardware using SYCL joint matrix, and (3)
the application and validation of this language feature and tuning techniques using the
GEMM benchmark and the ability to fuse kernels such as GEMM and GELU.
