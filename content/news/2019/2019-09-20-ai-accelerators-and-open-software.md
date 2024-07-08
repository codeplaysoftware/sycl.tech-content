---
contributor: rod
date: '2019-09-20T14:34:07+02:00'
external_url: https://gfxspeak.com/2019/09/20/accelerators-open-software/
image: ../../../static/images/news/2019-09-20-ai-accelerators-and-open-software.webp
title: AI Accelerators and open software
  - ai
  - artificial-intelligence
  - nvidia
  - cuda
  - codeplay
  - amd
  - hip
---

With the explosive interest in AI, Nvidia extended the reach of CUDA by developing containers—NGC—Nvidia GPU-accelerated
containers. The company has developed containers for AI software like TensorFlow, PyTorch, MXNet, TensorRT, RAPIDS, and
others.

But CUDA remains a closed, proprietary language and only runs efficiently on Nvidia GPUs. There are translation programs
like AMD’s Boltzmann Initiative and HIP (Heterogeneous-compute Interface for Portability) for porting CUDA source code
to a common C++ programming model.

Edinburgh-based Codeplay has also contributed to the TensorFlow stack, enabling it with SYCL, allowing any AI program to
run on any OpenCL-enabled CPU, GPU, custom AI accelerators, DSPs, or FPGA. Intel has likewise adopted this approach by
recently announcing their OneAPI across their processors (GPU, AI, and FPGA) with SYCL inside.
