---
title: Set CPU and GPU Levels
---
Sets the clock rates for the CPU and GPU on mobile devices.

## Overview

Sets the clock rates for the CPU and GPU on mobile devices, as described in [Power Management](/documentation/mobilesdk/latest/concepts/mobile-power-overview/). For current hardware, the CPU and GPU levels can be set to 0, 1, 2, or 3. A value of 0 causes the CPU or GPU to operate at the slowest clock rate, which is most power efficient. A value of 3 causes the CPU or GPU to operate at the fastest clock rate, which produces the most heat and uses the most battery power.

Note that the Oculus Go provides a feature called Dynamic Clock Throttling, which treats the CPU and GPU levels as a baseline; the system can choose to dynamically increase the CPU and GPU clock rates based on application and system performance. For more information, see [Power Management](/documentation/mobilesdk/latest/concepts/mobile-power-overview/).

## Managing Power Consumption

Mobile devices are typically constrained by the processing power of the device and its ability to dissipate heat.

To set your clock level in Unreal apps, use the SetCPUAndGPULevels blueprint.

On Oculus Go, we've made the management of CPU and GPU level much simpler by making it almost entirely automatic. This feature is called Dynamic Throttling. Oculus Go applications are compatible with Gear VR, and the basic power management API remains the same. The developer can set CPU and GPU levels between 0 and 3 on Gear VR, and between 0 and 4 on Oculus Go. On Go, these levels are treated as a baseline, and the system can choose to dynamically clock the CPU and GPU up as necessary to maintain performance. The goal of this system is to retain advantages of Gear VR's Fixed Clock Policy while trying to mitigate its drawbacks.

For more information on power management see: [Managing Power Consumption](/documentation/mobilesdk/latest/concepts/mobile-power-overview/#mobile-power-overview)

## Blueprint

![](/images/documentation-unreal-latest-concepts-unreal-blueprints-set-cpu-and-gpu-levels-0.png)  
## Arguments

* CPU Level: The setting for the CPU clock rate. Allowable values are: 0, 1, 2, or 3.
* GPU Level: The setting for the GPU clock rate. Allowable values are: 0, 1, 2, or 3.
## Output

* No output.
