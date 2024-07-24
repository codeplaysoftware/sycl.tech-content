---
contributor: scott
date: '2018-07-10T08:08:10.490000+00:00'
title: 'Solving Maxwells Equations with Modern C++ and SYCL: A Case Study'
external_url: https://ieeexplore.ieee.org/document/8445127
authors:
  - name: Ayesha Afzal
  - name: Christian Schmitt
  - name: Samer Alhaddad
  - name: Yevgen Grynko
  - name: Jurgen Teich
  - name: Jens Forstner
  - name: Frank Hannig
tags:
  - maxwell
  - c++
  - case-study
---

In scientific computing, unstructured meshes are a crucial foundation for the simulation of real-world physical
phenomena. Compared to regular grids, they allow resembling the computational domain with a much higher accuracy, which
in turn leads to more efficient computations. There exists a wealth of supporting libraries and frameworks that aid
programmers with the implementation of applications working on such grids, each built on top of existing parallelization
technologies. However, many approaches require the programmer to introduce a different programming paradigm into their
application or provide different variants of the code. SYCL is a new programming standard providing a remedy to this
dilemma by building on standard C++ 17 with its so-called single-source approach: Programmers write standard C++ code
and expose parallelism using C++ 17 keywords. The application is then transformed into a concrete implementation by the
SYCL implementation. By encapsulating the OpenCL ecosystem, different SYCL implementations enable not only the
programming of CPUs but also of heterogeneous platforms such as GPUs or other devices. For the first time, this paper
showcases a SY CL-based solver for the nodal Discontinuous Galerkin method for Maxwell's equations on unstructured
meshes. We compare our solution to a previous C-based implementation with respect to programmability and performance on
heterogeneous platforms.
