---
title: Performance Head-Up Display
---

The Performance Head-Up Display (HUD) enables you or your users to view performance information for applications built with the SDK. 

The Performance HUD screens are rendered by the compositor, which enables them to be displayed with a single SDK call to ovr_EndFrame. In the Oculus Debug Tool or OculusWorldDemo, you can toggle through the Performance HUD screens by pressing F11.

## Performance Summary

 The Performance Summary HUD displays the frame rate of the application and the unused hardware performance available. This HUD can be used by you or the user to tune an application's simulation and graphics fidelity. Because the user cannot disable V-Sync, it can be used to gauge performance instead of a frame rate counter. It is also useful for troubleshooting whether issues are related to the application or the hardware setup. 

The following image shows the Performance Summary HUD:

![](/images/documentationpcsdklatestconceptsdg-hud-0.png)

The following table describes each metric:

|            Metric            |                                                                                                                                                                                                                                                                                                                                              Description                                                                                                                                                                                                                                                                                                                                              |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| App Motion-to-Photon Latency |                                                                                                                                                                                                               Latency from when the last predicted tracking information was queried by the application using ovr_GetTrackingState() to when the middle scanline of the target frame is illuminated on the HMD display. This is the same information provided by the Latency Timing HUD.                                                                                                                                                                                                               |
|      Unused performance      | Designed to help the user verify that the PC is powerful enough to avoid dropping frames, this displays the percentage of available PC performance not used by the application and compositor. This is calculated using the CPU and GPU time tracked by the Application Render Timing HUD divided by the native frame time (inverse of refresh rate) of the HMD. **Note:** As GPU utilization approaches 100%, adaptive queue ahead will choose an earlier render start point. If this start point overlaps with the compositor process in the previous frame, the performance will appear spiky. If you start to lower utilization, the graph will show an initial drop before becoming more linear. |
|  Application Frames Dropped  |                                                                                                                                                                                                                    Increments each time the application fails to submit a new set of layers using ovr_EndFrame before the compositor is executed before each V-Sync (Vertical Synchronization). This is identical to App Missed Submit Count in the Application Render Timing HUD.                                                                                                                                                                                                                    |
|  Compositor Frames Dropped  |                                                                                                                                                                                                                                               Increments each time the compositor fails to present a new rendered frame at V-Sync (Vertical Synchronization). This is identical to Compositor Missed V-Sync Count in the Compositor Render Timing HUD.                                                                                                                                                                                                                                               |

## Latency Timing

The Latency Timing HUD displays the App to Mid - Photon, Timewarp to Photon - Start, and Timewarp to Photon - Start graphs. 

The following screenshot shows the Latency Timing HUD:

![](/images/documentationpcsdklatestconceptsdg-hud-1.png)

The following table describes each metric:

|           Metric           |                                                                                       Description                                                                                       |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| App Tracking to Mid-Photon |     Latency from when the app called ovr_GetTrackingState() to when the target frame eventually was shown (i.e.illuminated) on the HMD display - averaged mid - point illumination     |
|   Timewarp to Mid-Photon   | Latency from when the last predicted tracking info is fed to the GPU for timewarp execution to the point when the middle scanline of the target frame is illuminated on the HMD display |
|   Flip to Photon - Start   |                 Time difference from the point the back buffer is presented to the HMD to the point the target frame's first scanline is illuminated on the HMD display                 |

## Application Render Timing

The Application Render Timing HUD displays application-specific render timing information. 

The following screenshot shows the Application Render Timing HUD:

![](/images/documentationpcsdklatestconceptsdg-hud-2.png)

The following table describes each metric:

|         Metric         |                                                                                                                                                                                                                                                                                                                                               Description                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| App Missed Submit Count |                                                                                                                                                                                                                                                             Increments each time the application fails to submit a new set of layers using ovr_EndFrame before the compositor is executed and before each V-Sync (Vertical Synchronization).                                                                                                                                                                                                                                                             |
|     App Frame-rate     |                                                                                                                                                                                                                                                   The rate at which application rendering calls ovr_EndFrame. It will never exceed the native refresh rate of the HMD as the call to ovr_EndFrame throttles the application's CPU execution as needed.                                                                                                                                                                                                                                                   |
|   App Render GPU Time   | The total GPU time spent on rendering by the client application. This includes the work done by the application after returning from ovr_EndFrame, using the mirror texture if applicable. It can also include GPU command-buffer "bubbles" if the application's CPU thread doesn't push data to the GPU fast enough to keep it occupied. Similarly, if the app pushes the GPU close to full utilization, the work on next frame (N+1) might be preempted by the compositor's render work on the current frame (N). Because of how the application GPU timing query operates, this can lead to artificially inflated application GPU times as they will start to include the compositor GPU usage times. |
|   App Render CPU Time   |                                                                                                                                                      The time difference from when the application continued execution on CPU after ovr_EndFrame returned the subsequent call to ovr_EndFrame. This will show "N/A" if the latency tester is not functioning as expected (e.g., HMD display is sleeping due to prolonged inactivity). This includes the IPC call overhead to the compositor after ovr_EndFrame is called by the client application.                                                                                                                                                      |
|  App Queue Ahead Time  |                                                                                                                                       To improve CPU and GPU parallelism and increase the amount of time that the GPU has to process a frame, the SDK automatically applies queue ahead up to 1 frame. This value displays the amount of queue ahead time being applied (in milliseconds). For more information about adaptive queue ahead, see `Adaptive Queue Ahead`_.  .. _Adaptive Queue Ahead: /documentation/pcsdk/latest/concepts/dg-render/#dg-queue-ahead                                                                                                                                       |

