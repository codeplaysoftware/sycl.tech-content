---
contributor: scott
date: '2024-09-25T09:43:10'
title: 'miniLB: A Performance Portability Study of Lattice-Boltzmann Simulations'
external_url: 'https://www.arxiv.org/abs/2409.16781'
authors:
  - Luigi Crisci,
  - Biagio Cosenza
  - Giorgio Amati
  - Matteo Turisini
tags:
  - sycl
  - lbm
  - cfd
  - fluid-dynamics
  - portability
---

The Lattice Boltzmann Method (LBM) is a computational technique of Computational Fluid Dynamics (CFD) that has gained
popularity due to its high parallelism and ability to handle complex geometries with minimal effort. Although LBM
frameworks are increasingly important in various industries and research fields, their complexity makes them difficult
to modify and can lead to suboptimal performance. This paper presents miniLB, the first, to the best of our knowledge,
SYCL-based LBM this http URL addresses the need for a performance-portable LBM proxy app capable of abstracting complex
fluid dynamics simulations across heterogeneous computing systems. We analyze SYCL semantics for performance portability
and evaluate miniLB on multiple GPU architectures using various SYCL implementations. Our results, compared against a
manually-tuned FORTRAN version, demonstrate effectiveness of miniLB in assessing LBM performance across diverse
hardware, offering valuable insights for optimizing large-scale LBM frameworks in modern computing environments.
