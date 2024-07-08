---
contributor: anonymous
date: '2018-07-23T12:08:17+02:00'
external_url: https://cris.fau.de/converis/portal/Publication/200969642?auxfun=&lang=en_GB
image: ../../../static/images/news/2018-07-23-solving-maxwell-s-equations-with-modern-c-and-sycl-a-case-study.webp
title: 'Solving Maxwell''s Equations with Modern C++ and SYCL: A Case Study'
tags:
  - maxwell
  - equations
  - compute
  - parallelization
  - case-study
---

In scientific computing, unstructured meshes are a crucial foundation for the simulation of real-world physical
phenomena. Compared to regular grids, they allow resembling the computational domain with a much higher accuracy, which
in turn leads to more efficient computations.

There exists a wealth of supporting libraries and frameworks that aid programmers with the implementation of
applications working on such grids, each built on top of existing parallelization technologies. However, many approaches
require the programmer to introduce a different programming paradigm into their application or provide different
variants of the code. SYCL is a new programming standard providing a remedy to this dilemma by building on standard
C++17 with its so-called single-source approach: Programmers write standard C ++ code and expose parallelism using C++17
keywords.
