---
title: Get Current Display Frequency
---

Returns the current display frequency for the connected HMD.

## Overview

Returns the current display frequency for the connected headset. For the Oculus Rift, this value is always 90 Hz. For Gear VR, this value is always 60 Hz. For Oculus Go, this value may either be 60 Hz or 72 Hz.

## Blueprint

![](/images/documentationunreallatestconceptsunreal-blueprints-get-current-display-frequency-0.png)

## Arguments

* No arguments.


## Output

* Return Value: A floating point value that indicates the current display frequency of the connected headset, in frames per second. Example return value: 72.0


## Sample

In this sample, the frame rate is set to 72 Hz if it is currently 60 Hz. TBD

![](/images/documentationunreallatestconceptsunreal-blueprints-get-current-display-frequency-1.png)
