---
contributor: anonymous
date: '2021-12-22T09:28:16.201000+00:00'
title: Accelerating Real-World AI Software using the RISC-V Vector Extension
external_url: https://www.youtube.com/watch?v=AKtG9kSRXNk
type: presentation
featuring: 
  - name: Colin Davidson
    affiliation_at_video_production_time: Codeplay Software
  - name: Alastair Murray
    affiliation_at_video_production_time: Codeplay Software
---

Software developers and processor designers are looking to accelerate the latest AI and machine learning applications
requiring parallel processing architectures. The RISC-V Vector (RVV) extension is a recent addition to the RISC-V ISA
providing the basis for translating vector and scalar based computation onto parallel processor cores. RVV defines a way
to accelerate AI computation, e.g., tensor datasets, in parallel on multi-core processors. However, the extension only
defines the interface, and still needs to be implemented at the compiler level to enable the division of workload across
different processors. This presentation will show how Codeplay has enabled neural network software algorithms to execute
on the RVV extension with automatic vectorization; all using open standards including SYCL, and open-source software. We
will explore the practical steps needed to implement RVV using a Spike simulator, the required software frameworks,
libraries, and toolkits to bring together, and how to enable a complex application using a real-world neural network.
