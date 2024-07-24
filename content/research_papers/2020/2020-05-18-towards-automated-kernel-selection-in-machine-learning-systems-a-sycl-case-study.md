---
contributor: scott
date: '2022-05-18T08:08:10.490000+00:00'
title: 'Towards automated kernel selection in machine learning systems: A SYCL case study'
external_url: https://ieeexplore.ieee.org/document/9150358
authors:
  - name: John Lawson
tags:
  - tuning
  - sycl
  - gpgpu
  - machine-learning
  - ai
---

Automated tuning of compute kernels is a popular area of research, mainly focused on finding optimal kernel parameters
for a problem with fixed input sizes. This approach is good for deploying machine learning models, where the network
topology is constant, but machine learning research often involves changing network topologies and hyperparameters.
Traditional kernel auto-tuning has limited impact in this case; a more general selection of kernels is required for
libraries to accelerate machine learning research. In this paper we present initial results using machine learning to
select kernels in a case study deploying high performance SYCL kernels in libraries that target a range of heterogeneous
devices from desktop GPUs to embedded accelerators. The techniques investigated apply more generally and could similarly
be integrated with other heterogeneous programming systems. By combining auto-tuning and machine learning these kernel
selection processes can be deployed with little developer effort to achieve high performance on new hardware.
