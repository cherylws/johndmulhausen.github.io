---
title: "Tutorial: Optimizing a Sample Application"
---
This section is a tutorial that provides a detailed hands-on guide to VR performance optimization.

This tutorial leads you through the process of optimizing a sample application by using:

* Oculus Debug Tool
* Oculus Performance HUD
* Lost Frame Capture Tool
* Event Tracing for Windows (ETW)
* ovrlog/ovrlog\_win10 and xperf
* Windows Performance Analyzer (WPA)
* GPUView
## Install Components

**1. Install the Oculus PC-SDK:**

[https://developer.oculus.com/documentation/pcsdk/latest/concepts/book-gsg/](/documentation/pcsdk/latest/concepts/book-gsg/)**2. Install Visual Studio 2015:**

<https://msdn.microsoft.com/en-us/library/mt613162.aspx>Note: The Oculus ORT demo applications which will be used in this tutorial and the Windows Driver Kit (WDK) are not yet compatible with Visual Studio 2017.**3. Install GPUView. **

GPUView is included in the Windows Performance Toolkit (WPT) included in the Windows 8.1 SDK, available at:

<https://developer.microsoft.com/en-us/windows/downloads/sdk-archive>**4. Install Event Tracing for Windows (ETW).**

ETW is included in the Windows Driver Kit 8.1: <https://developer.microsoft.com/en-us/windows/hardware/windows-driver-kit>.

**5. Install both of the following:**

* Windows SDK for Windows 10, version 1703 (or later)
* WDK for Windows 10, version 1703 (or later)
**6. Install the Windows Performance Analyzer (WPA).**

WPA is included in the Windows Assessment and Deployment Kit (Windows ADK):

<https://developer.microsoft.com/en-us/windows/hardware/windows-assessment-deployment-kit>

## Create an Application with a Performance Issue

We will work with the ORT Buffered Haptics sample project (which is located under the VS2013 folder at this writing):

 <SDK Folder>\Samples\OculusRoomTiny\_Advanced\ORT (Buffered Haptics)\Projects\Win\VS2013

**1. Run the Oculus application, and assure that your Rift is set up and working properly.**

**2. Open the following *solution* (not the project) in Visual Studio 2015:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-0.png)  
**3. Run this application in the Debugger (press F5), and view the scene in the Rift headset.**

As you turn your head, the scene behaves normally. In the Oculus Mirror, the eye displays remain centered and retain their usual shape. (In this example, a penetrated Oculus Guardian System boundary is shown.)

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-1.png)  
**4. Stop the Debugger.**

**5. Create a GPU performance issue.**

We will do this by editing the default texture shader routine that is used by this application, and adding a For loop that artificially overloads the GPU with an excessive amount of work, mimicking an expensive shader routine.

In this sample, the shader routine is contained in:

<Oculus SDK Folder>\Samples\OculusRoomTiny\_Advanced\Common\Win32\_DirectXAppUtil.h

Open this header file in Visual Studio, and add the following code to defaultPixelShaderSrc:

// Artificially overload the GPU with too much work, mimicking an expensive shader routine

" if (TexCol.a!=0) for (int i = 1; i < 10000; i++) { Color = Color * i * 2; Color = Color/i; Color = Color/2; } "

The location for this code is highlighted below:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-2.png)  
Note: You may wish to try different values for the loop variable. The 10,000 value shown above may be too extreme, depending upon the characteristics of your hardware. You might find that the tutorial works better with a value around 1500. Later in the tutorial, results will be shown with different values for that loop variable. This mimics different levels of shader complexity.**6. Run the application again.**

The result is a delay in eye rendering that is noticeable when you turn your head. In the headset, black vertical rectangular areas appear on the sides of the displays during head movement. In the Oculus Mirror, the eye displays appear flattened and off center as you turn your head.

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-3.png)  
In this example, we know the problem is due to the GPU issue which we purposefully created. However, in general, this symptom could be due to a number of issues, including CPU or GPU overload. We will begin to narrow down the problem using the Oculus Debug Tool.

## Using Oculus Debug Tool

**1. Run the Oculus Debug Tool: **

%PROGRAMFILES%\Oculus\Support\oculus-diagnostics\OculusDebugTool

