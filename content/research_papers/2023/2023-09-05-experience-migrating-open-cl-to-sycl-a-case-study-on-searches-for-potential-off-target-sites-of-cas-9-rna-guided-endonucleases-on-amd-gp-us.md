---
contributor: scott
date: '2023-09-05T08:08:10.490000+00:00'
title: 'Experience Migrating OpenCL to SYCL: A Case Study on Searches for Potential Off-Target Sites of Cas9 RNA-Guided Endonucleases on AMD GPUs'
external_url: https://ieeexplore.ieee.org/document/10256881
authors:
  - name: Zheming Jin
    affiliation: Oak Ridge National Laboratory
  - name: Jeffrey S. Vetter
    affiliation: Oak Ridge National Laboratory
tags:
  - sequence
  - analysis
  - opencl
  - migrating
  - cas9
  - rna
---

Cas-OFFinder is a popular application for genome editing. Its OpenCL implementation searches potential off-target sites
in parallel on a GPU. In this work, we describe our experience migrating the application from OpenCL to SYCL. Evaluating
the performance of the OpenCL and SYCL applications using human genome sequences shows that the SYCL program could
achieve performance portability on the target GPUs. Exploring the optimizations of the hotspot kernel in SYCL may
further improve the performance of the application by 9% to 23%.
