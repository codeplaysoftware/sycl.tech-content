---
contributor: max
date: '2024-01-24T08:08:10.490000'
title: 'Lessons Learned Migrating CUDA to SYCL: A HEP Case Study with ROOT RDataFrame'
external_url: https://arxiv.org/pdf/2401.13310
authors:
  - name: Jolly Chen
  - name: Monica Dessole
  - name: Ana Lucia Varbanescu
tags:
  - sycl
  - gpu
  - cuda
  - heterogeneous-programming
---

The world’s largest particle accelerator, located at CERN, produces petabytes of data that need to be analysed
efficiently, to study the fundamental structures of our universe. ROOT is an open-source C++ data analysis framework,
developed for this purpose. Its high-level data analysis interface, RDataFrame, currently only supports CPU parallelism.
Given the increasing heterogeneity in computing facilities, it becomes crucial to efficiently support GPGPUs to take
advantage of the available resources. SYCL allows for a single-source implementation, which enables support for
different architectures. In this paper, we describe a CUDA implementation and the migration process to SYCL, focusing on
a core high energy physics operation in RDataFrame – histogramming. We detail the challenges that we faced when
integrating SYCL into a large and complex code base. Furthermore, we perform an extensive comparative performance
analysis of two SYCL compilers, AdaptiveCpp and DPC++, and the reference CUDA implementation. We highlight the
performance bottlenecks that we encountered, and the methodology used to detect these. Based on our findings, we provide
actionable insights for developers of SYCL applications.
