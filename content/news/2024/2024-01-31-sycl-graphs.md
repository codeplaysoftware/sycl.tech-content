---
contributor: rod
date: '2024-01-31T11:24:13.294335'
external_url: https://codeplay.com/portal/blogs/2024/01/22/sycl-graphs
image: ../../../static/images/news/2024-01-31-sycl-graphs.webp
title: SYCL Graphs
tags:
  - graphs
  - blog
  - oneapi
  - nvidia
  - amd
---

Ben Tracy, a Senior Software Engineer at Codeplay, has prepared this blog that introduces SYCL Graphs. This has
recently been introduced in Codeplay's plugins for oneAPI, and you can read about the feature here.

"When working with accelerated applications, such as when using GPUs, developers write **compute kernels** that
are executed one by one on the accelerator. This is called “offloading”, as in, developers are moving computation
off the CPU onto the GPU. Typically, computational kernels operate on data that is coming from the host,
perform some manipulation with that data, and then data goes back to the host CPU so that the application can
continue. However, as more workloads are offloaded to accelerators, it has become increasingly common to offload
multiple kernels that operate with data to the device..."  
