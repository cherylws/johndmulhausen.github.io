---
title: Changes in Version 1.14.x
---



## Overview of Release 1.14.x

This release introduces improved support for three sensors and the Oculus Performance Profiler.

## New Features for 1.14.x

* The Oculus app now fully supports setting up three sensors for experimental 360° tracking. When connecting a third sensor, you are automatically prompted to set up experimental 360° tracking.
* The runtime now includes the Oculus Performance Profiler which displays a graph that shows statistics on the performance of your application. You can view the statistics in real time or export them to a CSV file. For more information, see [Performance Profiler](/documentation/pcsdk/latest/concepts/dg-performance-profiler/ "The Oculus Performance Profiler displays a graph that shows statistics on the performance of your application.").
* The Oculus Debug Tool moved from the SDK to the runtime. The new location is Program Files\Oculus\Support\oculus-diagnostics\OculusDebugTool.exe.
* Improved efficiency when updating the Oculus software.
* You'll now see where your Touch controllers are located as soon as you enter VR.
* Many games and experiences that previously required the Xbox One Wireless Controller can now be played using Touch controllers. These apps will use the buttons and triggers on Touch, but won’t support Touch controller tracking during gameplay. Apps are marked “Touch (as gamepad)” in the Oculus Store. 


## API Changes for 1.14.x

Previously, if the app collecting performance statistics did not have focus, the statistics would be zeroed out. Now, the statistics are returned with the process ID of the application that currently has focus (VisibleProcessId). This is useful when building performance tools that are separate from your game or experience.

## Known Issues

The following are known issues:

* Some older AMD CPUs are not currently compatible with Asynchronous SpaceWarp (ASW), which might cause your system to repeatedly crash. The workaround is to disable ASW by setting its registry key to 0. For more information, see [Asynchronous SpaceWarp](/documentation/pcsdk/latest/concepts/asynchronous-spacewarp/ "Asynchronous Spacewarp (ASW) is a frame-rate smoothing technique that almost halves the CPU/GPU time required to produce nearly the same output from the same content.").
* If you encounter intermittent tracking issues, remove the batteries from any Engineering Sample Oculus Remotes that you paired with your headset and contact Developer Relations for replacement remotes.
* If you bypass the shim and communicate with the DLL directly, without specifying a version to ovr\_Initialize, the DLL has no way of knowing the SDK version with which the application was built. This can result in unpredictable or erratic behavior which might cause the application to crash.
* There are some USB chipsets that do not meet the USB 3.0 specification and are incompatible with the Oculus Rift sensor. If you receive a notification in Oculus Home or the Oculus App, plug the sensor into a different USB 3.0 port (blue). If none of the USB 3.0 ports work, plug the sensor into a USB 2.0 port (black). 
* Antivirus software, such a McAfee, can cause installation issues. To work around the issue, make sure you have the latest updates and disable real-time scanning.
* If you encounter installation issues, delete the Oculus folder and install the software again.
* If the Rift displays a message that instructs you to take off the headset, remove it and place it on a flat surface for 10-15 seconds.
* The keyboard and mouse do not work in Oculus Home. To select an item, gaze at it and select it using the Oculus Remote or Xbox controller.
* Bandwidth-intensive USB devices, such as web cams and high-end audio interfaces, might not work when using the Rift. To work around this issue, install the device on another USB host controller or a separate computer.
* For dual-boot systems using DK2 or CB1 HMDs, the OS selection screen might appear on the HMD instead of the monitor. To work around this, try plugging the HMD into a different port or unplug the HMD while booting.
* If you are running your application from the Unity Editor and you press the controller's home button to return to Oculus Home, you will be prompted to close the application. If you select OK, Unity might remain in a state where it is running, but will never get focus. To work around this, restart Unity.

