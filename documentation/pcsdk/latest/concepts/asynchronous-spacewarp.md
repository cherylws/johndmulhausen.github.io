---
title: Asynchronous SpaceWarp
---
Asynchronous Spacewarp (ASW) is a frame-rate smoothing technique that almost halves the CPU/GPU time required to produce nearly the same output from the same content.

## Overview

ASW applies animation detection, camera translation, and head translation to previous frames in order to predict the next frame. As a result, motion is smoothed and applications can run on lower performance hardware. For a great introduction to ASW, please see [Asynchronous Spacewarp](/blog/asynchronous-spacewarp/).

The Rift operates at 90Hz. With ASW, when an application fails to submit frames at 90Hz, the Rift runtime drops the application down to 45Hz with ASW providing each intermediate frame. 

By default, ASW is enabled for all supported Rift versions. 

ASW tends to predict linear motion better than non-linear motion. If your application is dropping frames, you can either adjust the resolution or simply allow ASW to take over.

## Requirements

ASW requires the following:

* Oculus Runtime 1.9 or later
* Windows 8 or later
* For NVIDIA, driver 373.06 or later
* For AMD, driver 16.40.2311 or later
Until the minimum specification is released, we recommend the following GPU versions for ASW testing:

ManufacturerSeriesMinimum RAMMinimum ModelNVIDIAPascal3GB1060NVIDIAMaxwell4GB960AMDPolaris4GB470## Testing ASW

To test ASW, start the Oculus Debug Tool, which is located here:

C:\Program Files\Oculus\Support\oculus-diagnostics\OculusDebugToolSet the Asynchronous Spacewarp option to one of the following values (or run tests using various different options):

* Auto enables ASW, so that it is applied automatically when needed.
* Disabled disables ASW.
* Force 45fps, ASW disabled causes the refresh rate to be 45hz with ASW disabled.
* Force 45fps, ASW enabled causes the refresh rate to be 45hz with ASW enabled 
![](/images/documentation-pcsdk-latest-concepts-asynchronous-spacewarp-0.png)  
