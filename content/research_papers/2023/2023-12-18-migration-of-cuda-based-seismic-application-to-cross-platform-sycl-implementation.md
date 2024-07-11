---
contributor: scott
date: '2023-12-18T08:08:10.490000+00:00'
title: 'Migration of CUDA Based Seismic Application to Cross-Platform SYCL Implementation'
external_url: https://ieeexplore.ieee.org/document/10502402
authors:
  - name: Om Jadhav
    affiliation: HPC-Technologies Group
  - name: Sandeep Agrawal
    affiliation: HPC-Technologies Group
  - name: Abhishek Srivastava
    affiliation: HPC-SE&A Group
  - name: Richa Rastogi
    affiliation: HPC-SE&A Group
  - name: Sanjay Wandhekar
    affiliation: HPC-Technologies Group
  - name: Vinutha SV
    affiliation: Intel Technology India Pvt. Ltd
  - name: Jyotsna Khemka
    affiliation: Intel Technology India Pvt. Ltd
tags:
  - acoustic-waves
  - seismic-data
  - manually-optimized
  - cuda
  - migration
---

Here, we present the migration of a CUDA based seismic application, named SeisAcoMod2D, to SYCL codebase using Intel®
oneAPI. SYCL programming enables developers to have single source codebase across different computing architectures and
vendors of CPUs, GPUs, and FPGAs. SeisAcoMod2D performs acoustic wave propagation using finite difference time domain
modelling, which is useful in oil exploration applications. The migrated SYCL code has been optimized for GPUs and the
output data is validated. The migrated unified SYCL code is executed on GPUs from Intel and Nvidia and on CPUs from
Intel. The performance of the SYCL code is found similar to that of the CUDA code on Nvidia® A100 GPU. A speed up of
1.75x is obtained on Intel® Data Center GPU Max 1550 GPU (Ponte Vecchio) over Nvidia® A100 (80GB) GPU.
