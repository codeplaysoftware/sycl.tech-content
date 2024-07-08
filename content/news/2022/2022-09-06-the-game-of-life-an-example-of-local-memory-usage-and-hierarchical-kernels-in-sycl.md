---
contributor: anonymous
date: '2022-09-06T16:13:40.933000+00:00'
external_url: https://www.codeplay.com/portal/blogs/2022/09/05/the-game-of-life-an-example-of-local-memory-usage-and-hierarchical-kernels-in-sycl.html
image: ../../../static/images/news/2022-09-06-the-game-of-life-an-example-of-local-memory-usage-and-hierarchical-kernels-in-sycl.webp
title: 'The Game of Life: An Example of Local Memory Usage and Hierarchical Kernels in SYCL'
tags:
  - parallelization
  - game-of-life
  - tutorial
---

John Conway’s cellular automaton, the Game of Life, has long been a staple project for those learning to code. It is
also an “embarrassingly parallel” problem, making it a great learning tool for teaching ourselves how to parallelize
processes using SYCL™. You will find that even the simplest parallel implementation of the Game of Life will yield a
significant performance boost, however there are even more optimizations we can apply to squeeze as much performance out
of our code.

One such optimization is the use of local memory.
