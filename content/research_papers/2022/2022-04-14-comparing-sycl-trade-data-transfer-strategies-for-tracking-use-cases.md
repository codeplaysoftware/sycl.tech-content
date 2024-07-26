---
contributor: rod
date: '2022-04-14T08:08:10.490000+00:00'
title: Comparing SYCL&trade; Data Transfer Strategies for Tracking Use Cases
external_url: https://iopscience.iop.org/article/10.1088/1742-6596/2438/1/012018/pdf
authors:
  - Sylvain Joube
  - Hadrien Grasland
  - David Chamont
  - Elisabeth Brunet
tags:
  - performance
  - benchmarking
---

The aim of this work is to compare the performance and ease of programming of the various data transfer strategies
provided by SYCL 2020: buffers/accessors on one hand and the different storage types exposed by Unified Shared Memory (
USM) on the other hand. We measured the relative performance of USM exclusively located either on the host (USM host) or
on the device(USM device), or automatically managed and moved (USM shared). We also tried to quantify the impact of
formatting data in a GPU-friendly manner as opposed to using a regular pointer based structure in which the C++
allocator was replaced by the SYCL allocator sycl::malloc. We first made a PCIe-bound micro-benchmark to test the SYCL
memory models with a simple access pattern. We then switched to a real use-case provided by Traccc, a research project
associated to the ACTS particle tracking library. The algorithm of interest is SparseCCL, a clustering algorithm used on
the first step of track reconstruction. For consistency, all tests were made on a single hardware architecture: a recent
server having a discrete GPU with dedicated VRAM, representative of the hardware currently used by the ACTS team.
