---
contributor: max
date: '2019-09-02T10:57:29+01:00'
title: 'Celerity: High-level C++ for Accelerator Clusters'
external_url: https://www.cosenza.eu/papers/ThomanEUROPAR19.pdf
authors:
  - Peter Thoman
  - Philip Salzmann
  - Biagio Cosenza
  - Thomas Fahringer
tags:
  - clusters
  - scientific
  - accelerators
  - celerity
---

In the face of ever-slowing single-thread performance growth for CPUs, the scientific and engineering communities
increasingly turn to accelerator parallelization to tackle growing application workloads. Existing means of targeting
distributed memory accelerator clusters impose severe programmability barriers and maintenance burdens.

The Celerity programming environment seeks to enable developers to scale C++ applications to accelerator clusters with
relative ease, while leveraging and extending the SYCL domain-specific embedded language.By having users provide minimal
information about how data is accessed within compute kernels, Celerity automatically distributes work and data.
