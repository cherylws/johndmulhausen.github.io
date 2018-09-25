---
title: Oculus Rift: Testing and Performance Analysis
---
This guide describes basic testing and performance analysis for Oculus Rift development in Unreal. 

VR application debugging is a matter of getting insight into how the application is structured and executed, gathering data to evaluate actual performance, evaluating it against expectation, then methodically isolating and eliminating problems.

When analyzing or debugging, it is crucial to proceed in a controlled way so that you know specifically what change results in a different outcome. Focus on bottlenecks first. Only compare apples to apples, and change one thing at a time (e.g., resolution, hardware, quality, configuration).

Always be sure to profile, as systems are full of surprises. We recommend starting with simple code, and optimizing as you go - don’t try to optimize too early.

## Performance Targets

Before debugging performance problems, establish clear targets to use as a baseline for calibrating your performance.

These targets can give you a sense of where to aim, and what to look at if you’re not making frame rate or are having performance problems.

Below you will find some general guidelines for establishing your baselines, given as approximate ranges unless otherwise noted.

**PC**

* 90 FPS (required by Oculus Store)
* 500-1,000 draw calls per frame
* 1-2 million triangles or vertices per frame
For more information, see:

* [PC SDK Developer Guide](/documentation/pcsdk/latest/concepts/book-dg/)
* Oculus Store Submission Requirements
	+ [Oculus Rift App Requirements](/documentation/publish/latest/concepts/publish-mobile-req/)
	+ [Rift Virtual Reality Check (VRC) Guidelines](/distribute/latest/concepts/publish-rift-app-submission/)
	
## Rift Performance HUD

The Oculus Performance Heads-Up Display (HUD) is an important, easy-to-use tool for viewing timings for render, latency, and performance headroom in real-time as you run an application in the Oculus Rift. The HUD is easily accessible through the Oculus Debug Tool provided with the PC SDK. You may activate it in the Viewport by pressing the ~ key.

For more details, see the [Performance Heads-Up Display](/documentation/pcsdk/latest/concepts/dg-hud/) and [Oculus Debug Tool](/documentation/pcsdk/latest/concepts/dg-debug-tool/) sections of the Oculus Rift Developers Guide.

## Rift Performance Guide

For a deep discussion of performance optimization techniques with the native PC-SDK, which provides a lot of generally useful performance optimization information that can also apply to UE4 applications, please see[Oculus Performance Optimization Guide](/documentation/pcsdk/latest/concepts/dg-performance-opt-guide/).

## Rift Compositor Mirror

The compositor mirror is an experimental tool for viewing exactly what appears in the headset, with Asynchronous TimeWarp and distortion applied.

The compositor mirror is useful for development and troubleshooting without having to wear the headset. Everything that appears in the headset will appear, including Oculus Home, Guardian boundaries, in-game notifications, and transition fades. The compositor mirror is compatible with any game or experience, regardless of whether it was developed using the native PC SDK or a game engine.

For more details, see the [Compositor Mirror](/documentation/pcsdk/latest/concepts/dg-compositor-mirror/) section of the PC SDK Guide.

## Graphics Debugging

**Mali Graphics Debugger**

If you have a Mali phone, such as a GALAXY S6, you can use the Mali Graphics Debugger built into Unreal by selecting it by opening **Project Settings**, selecting the **Android** option on the left, and setting **Graphics Debugger** to **Mali Graphics Debugger**.

Note that because there are no swap buffers in VR, Gear VR does not currently support frame delimiters. Consequently, application frames will be displayed as different render passes of the same frame.

![](/images/documentation-unreal-latest-concepts-unreal-debug-rift-0.png)  
## Additional Third-Party Tools

**ETW and GPUView**

[Event Tracing for Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/bb968803%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396) (ETW) is a trace utility provided by Windows for performance analysis. [GPUView](https://msdn.microsoft.com/en-us/library/windows/desktop/jj585574%28v=vs.85%29.aspx?f=255&MSPPError=-2147217396) view provides a window into both GPU and CPU performance with DirectX applications. It is precise, has low overhead, and covers the whole Windows system. 

In some cases ETW and GPUView may be useful for debugging problems such as system-level contention with background processes. For a detailed description of how to use ETW with our native Rift SDK, see [VR Performance Optimization Guide](/documentation/pcsdk/latest/concepts/dg-performance-opt-guide/) in our PC SDK Developer Guide. Not all of the content will be relevant to the Unreal developer, but it contains a lot of applicable conceptual material that may be very useful.

**Systrace**

Reports complete Android system utilization. Available here: [http://developer.android.com/tools/help/systrace.html](https://developer.android.com/tools/help/systrace.html)

**NVIDIA NSight**

NSight is a CPU/GPU debug tool for NVIDIA users, available in a [Visual Studio version](https://developer.nvidia.com/nvidia-nsight-visual-studio-edition) and an [Eclipse version](https://developer.nvidia.com/nsight-eclipse-edition).

Mac OpenGL Monitor

An OpenGL debugging and optimizing tool for OS X. Available here: [https://developer.apple.com/library/mac/technotes/tn2178/\_index.html#//apple\_ref/doc/uid/DTS40007990](https://developer.apple.com/library/mac/technotes/tn2178/_index.html#//apple_ref/doc/uid/DTS40007990)

**APITrace**

<https://apitrace.github.io/>

## Other Resources

For detailed information about Oculus development, go to:

* Unreal: Virtual Reality Development: [https://docs.unrealengine.com/latest/INT/Platforms/VRZ/](https://docs.unrealengine.com/latest/INT/Platforms/VR/)
* Unreal: Oculus Rift wiki: [https://wiki.unrealengine.com/Oculus\_Rift](https://wiki.unrealengine.com/Oculus_Rift)
* Oculus Forums/Unreal: <https://forums.oculus.com/developer/categories/unreal>
* Unreal Forums/VR Development: <https://forums.unrealengine.com/forumdisplay.php?27-VR-Development>
## Contact

Visit our developer support forums at [https://developer.oculus.com](/).

Our Support Center can be accessed at [https://support.oculus.com](https://support.oculus.com/).

