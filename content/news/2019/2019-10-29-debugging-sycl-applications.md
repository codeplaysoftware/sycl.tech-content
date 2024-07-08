---
contributor: rod
date: '2019-10-29T13:00:07+02:00'
external_url: https://www.codeplay.com/portal/10-29-19-debugging-sycl-applications
image: ../../../static/images/news/2019-10-29-debugging-sycl-applications.webp
title: Debugging SYCL Applications
tags:
  - debugging
  - applications
  - development
---

It's inevitable that you will need to debug your SYCL code at some point. While many of the techniques used are similar
to the way this would be done in any C++ code, there are some things to keep in mind. It's not always easy to debug your
code on the actual device you are executing on, for example a GPU, so SYCL offers a "host device" that can be used to
emulate what happens on the target device, and makes it much easier to track down where things are going wrong. This
post also outlines how you might go about debugging on your target device.
