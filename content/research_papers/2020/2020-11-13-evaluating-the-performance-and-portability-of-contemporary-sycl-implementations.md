---
contributor: scott
date: '2020-11-13T08:08:10.490000+00:00'
title: 'Evaluating the Performance and Portability of Contemporary SYCL Implementations'
external_url: https://ieeexplore.ieee.org/document/9309045
authors:
  - name: Beau Johnston
  - name: Jeffrey S. Vetter
  - name: Josh Milthorpe
tags:
  - benchmarks
  - performance
  - portability
---

SYCL is a single-source programming model for heterogeneous systems; it promises improved maintainability, productivity,
and opportunity for compiler optimization, when compared to accelerator specific programming models. Several
implementations of the SYCL standard have been developed over the past few years, including several backends using
contemporary accelerator languages, like OpenCL, CUDA, and HIP. These implementations vary widely in their support for
specific features of the standard and in their performance. As SYCL grows in popularity, developers need to know how
features are implemented across popular implementations in order to make proper design choices. In this paper, we
evaluate the existing SYCL implementations for important SYCL features across a range of hardware in order to understand
SYCL's performance and portability. This work uses the newest SYCL benchmark suite (SYCL-Bench, 38 kernels) to evaluate
these four existing implementations, comparing support of language features across backends and highlighting feature
completeness and performance. For features, we focus on the five major SYCL parallel constructs, using a motivating
example of the matrix multiplication benchmark. Our results show that the basic data parallelism construct is the best
choice for performance on current SYCL implementations, and we identify opportunities for improvement in several of the
SYCL implementations.
