---
contributor: rod
date: '2022-05-30T10:57:44.284000+00:00'
title: SYCLcon '22 - Towards a Portable Drug Discovery Pipeline with SYCL 2020
external_url: https://www.youtube.com/watch?v=z6xQnSy3yMY
type: presentation
featuring:
  - name: Luigi Crisci
    affiliation_at_video_production_time: Univerity of Salerno
---

The outcome of the drug discovery process is a molecule that has strong interaction with the target protein. Domain
experts expect a beneficial effect from this interaction. The virtual screening is one of the early stages of the
process, and it aims at finding promising molecules to forward to later stages. We perform this task in-silico to
evaluate a very large chemical library in a short time frame. This activity typically comprises two compute-intensive
tasks: a docking function that predicts the displacement of atoms, and a scoring function, which estimates the
interaction strength Dompé Farmaceutici led the development of LiGen, a molecular docking platform targeting
High-Performance Computing systems. LiGen has been used for the discovery of novel treatments in the fight against viral
infections and multidrug-resistant bacteria. The LiGen processing pipeline includes two main components, ligen-dock
and ligen-score, originally developed in OpenACC, refactored to CUDA using non-portable target-specific
optimizations.