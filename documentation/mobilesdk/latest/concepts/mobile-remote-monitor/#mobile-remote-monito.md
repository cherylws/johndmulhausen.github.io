---
title: Oculus Remote Monitor
---
The Oculus Remote Monitor client connects to VR applications running on remote devices to capture, store, and analyze data streams.

Oculus Remote Monitor is compatible with any Oculus mobile application built with Unity, Unreal Engine, or Native development tools.

Download the Oculus Remote Monitor client:

* [Oculus Remote Monitor for Windows](/downloads/package/oculus-remote-monitor-for-windows/)
* [Oculus Remote Monitor for macOS](/downloads/package/oculus-remote-monitor-for-os-x/)
![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-0.png)  
## Setup

### Enable Capture Server

Note: Some of the menu locations described in this process might slightly differ depending on your Samsung model.To enable the Capture Server on a device:

1. Enable Developer Mode (instructions [here](unresolvable-reference)) and USB Debugging on your device (instructions [here](/documentation/mobilesdk/latest/concepts/mobile-device-setup/ "This section will provide information on how to set up your supported Gear VR device for running, debugging, and testing your mobile application.")).
2. Plug your device into your computer via USB. 
3. If your device requests permission to "Allow USB debugging", accept.
4. Open Oculus Remote Monitor and select **Settings > Set ADB Path**. Verify that the ADB Path is set to your local installation of adb (included with the Android SDK). For example: C:\Users\$username\AppData\Local\Android\sdk\platform-tools\adb.exe
5. Click **Enable/Disable Remote Capture Server** in the Remote Capture menu. You should now see the device ID of your connected device in the Device Settings list. Select your device ID and click **OK**.
The Capture Server will now run automatically whenever a VR application starts. You may need to restart your VR app for it to appear for debugging.

Note: If you reboot your device, the Device Settings are reset and you must click the Enable Capture check box again.### Network Setup

Oculus Remote Monitor uses a UDP-broadcast-based auto-discovery mechanism to locate remote hosts, and then a TCP connection to access the capture stream. The host and the client must be on the same subnet, and the network must not block or filter UDP broadcasts or TCP connections.

If you are on a network that may have such restrictions (e.g., a corporate network), we recommend setting up a dedicated network or tethering directly to your device. Furthermore, frame buffer capturing is extremely bandwidth intensive. If your signal strength is low or you have a lot of interference or traffic on your network, you may need to disable Capture Frame Buffer before connecting to improve capture performance.

Oculus Remote Monitor uses UDP port 2020 and TCP ports 3030->3040.

### Application Setup

Because we use a direct network connection, the following permission is required in your application's AndroidManifest.xml:

<!-- Network access needed for OVRMonitor --> <uses-permission android:name="android.permission.INTERNET" />## Basic Usage

### Stream Remote Capture

