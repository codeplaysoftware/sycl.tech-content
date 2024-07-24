---
contributor: rod
date: '2019-09-02T10:57:29+01:00'
title: Performance Portability of Multi-Material Kernels
external_url: https://sc19.supercomputing.org/proceedings/workshops/workshop_files/ws_p3hpc106s2-file1.pdf
authors:
  - name: Istvan Z. Reguly
tags:
  - portability
  - performance
  - benchmarking
  - openaac
  - openmp
---

Trying to improve performance, portability, and productivity ance portability and code divergence metrics, contrasting
performance, portability, and productivity of an application presents non-trivial trade-offs, which are often difficult
to quantify. Recent work has developed metrics for performance portability, as well some aspects of productivity - in
this case study, we present a set of challenging computational kernels and their implementations from the domain of
multi-material simulations, and evaluate them using these metrics. Three key kernels are implemented using OpenMP,OpenMP
offload, OpenACC, CUDA, SYCL, and KOKKOS, and tested on ARM ThunderX2, IBM Power 9, Intel KNL, Broadwell, and Skylake
CPUs, as well as NVIDIA P100 andV100 GPUs. We also consider the choice of compilers, evaluating LLVM/Clang, GCC, PGI,
Intel, IBM XL, and Cray compilers, where available. We present a detailed performance analysis, calculate perform
