---
contributor: scott
date: '2022-12-23T08:08:10.490000+00:00'
title: 'A memory bank conflict prevention mechanism for SYCL on SX-Aurora TSUBASA'
external_url: https://ieeexplore.ieee.org/document/9644088
authors:
  - name: Wenbin Wang
    affiliation: Tohoku University
  - name: Jiahao Li
    affiliation: Tohoku University
  - name: Yohichi Shimomura
    affiliation: Tohoku University
  - name: Hiroyuki Takizawa
    affiliation: Tohoku University
tags:
  - performance
  - runtime
  - bandwidth
  - programming
  - supercomputers
  - libraries
  - kernel
---

A modern vector supercomputer, NEC SX-Aurora TSUBASA, consists of Vector Hosts (VHs) and Vector Engines (VEs). A VH is a
standard CPU to perform general tasks and hosting the VEs, while a VE is a special device designed to operate on long
vectors, and provides world’s top-class theoretical memory bandwidth of 1.53 TB/s. However, in some cases, the sustained
memory bandwidth achieved in practical use is far from the theoretical one. This is because frequent memory bank
conflicts cause performance degradation. The purpose of this work is to achieve high sustained memory bandwidth by
introducing a bank conflict prevention mechanism to a SYCL implementation, named neoSYCL. The evaluation results using
several kernels clearly show that this mechanism can be used without changing the standard interface defined in the SYCL
specification. It is also demonstrated that the proposed approach can successfully prevent memory bank conflicts, and
thus achieve higher sustained memory bandwidths than the original one, meaning to expect higher sustained performance on
memory-intensive scientific applications.
