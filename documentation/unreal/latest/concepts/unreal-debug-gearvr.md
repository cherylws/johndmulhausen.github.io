---
title: Gear VR: Testing and Performance Analysis
---
This guide describes basic testing and performance analysis for Gear VR development in Unreal. 

VR application debugging is a matter of getting insight into how the application is structured and executed, gathering data to evaluate actual performance, evaluating it against expectation, then methodically isolating and eliminating problems.

When analyzing or debugging, it is crucial to proceed in a controlled way so that you know specifically what change results in a different outcome. Focus on bottlenecks first. Only compare apples to apples, and change one thing at a time (e.g., resolution, hardware, quality, configuration).

Always be sure to profile, as systems are full of surprises. We recommend starting with simple code, and optimizing as you go - don’t try to optimize too early.

## Performance Targets

Before debugging performance problems, establish clear targets to use as a baseline for calibrating your performance.

These targets can give you a sense of where to aim, and what to look at if you’re not making frame rate or are having performance problems.

Below you will find some general guidelines for establishing your baselines, given as approximate ranges unless otherwise noted.

**Display Refresh Rate**

* 60 FPS (required by Oculus Store)
* 50-100 draw calls per frame
* 50,000-100,000 triangles or vertices per frame
**VRC Guidance**

* [Mobile Virtual Reality Check (VRC) Guidelines](/documentation/publish/latest/concepts/publish-mobile-req/)
## Debug Console

If your phone is set to Developer Mode, you may bring up a debug console for VR applications by pressing the screen with four fingers simultaneously while the application is running. 

Enter stat unit in the console for information about your application frame rate and CPU performance.

## Oculus Remote Monitor

The Oculus Remote Monitor client connects to VR applications running on remote mobile devices to capture, store, and display the streamed-in data. The VrCapture library is automatically included in Unreal projects, so setup and use of the Oculus Remote Monitor is easy.

![](/images/documentation-unreal-latest-concepts-unreal-debug-gearvr-0.png)  
Oculus Remote Monitor is available from our [Downloads](/downloads/unreal-engine/) page. For more information about setup, features, and use, see [Oculus Remote Monitor](/documentation/mobilesdk/latest/concepts/mobile-remote-monitor/) in our Mobile SDK guide.

* The Frame Buffer Viewer provides a mechanism for inspecting the frame buffer as the data is received in real-time, which is particularly useful for monitoring play test sessions. When enabled, the Capture library will stream a downscaled pre-distortion eye buffer across the network.
* The Performance Data Viewer provides real-time and offline inspection of the following on a single, contiguous timeline: 
	+ CPU/GPU events
	+ Sensor readings
	+ Console messages, warnings, and errors
	+ Frame buffer captures
	
* The Logging Viewer provides raw access to various messages and errors tracked by thread IDs.
* Nearly any constant in your code may be turned into a knob that can be updated in real-time during a play test.
## OVR Metrics Tool

OVR Metrics Tool reports application frame rate, heat, GPU and CPU throttling values, and the number of tears and stale frames per second. It is available for download from our [Downloads page](/downloads/).

OVR Metrics Tool can be run two modes. In Report Mode, it displays performance report about a VR session after it is complete. Report data may be easily exported as a CSV and PNG graphs.

![](/images/documentation-unreal-latest-concepts-unreal-debug-gearvr-1.png)  
In Performance HUD Mode, OVR Metrics Tool renders performance graphs as a VR overlay over any running Oculus application.

![](/images/documentation-unreal-latest-concepts-unreal-debug-gearvr-2.jpg)  
For more information, see [OVR Metrics Tool](/documentation/mobilesdk/latest/concepts/mobile-ovrmetricstool/) in our Mobile SDK Guide.

## Graphics Debugging

Different versions of the Gear VR ship with two possible chipsets:

* ARM for international phones
* Qualcomm for US/Canadian phones
With international phones, you can use Mali Graphics Debugger (MGD), as described below. On the US/Canadian phones, MGD doesn't work and you should use the [Snapdragon Profiler](https://developer.qualcomm.com/software/snapdragon-profiler) instead.

**Mali Graphics Debugger**

If you have a Mali phone, such as a GALAXY S6, you can use the Mali Graphics Debugger built into Unreal by selecting it by opening **Project Settings**, selecting the **Android** option on the left, and setting **Graphics Debugger** to **Mali Graphics Debugger**.

Note that because there are no swap buffers in VR, Gear VR does not currently support frame delimiters. Consequently, application frames will be displayed as different render passes of the same frame.

![](/images/documentation-unreal-latest-concepts-unreal-debug-gearvr-3.png)  
## GDB Debugging

Oculus branches of Unreal add support for debugging mobile sessions using ndk-gdb, a small shell script wrapped around GNU GDB that is included with the Android NDK.

Using ndk-gdb from the command line adds convenient features to your debugging workflow by allowing, for example, adding breakpoints, stepping through code, and inspecting variables with a command line interface.

To use ndk-gdb for debugging: 

1. Enable remote port forwarding to link your target mobile port to a PC port: adb forward tcp:$port tcp:$port
2. Set your device to Developer Mode (as described in our Mobile Developer Guide [here](/documentation/mobilesdk/latest/concepts/mobile-troublesh-device-run-app-outside/)).
3. Launch the application you wish to debug. 
4. Start gdbserver on the mobile device with the following Unreal console command: gdbserver $port where $port is your port number. You application should freeze, and will now be ready for debugging.
5. Launch the ndk-gdb client from the command line on your computer with the command gdb.exe. When it launches, type target remote :$port in the GDB command line to attach to your mobile device.
For more information on using GDB for debugging, see the [GNU GDB documentation](https://www.gnu.org/software/gdb/documentation/).

## Additional Third-Party Tools

**Systrace**

Reports complete Android system utilization. Available here: [http://developer.android.com/tools/help/systrace.html](https://developer.android.com/tools/help/systrace.html)

**NVIDIA NSight**

NSight is a CPU/GPU debug tool for NVIDIA users, available in a [Visual Studio version](https://developer.nvidia.com/nvidia-nsight-visual-studio-edition) and an [Eclipse version](https://developer.nvidia.com/nsight-eclipse-edition).

**Mac OpenGL Monitor**

An OpenGL debugging and optimizing tool for OS X. Available here: [https://developer.apple.com/library/mac/technotes/tn2178/\_index.html#//apple\_ref/doc/uid/DTS40007990](https://developer.apple.com/library/mac/technotes/tn2178/_index.html#//apple_ref/doc/uid/DTS40007990)

**APITrace**

<https://apitrace.github.io/>

## Other Resources

For detailed information about Oculus development, go to:

* Unreal: Virtual Reality Development: [https://docs.unrealengine.com/latest/INT/Platforms/VRZ/](https://docs.unrealengine.com/latest/INT/Platforms/VR/)
* Oculus Forums/Unreal: <https://forums.oculus.com/developer/categories/unreal>
* Unreal Forums/VR Development: <https://forums.unrealengine.com/forumdisplay.php?27-VR-Development>
## Contact

Visit our developer support forums at [https://developer.oculus.com](/).

Our Support Center can be accessed at [https://support.oculus.com](https://support.oculus.com/).

