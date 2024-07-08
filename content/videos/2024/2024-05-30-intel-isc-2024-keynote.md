---
contributor: max
date: '2024-05-30T16:25:20'
title: 'Intel ISC 2024 Keynote'
external_url: https://www.youtube.com/watch?v=MlvJmiCkXgc
type: presentation
tags:
  - oneapi
  - dpc++
  - nvidia
  - cuda
featuring:
  - username: andrew
  - username: rod
  - name: Kalyan Kumaran
    affiliation_at_video_production_time: Argonne National Laboratory
  - name: Tobias Ribizel
    affiliation_at_video_production_time: Karlsruhe Institute of Technology
  - name: Bongjun Kim
    affiliation_at_video_production_time: Samsung Advanced Institute of Technology
    
---

Khronos APIs for Heterogeneous Compute and Safety: SYCL and SYCL SC - Michael Wong, Nevin Liber & Verena Beckham -
CppCon 2023 <https://github.com/CppCon/CppCon2023>.

Khronos is an international consortium, non-profit standards consortium that is open to all, with royalty-free standards
for the industry to use. Our focus is on enabling applications to access the power of acceleration for 3D graphics,
virtual and augmented reality, and parallel computation. For the last 5 years, Khronos has sponsored a Quiet room for
attendees to use. Khronos specializes in 3D acceleration APIs including Vulkan and OpenGL, and the new ANARI API for
scientific visualization, initiatives around 3D asset formats including glTF; the OpenXR API standard for portable
augmented and virtual reality; and most relevant to C++, a family of APIs and languages for parallel computation, vision
acceleration and inferencing.

These are specifically SYCL which has been presented before, and continues to evolve to serve all hardware acceleration
targets or fall back to CPU if there are no accelerators. There is also now SYCL Safety Critical which we will showcase
its continuing progress and adoption in the automotive domain by AUTOSAR.

SYCL is a C++ language framework that uses template libraries to dispatch selected parts of a standard C++ application
to acceleration processors. SYCL enables complex C++-based applications and libraries, such as complete machine learning
frameworks, to be directly compiled and accelerated to performance levels that in many cases outperform hand-tuned code.
Offloaded C++ code is sent to the SYCL compiler for the target accelerator processors, that often uses OpenCL as a
backend, the remainder of the C++ code is sent to the C++ compiler for the host CPU. This talk will have parts that
discuss how ISO C++ is integrated into SYCL and how SYCL influences ISO C++. These include mdspan and/or executors.

SYCL SC is in early stages of a new WG that has completed a 1 year gap analysis on what is need to safety in C++ offload
accelerators, for improved determinism, better robustness that implements error handling, and smaller SPI to reduce
efforts for certification.

This talk will describe most recent progress in Khronos SYCL and SYCL SC, as well as areas that SYCL relates to C++,
such as mdspan, and its use in both High Performance computing, and the safety critical industry, such as our 
collaboration with AUTOSAR.
