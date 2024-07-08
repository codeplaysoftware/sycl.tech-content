---
contributor: max
date: '2022-07-18T15:15:31.329000+00:00'
external_url: https://www.hipeac.net/magazine/7162/
image: ../../../static/images/news/2022-07-18-accelerating-made-simpler-with-celerity.webp
title: Accelerating Made Simpler With Celerity
tags:
  - hipeac
  - celerity
  - opencl
  - mpi
  - cuda
  - hip
---

On page 31 of the hiPEAC magazine is an article by Biagio Cosenza and Peter Thoman who are part of the Celerity project.

‘Several of those of us working on Celerity have worked with GPUs for many years,’ explains Biagio. ‘What we saw was
that existing technologies made an already difficult task – writing and maintaining efficient software for distributed
compute clusters – even more challenging: now you not only needed to manage the distribution of data and work across
cluster nodes,but also to GPUs on each individual node, generally using a completely separate technology. An example
would be an MPI+ CUDA hybrid program, or MPI + OpenCL if you planned to support vendor-agnostic technologies.’‘However,
we also had previous experience with academic projects seeking to automate this entire stack and saw how ultimately they
fell short of their goals,’ adds Peter. ‘So when SYCL™ was released as a vendor-agnostic, high-level standard for
writing single-node applications targeting heterogeneous hardware, we asked ourselves whether it would be possible to
extend it to clusters of GPUs and accelerators with minimal code changes. We had one key idea – the concept of range
mappers – and Celerity was born.’
