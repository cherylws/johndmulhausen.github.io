---
title: Guidelines for VR Performance Optimization
---

This section covers the general principles that you should follow in order to effectively optimize your VR applications.

## Overview

Optimizing VR applications can be challenging. It is easy to go down the wrong path, and end up optimizing code that doesn’t improve the overall performance of your application. It is important to identify and focus on where the bottlenecks really are, and optimize those sections first.

VR performance issues are generally of two types: CPU issues and GPU issues. The CPU tends to be involved with simulation logic, state management, and generating the scene to be rendered. The GPU tends to be involved with sampling textures and shading for the meshes in your scenes. It is important to determine whether a performance problem is due to CPU load or GPU load, and to optimize your code accordingly.

In general, you follow Amdahl’s Law for parallel programming: Optimize the sections that are utilizing the system the most. Focus on the big expensive code paths. This document will provide guidance on how to identify these. Don’t focus on issues which, even if you reduce the costs to near zero, you would only achieve minor reductions to the overall performance costs. 

It is not uncommon for one area within your application to utilize a large percentage of the system’s processing time, while the remaining areas consume much smaller percentages. You should aim to optimize the larger problem area first.

As you optimize your application, strive to change one thing at a time. Keep in mind that there can be non-trivial interactions between the changes you make, especially with complex VR applications. If you are tracking down a performance regression in your application, try to locate in your version control software history the single change that caused the performance problem you are experiencing. Then, look for the root cause of the performance issue there. Don’t assume that multiple changes work together to cause a single performance problem.

For many people, it is easy to get a bit pedantic or obsessive about things that don’t matter in terms of bottom line performance. It is usually best to simply consider timing issues: Is the application hitting frame rate? If so, you may not need to further optimize your application, even if your code is not designed as well as would be ideal. Focus on what really counts, in terms of performance issues that impact the user experience.

## Techniques for Hitting Frame Rate

With VR, every frame must be typically drawn twice, once for each eye. That typically means that every draw call is issued twice, every mesh is drawn twice, and every texture is bound twice. There is also a small amount of overhead that is required to apply distortion and TimeWarp to the final output frame (approximately 2 ms per frame). Since the Rift refreshes frames at 90 Hz, it can be challenging to hit fame rate consistently. 

The following general guidelines can help you to meet frame rate:

* Limit each frame to a maximum of 500-1,000 draw calls 
* Limit each frame to a maximum of 1-2 million triangles or vertices 
* Use as few textures as possible, although they can be large. Smaller working sets, texture compression, and mipmapping will minimize texture bandwidth consumption. 
* Limit the time spent in script (or other logic) execution to 1 ~ 3 ms, for example when running Unity Update() 
* Systems are full of surprises, so always run a profiler to understand the way your application is using resources. 
* Don’t optimize too early in the development process. Simplify the code first. Conversely, don’t ignore obvious performance issues when you identify them. 
* Don’t rely on unproven technology or techniques that are not known to be performant.
* Everything is relative. Compare apples to apples. 
* Change one thing at a time: resolution, hardware resources, image quality, etc. 
* Some artifacts are worse than others. Dropped frames that cause discomfort are not worth better quality graphics. 
* Don’t rely on Asynchronous SpaceWarp (ASW) to hit rendering frame rate. ASW generates intermediate frames based on very recent head pose information, if your application begins to drop frames. It works by distorting the previous frame to match the more recent head pose. While ASW will help smooth out a few dropped frames now and then, applications must meet a consistent 90 frames per second (FPS) on a recommended spec machine and maintain 45 frames per second on a minimum spec machine to qualify for the Oculus Store. 


* Due to higher resolution and GPU load, the CPU tends to be less of a bottleneck on the Rift, when compared with mobile VR devices. 
* Graphical styles with simple shaders and relatively few polygons can often provide just as good of a VR experience as photorealistic graphics, which typically require significantly more processing in order to render each frame. 
* Use techniques such as Level of Detail (LOD), culling, and batching. 
* Cut the shading rate by scaling eye buffers, and using Oculus octilinear rendering (which leverages NVIDIA Lens Matched Shading). 
* Use projector shadows to save bandwidth. 
* When you are rendering to the cascaded shadow map, which can cost a lot in terms of bandwidth, consider the resolution and the number of cascades you are using. Try not to use expensive filtering. However, this approach pretty quickly ends up producing lower quality graphics. So you might use projector shadows. 
* Use simplified shader math and baked shading if necessary.


## Common Causes of Performance Problems

Performance problems are most commonly caused by the following issues (in order of severity):

|                                          **Performance Problem**                                          |   **Resource Costs**   |
|-----------------------------------------------------------------------------------------------------------|------------------------|
|                 Scenes that require dependent renders, including shadows and reflections                 |        CPU, GPU        |
|                   Binding of Vertex Buffer Objects (VBOs) in order to issue draw calls                   |  CPU, Graphics Driver  |
| Transparency, multi-pass shaders, per-pixel lighting, and other effects that fill large numbers of pixels |          GPU          |
|                           Large texture loads, blits, and other forms of memcpy                           | GPU, Memory Controller |
|                                             Skinned animation                                             |        CPU, GPU        |
|                                     Unity garbage collection overhead                                     |          CPU          |
