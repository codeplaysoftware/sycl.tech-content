---
contributor: max
date: '2021-01-20T08:17:24.490000+00:00'
external_url: https://techdecoded.intel.io/resources/solving-a-2d-heat-equation-using-data-parallel-c-dpc/?linkId=100000027947363#gs.qinbf4
image: ../../../static/images/news/2021-01-20-solving-a-2d-heat-equation-using-sycl-and-dpc.webp
title: Solving a 2D Heat Equation Using SYCL and DPC++
tags:
  - prace
  - dpc++
  - oneapi
  - intel
  - advanced-computing
---

The heat equation is a problem commonly used in parallel computing tutorials. In fact, we start from one such exercise
published by the Partnership for Advanced Computing in Europe (PRACE). The original code1 describes a C and MPI
implementation of a 2D heat equation, discretized into a single point stencil.

The 2D plane is divided into cells, with each cell being updated every timestep based on the previous values of itself
and its four neighbours.

A more detailed explanation of the problem can be found on the PRACE repository.
