---
contributor: scott
date: '2020-02-27T10:57:29+01:00'
ends: '2020-02-27T01:00:00+01:00'
starts: '2020-02-27T01:00:00+01:00'
title: Developing parallel applications with SYCL, an open standards alternative to CUDA
location: 'Edinburgh, Scotland'
external_url: 'https://www.macs.hw.ac.uk/cs/seminars/20200227.html'
---

This talk will introduce application development using the SYCL programming model. SYCL allows users to write standard
C++ code which is then executed on a range of heterogeneous architectures including CPUs, GPUs, DSPs, FPGAs and other
accelerators. On top of this SYCL also provides a high-level abstraction which allows users to describe their
computations as a task graph with data dependencies, while the SYCL runtime performs data dependency analysis and
scheduling. SYCL also supports a host device which will execute on the host CPU with the same execution and memory model
guarantees as OpenCL for debugging purposes, and a fallback mechanism which allows an application to recover from
failure. 
