---
contributor: rod
date: '2019-07-01T10:26:09+02:00'
external_url: https://hgpu.org/?p=18968
image: ../../../static/images/news/2019-07-01-resyclator-transforming-cuda-c-source-code-into-sycl.webp
title: 'ReSYCLator: Transforming CUDA C++ Source Code into SYCL'
tags:
  - resyclator
  - transforming
  - cuda
  - migration
  - porting
---

CUDA while very popular, is not as flexible with respect to target devices as OpenCL. While parallel algorithm research
might address problems first with a CUDA C++ solution, those results are not easily portable to a target not directly
supported by CUDA. In contrast, a SYCL C++ solution can operate on the larger variety of platforms supported by OpenCL.
ReSYCLator is a plug-in for the C++ IDE Cevelop[2], that is itself an extension of Eclipse-CDT. ReSYCLator bridges the
gap between algorithm availability and portability, by providing automatic transformation of CUDA C++ code to SYCL C++.
A first attempt basing the transformation on NVIDIA’s Nsight Eclipse CDT plug-in showed that Nsight’s weak integration
into CDT’s static analysis and refactoring infrastructure is insufficient. Therefore, an own CUDA-C++ parser and CUDA
language support for Eclipse CDT was developed (CRITTER) that is a sound platform for transformations from CUDA C++
programs to SYCL based on AST transformations.
