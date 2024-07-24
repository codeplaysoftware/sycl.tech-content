---
contributor: scott
date: '2021-11-24T08:08:10.490000+00:00'
title: 'Efficient Hardware-Agnostic DBMS Operator Implementation Using SYCL'
external_url: https://ieeexplore.ieee.org/document/9681747
authors:
  - name: Daniil Kulikov
  - name: Daria Nikolskaia
  - name: Petr Kurapov
tags:
  - parallel programming
  - hash-join
  - gpu
  - dbms
---

Heterogeneous hardware requires tedious optimization of DBMS algorithms for each platform it supports when implemented
with vendor-specific toolchains. Such an approach inevitably leads to specialization and maintainability issues. In this
paper we evaluate several hash-joins implemented with a high-level language SYCL and compare the data across different
execution devices. We provide a roof-line performance estimations for algorithms and show these implementations are on
par with existing hardware specific implementations.