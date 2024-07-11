---
contributor: scott
date: '2024-03-02T08:08:10.490000+00:00'
title: 'Experiences Building an MLIR-Based SYCL Compiler'
external_url: https://ieeexplore.ieee.org/document/10444866
authors:
  - name: Ettore Tiotto
    affiliation: Intel Corporation
  - name: Víctor Pérez
    affiliation: Codeplay Software
  - name: Whitney Tsang
    affiliation: Intel Corporation
  - name: Lukas Sommer
    affiliation: Codeplay Software
  - name: Julian Oppermann
    affiliation: Codeplay Software
  - name: Victor Lomüller
    affiliation: Codeplay Software
  - name: Mehdi Goli
    affiliation: Codeplay Software
  - name: James Brodman
    affiliation: Intel Corporation
tags:
  - SYCL
  - MLIR
  - compiler
  - optimization
  - heterogeneous-programming
---

Similar to other programming models, compilers for SYCL, the open programming model for heterogeneous computing based on
C++, would benefit from access to higher-level intermediate representations. The loss of high-level structure and
semantics caused by premature lowering to low-level intermediate representations and the inability to reason about host
and device code simultaneously present major challenges for SYCL compilers. The MLIR compiler framework, through its
dialect mechanism, allows to model domain-specific, high-level intermediate representations and provides the necessary
facilities to address these challenges. This work therefore describes practical experience with the design and
implementation of an MLIR-based SYCL compiler. By modeling key elements of the SYCL programming model in host and device
code in the MLIR dialect framework, the presented approach enables the implementation of powerful device code
optimizations as well as analyses across host and device code. Compared to two LLVM-based SYCL implementations, this
yields speedups of up to 4.3x on a collection of SYCL benchmark applications. Finally, this work also discusses
challenges encountered in the design and implementation and how these could be addressed in the future.
