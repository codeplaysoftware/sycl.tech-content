---
contributor: scott
date: '2022-11-13T08:08:10.490000+00:00'
title: 'A First Step towards Support for MPI Partitioned Communication on SYCL-programmed FPGAs'
external_url: https://ieeexplore.ieee.org/document/10027494
authors:
  - name: Steffen Christgau
    affiliation: Zuse Institute Berlin, Berlin
  - name: Marius Knaust
    affiliation: Zuse Institute Berlin, Berlin
  - name: Thomas Steinke
    affiliation: Zuse Institute Berlin, Berlin
tags:
  - fpgas
  - mpi
  - oneapi
  - dpc++
---

Version 4.0 of the Message Passing Interface standard introduced the concept of Partitioned Communication, which adds
support for multiple contributions to a communication buffer. Although initially targeted at multithreaded MPI
applications, Partitioned Communication currently receives attraction in the context of accelerators, especially GPUs.
In this publication it is demonstrated that this communication concept can be implemented for SYCL-programmed FPGAs.
This includes a discussion of the design space and the presentation of a prototype implementation. Experimental results
show that a lightweight implementation on top of an existing MPI library is possible. The presented approach also
reveals issues in both the SYCL and the MPI standard, which needs to be addressed for improved support for the intended
communication style.
