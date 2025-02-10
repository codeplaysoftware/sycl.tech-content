---
contributor: max
date: '2025-02-02T12:11:00'
title: 'Building Tool Chains for RISC-V AI Accelerators'
external_url: 'https://www.youtube.com/watch?v=DqNWF26A8Io'
type: presentation
tags:
  - oneapi
  - risc-v
featuring:
  - name: Jeremy Bennett
    affiliation_at_video_production_time: Embecosm
---

Building Tool Chains for RISC-V AI Accelerators - Jeremy Bennett, Embecosm

Our client is developing a massively parallel 64-bit chip for AI inference workloads.
To facilitate early software development, we are bringing up an AI tool flow for this
chip in a QEMU RISC-V environment. In this talk, we'll share our experience of getting
three key AI frameworks working with RISC-V QEMU: Pytorch, Tensorflow and the OpenXLA
compiler. Our talk will share our experience addressing two key issues. We will describe
the challenges we faced, their solutions and reflect on the lessons learned for future work.
The first of these is simply getting the tools to effectively run in an emulated
RISC-V environment. These tools are large, fast moving pieces of software with extensive
external dependencies. Our second challenge is performance. AI workloads are inherently
parallel, and hence run efficiently on vector enabled hardware. However RISC-V vector (RVV)
is relatively new, and we experienced difficulty getting the performance we expected
out of the tool flow. At the end of this talk, we hope our audience will have a better
understanding of the challenges in bringing up an AI tool flow under QEMU. We hope our
experience will help them bring up their own AI tool flows.
