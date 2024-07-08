---
contributor: max
date: '2022-05-10T12:58:35.209000+00:00'
external_url: https://www.intel.com/content/www/us/en/developer/articles/technical/cuda-sycl-migration-jacobi-iterative-method.html
image: ../../../static/images/news/2022-05-10-migrating-the-jacobi-iterative-method-from-cuda-to-sycl.webp
title: 'Migrating the Jacobi Iterative Method from CUDA to SYCL'
tags:
  - cuda
  - nvidia
  - migration
  - intel
  - vtune
---

The Jacobi iterative method is used to find approximate numerical solutions for systems of linear equations of the form
Ax = b in numerical linear algebra, which is diagonally dominant. The algorithm starts with an initial estimate for x
and iteratively updates it until convergence. The Jacobi method is guaranteed to converge if matrix A is diagonally
dominant.

## CUDA to SYCL migration approach

This document covers two approaches for CUDA to SYCL migration:

* The first approach is manual migration by analyzing CUDA source and replacing all CUDA-specific calls with equivalent
  SYCL calls. This approach helps a CUDA developer to understand SYCL programming. Once the migration is complete, we do
  performance analysis using VTuneTM Profiler and Intel® Advisor Roofline to understand the performance bottlenecks. We
  then look at optimizing the code for performance.
* The second approach is using Intel® oneAPI Data Parallel C++ Compatibility Tool (DPCT) to automatically migrate CUDA
  source to SYCL source. The tool migrates 80–90 percent of the code and generates a warning for the rest, which has to
  be manually migrated to SYCL. We look at DPCT generated warnings and learn how to migrate the code that was not
  migrated by the DPCT. This approach helps to accelerate the migration of CUDA source to SYCL and has proven especially
  helpful for large code bases.
