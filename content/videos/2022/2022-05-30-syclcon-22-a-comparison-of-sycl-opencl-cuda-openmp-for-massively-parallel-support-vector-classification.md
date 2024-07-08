---
contributor: max
date: '2022-05-30T10:57:44.284000+00:00'
title: SYCLcon 2022 - A Comparison of SYCL, OpenCL, CUDA, & OpenMP for Massively Parallel Support Vector Classification
external_url: https://www.youtube.com/watch?v=-yphY7Rtltc
type: presentation
tags:
  - artificial-intelligence
  - ai
  - supercomputing
  - hpc
  - opencl
  - cuda
  - openmp
  - comparisons
featuring:
  - name: Marcel Breyer
    affiliation_at_video_production_time: University of Stuttgart
  - name: Alexander Van Craen
    affiliation_at_video_production_time: University of Stuttgart
  - name: Dirk Pflüger
    affiliation_at_video_production_time: University of Stuttgart
---

In scientific computing and Artificial Intelligence (AI), which both rely on massively parallel tasks, frameworks like
the Compute Unified Device Architecture (CUDA) and the Open Computing Language (OpenCL) are widely used to harvest the
computational power of accelerator cards, in particular of Graphics Processing Units (GPUs). A few years ago, GPUs from
NVIDIA were used almost exclusively for these tasks but meanwhile, AMD and Intel are increasing their shares of the GPU
market. This introduces many new challenges for code development, as the prevailing CUDA code can only run on NVIDIA
hardware and must be adapted or even completely rewritten to run on GPUs from AMD or Intel.

In this paper, we compare the different competing programming frameworks OpenMP, CUDA, OpenCL, and SYCL, paying special
attention to the two SYCL implementations hipSYCL and DPC++. Thereby, we investigate the different frameworks with
respect to their usability, performance, and performance portability on a variety of hardware platforms from different
vendors, i.e., GPUs from NVIDIA, AMD, and Intel and Central Processing Units (CPUs) from AMD and Intel. Besides
discussing the runtimes of these frameworks on the different hardware platforms, we also focus our comparison on the
differences between the nd\_range kernel formulation and the SYCL specific hierarchical kernels.

Our Parallel Least Squares Support Vector Machine (PLSSVM) library implements backends for the four previously mentioned
programming frameworks for a Least Squares Support Vector Machine (LS-SVM). At its example, we show which of the
frameworks is best suited for a standard workload that is frequently employed in scientific computing and AI, depending
on the target hardware: The most computationally intensive part of our PLSSVM library is solving a system of linear
equations using the Conjugate Gradient (CG) method. Specifically, we parallelize the implicit matrix-vector
multiplication inside the CG method, a workload common in many scientific codes.

The PLSSVM code, utility scripts, and documentation are all available on GitHub: https://github.com/SC-SGS/PLSSVM.
