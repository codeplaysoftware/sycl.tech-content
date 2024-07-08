---
contributor: rod
date: '2019-06-12T12:46:42+02:00'
external_url: https://www.codeplay.com/portal/06-11-19-sycl-cpp-generic-interfaces-with-generic-lambdas
image: ../../../static/images/news/2019-06-12-generic-interfaces-with-generic-lambdas-with-c-and-sycl.webp
title: Generic Interfaces with Generic Lambdas with C++ and SYCL
tags:
  - lambda
  - c++
  - c++11
---

C++ Lambdas, first introduced in C++11, are an important part of the way that the SYCL standard is defined and
implemented. SYCL is required to handle different types and pass around functions so lambdas are a good fit allowing
anonymous function objects to be passed to SYCL kernels. We talk about how we use lambdas in our guides and
documentation, but never about how lambdas work or even how to use them in SYCL, so in this blog post we will examine
how they can be used in SYCL.
