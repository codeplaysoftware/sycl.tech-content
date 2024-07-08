---
contributor: scott
date: '2022-05-30T10:57:44.284000+00:00'
title: SYCLcon '22 - Interfacing SYCL and Python for XPU Programming
external_url: https://www.youtube.com/watch?v=4leDqMKPLbA
type: presentation
featuring:
  - name: Diptorup Deb
    affiliation_at_video_production_time: Intel Corporation
  - name: Oleksandr Pavlyk
    affiliation_at_video_production_time: Intel Corporation
---

This paper introduces a new framework to help build and use SYCL-based Python native extensions. We present the core
design and implementation detail of the framework that includes an overview of the API, a technique to support
asynchronous SYCL kernel execution via Python, and discussion around the usage of Python extension generator tools to
build SYCL-based extensions. Details of ongoing work are presented and we demonstrate the development of a performance
portable Python native extension that relies on the SYCL-based oneMKL specification.