**2. The Oculus Debug Tool window appears:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-4.png)  
Make sure:

* **Visible HUD** is set to **Performance**
* Under **Performance HUD**, the **Mode** is set to **Performance Summary**
**3. As a convenience, you may launch the application by selecting File > Launch App...**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-5.png)  
**4. Launch the application binary, which is located here:**

Oculus\_SDK>\Samples\OculusRoomTiny\_Advanced\ORT (Buffered Haptics)\Bin\Windows\Win32\Debug\VS2013\z.Buffered Haptics.exe

**5. In the headset, you should now see the Oculus Performance HUD:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-6.png)  
The HUD displays a performance summary showing four metrics:

* App Motion-to-Photon Latency — This indicates how long it takes from the time the application was given control until the time the frame completed. Most of this is the application rendering time. The value shown above is about 284 ms, which is an extremely high value, and clearly represents a problem. Based on this, the HUD provides a recommendation for how much the application should change the level of CPU utilization, in this case about a 15x reduction in utilization.
* Performance Headroom — This is the percentage of the rendering time that is still available to be used, before the application will begin to exhibit performance problems. (It is calculated as follows: 1 - (FrameRenderTime / FrameVSyncToNextVsync). For example, if the frame took 5 ms to render, then the headroom will be: 1 - (5/11.11) = 0.54 = 54%) In this example, the Performance Headroom is actually a large negative number, which indicates that the application is dropping frames.
* Application Frames Dropped — This is the number of frames that have been dropped by the application. In this example, a very large number of frames are being dropped, and therefore the line has turned red.
* Compositor Frames Dropped — This is the number of frames that have been dropped by the Oculus Compositor.
Clearly this application is spending too much time in the App Motion-to-Photon Latency category. The problem is actually highly exaggerated in this example. Spending 18 ms per frame would be a more typical example of a performance problem.

**6. Under Performance HUD, set Mode to App Render Timing:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-7.png)  
The content of the Oculus Performance HUD now displays application render timing data. Here you can easily compare the computational loads on the CPU and GPU:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-8.png)  
It is easy to see that the problem is with the GPU load. Again, this is a very exaggerated example, but it serves to illustrate the kind of insights you can gain by using these analysis tools.

## Using Lost Frame Capture Tool

Next, we will look at the frames that are dropped by this application, using the Lost Frame Capture tool.

**1. Click the Lost Frame Capture button in the Oculus Debug Tool:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-9.jpg)  
**2. The Lost Frame Capture tool appears:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-10.jpg)  
3. Make sure the application is displayed in the Oculus headset.

(The Lost Frame Capture tool is specific to Oculus, and knows to capture frames for the currently running Oculus application.)

**4. Click Record in the Lost Frame Capture tool.**

**5. Perform a few actions with the application, such as moving the headset in different directions. **

**6. Take off the headset, and click the **Stop** button in the Lost Frame Capture tool window.**

**7. Optionally, click **Save** to save the captured data to an Oculus Debug Archive (ODA) file. Name it appropriately, for example app\_1000.oda (if the loop variable in the shader routine was set to 1000).**

**You can now see the lost frames, and even step through them by moving the cursor up and down the list of frames:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-11.png)  
If you see that certain objects tend to come into view when frames are lost, you may need to optimize the rendering for those objects by reducing the number of polygons they contain, simplifying the shaders they use, simplifying their alpha blending routines, and so forth.

## Using ovrlog

We are now going to capture low-level events using Event Tracing for Windows (ETW). This will make it possible to analyze the behavior of the application at a much finer level of detail. We will do this by running the ovrlog utility (which provides a convenient way to start and stop ETW sessions). The events are captured into an Event Trace Log (.etl) file. We will analyze the event stream using two tools: Windows Performance Analyzer (WPA) and GPUView. You can think of WPA as providing a higher-level view of the event stream. Essentially WPA provides charts and graphs that *summarize* the performance-related characteristics of the event stream. GPUView, on the other hand, displays a highly-granular view of the events, themselves. So, with GPUView, you can drill down into the fine details of the interactions between the CPU and GPU workloads, and fine tune your application in order to optimize the timing and content of those workloads.

