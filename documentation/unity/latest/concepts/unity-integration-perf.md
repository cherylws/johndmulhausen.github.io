---
title: Debugging and Performance Analysis in Unity
---

In this guide, we’ll review baseline targets, recommendations, tools, resources, and common workflows for performance analysis and bug squashing for Unity VR applications.

## General Tips

VR application debugging is a matter of getting insight into how the application is structured and executed, gathering data to evaluate actual performance, evaluating it against expectation, then methodically isolating and eliminating problems.

When analyzing or debugging, it is crucial to proceed in a controlled way so that you know specifically what change results in a different outcome. Focus on bottlenecks first. Only compare apples to apples, and change one thing at a time (e.g., resolution, hardware, quality, configuration). 

Always be sure to profile, as systems are full of surprises. We recommend starting with simple code, and optimizing as you go - don’t try to optimize too early.

We recommend creating a non-VR version of your camera rig so you can swap between VR and non-VR perspectives. This allows you to spot check your scenes, and it may be useful if you want to do profiling with third-party tools (e.g., Adreno Profiler).

It can be useful to disable **Multithreaded Rendering** in **Player Settings** during performance debugging. This will slow down the renderer, but also give you a clearer view of where your frame time is going. Be sure to turn it back on when you’re done!

## Performance Targets

Before debugging performance problems, establish clear targets to use as a baseline for calibrating your performance.

These targets can give you a sense of where to aim, and what to look at if you’re not making frame rate or are having performance problems.

Below you will find some general guidelines for establishing your baselines, given as approximate ranges unless otherwise noted.

### Mobile

* 60 FPS (required by Oculus)
* 50-100 draw calls per frame
* 50,000-100,000 triangles or vertices per frame


### PC

* 90 FPS (required by Oculus)
* 500-1,000 draw calls per frame
* 1-2 million triangles or vertices per frame


For more information, see:

