---
contributor: rod
date: '2020-01-17T09:31:36+02:00'
title: Tensorflow on open source GPUs Using SYCL
external_url: https://www.youtube.com/watch?v=KfDQb6xOkXg
type: presentation
featuring: 
  - name: David Airlie
    affiliation_at_video_production_time: Red Hat
---

One of the biggest uses for GPU compute is AI/Machine Learning applications. The tensorflow library from Google is one
of the most used frameworks in the AI/ML area. To deploy tensorflow on GPUs currently, the closed source nvidia stack is
required using CUDA. This talk will explore the work done and left to do to enable a tensorflow deployment on open
source Mesa drivers. The use of SYCL via LLVM and OpenCL along with work towards enabling OpenCL on a broader range of
hardware will be discussed.
