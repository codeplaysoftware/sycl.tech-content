---
contributor: rod
date: '2021-09-23T13:02:15.404000+00:00'
external_url: https://enccs.se/news/2021/09/gromacs-adopts-hipsycl-for-amd-gpu-support/
image: ../../../static/images/news/2021-09-23-gromacs-adopts-hipsycl-for-future-amd-gpu-support.webp
title: GROMACS Adopts hipSYCL for Future AMD GPU Support
tags:
  - gromacs
  - hipsycl
  - amd
---

It was attractive to consider using SYCL in GROMACS also for AMD GPUs, since there was already effort underway in
GROMACS in that direction targeting Intel GPUs. The hipSYCL (<https://github.com/illuhad/hipSYCL>) open-source project
run at Heidelberg University already supported CPUs, as well as Nvidia and AMD GPUs in SYCL by extending existing clang
toolchains, and was also funded by Intel to support the recent SYCL 2020 standard. We already wanted to use hipSYCL as
our portability check of the DPC++ code for Intel GPUs. We built a working relationship with the hipSYCL team led by
Aksel Alpay.
