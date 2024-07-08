---
contributor: anonymous
date: '2022-05-30T09:38:59.951000+00:00'
title: On the Compilation Performance of Current SYCL Implementations
external_url: https://www.youtube.com/watch?v=WnyfAh2xg6w
type: presentation
tags:
  - performance
  - comparisons
featuring:
  - name: Peter Thoman
    affiliation_at_video_production_time: University of Innsbruck
  - name: Facundo Molina Heredia
    affiliation_at_video_production_time: University of Innsbruck
  - name: Thomas Fahringer
    affiliation_at_video_production_time: University of Innsbruck
---

In this work we set out to study the relative compile-time performance and the impact of various SYCL features on
compilation times across a selection of the most widely-used SYCL implementations. To this end, we introduce a code
generator which creates SYCL kernels stressing various API features and instruction types, either in isolation or in
combination, as well as an infrastructure to largely automate related experiments. We apply this infrastructure in a
large-scale synthetic evaluation totaling 96000 compiler runs, which also includes a study of the compilation
performance over time of the most widespread implementations. In addition to these synthetic experiments, we validate
the applicability of our findings by measuring the compile times of two real-world industrial SYCL applications.
