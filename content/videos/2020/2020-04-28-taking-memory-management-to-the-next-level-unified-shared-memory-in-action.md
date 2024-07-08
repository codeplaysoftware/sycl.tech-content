---
contributor: rod
date: '2020-04-28T15:40:36+02:00'
title: 'Taking Memory Management to the Next Level - Unified Shared Memory in Action'
external_url: https://www.youtube.com/watch?v=p8jp0OkO__s
type: presentation
featuring:
  - name: Michal Mrozek
    affiliation_at_video_production_time: Intel Corporation
---

When adding OpenCL or SYCL acceleration to existing code bases it is desirable to represent memory allocations using
pointers. This aligns naturally with the Shared Virtual Memory (SVM) capabilities in standard OpenCL, but we found many
properties of SVM that are either cumbersome to use or inefficient.

This talk will describe Unified Shared Memory (USM), which is designed to address these shortcomings and take SVM to the
next level. 
