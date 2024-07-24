---
contributor: scott
date: '2023-10-17T08:08:10.490000+00:00'
title: 'Comparing Performance and Portability Between CUDA and SYCL for Protein Database Search on NVIDIA, AMD, and Intel GPUs'
external_url: https://ieeexplore.ieee.org/document/10306194
authors:
  - name: Manuel Costanzo
  - name: Enzo Rucci
  - name: Carlos García-Sánchez
  - name: Marcelo Naiouf
  - name: Manuel Prieto-Matías
tags:
  - cuda
  - gpu
  - portability
  - performance
  - comparison
  - nvidia
  - amd
  - intel
---

The heterogeneous computing paradigm has led to the need for portable and efficient programming solutions that can
leverage the capabilities of various hardware devices, such as NVIDIA, Intel, and AMD GPUs. This study evaluates the
portability and performance of the SYCL and CUDA languages for one fundamental bioinformatics application (
Smith-Waterman protein database search) across different GPU architectures, considering single and multi-GPU
configurations from different vendors. The experimental work showed that, while both CUDA and SYCL versions achieve
similar performance on NVIDIA devices, the latter demonstrated remarkable code portability to other GPU architectures,
such as AMD and Intel. Furthermore, the architectural efficiency rates achieved on these devices were superior in 3 of
the 4 cases tested. This brief study highlights the potential of SYCL as a viable solution for achieving both
performance and portability in the heterogeneous computing ecosystem.
