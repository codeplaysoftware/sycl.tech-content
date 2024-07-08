---
contributor: rod
date: '2023-08-28T09:26:51.431486'
title: Khronos Sycl Language Framework for C++ Accelerators
external_url: https://www.youtube.com/watch?v=Yz-_gDpj4vc
type: presentation
tags:
  - mips
  - accuconf
  - presentation
  - conference
  - exascale
featuring:
  - username: michael
---

Have you ever wanted to take advantage of all the MIPS in your machine with one programming language? Have you ever
wanted to support any kind of offload devices in C++, be they FPGA, GPUs, matrix/tensors, or DSPs? Many people have by
augmenting a SYCL compiler. Have you wondered why US National Labs are choosing SYCL as a standard programming model for
exascale computing? This is because they know maximum performance can be achieved with a combination of host and
accelerator devices in any vendor combination, so they choose SYCL. Khronos SYCL is a framework language built on top of
Modern C++. It is backed by an open standard in Khronos and enables ML frameworks and Standard C++ code on top of
template libraries with lambda functions that have host and accelerate device code in a single source, but still enable
separate compilation of host and device code. The device SYCL compiler may employ kernel fusion for better performance
and the host CPU compiler can be any C++ compiler, from clang, GCC, VS C++, or IBM XL compiler. Many people have built
SYCL compiler additions to dispatch to any variety of devices very quickly, from students to academia, to industry.
There are already a number of backends including CUDA, PTX, OpenMP, AMD, NEC, Huawei, Kokkos, Raja, and TBB in addition
to OpenCL. There are also many interesting use cases with complex modern C++. PyTorch, Blender, ray-tracing, Flashlight
ML, Eigen and Tensorflow, Gromacs, and CERN’s ATLAS experiment for high energy physics. This talk from members of the
SYCL and C++ community will talk about highlighted features from the latest SYCL 2020 as related to ISO C++. SYCL can
serve even more Extreme Heterogeneity where Data Movement is still King. We also are entering the era of software and
hardware Codesign with extreme Heterogeneity and SYCL can be a part of a standard programming model for all HPC,
Embedded AI/ML, and Automotive This talk will showcase these features and show how SYCL 2020 has increased
expressiveness and simplicity for modern C++ heterogeneous programming.
