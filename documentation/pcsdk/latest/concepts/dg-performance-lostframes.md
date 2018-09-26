---
title: Lost Frame Capture Tool
---

The Lost Frame Capture tool collects information about dropped frames while your VR application is running. You can then replay the dropped frames while viewing statistical data, in order to help track down performance problems within your application.

## Overview

When you submit a VR application to the Oculus Store, it is examined by Oculus engineers to ensure that it adheres to the Rift Virtual Reality Checklist (VRC), which specifies a number of requirements that your application must satisfy, including performance targets. For information about the VRC, see: [https://developer.oculus.com/distribute/latest/concepts/publish-rift-app-submission/](/distribute/latest/concepts/publish-rift-app-submission/). If your application fails due to performance issues, it is generally because it failed to maintain the required frame rate of 90 frames per second at some point during its execution. (Large clusters of dropped frames are not allowed outside of scene transitions. Applications are allowed to drop frames while loading code into memory, or transitioning from scene to scene.) 

If your application is rejected for performance reasons, you will need to address the those issues, and re-submit the application. However, in the past it has been difficult for developers to pinpoint the exact problem areas within their application. Oculus will soon begin providing an Oculus Debug Archive (ODA file) to developers, whenever their application is rejected because of performance issues. You can use the Lost Frame Capture tool to load the ODA file, and then analyze the performance of your application. With this tool, you can see exactly where the performance problems occurred, and even view the lost frames that are causing performance issues.

You can also use the Lost Frame Capture tool to analyze your applications before you submit them to Oculus. This helps you to discover and address any performance issues prior to submission.

The rest of this document describes how to use the Lost Frame Capture tool.

## Launching the Lost Frame Capture Tool

1. Run the Oculus Debug Tool, located here: C:\Program Files\Oculus\Support\oculus-diagnostics\OculusDebugTool.exe
2. The Oculus Debug Tool appears. Click the Lost Frame Capture button: ![](/images/documentationpcsdklatestconceptsdg-performance-lostframes-0.png)


3. The Lost Frame Capture tool appears: ![](/images/documentationpcsdklatestconceptsdg-performance-lostframes-1.png)


4. The following actions are available when appropriate:* Click Record to begin capturing lost frames from the currently running Oculus session. * Click Save to save the currently captured content to an Oculus Debug Archive (ODA) file. * Click Load to load an existing Oculus Debug Archive (ODA) file. * Click Summary to view a statistical summary based on the currently loaded ODA file or the current capture session (whichever applies). 




## Analyzing the Lost Frame Capture Output

* An ODA file that you previously created yourself.
* An ODA file that you received from Oculus, if your submitted application did not pass the VRC.


You can also analyze the Lost Frame Capture output that you captured during the currently running session, without necessarily saving that output to an ODA file.

Before you submit your application to Oculus, it is a good idea to run it, and collect the Lost Frame Capture output. While running your application, you should go through all the scenarios that end users may encounter. Then, analyze the resulting output to determine if there were any large clusters of dropped frames outside of scene transitions. If you discover any performance problems, fix them before submitting your application to Oculus. 

To load and analyze an ODA file, follow these steps:

1. Launch the Lost Frame Capture tool (as described above).
2. Click the Load button: ![](/images/documentationpcsdklatestconceptsdg-performance-lostframes-2.png)


3. Select the .oda file to load.
4. The Lost Frame Capture tool populates the main window: ![](/images/documentationpcsdklatestconceptsdg-performance-lostframes-3.png)

This window lists the frames that were lost during the time that the ODA content was being captured. The frame indexes are listed in the first column. You will notice that the lost frames are sometimes grouped into folder-like structures. This is intended to help you recognize when multiple frames are lost in close proximity to each other. Whenever a sequence of frames is lost, where there is never a gap of more than one second between any two lost frames, those lost frames are grouped together into a folder structureâ€”called a *lost frame cluster*.

You can select a frame at the top level of the list, or a frame from within a lost frame cluster. The rendered left and right eye views for the frame are displayed on the right. A graph appears below, which indicates the frame rate for a set of lost frames, where 90 frames per second is the top-most value in the graph. When the graph dips down, it indicates that frames are being generated at a lower frame rate (which, if it is sustained, is not acceptable since it results in a poor user experience).

In the example above, the currently selected frame was generated at a rate of 56.3 frames per second, as indicated by the horizontal line. You can step through the lost frames using the arrow keys, and see how the line moves over time. The point at which the horizontal line intersects the vertical dashed line in the grid, and which also intersects the graph, indicates where the currently selected frame is in the timeline.

This graph view helps you to visualize how the frame rate for the currently selected frame compares with other nearby frames (if you are stepping through frames within a cluster). For example, you can compare the current level of the horizontal line to the overall graph. This can make it much easier to spot where a problem is beginning, and where it is at its worst. In many cases, you should be able to get an intuitive grasp of what the problem is by simply looking at the content of the frames. For example, an object may come into view when the frame rate drops. Perhaps the shader that is used by that object is too complex, or some other aspect of the rendering process for that object is using up too much of the CPU or GPU resources.




## Columns in the Display

The columns displayed by the Lost Frame Capture tool are listed in the following table. You can click on any column header in order to sort the rows by that column. If you sort by a column other than Lost Frame Index, the clusters are sorted as a group at the top of the list, and the non-clustered individual frames are sorted as a group at the bottom of the list. 

The columns include:

|   Lost Frame Index   |                                                                                                                                                                                                                                                                                                                                                    The frame index for the lost frame in this row.                                                                                                                                                                                                                                                                                                                                                    |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   Queue Ahead (ms)   |                                                                                                                                                                               The queue ahead time in milliseconds for the frame. (For information about queue ahead time, see https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-render/#dg-queue-ahead_.)  .. _https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-render/#dg-queue-ahead: https://developer.oculus.com/documentation/pcsdk/latest/concepts/dg-render/#dg-queue-ahead                                                                                                                                                                               |
|    App Time (ms)    |                                                                                                                                                                                                                                                                                                                                 The amount of time that the application spent processing the frame (in milliseconds).                                                                                                                                                                                                                                                                                                                                 |
| Compositor Time (ms) |                                                                                                                                                                                                                                                                                                                              The amount of time that the Oculus compositor spent processing the frame (in milliseconds).                                                                                                                                                                                                                                                                                                                              |
|     Frame Count     |                    The number of frame cycles represented by the row. For a single frame, this number indicates the number of frame cycles that this frame required. Often this number is 2, since the frame was lost, and was not able to be rendered within a single frame cycle. For lost frame clusters, this number can be much higher, since it represents the number of frame cycles required by all of the frames within the cluster. The Frame Count column can be very helpful, since you can see by simply scanning down the column where a large number of frames were all dropped in close proximity to each other. When this happens, it is likely that you have a performance issue that occurred at that location.                    |
|   Frame Rate (hz)   | The frame rate for the currently selected row. For a single frame, this is the frame rate that would result if frames were processed continually at the rate of the currently selected frame, expressed in frames per second (hz).For a cluster, this is the frame rate that would result if the *average frame rate* of the frames within the cluster proceeded continuously, expressed in frames per second (hz). Note that this is the average frame rate for the *lost frames* within the time period represented by the cluster. It is entirely possible (and would, in fact, usually be that case) that many other frames were processed within that time frame, but they were not lost frames and are not shown in the Lost Frame Capture tool. |
|        V-Sinc        |                                                                                                                                                                                                                          The vsinc (vertical synchronization) for the row. When a single frame is selected, this is the location in the timeline where the vsync occurred for that frame (in seconds from the start of the capture period). When a cluster is selected, this is the vsync for the first frame in the cluster.                                                                                                                                                                                                                          |
|    Duration (ms)    |                                                                   The length of time (in milliseconds) that frames were persistently dropped, for the currently selected row.When a single frame is selected, this is the length of time that was spent processing that frame.When a cluster is selected:* The period begins when the system starts processing the first dropped frame in the cluster. * The period ends when the system finishes processing the last dropped frame in the cluster.  * The Duration value includes the processing time for all frames that were processed between the start time and the end time, including dropped frames and non-dropped frames.                                                                   |

## Recording an ODA File

To capture any lost frames produced by your application, and then save that content as an ODA file:

1. Click Record.
2. Perform whatever actions are of interest in the VR application.
3. Take off headset, and stop the recording. (A Stop button is available in the Lost Frame Capture tool window.)
4.  Click Save to save the captured data to an ODA file.


## View Performance Summary

To view a set of overall statistics for the currently open ODA file, or the current recording session, click the Summary button. The Performance Summary popup window is displayed:

![](/images/documentationpcsdklatestconceptsdg-performance-lostframes-4.png)