**1. Start a Windows CMD window *with admin privileges*.**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-12.png)  
During the rest of this tutorial, you will run the ovrlog\_win10 script or the ovrlog script – depending on whether you are running Windows 10 or an earlier version of Windows, respectively. This script calls the xperf utility which starts an ETW trace session that captures the events that occur while the VR application is running.

*You must run the **ovrlog\_win10** (or **ovrlog**) script with admin privileges*. Elevated privileges are required in order to perform kernel-level event tracing, which is necessary in order to capture all the events that are relevant to Oculus applications.

The first time you run the ovrlog\_win10 or ovrlog script, it performs the following actions:

* Locates the xperf utility
* Installs the Oculus manifest of event definitions that provide insight regarding Oculus application performance
* Runs the xperf utility in order to start an ETW session
* Begins capturing events
The second time you run the ovrlog\_win10 or ovrlog script, it performs the following actions:

* Halts the ETW session
* Uninstalls the Oculus manifest
* Aggregates results into a trace file (<xperf\_folder>\trace\merged.etl) that you can subsequently load into WPA or GPUView in order to analyze the flow of events that occurred
**2. Make sure the Xperf folder provides permissions to Authenticated Users for:**

* Full control
* Modify
The Xperf folder is located here:

%PROGRAMFILES%\Oculus\Support\oculus-diagnostics\ETW

So, the permissions for the Xperf folder should appear as follows:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-13.png)  
**3. Prepare to run through the following four steps cleanly, in reasonably quick succession.**

After you complete these four steps, if you see error messages in the console output (which appear in red), then try deleting the %PROGRAMFILES%\Oculus\Support\oculus-diagnostics\ETW\trace\ folder.

This is necessary so that the intermediate trace files don’t conflict when you run ovrlog\_win10 or ovrlog. After you delete this folder, run through the following four steps again.

**4. Run the Buffered Haptics application, and make sure it is currently being viewed in the headset. (You can run it directly within the Visual Studio debugger, if desired.)**

**5. Run the following script from a Command Prompt *with admin privileges*:**

%PROGRAMFILES%\Oculus\Support\oculus-diagnostics\ETW\overlog\_win10.cmd

or if you are using a Windows version prior to Windows 10:

%PROGRAMFILES%\Oculus\Support\oculus-diagnostics\ETW\overlog.cmd

**6. Perform any desired action within the VR application, while continuing to view it within the headset.**

**7. Run ovrlog\_win10 or ovrlog again to stop capturing events.**

Alternatively, you can run the ovrlog\_win10 or ovrlog command with the argument “stop” to stop tracing. Running the command again with no arguments from the same command prompt will stop tracing, and is the way most people typically use the command. However, this method is more failure-prone due to its reliance on environment variable settings.

The following file should be generated:

%PROGRAMFILES%\Oculus\Support\oculus-diagnostics\ETW\trace\merged.etl

## Using Windows Performance Analyzer (WPA)

**1. Start Windows Performance Analyzer (WPA), which is located here:**

C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit

**2. The WPA window appears:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-14.png)  
**3. Select **File > Open**, and open the merged.etl file that was produced above:**

%PROGRAMFILES%\Oculus\Support\oculus-diagnostics\ETW\trace\merged.etl

**4. You should see the following:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-15.png)  
**5. To check the CPU usage, double click on the small Computation window in the left panel. The full CPU usage graph is displayed in the work area:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-16.png)  
**6. Scroll down to see the z.Buffered.Haptics.exe process. You can see it is using a very small percentage of the CPU resources:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-17.png)  
It is clear from the above that the performance problem is not due to over utilization of the CPU resource in this application.

**7. To view the GPU usage, expand the Video tab:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-18.png)  
It is immediately clear by looking at the small Video window that the GPU is overloaded. (Actually, this example is rather extreme. A typical GPU usage issue would be less pronounced than what we are seeing here.)

