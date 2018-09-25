---
title: LibOVR Integration
---
The Oculus SDK is designed to be as easy to integrate as possible. This guide outlines a basic Oculus integration with a C/C++ game engine or application.

We’ll discuss initializing the LibOVR, HMD device enumeration, head tracking, frame timing, and rendering for the Rift.

Many of the code samples below are taken directly from the OculusRoomTiny demo source code (available in Oculus/LibOVR/Samples/OculusRoomTiny). OculusRoomTiny and OculusWorldDemo are great places to view sample integration code when in doubt about a particular system or feature. 

## Overview of the SDK

There are three major phases when using the SDK: setup, the game loop, and shutdown.

To add Oculus support to a new application, do the following:

1. Initialize LibOVR through ovr\_Initialize.
2. Call ovr\_Create and check the return value to see if it succeeded. You can periodically poll for the presence of an HMD with ovr\_GetHmdDesc(nullptr).
3. Integrate head-tracking into your application’s view and movement code. This involves: 
	1. Obtaining predicted headset orientation for the frame through a combination of the GetPredictedDisplayTime and ovr\_GetTrackingState calls.
	2. Applying Rift orientation and position to the camera view, while combining it with other application controls.
	3. Modifying movement and game play to consider head orientation.
	
4. Initialize rendering for the HMD. 
	1. Select rendering parameters such as resolution and field of view based on HMD capabilities. 
		* See: ovr\_GetFovTextureSize and ovr\_GetRenderDesc.
		
	2. Configure rendering by creating D3D/OpenGL-specific swap texture sets to present data to the headset. 
		* See: ovr\_CreateTextureSwapChainDX and ovr\_CreateTextureSwapChainGL.
		
	
5. Modify application frame rendering to integrate HMD support and proper frame timing: 
	1. Make sure your engine supports rendering stereo views.
	2. Add frame timing logic into the render loop to obtain correctly predicted eye render poses.
	3. Render each eye’s view to intermediate render targets.
	4. Submit the rendered frame to the headset by calling the functions ovr\_WaitToBeginFrame, ovr\_BeginFrame, and ovr\_EndFrame.
	
6. Customize UI screens to work well inside of the headset.
7. Destroy the created resources during shutdown. 
	* See: ovr\_DestroyTextureSwapChain, ovr\_Destroy, and ovr\_Shutdown.
	
A more complete summary of rendering details is provided in the [Rendering Setup Outline](/documentation/pcsdk/latest/concepts/dg-render/#dg_render_distortion "The Oculus SDK makes use of a compositor process to present frames and handle distortion.") section.