## Compositor Render Timing

The Compositor Render Timing HUD displays render timing information for the Oculus Runtime Compositor. The Oculus Compositor applies distortion and TimeWarp to the layered eye textures provided by the VR application.

The following screenshot shows the Compositor Render Timing HUD:

![](/images/documentationpcsdklatestconceptsdg-hud-3.png)

The following table describes each metric:

|             Metric             |                                                                                                                                                     Description                                                                                                                                                     |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Compositor Missed V-Sync Count |                                                                                                   Increments each time the compositor fails to present a new rendered frame at V-Sync (Vertical Synchronization).                                                                                                   |
|     Compositor Frame-rate     | The rate of the final composition; this is independent of the client application rendering rate. Because the compositor is always locked to V-Sync, this value will never exceed the native HMD refresh rate. But, if the compositor fails to finish new frames on time, it can drop below the native refresh rate. |
|      Compositor GPU Time      |                       The amount of time the GPU spends executing the compositor renderer. This includes TimeWarp and distortion of all layers submitted by the application. The amount of active layers, their resolutions, and the requested sampling quality can all affect the GPU times.                       |
|     Comp Gpu-End to V-Sync     |                                                                         The amount of time between when the GPU completes the compositor rendering to the point in time when V-Sync is hit and that buffer starts scanning out on the HMD.                                                                         |

## Asynchronous SpaceWarp Stats

 The Asynchronous SpaceWarp (ASW) HUD displays activity and tracking statistics for ASW, which runs as part of the Oculus Runtime Compositor. ASW automatically activates when an application fails to meet the required native frame rate for the connected HMD. Once active, ASW forces the application to run at half the normal frame rate while extrapolating every other frame. This gives the application more time to complete its work.

The following screenshot shows the ASW HUD:

![](/images/documentationpcsdklatestconceptsdg-hud-4.png)

The following table describes each metric:

|          Metric          |                                                                                                                           Description                                                                                                                           |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        ASW Status        | Shows the availability and current status of ASW. "Not Available" can be due to the OS and/or GPU type used on the PC. "Available - Not Active" will mean the application is successfully maintaining the required native refresh rate, so ASW is not activated. |
|  ASW Active-Toggle Count  |                                                                                          Tracks the number of times ASW has been activated for the lifetime of the HMD.                                                                                          |
| ASW Presented-Frame Count |                            Tracks the number of frames extrapolated by ASW that were displayed. When ASW is active, since the app is forced to run at half-rate, expect this value to increase by 45 fps on a 90 Hz refresh rate HMD.                            |
|  ASW Failed-Frame Count  |           Tracks the number of extrapolated frames ASW needed to display, but failed to prepare in time. This can occur for different reasons, but might be caused by contention for OS resources or when the capabilities of the system are exceeded.           |

## Version Information

The Version Information HUD displays information about the HMD and the version of the SDK used to create the app. 

The following screenshot shows the Version Information HUD:

![](/images/documentationpcsdklatestconceptsdg-hud-5.png)

The following table describes each piece of information:

|          Name          |                                                      Description                                                      |
|------------------------|-----------------------------------------------------------------------------------------------------------------------|
|  OVR SDK Runtime Ver  | Version of the currently installed runtime. Every VR application that uses the OVR SDK since 0.5.0 uses this runtime. |
| OVR SDK Client DLL Ver |                               The SDK version that the client app was compiled against.                               |
|        HMD Type        |                                                   The type of HMD.                                                   |
|       HMD Serial       |                                             The serial number of the HMD.                                             |
|      HMD Firmware      |                                      The version of the installed HMD firmware.                                      |
|     Sensor Serial     |                                      The serial number of the positional sensor.                                      |
|    Sensor Firmware    |                               The version of the installed positional sensor firmware.                               |
