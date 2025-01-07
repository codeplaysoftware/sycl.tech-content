---
contributor: max
date: '2024-12-19T09:43:10'
title: 'Implementation of Two Numerical Solvers for the Study of Non-Equilibrium Gas Dynamics on GPU-Accelerated Platforms using SYCL'
external_url: 'https://ruor.uottawa.ca/items/cb39b8e3-9904-4a65-89bf-5414d364e759'
authors:
  - El-Ghotmi, Osman
tags:
  - sycl
  - gpu
  - portability
---

The application of GPUs has extended beyond traditional graphics rendering because their
parallel processing capabilities can accelerate many general-purpose tasks, such as machine
learning and scientific computing. This thesis presents the implementation of two numerical
solvers for the solution of non-equilibrium gas flows. It also demonstrates the computational
performance of the two solvers when developed to target GPU-based supercomputers using the SYCL
programming model. The first solver incorporates a novel ray-tracing technique and accurate
mathematical relations to efficiently compute any observable property of free-molecular flow
past convex shapes (FMFC). It computes integrals of the Maxwell-Boltzmann distribution function
to create an algorithm that quickly evaluates any moment of the local particle-velocity
distribution. This highly efficient technique is extended for GPUs to accelerate the
computation of accurate results. Results produced with the solver serve as robust benchmarks
in the validation of other scientific models that describe fluid motion in non-equilibrium
regimes. The second solver extends a CPU-based implementation of the discontinuous Galerkin Hancock (DGH)
method into an efficient GPU code. The DGH scheme is a high-order numerical method that
solves hyperbolic partial differential equations (PDEs) with stiff source terms. This class
of equations is common in many models that are used to describe non-equilibrium gas flows.
The GPU implementation of the DGH solver that is presented in this work provides a
computationally efficient and numerically accurate method to compute the solution for these
models. Results produced by the FMFC and DGH solvers showcase their accuracy and parallel
scalability as efficient GPU algorithms. Furthermore, the effectiveness of the FMFC
solver as a validation tool is demonstrated by producing benchmarks to confirm the
accuracy of scientific models that are solved with numerical schemes such as DGH.