* [PC SDK Developer Guide](https://developer.oculus.com/documentation/pcsdk/latest/concepts/book-dg/)
* [Mobile VR Application Development](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/book-intro/)


## Unity Profiling Tools

This section details tools provided by Unity to help you diagnose application problems and bottlenecks.

### Unity Profiler

Unity comes with a built-in profiler (see Unity’s [Profiler manual](http://docs.unity3d.com/Manual/Profiler.html)). The Unity Profiler provides per-frame performance metrics, which can be used to help identify bottlenecks.

**PC Setup**

To use Unity Profiler with a Rift application, select **Development Build** and **Autoconnect Profiler** in **Build Settings** and build your application. When you launch your application, the Profiler will automatically open.

**Mobile Setup**

You may profile your application as it is running on your Android device using adb or Wi-Fi. For steps on how to set up remote profiling for your device, please refer to the Android section of the following Unity documentation: [https://docs.unity3d.com/Documentation/Manual/Profiler.html](https://docs.unity3d.com/Documentation/Manual/Profiler.html).

![](/images/documentationunitylatestconceptsunity-integration-perf-0.jpg)

The Unity Profiler displays CPU utilization for the following categories: Rendering, Scripts, Physics, GarbageCollector, and Vsync. It also provides detailed information regarding Rendering Statistics, Memory Usage (including a breakdown of per-object type memory usage), Audio and Physics Simulation statistics.

GPU Usage data for Android is not available at this time.

The Unity profiler only displays performance metrics for your application. If your app isn’t performing as expected, you may need to gather information on what the entire system is doing.

### Show Rendering Statistics

Unity provides an option to display real-time rendering statistics, such as FPS, Draw Calls, Tri and Vert Counts, VRAM usage. While in the Game View, pressing the Stats button above the Game View will display an overlay showing realtime render statistics. Viewing stats in the Editor can help analyze and improve batching for your scene by indicating how many draw calls are being issued and how many are being saved by batching (the OverDraw render mode is helpful for this as well).

![](/images/documentationunitylatestconceptsunity-integration-perf-1.png)

### Show GPU Overdraw

Unity provides a specific render mode for viewing overdraw in a scene. From the Scene View Control Bar, select OverDraw in the drop-down Render Mode selection box. 

In this mode, translucent colors will accumulate providing an overdraw “heat map” where more saturated colors represent areas with the most overdraw.

![](/images/documentationunitylatestconceptsunity-integration-perf-2.jpg)

### Unity Built-in Profiler

Unity Built-in Profiler (not to be confused with Unity Profiler) provides frame rate statistics through logcat, including the number of draw calls, min/max frametime, number of tris and verts, et cetera.

To use this profiler, connect to your device over Wi-Fi using ADB over TCPIP as described in the [Wireless usage](https://developer.android.com/tools/help/adb.html#wireless) section of Android’s adb documentation. Then run `adb logcat` while the device is docked in the headset. 

See [Unity’s Measuring Performance with the Built-in Profiler](http://docs.unity3d.com/Manual/iphone-InternalProfiler.html) for more information. For more on using adb and logcat, see [Android Debugging](/documentation/mobilesdk/latest/concepts/book-anddebug/) in the Mobile SDK documentation.

## Oculus Performance Heads-Up Display (HUD) for the Rift



### Oculus Performance Head-Up Display (HUD)

The Oculus Performance Head-Up Display (HUD) is an important, easy-to-use tool for viewing timings for render, latency, and performance headroom in real-time as you run an application in the Oculus Rift. The HUD is easily accessible through the Oculus Debug Tool provided with the PC SDK. For more details, see the [Performance Head-Up Display](/documentation/pcsdk/latest/concepts/dg-hud/) and [Oculus Debug Tool](/documentation/pcsdk/latest/concepts/dg-debug-tool/) sections of the Oculus Rift Developers Guide.

### Compositor Mirror

The compositor mirror is an experimental tool for viewing exactly what appears in the headset, with Asynchronous TimeWarp and distortion applied.

The compositor mirror is useful for development and troubleshooting without having to wear the headset. Everything that appears in the headset will appear, including Oculus Home, Guardian boundaries, in-game notifications, and transition fades. The compositor mirror is compatible with any game or experience, regardless of whether it was developed using the native PC SDK or a game engine.

For more details, see the [Compositor Mirror](/documentation/pcsdk/latest/concepts/dg-compositor-mirror/) section of the PC SDK Guide.

## Oculus Remote Monitor for Gear VR



Oculus Remote Monitor is a client for Windows and Mac OS X that connects to VR applications running on remote devices to capture, store, and display the streamed-in data. It provides visibility into Android VR and GLES activity, and includes low-res rendered image snapshots for a visual reference to its timeline-based display. Remote Monitor is available for download from our Downloads page.

![](/images/documentationunitylatestconceptsunity-integration-perf-3.png)

The Remote Monitor client uses VrCapture, a low-overhead remote monitoring library. VrCapture is designed to help debug behavior and performance issues in mobile VR applications. VrCapture is included automatically in any project built with Unity 5 or later, or compiled with the Legacy Integration.

For more information on setup, configuration, and usage, please see [VrCapture and Oculus Remote Monitor](/documentation/mobilesdk/latest/concepts/mobile-remote-monitor/#mobile-remote-monitor). 

## Additional Third-Party Tools



**ETW + GPUView**

[Event Tracing for Windows](https://msdn.microsoft.com/en-us/library/windows/desktop/bb968803%28v=vs.85%29.aspx?f=255&amp;MSPPError=-2147217396) (ETW) is a trace utility provided by Windows for performance analysis. [GPUView](https://msdn.microsoft.com/en-us/library/windows/desktop/jj585574%28v=vs.85%29.aspx?f=255&amp;MSPPError=-2147217396) view provides a window into both GPU and CPU performance with DirectX applications. It is precise, has low overhead, and covers the whole Windows system. Custom event manifests.

ETW profiles the whole system, not just the GPU. For a sample debug workflow using ETW to investigate queuing and system-level contention, see Example Workflow: PC below.

**Systrace**

Reports complete Android system utilization. Available here: [http://developer.android.com/tools/help/systrace.html](https://developer.android.com/tools/help/systrace.html)

**NVIDIA NSight**

NSight is a CPU/GPU debug tool for NVIDIA users, available in a [Visual Studio version](https://developer.nvidia.com/nvidia-nsight-visual-studio-edition) and an [Eclipse version](https://developer.nvidia.com/nsight-eclipse-edition).

**Mac OpenGL Monitor**

An OpenGL debugging and optimizing tool for OS X. Available here: [https://developer.apple.com/library/mac/technotes/tn2178/_index.html#//apple_ref/doc/uid/DTS40007990](https://developer.apple.com/library/mac/technotes/tn2178/_index.html#//apple_ref/doc/uid/DTS40007990)

**APITrace**

[https://apitrace.github.io/](https://apitrace.github.io/)

## Analyzing Slowdown

In this guide, we take a look at three of the areas commonly involved with slow application performance: pixel fill, draw call overhead, and slow script execution. 

### Pixel Fill

Pixel fill is a function of overdraw and of fragment shader complexity. Unity shaders are often implemented as multiple passes (draw diffuse part, draw specular part, and so forth). This can cause the same pixel to be touched multiple times. Transparency does this as well. Your goal is to touch almost all pixels on the screen only one time per frame.

Unity's Frame Debugger (described in [Unity Profiling Tools](/documentation/unity/latest/concepts/unity-perf/#unity-perf-profiling-tools)) is very useful for getting a sense of how your scene is drawn. Watch out for large sections of the screen that are drawn and then covered, or for objects that are drawn multiple times (e.g., because they are touched by multiple lights).

Z-testing is faster than drawing a pixel. Unity does culling and opaque sorting via bounding box. Therefore, large background objects (like your Skybox or ground plane) may end up being drawn first (because the bounding box is large) and filling a lot of pixels that will not be visible. If you see this happen, you can move those objects to the end of the queue manually. See [Material.renderQueue](http://docs.unity3d.com/ScriptReference/Material-renderQueue.html) in Unity's Scripting API Reference for more information.

Frame Debugger will clearly show you shadows, offscreen render targets, et cetera.

### Draw Calls

Modern PC hardware can push a lot of draw calls at 90 fps, but the overhead of each call is still high enough that you should try to reduce them. On mobile, draw call optimization is your primary scene optimization.

Draw call optimization is usually about batching multiple meshes together into a single VBO with the same material. This is key in Unity because the state change related to selecting a new VBO is relatively slow. If you select a single VBO and then draw different meshes out of it with multiple draw calls, only the first draw call is slow.

Unity batches well when given properly formatted source data. Generally:

* Batching is only possible for objects that share the same material pointer.
* Batching doesn't work on objects that have multiple materials.
* Implicit state changes (e.g. lightmap index) can cause batching to end early.


Here is a quick checklist for maximizing batching:

* Use as few textures in the scene as possible. Fewer textures require fewer unique materials, so they are easier to batch. Use texture atlases.
* Bake lightmaps at the largest atlas size possible. Fewer lightmaps require fewer material state changes. Gear VR can push 4096 lightmaps without too much trouble, but watch your memory footprint.
* Be careful not to accidentally instance materials. Note that accessing Renderer.material automatically creates an instance (!) and opts that object of batching. Use Renderer.sharedMaterial instead whenever possible.
* Watch out for multi-pass shaders. Add noforwardadd to your shaders whenever you can to prevent more than one directional from applying. Multiple directionals generally break batching.
* Mark all mesh that never moves as Static in the editor. Note that this will cause the mesh to be combined into a mega mesh at build time, which can increase load time and app size on disk, though usually not in a material way. You can also create a static batch at runtime (e.g., after generating a procedural level out of static parts) using StaticBatchingUtility.
* Watch your static and dynamic batch count vs the total draw call count using the Profiler, internal profiler log, or stats gizmo.


### Script Performance

Unity's C# implementation is fast, and slowdown from script is usually the result of a mistake and/or an inadvertent block on slow external operations such as memory allocation. The Unity Profiler can help you find and fix these scripts.

Try to avoid foreach, lamda, and LINQ structures as these allocate memory needlessly at runtime. Use a for loop instead. Also, be wary of loops that concatenate strings.

Game Object creation and destruction takes time. If you have a lot of objects to create and destroy (say, several hundred in a frame), we recommend pooling them.

Don't move colliders unless they have a rigidbody on them. Creating a rigidbody and setting `isKinematic` will stop physics from doing anything but will make that collider cheap to move. This is because Unity maintains two collider structures, a static tree and a dynamic tree, and the static tree has to be completely rebuilt every time any static object moves.

Note that coroutines execute in the main thread, and you can have multiple instances of the same coroutine running on the same script. 

We recommend targeting around 1-2 ms maximum for all Mono execution time.

## PC Debug Workflow

In this guide, we’ll use the example of a hypothetical stuttering app scene and walk through basic steps debugging steps. 

### Where to Start

Begin by running the scene with the [Oculus Performance HUD](/documentation/unity/latest/concepts/unity-perf/#unity-perf-hud).

If the scene drops more than one frame every five seconds, check the render time. If it’s more than 8 ms, have a look at GPU utilization. Otherwise, look at optimizing CPU utilization. If observed latency is greater than 30 ms, have a look at queuing.

### CPU Profiling (Unity Profiler)

Look for the tallest bars in the CPU Usage graph in the Unity Profiler. Sort hierarchy by Total CPU time, and expand to see which objects and calls take the most time.

If you find garbage collection spikes, don’t allocate memory each frame.

### GPU Profiling (Unity Profiler)

Are your rendering stats too high? (For reference baselines, see [Performance Targets](/documentation/unity/latest/concepts/unity-perf/#unity-perf-targets).

Check for hogs in your hierarchy or timeline view, such as any single object that takes 8 ms to render. The GPU may also wait for long stalls on CPU. Other potential problem areas are mesh rendering, shadows, vsync, and subsystems.
