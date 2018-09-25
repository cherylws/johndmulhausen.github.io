---
title: SDK Performance Statistics
---
The SDK performance statistics provide information about application and compositor performance on the system.

Stats are populated after each call to ovr\_EndFrame. To get performance stats, use ovr\_GetPerfStats().

To reset the stats, use ovr\_ResetPerfStats.

Note: If your performance tool runs separately from your application, make sure to read the VisibleProcessId in case your application loses focus.The following table describes performance statistics:

StatisticsStatisticsDescriptionovrPerfStatsPerCompositorFrameThe per-compositor frame statistics in the following tables.AnyFrameStatsDroppedIf the app calls ovr\_EndFrame at a rate less than 18 fps, then when calling ovr\_GetPerfStats, expect AnyFrameStatsDropped to become ovrTrue while FrameStatsCount is equal to ovrMaxProvidedFrameStats.AdaptiveGpuPerformanceScaleAn edge-filtered value that you can use to adjust the graphics quality of the application to keep the GPU utilization in check. The value is calculated as: (desired\_GPU\_utilization / current\_GPU\_utilization). 

When this value is 1.0, the GPU is doing the right amount of work for the app. Lower values mean the application needs to reduce the GPU utilization. 

Note: If the app directly drives render-target resolution using this value, make sure to take the square-root of the value before scaling the resolution with it. Changing the render target resolution is only one of the many things your application can do increase or decrease the amount of GPU utilization. Since AdaptiveGpuPerformanceScale is edge-filtered and does not change rapidly (i.e., it reports non-1.0 values once every couple of seconds), your application can make the necessary adjustments and continue watching the value to see if it has been satisfied.

AswIsAvailableReturns true if ASW is available for this system, based on the user's GPU, operating system, and debug override settings.The following table describes statistics specific to your application's performance:

Application StatisticsStatisticDescriptionAppFrameIndexIndex that increments with each ovr\_EndFrame call.AppDroppedFrameCountIncrements each time the application fails to submit a new set of layers using ovr\_EndFrame before the compositor is executed before each V-Sync (Vertical Synchronization).AppMotionToPhotonLatencyLatency from when the last predicted tracking information was queried by the application using ovr\_GetTrackingState() to when the middle scanline of the target frame is illuminated on the HMD display. This is the same information provided by the Latency Timing HUD.AppQueueAheadTimeTo improve CPU and GPU parallelism and increase the amount of time that the GPU has to process a frame, the SDK automatically applies queue ahead up to 1 frame. This value displays the amount of queue ahead time being applied (in milliseconds). For more information about adaptive queue ahead, see [Adaptive Queue Ahead](/documentation/pcsdk/latest/concepts/dg-render/#dg-queue-ahead).AppCpuElapsedTimeThe time difference from when the application continued execution on CPU after ovr\_EndFrame returned the subsequent call to ovr\_EndFrame. This will show "N/A" if the latency tester is not functioning as expected (e.g., HMD display is sleeping due to prolonged inactivity). This includes the IPC call overhead to the compositor after ovr\_EndFrame is called by the client application.AppGpuElapsedTimeThe total GPU time spent on rendering by the client application. This includes the work done by the application after returning from ovr\_EndFrame, using the mirror texture if applicable. 

It can also includes GPU command-buffer "bubbles" if the application's CPU thread doesn't push data to the GPU fast enough to keep it occupied. Similarly, if the app pushes the GPU close to full-utilization, the work on next frame (N+1) might be preempted by the compositor's render work on the current frame (N). Because of how the application GPU timing query operates, this can lead to artificially inflated application GPU times as they will start to include the compositor GPU usage times. 

The compositor operates asynchronously and will increment for each vsync, regardless of whether the application calls ovr\_EndFrame. 

The following table describes compositor statistics:

Compositor StatisticsStatisticDescriptionCompositorFrameIndexIndex that increments each time the SDK compositor completes a distortion/TimeWarp pass. CompositorDroppedFrameCountIncrements each time the compositor fails to present a new rendered frame at V-Sync (Vertical Synchronization). CompositorLatencySpecifies the TimeWarp latency, which corrects app latency and dropped frames.CompositorCpuElapsedTimeThe amount of time in seconds spent on the GPU by the SDK compositor. Any time spent on the compositor takes available GPU time away from the application. CompositorGpuElapsedTimeThe amount of time the GPU spends executing the compositor renderer. This includes TimeWarp and distortion of all layers submitted by the application. The amount of active layers, their resolutions, and the requested sampling quality can all affect the GPU times.CompositorCpuStartToGpuEndElapsedTimeThe amount of time from when the CPU kicks off the compositor to when the compositor completes distortion and TimeWarp on the GPU. If the time is not available, it returns -1.0f. CompositorGpuEndToVsyncElapsedTimeThe amount of time between when the GPU completes the compositor rendering to the point in time when V-Sync is hit and that buffer starts scanning out on the HMD. The Asynchronous SpaceWarp (ASW) HUD displays activity and tracking statistics for ASW, which runs as part of the Oculus Runtime Compositor. ASW automatically activates when an application fails to meet the required native frame rate for the connected HMD. Once active, ASW forces the application to run at half the normal frame rate while extrapolating every other frame. This gives the application more time to complete its work.

The following table describes Asynchronous SpaceWarp (ASW) statistics:

ASW StatisticsStatisticDescriptionAswIsActiveShows the availability and current status of ASW. "Not Available" can be due to the OS and/or GPU type used on the PC. "Available - Not Active" will mean the application is successfully maintaining the required native refresh rate, so ASW is not activated.AswActivatedToggleCountTracks the number of times ASW has been activated for the lifetime of the HMD.AswPresentedFrameCountTracks the number of frames extrapolated by ASW that were displayed. When ASW is active, since the app is forced to run at half-rate, expect this value to increase by 45 fps on a 90 Hz refresh rate HMD.AswFailedFrameCountTracks the number of extrapolated frames ASW needed to display, but failed to prepare in time. This can occur for different reasons, but might be caused by contention for OS resources or when the capabilities of the system are exceeded.