**8. Remove the Computation graph from the work area, and double click on the Video window to display the GPU usage graph in the work area:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-19.png)  
In this example, the application was actively running at the time ovrlog\_win10 or ovrlog was run the first time. About half way through the event capture period, the headset was set down. At that point, the VR application was frozen, re-rendering a single frame. The Compositor is not called during that time period, so the GPU usage of OVRServer\_v64.exe goes to zero. Subsequently, after a few seconds, ovrlog\_win10 or ovrlog was run for the second time, and the event capture period ended.

**9. Select a small portion of the graph where both the application and the Compositor are executing, by dragging the mouse horizontally over the area. Then, use Ctrl-ScrollWheel (on the mouse) to zoom in so that you can see 100ths of a second.**

Note: This time scale is close to the frame rate, which is 90 frames per second.In the loop that we created within the shader routine, you can experiment by setting the loop variable so that it loops through 100, 500, 1000, or more cycles per pixel. The exact behavior that the application will exhibit -- given different values for the loop variable -- depends on the characteristics of the computer that you are using, and how heavily loaded it is during the event capture period.

When the loop variable is set to a relatively low value, and you zoom in to 100ths of a second, you should see a result similar to the following:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-20.png)  
Here you can see clearly see the frame cycles. The application (shown in green) consumes a fairly large amount of the GPU resource during each frame, and the Compositor (shown in light brown) consumes a smaller amount of the GPU resource for the same frame.

When the loop in the shader routine is run more times per pixel, the situation becomes tighter:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-21.png)  
Here there is very little time, if any, between the time the application finishes processing the frame, and the time that the Compositor outputs the frame. The Compositor is also using GPU processing *at the same time* as the application (as you can see by the fact that the two usage graphs are stacked). In this example, the shader routine is at or above the limit of complexity that is acceptable for a good user experience.

When the loop variable in the shader routine is increased even further, the situation becomes significantly worse:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-22.png)  
Here is it no longer possible to even see the frame cycles clearly.

Essentially, the GPU never finishes what it is doing. You can see that z.Buffered Haptics.exe is the process that is heavily utilizing the GPU, by highlighting that process, and viewing the corresponding activity in the graph. None of the other processes are using the GPU very much at all.

We will now look a little closer at the trace data within WPA.

**10. Zoom in further, and click on the icon to display the graph only:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-23.png)  
The table disappears and only the graph is visible::

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-24.png)  
**11. Drag down the bottom of the chart, in order to enlarge the view:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-25.png)  
In the Series box on the left, open the hierarchies under z.Buffered.Haptics.exe and OVRServer\_x64.exe, and select Render under z.Buffered.Haptics.exe:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-26.png)  
The space above the z.Buffered Haptics.exe process that is involved in rendering is filled in. As you can see, by far most of the time is being used for rendering within z.Buffered Haptics.exe. (This is, of course, the result we expect, given the loop the we inserted into the shader routine.)

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-27.png)  
WPA does not provide a detailed view of what the application is actually doing with the GPU, but we know there are two major phases to the GPU activity: a rendering phase and a BLT phase (a buffer copy at the end of the cycle). If you select BLT, you will find that very little time is spent on that phase.

**12. In the Series box on the left, select Render under OVRServer\_x64.exe. You can see that all of the GPU time used by the server is applied toward rendering:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-28.png)  
If you hold down the mouse and drag from one point in the cycle to the identical point in the next cycle, you can see that the duration is about 11.1 microseconds, which is a 90th of a second. This is the frame rate for the Rift. So, we can see in this example that frame rate is being met.

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-29.png)  
It is not possible to actually display the VSync events in WPA. But, you can usually identify the frame cycles, as in the example above.

## Using GPUView

In the following steps, we will view the ETW trace file(s) within GPUView. WPA doesn’t show the specific queuing of packets (indivisible collections of computational work) on each hardware resource. GPUView provides that level of analysis.

**1. Start GPUView:**

c:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\gpuview\GPUView.exe

**2. When GPUView launches, it first displays a File Manager dialog. Locate the merged.etl file that you wish to analyze and load it into GPUVIew:**

%PROGRAMFILES%\Oculus\Support\oculus-diagnostics\ETW\trace\merged.etl

The GPUView window appears and presents a high-level view of the ETW trace that was captured in the merged.etl file during the time that the application was running:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-30.png)  
In this example, the merged.etl file represents the behavior of the application when the loop variable was set to 1500. This behavior may vary, however, depending on the characteristics of your hardware.

