---
title: Oculus Unreal Engine 4 Integration 1.25 Release Notes
---

These release notes describe changes to Oculus's Unreal Engine 4.19 available from the Oculus GitHub repository.

## 1.25.0

New Features

* **Fixed Foveated Rendering (FFR) on Oculus Go** – FFR enables the edges of the eye buffers to be rendered at a lower resolution than the center portion of the eye buffers. FFR is available only on Oculus Go. Unreal provides support for FFR which can easily be accessed through a set of Blueprints. For a general introduction to FFR, please see the blog article [Optimizing Oculus Go for Performance](https://developer.oculus.com/blog/optimizing-oculus-go-for-performance/). The effect of using FFR is nearly imperceptible, but it provides important benefits, including:


	+ Significantly improves GPU fill performance
	+ Reduces power consumption, and thereby reduces heat and increases battery life
	+ Enables apps to increase the resolution of eye textures, which improves the viewing experience, while maintaining performance and power consumption levels
	The following Blueprints provide easy access to the FFR functionality for Unreal applications that run on Oculus Go:


	+  Get Tiled Multires Level
	+ Set Tilted Multires Level 
	For more information, see [Rendering](/documentation/unreal/latest/concepts/unreal-advanced-rendering/ "This section describes important rendering options and tools that can significantly improve your application.").


* **Dynamic Display Frequency Throttling on Oculus Go** – With Oculus Go, you can switch the frame rate between 60 Hz and 72 Hz. All mobile devices must deal with heat and battery issues. Mobile chipsets are very efficient, but they still generate a significant amount of heat and draw a lot of battery power during computationally intense tasks. On a phone or tablet, it is normal for an overtaxed mobile CPU to simply slow down in order to avoid overheating. On a VR device, that approach generally leads to a loss of application frame rate, which reduces the quality of the experience and can immediately make users uncomfortable. One solution is to dynamically downgrade the display frequency from 72 Hz to 60 Hz during heavy rendering. Three Blueprints are provided to make it easy to manage the display frequency for Unreal applications that run on Oculus Go:
	+ Get Available Display Frequencies – Retrieves an array of floats that represent the available display frequencies
	+ Get Current Display Frequency – Retrieves a float that represents the current display frequency
	+ Set Display Frequency – Accepts a float and sets the current display frequency to that value 
	For more information, see [Rendering](/documentation/unreal/latest/concepts/unreal-advanced-rendering/ "This section describes important rendering options and tools that can significantly improve your application.").


* **Native Gear VR Touchpad Integration** – The Oculus UE4 integration provides a native interface to the Gear VR touchpad. Prior to this release of the Oculus UE4 integration, the touchpad was linked to the Android integration which did not work properly in all situations. The following Blueprints facilitate adding the native Gear VR touchpad integration into your Unreal applications:
	+ Oculus Touchpad Back
	+ Oculus Touchpad Press
	+ Oculus Touchpad X-Axis
	+ Oculus Touchpad Y-Axis
	+ Get Oculus Touchpad X-Axis
	+ Get Oculus Touchpad Y-Axis
	


Bug Fixes

* Not applicable


Known Issues

* There's a bug affecting the ovr\_SetBoundaryLookAndFeel API by which color set operations to the visualized boundary grid don't work if they're called while the HMD is not being worn.
* A significant drop in frame rate occurs when UE4 is not in focus in VR preview mode. To avoid this issue, uncheck the Use Less CPU when in **Background** in **Edit** &gt; **Editor Preferences** &gt; **General** (left sidebar) &gt; **Miscellaneous** (left sidebar) &gt; **Performance**.
* Exclusive Mode issues: Setting the mirror window to full-screen exclusive mode will not work correctly if the monitor and HMD are connected to different GPUs.
* Stereo Layer Depth Ordering: Doesnâ€™t support head-locked layers, only world-locked and tracker-locked.
* Hybrid Monoscopic Rendering: In Unreal version 4.15, this feature is available for mobile only.

