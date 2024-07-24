---
contributor: scott
date: '2023-10-31T08:08:10.490000+00:00'
title: 'Accelerating Hyperdimensional Classifier with SYCL'
external_url: https://ieeexplore.ieee.org/document/10321902
authors:
  - name: Zheming Jin
  - name: Jeffrey S. Vetter
tags:
  - parallel
  - search
  - dimension
  - accelerating
  - performance
  - mathematial
---

Hyperdimensional (HD) computing is based on mathematical properties of high-dimensional spaces which show remarkable
agreement with brain-controlled behaviors. Rahimi et al. describe an HD-based classifier for the task of
recognizing the languages of text samples. It consists of an encoding module that generates a hypervector for each
text sample and a search module that compares the generated vector with a set of trained hypervectors. One of the
challenges of the HD computing research is that hardware simulation of the classifier is extremely time-consuming with
many text samples. To address the challenge, the classifier may be modelled as a compute routine in Open Computing
Language (OpenCL) and executed on graphics processing units (GPUs) for acceleration. While OpenCL allows for
writing parallel and portable programs targeting vendors’ computing platforms, writing an OpenCL program tends to be
error-prone and time-consuming. Built on the underlying concepts, portability, and efficiency of OpenCL, SYCL defines a
single-source abstract layer in C++. In this work, we adopt the SYCL abstraction for productivity and performance.
Compared to the OpenCL application, the SYCL application approximately reduces the lines of code by 24% and increases
the performance by 2.13X on four GPUs. In addition, the speedups of executing the application in parallel over the
fastest serial execution on the four heterogeneous computing systems are approximately 2.11X, 1.23X, 1.56X, and 1.03X,
respectively.