**3. Many processes are captured in the trace, including kernel-level processes and processes related to other applications. These processes are not of interest in this tutorial. So, in order to simplify the display, collapse all processes with:**

**View > Process > Hide All Processes**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-31.png)  
**4. We only want to show the z.Buffered Haptics.exe process. So, right click on that process and select **Hide/Show Process**:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-32.png)  
At the top of the screen, the hardware resources are shown. At the bottom of the screen the corresponding activities in the application are shown:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-33.png)  
**5. Zoom in by selecting a relevant portion of the event flow, and typing Ctrl-Z:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-34.png)  
To zoom incrementally outward, type Z. To zoom all the way out to the original view, type Ctrl-H.

An expanded view is shown (below). In this example, the headset was stationary as the trace began, and was then moved actively around the scene. You can see that the frames are separated by space on the right hand side of the display. That may or may not indicate that frames are being dropped. This depends on the timing.

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-35.png)  
**6. To examine the timing more carefully, zoom in further by selecting a section and typing Ctrl-Z:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-36.png)  
**7. You can now see the packets in greater detail:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-37.png)  
Select a frame and look at the time scale shown at the top of the screen. The time scale increments are 10 ms. To hit the required frame rate of 90 frames per second, the frame cycle must be completed within about 11.1 ms. You can see that the frame is taking longer than that, and in fact the subsequent frame is delayed, as indicated by the blank space between the frames. So, in this example, every other frame is being dropped on the right-hand side of the timeline:

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-38.png)  
At this zoom level, you can see stacks of colored rectangles, which are called packets. A packet is the minimum indivisible unit of work that the application schedules to run on the CPU or GPU. A *fence* is a synchronization primitive that assures that one operation completes before the next operation begins.

The fences appear as the pink boxes above.

The dark blue packets are collections of graphics commands that resolve to GPU work.

**8. Click on a packet. You can now see the exact life cycle for that packet, as well as detailed information about it:**

![](/images/documentation-pcsdk-latest-concepts-dg-performance-tutorial-39.png)  
In GPUView, the packets are arranged in stacks, with time progressing along the horizontal axis. The packet at the bottom is the item that is currently being worked on. The further up the stack you go, the further back in line the packet is. The height of the stack shrinks as work is finished, and grows as more work is added to the queue. By clicking on a packet, you can see its life cycle, as well as the dependencies between packets.

In WPA, we could have zoomed in and determined the exact frame index for a frame that we are interested in examining. We could then use that frame index to locate the same frame within GPUView. This is helpful because GPUView does not provide a contextual top-down view.

In the above example, the application called the DirectX driver, and requested that it render a primitive. That driver call created GPU work. So, the 3D pipe is processing that work in the highlighted selection.

The typical flow is: initialize, submit CPU work, submit related graphics work, install the fences that assure work is processed in the correct order, wait until the CPU work (and therefore the fence) finishes, then move on to the next frame.

The same GPU packet is highlighted across time, above. But at a later time, it is at the front of the queue (at the bottom), and is being processed. The width of the packet indicates how long it took to process it, in terms of the time scale shown along the top.

You can also obtain traces for the packets. If you see that your application is using the system heavily, and you don’t know why, you can see the exact sequence of calls that caused the problem.

It is very useful to be able to view the VSyncs within GPUView. But, the menu item **Options > Toggle VSync** does *not* display Oculus VSyncs. This menu item displays the VSyncs for the Windows monitor.

ovrlog\_win10 and ovrlog generate traces that include NVIDIA or AMD vsync events, depending on the hardware that your system is using. In order to display vsyncs within GPUView, you must run the following batch file before generating the ETW trace:

%PROGRAMFILES%\Oculus\Support\oculus-diagnostics\ETW\IHVETW\setup.bat

 Once the manifests are installed, the event that captures VSyncs for NVIDIA is:

NVIDIA-VR-DirectMode VsyncDPC

 There are similar events for AMD.

 Open the trace in GPUView, click Tools > Event Viewer, and then enable NVIDIA-VR-DirectMode, and vertical red lines should appear in your trace diagram.
