---
contributor: rod
date: '2018-01-30T18:26:15+01:00'
external_url: https://www.codeplay.com/portal/01-30-18-getting-sycl-to-interact-with-opencl-code
image: ../../../static/images/news/2018-01-30-using-template-sorcery-to-implement-sycl-interoperability.webp
title: Using Template Sorcery To Implement SYCL Interoperability
tags:
  - computecpp
  - opencl
---

Whilst developing ComputeCpp, our implementation of the SYCL standard, we've come across some fascinating
challenges. One of these is how we ensure C++ fundamental types are translated correctly from SYCL code through to
OpenCL, retaining their correct size and signedness.
