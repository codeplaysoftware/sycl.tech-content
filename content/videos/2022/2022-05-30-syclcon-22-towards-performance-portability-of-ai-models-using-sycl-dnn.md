---
contributor: max
date: '2022-05-30T10:57:44.284000+00:00'
title: SYCLcon '22 - Towards performance portability of AI models using SYCL-DNN
external_url: https://www.youtube.com/watch?v=yzBeXIXKmU0
type: presentation
featuring:
  - name: Muhammad Tanvir
    affiliation_at_video_production_time: Intel Corporation
---

The wide adoption of Deep Neural Networks (DNN) has served as an incentive to design and manufacture powerful and
specialized hardware technologies, targeting systems from Edge devices to Cloud and supercomputers. This huge diversity
soon becomes a burden due to the emerging dependencies between development stacks and deployment hardware. While the
proposed ONNX as a de facto for AI model description, provides the portability of AI models across various AI
frameworks, supporting DNN models on various hardware architectures remains challenging. Several existing AI frameworks
such as Tensorflow, Pytorch, ONNXRuntime provides performance portability via a dedicated backend implementations per
hardware architecture. While such approach provides wider support of hardware devices, maintainability and readability
remains challenging.
