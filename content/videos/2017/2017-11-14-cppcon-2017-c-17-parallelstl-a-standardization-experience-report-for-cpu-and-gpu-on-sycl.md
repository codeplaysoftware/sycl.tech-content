---
contributor: anonymous
date: '2017-11-14T10:55:31+01:00'
title: 'CppCon 2017: C++17 ParallelSTL: A Standardization Experience Report for CPU and GPU on SYCL'
external_url: https://www.youtube.com/watch?v=RoUYiHTsEFE
type: presentation
featuring:
  - username: michael
  - username: gordon
  - username: ruyman
---

Parallel STL is an implementation of the Technical Specification for C++ Extensions for Parallelism for both CPU and GPU
with SYCL Heterogeneous C++ language. This technical specification describes a set of requirements for implementations
of an interface that C++ programs may use to invoke algorithms with parallel execution. In practice, this specification
allows users to specify execution policies to traditional STL algorithms which will enable the execution of those
algorithms in parallel. The various policies can specify different kinds of parallel execution. For example, 
