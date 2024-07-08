---
contributor: max
date: '2020-04-28T14:30:36+02:00'
title: Debugging SYCL programs on heterogeneous Intel architectures
external_url: https://www.youtube.com/watch?v=-gQMHMdwamw
type: presentation
featuring:
  - name: Natalia Saiapova
    affiliation_at_video_production_time: Intel Corporation
---

Intel recently announced a large initiative named oneAPI that provides a direct programming model based on SYCL. As part
of the oneAPI distribution, we developed a debugger that can be used to debug SYCL programs that offload kernels to CPU,
GPU, or FPGA emulator devices. The debugger is based on GDB. It allows programmers to inspect the host and kernel
portion of their SYCL programs seamlessly in the same debug session. To realize the debugger, we made enhancements to
GDB including SIMD-based thread views and C++-related improvements. In this work we present the general architecture of
the debugger, provide a sample session of how it can be used to debug a SYCL kernel running on a GPU, and discuss the
encountered and anticipated challenges during the development phase. Currently a beta version of the debugger is
publicly available.
