---
contributor: max
date: '2024-03-09T08:08:10.490000+00:00'
title: 'XFLUIDS: A SYCL-based unified cross-architecture heterogeneous simulation solver for compressible reacting flows'
external_url: https://arxiv.org/abs/2403.05910
authors:
  - name: Jinlong Li
  - name: Shucheng Pan
tags:
  - sycl
  - hpc
  - cuda
  - hip
  - heterogeneous-programming
---

We present a cross-architecture high-order heterogeneous Navier-Stokes simulation solver, XFluids, for compressible
reacting multi-component flows on different platforms. The multi-component reacting flows are ubiquitous in many
scientific and engineering applications, while their numerical simulations are usually time-consuming to capture the
underlying multiscale features. Although heterogeneous accelerated computing is significantly beneficial for large-scale
simulations of these flows, effective utilization of various heterogeneous accelerators with different architectures and
programming models in the market remains a challenge. To address this, we develop XFluids by SYCL, to perform
acceleration directly targeted to different devices, without translating any source code. A variety of optimization
techniques have been proposed to increase the computational performance of XFluids, including adaptive range assignment,
partial eigen-system reconstruction, hotspot device function optimizations, etc. This solver has been open-sourced, and
tested on multiple GPUs from different mainstream vendors, indicating high portability. Through various benchmark cases,
the accuracy of XFluids is demonstrated, with approximately no efficiency loss compared to existing GPU programming
models, such as CUDA and HIP. In addition, the MPI library is used to extend the solver to multi-GPU platforms, with the
GPU-enabled MPI supported. With this, the weak scaling of XFluids for multi-GPU devices is larger than 95% for 1024
GPUs. Finally, we simulate both the inert and reactive multi-component shock-bubble interaction problems with
high-resolution meshes, to investigate the reacting effects on the mixing, vortex stretching, and shape deformation of
the bubble evolution.
