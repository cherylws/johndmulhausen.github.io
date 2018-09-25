---
title: Get GPU Utilization
---
Returns the CPU utilization availability and value.

## Overview

This blueprint can be used to determine how much GPU capacity is available at the time the blueprint is called. Note that GPU utilization levels typically vary widely, and often fluctuate within milliseconds. However, in some situations the GPU utilization level may remain consistent for longer periods of time. For example, a GPU may be completely overloaded on an ongoing basis if the rendering process is GPU-bound and is not keeping up with the frame rate.

## Blueprint

![](/images/documentation-unreal-latest-concepts-unreal-blueprints-get-gpu-utilization-0.png)  
## Arguments

* No arguments.
## Output

* Is GPU Available: A Boolean that is True if a GPU utilization value is available (and provided in GPU Utilization), and is False otherwise.
* GPU Utilization: A floating point value, between 0.0 and 1.0, that indicates the current load on the GPU, where 0.0 = no utilization, and 1.0 = fully utilized.
