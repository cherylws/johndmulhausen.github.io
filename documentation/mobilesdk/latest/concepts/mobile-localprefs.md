---
title: Android System Properties
---

Use Android System Properties to set various device configuration options for testing and debugging.

Use Android System properties to set device configuration options. Local Preferences are being deprecated and should no longer be used for setting debug options.

## System Properties

**Basic Usage**

Set value:

```
adb shell setprop &lt;name&gt; &lt;value&gt;
```

Example: 

```
adb shell setprop debug.oculus.frontbuffer 0
```

Result: Disables front buffer rendering.

Get current value:

```
adb shell getprop &lt;name&gt;
```

Example: 

```
adb shell getprop debug.oculus.gpuLevel
```

Result: Returns currently-configured GPU Level, e.g., 1.

Get all current values:

```
adb shell getprop | fgrep "debug.oculus"
```

Result: Returns all System Preferences settings on the device.

|         System Property         |      Values      |                                                                                                      Function                                                                                                      |
|---------------------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   debug.oculus.enableCapture   |       0, 1       |                                                                      Enables support for Oculus Remote Monitor to connect to the application.                                                                      |
|      debug.oculus.cpuLevel      |    0, 1, 2, 3    |                                                                                            Changes the fixed CPU level.                                                                                            |
|      debug.oculus.gpuLevel      |    0, 1, 2, 3    |                                                                                            Changes the fixed GPU level.                                                                                            |
|   debug.oculus.asyncTimewarp   |       0, 1       |                                                       Set to 0 to disable Asynchronous TimeWarp/enable Synchronous TimeWarp. Default is 1 (ATW is enabled).                                                       |
|    debug.oculus.frontbuffer    |       0, 1       |                                                                                            Disable/enable front buffer.                                                                                            |
|     debug.oculus.gpuTimings     |      0, 1, 2      |                                           Turns on GPU timings in logcat (off by default due to instability). A setting of 2 is necessary on phones using the Mali GPU.                                           |
|   debug.oculus.simulateUndock   |  -1, 0, 1, , 10  |                                                                         Simulate an undocking event after the specified number of seconds.                                                                         |
| debug.oculus.enableVideoCapture |       0, 1       | When enabled, each enterVrMode generates a new mp4 file in /sdcard/oculus/VideoShots/. Videos are full resolution, undistorted, single-eye, with full-compositing support. Defaults are 1024 resolution at 5 Mb/s. |
|    debug.oculus.phoneSensors    |       0, 1       |                                              Set to 0 to disable limited orientation tracking provided by phone sensors while in Developer Mode (enabled by default).                                              |
|    debug.oculus.textureWidth    |       1-max       |                                       Set the default VrApi texture width (default = 1024). Allows resetting apps to different resolutions for testing without repackaging.                                       |
|   debug.oculus.textureHeight   |       1-max       |                                       Set the default VrApi texture height (default = 1024). Allows resetting apps to different resolutions for testing without repackaging.                                       |
|    debug.oculus.videoBitrate    | No defined values |                                              Set the video capture bitrate (default = 5 Mb/s). Note - bitrates above 5 Mb/s may have a significant performance cost.                                              |
|  debug.oculus.videoResolution  | No defined values |                           Set the video capture resolution (default = 1024). Common resolutions are 512, 720, and 1024. Resolutions above 1024 may have a significant performance cost.                           |
