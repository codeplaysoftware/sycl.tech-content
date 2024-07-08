---
contributor: scott
date: '2021-05-04T15:16:50.484000+00:00'
external_url: https://www.hpcwire.com/off-the-wire/porting-a-lattice-qcd-code-suite-to-exascale-architectures/
image: ../../../static/images/news/2021-05-04-porting-a-lattice-qcd-code-suite-to-exascale-architectures.webp
title: Porting a Lattice QCD Code-Suite to Exascale Architectures
tags:
  - hotqcd
  - lqcd
  - chromodynamics
  - doe
  - intel
  - cuda
---

The fundamental interactions between the quarks and gluons that constitute protons and nuclei can be calculated
systematically by the physics theory known as lattice quantum chromodynamics (LQCD). These interactions account for 99
percent of the mass in the visible universe, but they can only be simulated with powerful computer systems such as those
housed at the U.S. Department of Energy’s (DOE) Argonne Leadership Computing Facility (ALCF).

As part of the effort to move operations to the backend and generalize the code, the developers are constructing
a [SYCL backend](https://software.intel.com/content/www/us/en/develop/tools/oneapi.html?cid=sem&source=sa360&campid=2021_q1_iags_us_iagsoapi_iagsoapiee_awa_text-link_generic_exact_cd_dpd-oneapi-dpc-comp_O-2J3MV_google_div_oos_non-pbm&ad_group=generic_oneapi-dpc-compatibility_awa&intel_term=sycl&sa360id=43700053515352181&gclid=EAIaIQobChMItoSVyOLe7wIVhIJbCh0bMQgHEAAYASAAEgIMS_D_BwE&gclsrc=aw.ds);
Intel, likewise, is adding an extension that expands SYCL’s functions with APIs similar to those of CUDA to make porting
as easy as possible for users.

As the other two applications, [Grid](https://github.com/paboyle/Grid/tree/develop/Grid) and HotQCD, already had
vendor-independent programming interfaces, the work being done to them is backend-intensive.
