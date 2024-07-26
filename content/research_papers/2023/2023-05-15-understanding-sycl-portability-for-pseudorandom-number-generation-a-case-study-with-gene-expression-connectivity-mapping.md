---
contributor: scott
date: '2023-05-15T08:08:10.490000+00:00'
title: 'Understanding SYCL Portability for Pseudorandom Number Generation: a Case Study with Gene-Expression Connectivity Mapping'
external_url: https://ieeexplore.ieee.org/document/10196601
authors:
  - Zheming Jin
  - Jeffrey S. Vetter
tags:
  - portability
  - pseudorandom
  - random-number
  - bioinformatics
---

Towards the goal of improving functional and performance portability of SYCL, we study a bioinformatics application that
has been accelerated with CUDA and fast pseudorandom number generation on a GPU. We describe the experience of migrating
pseudorandom number generation from CUDA to SYCL, evaluate the performance of pseudorandom number generators using the
CUDA random number generation library, suggest the support of the XORWOW pseudorandom number generator in the oneAPI
math kernel library (oneMKL) interface for performance portability, and identify the performance gap using the MKL
interface in SYCL that supports pseudorandom number generation with third-party libraries. We hope that the results are
valuable for the development of the SYCL ecosystem.
