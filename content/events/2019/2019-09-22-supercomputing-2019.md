---
contributor: rod
date: '2019-09-22T10:57:29+01:00'
ends: '2019-11-22T01:00:00+01:00'
starts: '2019-11-17T01:00:00+01:00'
title: Supercomputing 2019
location: 'Denver, CO, USA'
external_url: 'https://sc19.supercomputing.org/'
---

SC (formerly Supercomputing), the International Conference for High Performance Computing, Networking, Storage and
Analysis, is the annual conference established in 1988 by the Association for Computing Machinery and the IEEE Computer
Society.

## SYCL Sessions at Supercomputing 2019

### [SYCL: A Single-Source C++ Standard for Heterogeneous Computing](https://sc19.supercomputing.org/?post_type=page&p=3479&id=pec404&sess=sess110)

**Ronan Keryell (Xilinx)**

Many HPC programmers have not heard of SYCL, however, with the increasing importance of modern C++ in HPC, or just
seeking alternatives to proprietary languages, SYCL is becoming critical as a vendor neutral way to write C++ code that
embraces heterogeneous parallelism. SYCL is an open standard. There are multiple implementations available, both open
source and commercial.

### [Data Flow Pipes: A SYCL Extension for Spatial Architectures](https://sc19.supercomputing.org/presentation/?sess=sess110&id=ws_h2rc111#038;id=ws_h2rc111)

**Simon Mcintosh-Smith (University of Bristol)**

FIFOs are a common construct in design for spatial and data flow architectures. OpenCL 2.0 defined a “pipe” feature to
expose the FIFO construct, but the design didn’t meet all needs of spatial architectures. This talk describes a pipes
extension to the Khronos SYCL single-source, C++-based programming framework, that exposes a pipe abstraction which
closes the gaps in the OpenCL design, while also offering a more usable interface. The C++ type system is leveraged to
provide static connectivity guarantees without extensive compiler implementation effort, and to provide well-defined
interaction with C++ features. The described extension provides a usable interface that can also act as a substrate for
additional abstractions to be built on top. This talk will motivate the utility of FIFOs/pipes in high level language
FPGA design, describe the SYCL pipes extension and its mapping to SPIR-V and OpenCL, and provide examples of use in
common spatial design patterns.

### [DPC++ - A Technical Overview](https://intel.lineupr.com/sc19/item/dpc-a-technical-overview)

**Max Domeika (Intel)**

DPC++ is a new language to enact parallelism upon accelerators like Intel's GPUs and FPGAs. DPC++ is based upon Khronos
SYCL.

### [Lab: oneAPI Workshop](https://intel.lineupr.com/sc19/item/lab-oneapi-workshop)

**Ben Odom, Praveen Kundurthy, Rudy Cazabon (Intel)**

This lab will provide an overview of the oneAPI progamming model, language, libraries, tools and development process for
DPC++

### [An open ecosystem for HPC developers](https://intel.lineupr.com/sc19/item/an-open-ecosystem-for-hpc-developers)

**Andrew Richards (Codeplay Software)**

Developers can currently use SYCL to target a wide range of processors, including those from Intel, Arm, NVidia and
Renesas using ComputeCpp. Alongside this are a wide range of open source projects offering frameworks for BLAS, DNN and
more. During this presentation you can find out more about the implementations of SYCL that are available and the
projects that harness the SYCL standard for acceleration.

### [Performance Portability of a Wilson Dslash Stencil Operator Mini-App Using Kokkos and SYCL](https://sc19.supercomputing.org/?post_type=page&p=3479&id=ws_p3hpc116&sess=sess132)

**Bálint Joó, Thorsten Kurth, M. A. Clark, Jeongnim Kim, Christian Robert Trott, Dan Ibanez, Daniel Sunderland, Jack
Deslippe (Thomas Jefferson Accelerator Facility)**

We describe our experiences in creating mini-apps for the Wilson-Dslash stencil operator for Lattice Quantum
Chromodynamics using the Kokkos and SYCL programming models. In particular, we comment on the performance achieved on a
variety of hardware architectures, limitations we have reached in both programming models and how these have been
resolved by us, or may be resolved by the developers of these models.

### [Birds of a Feather: Khronos SYCL Heterogeneous C++ Status and Directions](https://sc19.supercomputing.org/presentation/?id=bof201&sess=sess307)

**Simon Mcintosh-Smith (University of Bristol)**

Many HPC programmers have not heard of SYCL, however, with the increasing importance of modern C++ in HPC, or just
seeking alternatives to proprietary languages, SYCL is becoming critical as a vendor neutral way to write C++ code that
embraces heterogeneous parallelism. SYCL is an open standard. There are multiple implementations available, both open
source and commercial.

In this BoF, experts and SYCL implementers will explain its advantages, how the language is governed, where it is going,
and why you need to be aware of it if you are intending to write C++ code which targets HPC machines.

### [Heterogeneous and Distributed ISO C++ for HPC Status and Directions](https://sc19.supercomputing.org/presentation/?id=bof200&sess=sess288)

**Hal Finkel (Argonne National Laboratory)**

After last two year's (SC17, SC18) successful Heterogeneous & Distributed Computing in C++ for HPC BoF, there was
popular demand for continuing updates on the progress of adding these capabilities into ISO C++. This includes task
dispatch with executors and the property mechanism, data layout, affinity, error handling and Asynchronous execution.

We have also finalized C++20, and this BoF will provide updates on what supports distributed and heterogeneous computing
from active participants in the standardization process. We will also look ahead on what is possible for C++20 and for
C++23.
