---
contributor: scott
date: '2019-09-02T10:57:29+01:00'
title: SYCL Code Generation for Multigrid Methods
external_url: https://www.researchgate.net/publication/333139223_SYCL_Code_Generation_for_Multigrid_Methods
authors:
  - name: Stefan Groth
  - name: Christian Schmitt
  - name: Jürgen Teich
  - name: Frank Hannig
tags:
  - multigrid
  - c++
---

Multigrid methods are fast and scalable numerical solvers for partial differential equations (PDEs) that possess a large
design space for implementing their algorithmic components. Code generation approaches allow formulating multigrid
methods on a higher level of abstraction that can then be used to define a problem and hardware-specific solution. Since
these problems have considerable implementation variability, it is crucial to define a general mapping of core
components in multigrid methods to the target software. With SYCL there exists a high-level C++ abstraction layer 
that is capable of targeting a multitude of possible architectures. We contribute a general way to map multigrid 
components to SYCL functionality and provide a performance evaluation for specific algorithmic components.
