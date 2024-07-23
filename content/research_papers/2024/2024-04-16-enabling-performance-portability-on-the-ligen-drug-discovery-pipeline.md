---
contributor: max
date: '2024-04-16T08:08:10.490000+00:00'
title: 'Enabling performance portability on the LiGen drug discovery pipeline'
external_url: https://www.sciencedirect.com/science/article/pii/S0167739X24001195
authors:
  - name: Luigi Crisci
  - name: Lorenzo Carpentieri
  - name: Biagio Cosenza
  - name: Leon Bogdanović
  - name: Gianmarco Accordi
  - name: Davide Gadioli
  - name: Emanuele Vitali
  - name: Gianluca Palermo
  - name: Andrea Rosario Beccari
tags:
  - gpu
  - sycl
  - hpc
  - cuda
  - hip
---

In recent years, there has been a growing interest in developing high-performance implementations of drug discovery processing software. To target modern GPU architectures, 
such applications are mostly written in proprietary languages such as CUDA or HIP. However, with the increasing heterogeneity of modern HPC systems and the availability of 
accelerators from multiple hardware vendors, it has become critical to be able to efficiently execute drug discovery pipelines on multiple large-scale computing systems, 
with the ultimate goal of working on urgent computing scenarios. This article presents the challenges of migrating LiGen, an industrial drug discovery software pipeline, 
from CUDA to the SYCL programming model, an industry standard based on C++ that enables heterogeneous computing. We perform a structured analysis of the performance portability 
of the SYCL LiGen platform, focusing on different aspects of the approach from different perspectives. First, we analyze the performance portability provided by the high-level semantics 
of SYCL, including the most recent group algorithms and subgroups of SYCL 2020. Second, we analyze how low-level aspects such as kernel occupancy and register pressure affect 
the performance portability of the overall application. The experimental evaluation is performed on two different versions of LiGen, implementing two different parallelization 
patterns, by comparing them with a manually optimized CUDA version, and by evaluating performance portability using both known and ad hoc metrics. The results show that,
thanks to the combination of high-level SYCL semantics and some manual tuning, LiGen achieves native-comparable performance on NVIDIA, while also running on AMD GPUs.
