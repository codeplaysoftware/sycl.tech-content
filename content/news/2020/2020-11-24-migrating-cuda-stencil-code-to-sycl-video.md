---
contributor: max
date: '2020-11-24T09:18:13.034000+00:00'
external_url: https://sc20.gallery.video/detail/videos/sc20/video/6208394344001/developing-a-cross-architecture-dpc-application-using-migrated-cuda-stencil-code
image: ../../../static/images/news/2020-11-24-migrating-cuda-stencil-code-to-sycl-video.webp
title: Migrating CUDA Stencil code to SYCL Video
tags:
  - cuda
  - migration
  - sycl
  - video
  - tutorial
  - guide
  - dpc++
  - oneapi
---

Data Parallel C++ (DPC++), the C++- and SYCL-based programming language of choice in the oneAPI programming environment,
promises to have a single source code that addresses multiple hardware architectures. However, starting from scratch or
rewriting existing application is tedious if not out of question in most cases. The Intel® DPC++ Compatibility Tool
addresses this issue by assisting in the migration from CUDA to DPC++. In this talk, we share our experiences with
migrating a typical CUDA stencil application code to DPC++ with the help of the tool. The presentation addresses the
basic porting process, required manual steps, and issues we faced with the tsunami simulation code easyWave. Besides
these procedural steps, we point out performance numbers of the hardware devices supported by oneAPI and its evolving
ecosystem. This is not limited to devices like Intel CPUs and GPUs, but includes promising numbers for NVIDIA hardware
as well. We also demonstrate what needs to be done to execute the migrated, CUDA-originated code on FPGAs.

**Steffen Christgau, Zuse Institute Berlin**
