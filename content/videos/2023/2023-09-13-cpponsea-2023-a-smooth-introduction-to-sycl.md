---
contributor: rod
date: '2023-09-13T09:38:20.837493'
title: 'CpponSea 2023: A Smooth Introduction to SYCL'
external_url: https://www.youtube.com/watch?v=nFvKpnA5Aj0&t=2s
type: presentation
tags: 
  - cppcon
  - learning
  - introduction
featuring:
  - name: Joel Falcou
    affiliation_at_video_production_time: University Paris-Sud
---

From HPC to mobile development, the prevalence of accelerators and other performance-driven architectures is a fact you
can't argue with anymore. What if you want to tap into those source of performances but you don't really want to
sacrifice the elegance of your C++20? What if you may want to explore some of those architectures now but change your
mind later without dropping all the code you already wrote?

That's where SYCL comes down. SYCL is an open standard aiming at providing a cross-platform programming model, tools and
compilers to target accelerators at large. Made to be interoperable with C++, it is simplified the design, debugging and
deployment of applications over a large selection of accelerators: multi-cores, GPGPU or even FPGA.

In this talk, we will give a short tour of SYCL saillant point, how to get started with it, how it can smoothly be
integrated in your C++ code without major changes in your programming habit, and we will conclude with some result of
such an integration in a High Energy Physic applications.
