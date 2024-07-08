---
contributor: scott
date: '2021-01-20T08:08:40.405000+00:00'
title: 'SYCL-Bench: A Versatile Cross-Platform Benchmark Suite for Heterogeneous Computing'
external_url: https://www.youtube.com/watch?v=pyGUBzDdY5s
type: presentation
featuring:
  - name: Aksel Alpay
    affiliation_at_video_production_time: Heidelberg University
  - name: Vincent Heuveline
    affiliation_at_video_production_time: Heidelberg University
  - name: Sohan Lal
    affiliation_at_video_production_time: TU Berlin
  - name: Nicolai Stawinoga
    affiliation_at_video_production_time: TU Berlin
  - name: Philip Salzmann
    affiliation_at_video_production_time: University of Innsbruck
  - name: Peter Thoman 
    affiliation_at_video_production_time: University of Innsbruck
  - name: Thomas Fahringer
    affiliation_at_video_production_time: University of Innsbruck
  - name: Biagio Cosenza
    affiliation_at_video_production_time: University of Salerno
---

The SYCL standard promises to enable high productivity in heterogeneous programming of a broad range of parallel
devices, including multicore CPUs, GPUs, and FPGAs. Its modern and expressive C++ API design, as well as flexible task
graph execution model give rise to ample optimization opportunities at run-time, such as the overlapping of data
transfers and kernel execution. However, it is not clear which of the existing SYCL implementations perform such
scheduling optimizations, and to what extent. Furthermore, SYCL's high level of abstraction may raise concerns about
sacrificing performance for ease of use. Benchmarks are required to accurately assess the performance behavior of
high-level programming models such as SYCL. To this end, we present SYCL-Bench, a versatile benchmark suite for device
characterization and runtime benchmarking, written in SYCL. We experimentally demonstrate the effectiveness of
SYCL-Bench by performing device characterization of the NVIDIA TITAN X GPU, and by evaluating the efficiency of the
hipSYCL and ComputeCpp SYCL implementations.
