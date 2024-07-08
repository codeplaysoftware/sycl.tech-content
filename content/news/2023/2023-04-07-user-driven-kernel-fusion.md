---
contributor: rod
date: '2023-04-07T12:12:48.130000+00:00'
external_url: https://codeplay.com/portal/blogs/2023/03/20/user-driven-kernel-fusion
image: ../../../static/images/news/2023-04-07-user-driven-kernel-fusion.webp
title: User-driven Kernel Fusion
tags:
  - extensions
  - codeplay
  - performance
---

The overhead linked to offloading work to an accelerator can be problematic, especially for short-running device
kernels. Fusing multiple smaller kernels into one can be a solution to this problem, but manual implementation of fused
kernels is tedious work, as it needs to be repeated for each potential combination of kernels. Codeplay have therefore
developed an extension for the SYCL standard for user-driven, automatic kernel fusion. If you want to learn how to
instruct the SYCL runtime to perform kernel fusion automatically for you, look no further and dive into this blog-post,
which explains the extension and demonstrates its use on a simple example.
