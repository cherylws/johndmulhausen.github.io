---
title: Workflows: The process flows you should follow
---
This section covers the workflows that you should use when tracking down performance problems.

## Overview

This section provides an overview of the workflows that you should follow when isolating and analyzing VR performance issues. Also see these slides from the 2015 Unity Unite conference: <https://imgur.com/a/SVs3I>.

Follow these workflows:

*Begin*

1. Choose a workload, such as a scene with judder in your application. 
2. View the scene while displaying the Oculus Performance HUD, or capture the scene in the Lost Frames Capture utility. Both of these tools are available within the Oculus Debug Tool. You can also use NVIDIA Frame Capture Analysis Tool for VR Games (FCAT VR).
3. IF dropped\_frame\_rate > 1 frame per 5 seconds THEN 
	* IF render\_time > 8 ms THEN *Analyze Rendering* ELSE *Analyze Call Hierarchy*.
	
*Analyze Rendering*

1. IF rendering time is excessive THEN 
	* Check if batches > 1000 
	* Check if triangles/vertices > 1,000,000 
	* Check if SetPass calls > 1000 
	
2. IF the hierarchy view uses excessive time THEN
	* Look for a single object that takes 8 ms or more to render 
	* Check to see if the CPU is stalled waiting on the GPU to complete tasks
	* Check if mesh rendering is too complex 
	* Check to see if shadows are too complex 
	* Check to see if VSync points arrive before the frames are fully rendered
	* Check the timeline view to see if there are scheduling bubbles
	
*Analyze Call Hierarchy*

1. Capture an ETW trace file, using ovrlog or ovrlog\_win10. 
2. Load the trace file into Windows Performance Analyzer (WPA).
3. Expand to see which objects/calls take the most time. 
4. IF there are garbage collection spikes THEN donâ€™t allocate memory for each frame. Note: If your scripts allocate and free memory during each frame cycle, this may result in fragmentation that eventually forces the garbage collection process to defragment the heap.
5. Once you have identified the objects/calls that take the most time, analyze the corresponding source code and optimize it. 
*Analyze Queuing and System-Level Contention*

1. Capture the Event Tracing for Windows (ETW) output by running ovrlog or ovrlog\_win10
2. Analyze the resulting merged.etl file in GPUVIew. 
3. Highlight processes within your application.
4. Show the VSyncs. 
5. Zoom in on the problem area. 
6. Examine the GPU packets, command packets, and fences.
7. Analyze the dependencies between these packets and the processes they are implementing. You can bring up the Event Viewer, which displays detailed information about each packet.
Note: GPU packets represent indivisible units of GPU work. Command packets represent indivisible packets of CPU work. And fences represent barriers that cannot be passed until the previous work is completed.The tutorial at the end of this guide provides detailed guidance for using WPA and GPUView.

