---
contributor: scott
date: '2022-05-18T08:08:10.490000+00:00'
title: 'A Case Study on the HACCmk Routine in SYCL on Integrated Graphics'
external_url: https://ieeexplore.ieee.org/document/9150310
authors:
  - Zheming Jin
  - Vitali Morozov
  - Hal Finkel
tags:
  - compute
  - haccmk
  - integrated-grapghics
  - case-study
---

As opposed to the Open Computing Language (OpenCL) programming model in which host and device codes are generally
written in different languages, the SYCL programming model can combine host and device codes for an application in a
type-safe way to improve development productivity. In this paper, we chose the HACCmk routine, a representative
compute-bound kernel, as a case study on the performance of the SYCL programming model targeting a heterogeneous
computing device. More specifically, we introduced the SYCL programming model, presented the OpenCL and SYCL
implementations of the routine, and compared the performance of the two implementations using the offline and online
compilation on Intel® IrisTM Pro integrated GPUs. We found that the overhead of online compilation may become
significant compared to the execution time of a kernel. Compared to the performance of OpenCL implementations, the SYCL
implementation can maintain the performance using the offline compilation. The number of execution units in a GPU are
critical to improving the raw performance of a compute-bound kernel.