If the host and client are on the same subnet and the network is configured correctly (see [Network Setup](/documentation/mobilesdk/latest/concepts/mobile-remote-monitor/#mobile-remote-monitor-setup) above), Oculus Remote Monitor automatically discovers any compatible applications running on the network.

To begin capturing and viewing data:

1. Click **Start Remote Capture** in the **Remote Capture** menu.
2. Select the host you want to monitor.
3. Click **Session Settings** and select the session settings you want to monitor. (Optional) 
4. Click **OK**.
### Open Capture File

Each time you connect to a host, the Oculus Remote Monitor automatically compresses and saves the incoming data stream to disk under a unique filename in the format package-YYYYMMDD-HHMMSS-ID.dat. The default recordings directory for these files are in your Documents folder, under the OVRMonitorRecordings sub-folder. You can change this directory in the **Settings** menu.

To open saved capture files, click **File > Open Local Capture File**.

### Performance Overview

The overview provides a high-level performance overview. It plots a graphical summary of the VrAPI messages and error conditions against a timeline.

To view the log, click on the **Overview** tab.

* Click the Performance Overview icon.
Move the pointer over the performance overview to reveal details of the collected data. Double-click anywhere in the overview to open the [Profiler Data](/documentation/mobilesdk/latest/concepts/mobile-remote-monitor/#mobile-remote-monitor#profilerdata) view at that precise point in the timeline.

![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-1.png)  
Frame Buffer

Screen captures of the pre-distorted frame buffer. Move the pointer over this section to view the screenshots captured at that point in time. 

Frames per Second

* Delivered Frames. A well-performing application continuously delivers 60 frames per second.


* Screen Tears. The number of tears per second. A well-performing application does not exhibit any tearing.


* Early Frames. The number of frames that are completed a whole frame early.


* Stale Frames. The number of stale frames per second. A well-performing application does not exhibit any stale frames.


For more information, see [Basic Performance Stats through Logcat](/documentation/mobilesdk/latest/concepts/mobile-logcat-perf-stats/ "A simple way to get some basic performance numbers is to use logcat with a filter for VrApi.").

Head-Pose Prediction Latency (ms)

The number of milliseconds between the latest sensor sampling for tracking and the anticipated display time of new eye images.Performance Levels

The CPU and GPU clock levels and associated clock frequencies, set by the application. Lower clock levels result in less heat and less battery drain.Thermal (°C)Temperatures in degrees Celsius. Well-optimized applications do not cause the temperature to rise quickly. There is always room for more optimization, which allows lower clock levels to be used, which, in return, reduces the amount of heat that is generated.Available Memory (GB)The amount of available memory, displayed every second. It is important to keep a reasonable amount of memory available to prevent Android from killing backgrounded applications, like Oculus Home.### Console

VrAPI reports various messages and error conditions to Android's logcat as well as to the Oculus Remote Monitor, which provides the thread and timestamp of each message. The Logging Viewer provides raw access to this data.

To view the log, click on the **Logs** tab.

Warnings and errors are color-coded to stand out easier, and unlike logcat, thread IDs are tracked so you know exactly when and where it occurred.

![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-2.png)  
### Remote Variables

Applications may expose user-adjustable parameters and variables in their code. Nearly any constant in your code may be turned into a knob that can be updated in real-time during a play test.

When streaming a capture, a control panel allowing you to view and adjust the available remote variables will automatically appear. 

![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-3.png)  
VrApi exposes CPU and GPU Levels to allow developers to quickly identify their required clock rates. Applications are also free to expose their own options that you can select or adjust.

**ShowTimeWarpTextureDensity**: This experimental feature toggles a visualization mode that colors the screen based on the texel:pixel ratio when running TimeWarp (green indicates 1:1 ratio; dark green < 1:1 ratio; red > 2:1 ratio). 

### Settings

You may view and adjust the settings in the Settings menu.

ADB Path

Configurable any time. If it does not point to a valid executable when Monitor runs, Monitor will attempt to locate a valid copy of adb by checking the environment variable. If that fails, Monitor will search under ANDROID\_HOME.

Recordings DirectorySpecifies the location in which Monitor will automatically store capture files when connected to a remote host. The default is the current user's Documents directory under OVRMonitorRecordings.Frame Buffer Compression QualityUsed for client-side recompression of the frame buffer. This helps offload compression load from the host while allowing for significant savings in memory usage on the client. Lower-quality settings provide greater memory savings, but may result in blocking artifacts in the frame buffer viewer.### Profiler Data

The Profiler Data view provides both real-time and offline inspection of the following data streams on a single, contiguous timeline:

* CPU/GPU events
* Sensor readings
* Console messages, warnings, and errors
* Frame buffer captures
VrAPI also has a number of other events embedded to help diagnose VR-specific scheduling issues.

To view the data streams, click on the **Profiler** tab.

The Profiler Data view has a number of controls to help you analyze the timeline.

* The space bar toggles between real-time timelines scrolling and freezing at a specific point in time. This lets you quickly alternate between watching events unfold in real-time and pausing to focus in on a point of interest without stopping or restarting.
* The mouse wheel zooms the view in and out.
* Right-click to save a screenshot of the current view or to hide a data stream. To un-hide hidden data streams, click **Show Hidden Data Streams**
* Click and drag to pan the timeline forwards or backwards in time.
![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-4.png)  
The Performance Data Viewer screen shows a selected portion of the application timeline:

Frame Buffer

Provides screen captures of the pre-distorted frame buffer, timestamped the moment immediately before the frame was handed off to the TimeWarp context. The left edge of each screenshot represents the point in time in which it was captured from the GPU.

VSync

Displays notches on every driver v-sync event.

GPU Context

GPU Zones inserted into the OpenGL Command Stream via Timer Queries are displayed in a similar manner as CPU events. Each row corresponds to a different OpenGL Context. Typical VR applications will have two contexts: one for TimeWarp, and one for application rendering. Note that on tiler GPUs, these events should be regarded as rough estimates rather than absolute data.

CPU Thread

Hierarchical visualization of wall clock time of various functions inside VrAPI along with OpenGL Draw calls inside the host application. Log messages are displayed on their corresponding CPU thread as icons. Mouse over each icon to display the corresponding message (blue circles), warning (yellow squares), or error (red diamonds).

SensorGeneral sensor data visualizer. CPU and GPU clocks are visualized in the screenshot shown above, but other data may be displayed here, such as thermal sensors, IMU data, et cetera.![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-5.png)  
## Using Oculus Remote Monitor to Identify Common Issues

### Tearing

Tearing occurs in VR applications any time TimeWarp rendering fails to render ahead of scanout. VrApi attempts to detect this with a GPU Sync Object to determine when the GPU completes rendering distortion for a given eye. If for any reason it does not complete in time, VrApi prints a warning to logcat, which Oculus Remote Monitor picks up.

V-sync %d: Eye %d, CPU latency %f, GPU latency %f, Total latency %fIf you are running on a Samsung GALAXY S6, you may also see tearing events by looking at the GPU Context that is running *WarpToScreen*.

Example:

![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-6.png)  
In this example, because the refresh rate of the display is 60 Hz, the ideal running time of WarpToScreen is 16.66 ms, but a scheduling/priority issue in the application caused the second eye to be executed 10 ms late, pushing WarpToScreen to run for 26.81 ms. The actual eye distortion draw calls are barely visible as two distinct notches under each WarpToScreen event on the GPU.

### Dropped Frames

Your Oculus Remote Monitor capture will show you any lost frames during the capture session and information about how the app was performing at the time the frame was lost. Use this data and the corresponding screenshot to troubleshoot problem areas in your app. 

Information about CPU/GPU levels can be found on the [Power Management](/documentation/mobilesdk/latest/concepts/mobile-power-overview/#mobile-power-overview "Power management is a crucial consideration for mobile VR development.") page. 

![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-7.png)  
### Application OpenGL Performance Issues

Oculus Remote Monitor is capable of capturing OpenGL calls across the entire process (enabled with the *Graphics API* option). Application-specific performance issues can therefore be spotted at times. In the example below, an application was mapping the same buffer several times a frame for a particle effect. On a Note 4 running KitKat, the GL driver triggered a sync point on the second glUnmapBuffer call, causing it to take away 2.73 ms - without the sync point, this same call takes around 0.03 ms. After spotting this issue, the developer was able to quickly fix the buffer usage and reclaim that CPU time.

![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-8.png)  
### Unlocked CPU Clocks

VrApi attempts to lock the CPU and GPU clocks at particular frequencies to ensure some level of execution speed and scheduling guarantees. These are configurable via the CPULevel and GPULevel available in the API.

When in VR Developer Mode, the clocks may occasionally unlock when out of the headset for too long. When this happens, the CPU/GPU Clock Sensors go from extremely flat to extremely noisy, typically causing many performance issues like tearing and missed frames, as seen below:

![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-9.png)  
Note that on a Samsung GALAXY S6, we allow the clocks to boost slightly under certain conditions, but only by a small amount in typical cases, and it should never drop below the requested level. It is also fairly common for some cores to go completely on and offline occasionally.

### Network Bandwidth Stalls

VrCapture uses a fixed-size FIFO internally to buffer events before they are streamed over the network. If this buffer fills faster than we can stream its contents, we are left in a tricky situation. If your network connection stalls long enough for any reason, it eventually causes the host application to stall as well.

This is easily spotted in Oculus Remote Monitor - look for around two seconds of extremely long events on the OVR::Capture thread followed by other threads stalling as well. We provide a large internal buffer, so a few network hitches shouldn’t affect your application, but if they persist long enough, a random event inside your application will eventually stall until the Capture thread is able to flush the buffer.

In the example below, several seconds of poor network connectivity (see by long AsyncStream\_Flush events) eventually caused the MapAndCopy event on the application’s render thread to stall until it was eventually released by the Capture thread:

![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-10.png)  
If you find it difficult to capture reliably because of this issue, we recommend disabling Frame Buffer Capturing before connecting, as this feature consumes the bulk of the bandwidth required.

### Thermal Limits

If your application requests CPU/GPU Levels are too high, the internal SoC and battery temperatures will rise slowly, yet uncontrollably, until it hits the thermal limit. When this happens, GearVR Service will terminate the application and display a thermal warning until the device cools down.

It may take quite a long time to encounter this scenario during testing. Monitoring thermals in Oculus Remote Monitor is a great way to quickly see if your application causes the device temperature to rise perpetually. Mouse over the Sensor graph to give the precise readout at any given time. We recommend keeping an eye on it.

If the temperature exceeds the device’s first thermal trip point, the graph turns bright red, which typically occurs a few minutes before GearVR Service shuts the application down, and should serve as a stern warning that you should probably lower the CPU/GPU Levels.

![](/images/documentation-mobilesdk-latest-concepts-mobile-remote-monitor-mobile-remote-monitor-11.png)  
