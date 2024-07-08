---
contributor: rod
date: '2022-05-30T10:57:44.284000+00:00'
title: 'SYCLcon 2022 - SYCL Concurrency on GPU Platforms: Empirical Measurement'
external_url: https://www.youtube.com/watch?v=VqiY-KZXATc
type: presentation
tags:
  - syclcon
  - concurrency
featuring:
  - name: Thomas Applencourt
    affiliation_at_video_production_time: Argonne National Laboratory
---

Execution of Independent SYCL commands may overlap” is an optimization that SYCL applications developers would like to
rely on.

By executing commands concurrently, developers hope that their code will run faster. This poster uses this empirical
metric to assess if a computing environment lives up to developers’ expectations. We run each individual command
serially to generate a baseline and then check if the same commands run faster when scheduled in a way that allows
concurrency.
