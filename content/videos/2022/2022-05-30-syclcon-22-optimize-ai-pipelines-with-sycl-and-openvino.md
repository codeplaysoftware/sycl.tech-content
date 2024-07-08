---
contributor: max
date: '2022-05-30T10:57:44.284000+00:00'
title: SYCLcon '22 - Optimize AI pipelines with SYCL and OpenVINO
external_url: https://www.youtube.com/watch?v=f55pAnfzJeU
type: presentation
tags:
  - optimization
  - openvino
  - ai
  - artificial-intelligence
featuring:
  - name: Nico Galoppo
    affiliation_at_video_production_time: Intel Corporation
---

Sensor data processing pipelines that are a “mix” of feature-engineered and deep learning based processing have become
prevalent today. For example, sensor fusion of point cloud data with RGB image streams is common in autonomous mobile
robots and self-driving technology. The state-of-the-art in computer vision for extracting semantic information from RGB
data is using deep learning today, and great advancements have been made recently in LiDAR odometry based on deep
learning. At the same time, other processing components in “mixed” pipelines still use feature-engineered approaches
that are not relying on deep neural nets.

Embedded compute platforms in robotics systems are inherently heterogeneous in nature, often with a variety of CPUs, (
integrated) GPUs, VPUs, and so on. This means that there is a growing need to implement “mixed” pipelines on
heterogeneous platforms that include a variety of xPUs. We want such pipeline implementations to benefit from the latest
advancements in data- and thread-parallel computation, as well as state-of-the-art in optimized inference of AI DNN
models. SYCL and OpenVINO are two open, industry supported APIs that allow a developer to do so.

It is not only important to optimize the individual components of the processing pipeline – it is at least as important
to also optimize the data flow and minimize data copies. This provides a way to benefit from the efficiencies in
inference runtime and compute graph optimizations provided by OpenVINO, in combination with the extensibility that SYCL
brings in implementing custom or non-DNN components. Similarly, the use of compatible synchronization primitives allows
the different runtimes to schedule work more efficiently on the hardware and avoid execution hiccups.

In this talk, we will demonstrate the mechanisms and primitives provided by both SYCL and OpenVINO to optimize the
dataflow between, and efficient execution of the workloads implemented in the respective APIs. We will provide an
example and show the impact on the overall throughput and latency of the end-to-end processing pipeline. The audience
will learn to recognize inefficiencies in their pipelines using profiling tools, and understand how to optimize those
inefficiencies using an easy-to-follow optimization recipe. Finally, we will provide guidance to developers of inference
engines other than OpenVINO on how to integrate similar interoperability features into their APIs, so that they too can
offer optimized SYCL-enabled AI pipelines to their users.
