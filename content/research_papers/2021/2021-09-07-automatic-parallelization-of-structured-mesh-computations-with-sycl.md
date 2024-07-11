---
contributor: scott
date: '2021-06-07T08:08:10.490000+00:00'
title: 'Automatic Parallelization of Structured Mesh Computations with SYCL'
external_url: https://ieeexplore.ieee.org/document/9555976
authors:
  - name: Gábor Dániel Balogh
    affiliation: Pázmány Péter Catholic University
  - name: István Reguly
    affiliation: Pázmány Péter Catholic University
tags:
  - parallel-programming
  - nvidia
  - intel
---

Structured meshes are widely used for scientific computations such as Computational Fluid Dynamics (CFD) applications or
finance. Modern applications often have grid points in the millions. To perform such computations parallelisation is
crucial. However it is unfeasible to port each application every time a new architecture arrives, hence in recent years
the demand for automatic parallelisation and optimisation for the used hardware is increasing. The OPS (Oxford Parallel
library for Structured mesh solvers) has shown good performance and scaling on a wide range of HPC architectures. This
research aims to extend the OPS framework with a SYCL backend to extend the range of architectures that OPS can support
and further increase Performance Portability of OPS applications. The performance of the Intel OneAPI is struggling with
reductions due to high synchronisation cost, but shows promising performance gain on builtin reduction constructs on an
Intel® Xeon® Gold 6226R. We compare the performance of hipSYCL on NVidia V100 GPU to the CUDA implementations.
