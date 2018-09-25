---
title: OVR Metrics Tool
---
OVR Metrics Tool is an application that provides performance metrics for Oculus mobile applications.

OVR Metrics Tool reports application frame rate, heat, GPU and CPU throttling values, utilization, and the number of tears and stale frames per second. It is available for download from our [Downloads page](/downloads/).

OVR Metrics Tool can be run two modes. In **Report Mode**, it produces a performance report about a VR session after it is complete. Report data may be easily exported as a CSV and PNG graphs.

In **Performance HUD Mode**, OVR Metrics Tool renders performance graphs as a VR overlay over any running Oculus application.

OVR Metrics Tool may be used with any Oculus mobile application, including those built with Unity, Unreal, or our native mobile SDK.

## Installation

Install OVRMetricsTool.apk on any Gear VR-compatible Android phone. For more details, see "Using adb to Install Applications" in our [adb guide](/documentation/mobilesdk/latest/concepts/mobile-adb/#mobile-android-debug-intro "This guide describes how to perform common tasks using adb.") or the "Install an App" section of [Google's adb documentation](https://developer.android.com/studio/command-line/adb.html).

## Report Mode Usage

Run your VR application and conduct a session you wish to gather data for. Note that data will be logged from every application you run, including Oculus Home.

After you have finished your session and exited VR, open OVR Metrics Tool from your phone's desktop launcher and click the log entry that corresponds to your application.

You will see a series of graphs describing the performance of your session. Use the buttons at the bottom of the report to save the information or share an image of the report.

![](/images/documentation-mobilesdk-latest-concepts-mobile-ovrmetricstool-0.png)  
## Performance HUD Usage

Connect to your device using adb (for general instructions, see our adb guide), Enable Performance HUD Mode with the following commands:

adb shell setprop debug.oculus.notifPackage com.oculus.ovrmonitormetricsservice adb shell setprop debug.oculus.notifClass com.oculus.ovrmonitormetricsservice.PanelService adb shell am force-stop com.oculus.ovrmonitormetricsserviceAfter setting these properties, restart OVR Metrics Tool. This can be done over adb with the following command: adb shell am force-stop com.oculus.ovrmonitormetricsserviceNote that these properties must be set after each phone restart.

Once Performance HUD Mode is enabled, you can customize the HUD itself using the Options screen in the OVR Metrics Tool toolbar menu or by using the following adb commands:

adb shell setprop debug.oculus.omms.enableGraph (true|false) // show or hide the graph adb shell setprop debug.oculus.omms.enableGraph2 (true|false) // show or hide a secondary graph stat (dependent on stat) adb shell setprop debug.oculus.omms.enableStats (true|false) // show or hide the stats adb shell setprop debug.oculus.omms.pitch (number) // set the pitch of the perf hud (degrees from center) adb shell setprop debug.oculus.omms.yaw (number) // set the yaw of the perf hud (degrees from center) adb shell setprop debug.oculus.omms.distance (number) // set the distance of the perf hud (meters) adb shell setprop debug.oculus.omms.scale (number) // set the scale of the perf hud (1,2, or 3) adb shell setprop debug.oculus.omms.headLocked (true|false) // whether to head lock the hud or position it in spaceThe app needs to be restarted for changes to take effect.

To disable Performance HUD Mode, restart your phone or send the following three adb commands:

adb shell setprop debug.oculus.notifPackage '' adb shell setprop debug.oculus.notifClass '' adb shell am force-stop com.oculus.ovrmonitormetricsservice![](/images/documentation-mobilesdk-latest-concepts-mobile-ovrmetricstool-1.jpg)  
## Remote Device Management

To enable remote device management, select Connect to Device from the Options menu. This will search for local Oculus devices over Bluetooth. Tap a device to connect to it. Once connected, you can configure the HUD of the remote device and trigger screenshots.

## Automatic Screenshots

You can have screenshots automatically taken if performance does not meet a set limit by turning on the Screenshot on Dropped Frames option from the Options menu.

Once turned on, if the FPS is less the value specified in Dropped/Sec, and it stays below this value for the number of seconds specified by the Seconds option, a screenshot will be taken. Screenshots are stored in /sdcard/OVRMonitorMetricsService/Screenshots/.

## CPU/GPU Utilizaton Monitoring

Enable CPU and GPU utilization monitoring with the following property:

adb shell setprop debug.oculus.vrapilayers UtilPoller*GPU utilization is not available on devices with Mali chipsets.

