---
contributor: rod
date: '2024-06-20T13:59:34.162543'
external_url: https://link.springer.com/article/10.1007/s11227-024-05957-6
title: 'SYCL in the edge: performance and energy evaluation for heterogeneous acceleration'
image: ../../../static/images/news/2024-06-20-sycl-in-the-edge-performance-and-energy-evaluation-for-heterogeneous-acceleration.webp
tags:
  - edge-computing
  - performance
  - hpc
  - portability
  - polybench
  - cuda
---

Edge computing is essential to handle increasing data volumes and processing capacities. It provides real-time and
secure data processing near data sources, like smart devices, alleviating cloud computing energy use, and saving
network bandwidth. Specialized accelerators, like GPUs and FPGAs, are vital for low-latency edge computing but the
requirements to customized code for different hardware and vendors suppose important compatibility issues.

This paper evaluates the potential of SYCL in addressing code portability issues encountered in edge computing. We
employed the Polybench suite to compare various SYCL implementations, specifically DPC++ and AdaptiveCpp, with the
native solution, CUDA. The disparity between SYCL implementations was negligible, at just 5%. Furthermore, we
evaluated SYCL in the context of specific edge computing applications such as video processing using three different
optical flow algorithms. The results revealed a slight performance gap of 3% when transitioning from CUDA to SYCL.

Upon evaluating energy consumption, the observed difference ranged from, depending on the application utilized. These
gaps are the price one may need to pay when achieving the ability to successfully run the same code on two distinct
edge boards. These findings underscore SYCL’s capacity to increase productivity in terms of development costs and
facilitate IoT deployment without being locked into a particular platform or manufacturer.
