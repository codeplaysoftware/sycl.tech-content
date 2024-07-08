---
contributor: rod
date: '2021-12-22T09:07:51.291000+00:00'
title: CppCon 2021 - Heterogeneous Modern C++ with SYCL 2020
external_url: https://www.youtube.com/watch?v=5awOtaJw8XM
type: presentation
featuring: 
  - username: michael
  - username: gordon
---

Heterogeneous programming in C++ used to be hard and low-level. Today, Khronos SYCL for Modern C ++ works with different
libraries, ML frameworks and Standard C++ code on top of template libraries with lambda functions that separate host and
accelerate device code in a single source, but still enables separate compilation of host and device code. The device
SYCL compiler may employ kernel fusion for better performance and the host CPU compiler can be any C++ compiler, from
clang, gcc, VS C++, or IBM XL compiler. SYCL enables accelerated code to pass into device OpenCL compilers or other
backends to dispatch to any variety of devices.

This talk from members of the SYCL community will talk about highlighted features from the latest SYCL 2020. SYCL 2020
is released after 3 years of intense work with significant adoption in Embedded, Desktop and HPC markets. It offers
improved programmability, smaller code size, faster performance and is based on C++17 whilst maintaining backwards
compatibility with SYCL 1.2.1.

It simplifies porting of standard C++ applications to SYCL with closer alignment and integration to ISO C++ and allows
multiple back-end acceleration and API independence. There are already a number of backends including CUDA, PTX, OpenMP,
AMD, NEC, and TBB in addition to OpenCL.

This talk will showcase these features and show how SYCL 2020 has increased expressiveness and simplicity for modern C++
heterogeneous programming.
