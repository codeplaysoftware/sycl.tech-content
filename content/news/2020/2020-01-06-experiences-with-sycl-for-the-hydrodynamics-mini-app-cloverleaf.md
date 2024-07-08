---
contributor: anonymous
date: '2020-01-06T08:00:07+02:00'
external_url: http://uob-hpc.github.io/2020/01/06/cloverleaf-sycl.html
image: ../../../static/images/news/2020-01-06-experiences-with-sycl-for-the-hydrodynamics-mini-app-cloverleaf.webp
title: Experiences with SYCL for the hydrodynamics mini-app, CloverLeaf
tags:
  - cloverleaf
  - hydrodynamics
  - kokkos
  - porting
  - blog
---

"We have most recently ported CloverLeaf to SYCL, and this blog post demonstrates our experiences. As a starting point,
we took our Kokkos port of CloverLeaf, which was already C++ throughout, with the key computational kernels already
ported to C++ lambda functions. The programming abstractions from Kokkos do differ a little to those in SYCL at a
high-level, however there are many similarities."
