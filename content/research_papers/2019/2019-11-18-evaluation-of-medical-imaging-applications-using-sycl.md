---
contributor: scott
date: '2019-11-18T10:57:29+01:00'
title: Evaluation of Medical Imaging Applications using SYCL
external_url: https://ieeexplore.ieee.org/document/8982983
authors:
  - name: Zheming Jin
  - name: Hal Finkel
tags:
  - benchmark
  - performance
  - medical
  - rodina
  - imaging
---

As opposed to the Open Computing Language (OpenCL) programming model in which host and device codes are written in
different languages, the SYCL programming model can combine host and device codes for an application in a type-safe way
to improve development productivity. In this paper, we chose two medical imaging applications (Heart Wall and Particle
Filter) in the Rodinia benchmark suite to study the performance and programming productivity of the SYCL programming
model. More specifically, we introduced the SYCL programming model, shared our experience of implementing the
applications using SYCL, and compared the performance and programming portability of the SYCL implementations with the
OpenCL implementations on an Intel® Xeon® CPU and an Iris® Pro integrated GPU. The results are promising. For the Heart
Wall application, the SYCL implementation is on average 15% faster than the OpenCL implementation on the GPU. For the
Particle Filter application, the SYCL implementation is 3% slower than the OpenCL implementation on the GPU, but it is
75% faster on the CPU. Using lines of code as an indicator of programming productivity, the SYCL host program reduces
the lines of code of the OpenCL host program by 52% and 38% for the Heart Wall and Particle Filter applications,
respectively.
