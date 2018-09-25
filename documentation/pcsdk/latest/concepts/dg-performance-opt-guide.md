---
title: VR Performance Optimization Guide
---
This guide provides actionable guidance for tracking down and solving VR performance issues.

## Why Performance Optimization?

In order to create the best VR experience for your users, it is important to optimize your applications for peak performance on Oculus recommended spec hardware. Otherwise, you may find that your applications exhibit judder, flickering black areas on the peripheries, or other performance-related problems.

In general, performance issues arise because it can be difficult for applications and game engines to keep up with Riftâ€™s refresh rate of 90 Hz. By carefully and systematically tracking down the issues that are causing performance problems and then implementing the necessary optimizations, you can create a significantly better overall user experience.

## Scope of this Guide

This guide targets both application developers and engine developers. 

This guide addresses a range of tools and methods. We start by covering high-level approaches that help you to narrow down the basic causes for the performance issues that your application may be exhibiting. Then we delve deeper into lower-level tools and analytical approaches, including Event Tracing for Windows (ETW), Windows Performance Analyzer (WPA), and GPUView. These lower-level approaches can be very helpful for solving complex and subtle VR performance issues, especially for game engine developers. 

At the end of this guide, we provide a step-by-step tutorial that utilizes all of the tools discussed in this guide, and includes code samples and screenshots. 

* **[Guidelines for VR Performance Optimization](/documentation/pcsdk/latest/concepts/dg-performance-guidelines/)**  
This section covers the general principles that you should follow in order to effectively optimize your VR applications.
* **[Workflows: The process flows you should follow](/documentation/pcsdk/latest/concepts/dg-performance-workflows/)**  
This section covers the workflows that you should use when tracking down performance problems.
* **[Performance Optimization Tools](/documentation/pcsdk/latest/concepts/dg-performance-tools/)**  
This section covers the tools that you should use when tracking down performance problems.
* **[Tutorial: Optimizing a Sample Application](/documentation/pcsdk/latest/concepts/dg-performance-tutorial/)**  
This section is a tutorial that provides a detailed hands-on guide to VR performance optimization.
* **[Additional Resources](/documentation/pcsdk/latest/concepts/dg-performance-additional-resources/)**  
This section provides links to additional resources that you can consult for more information about VR application optimization issues.
