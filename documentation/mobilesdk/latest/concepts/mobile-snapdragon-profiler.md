---
title: Snapdragon Profiler
---
The Qualcomm Snapdragon Profiler allows developers to analyze performance on Android devices with Snapdragon processors over USB, including CPU, GPU, memory, power, and thermal performance. 

Samsung Snapdragon phones running VrDriver 1.5.3 and later auto-detect when Snapdragon Profiler is running, and configure themselves for best capture.

## Basic Usage

1. Download and install the Snapdragon Profiler from [Qualcomm](https://developer.qualcomm.com/software/snapdragon-profiler).
2. Attach a Snapdragon-based S7 with Android M or N via USB, with VR developer mode enabled (for instructions, see [unresolvable-reference.xml](unresolvable-reference)).
3. Run Snapdragon Profiler. It is important to do this before starting the app you want to use.
4. Select *Connect to a Device*. If you do this right after starting, you may need to wait a few seconds for the phone icon to turn green (driver files are being transferred).
5. Click *connect*.
6. Run the VR app that you want to profile. Note that you will see poor performance because of optimizations related to the performance testing - it will not affect your session.
7. Select either *trace* or *snapshot* capture modes.
8. In the "Data Sources" panel, select the app name. Note that only applications with the OpenGL requirement set in the manifest will show up. If the application has the required manifest setting but does not appear, try rebooting the phone and restarting the Snapdragon Profiler.
9. For traces, enable *OpenGL ES -> Rendering stages* for the most useful information, then click start capture, wait a second or two, and click stop capture.
10. For snapshots, you can capture a frame of commands without any extra options checked. The capture process can take tens of seconds if there is a lot of texture data to transfer
11. We recommend shutting down and restarting the Snapdragon Profiler between sets of tests.
12. Quit Snapdragon Profiler before unplugging your phone, so it can clean up. Donâ€™t forget this step!
