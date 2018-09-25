---
title: Changes in Version 1.19.x
---
## New Features for 1.19.x

* Oculus Dash functionality—New API support has been added so that you can begin to prepare your applications for the upcoming release of Oculus Dash. See API Changes, below.
* Cubemap support—A new cubemap layer has been added. A cubemap consists of six rectangles which are placed around the user, as if the user is sitting inside of a room that is cube shaped. Cubemaps appear to be at infinite distance, and provide the background for all other objects in the VR experience. For example, you can use cubemaps to create the sky that will appear behind buildings, trees, and other objects. You don't need to handle occlusion by objects in the foreground. You can simply setup the cubemap, and it will appear in the background everywhere in your scene.
* Octilinear rendering—Octilinear rendering implements NVIDIA Lens Matched Shading. You can enable octilinear rendering to improve the performance of your applications when they are executed on an NVIDIA GPU. Octilinear rendering is essentially a way to compress the screen buffers, so that about 20% less work is required to render each frame.
* More flexible graphics submission APIs—The ovr\_SubmitFrame API has been deprecated, and replaced by a set of more flexible graphics submission APIs. The new APIs enable more sophisticated performance optimization, especially in multi-threaded environments. See API Changes, below.
## API Changes

* New Lifecycle functionality related to Dash: 
	+ ovrInit\_FocusAware is a flag that your application should set to True if it is prepared to respond to ovrSessionStatus focus states, including ovrSessionStatus::HasInputFocus. If you set this flag to True, your application should respond to a loss of focus by hiding any representations of the user’s hands, and by pausing all activity.
	+ HasInputFocus is a flag that will be True if your application is the foreground application. If this flag is False, then your application is in the background, but may still be visible. When your application is in the background, it should hide any representations of the user’s hands, hide any near field objects (within about one meter of the user), and pause all activity. Note that the VR Compositor may use up to 3 ms of additional rendering time during each frame cycle while HasInputFocus is False. Because of this, it is a good idea to switch your application into a lower performance mode, if possible, as long as HasInputFocus is False.
	
* New graphics submission APIs: ovr\_SubmitFrame has been deprecated and replaced by a more flexible set of graphics submission APIs which provide the ability to split apart the frame submission functionality. This enables more sophisticated performance optimizations, especially in multi-threaded environments. The new APIs are: 
	+ ovr\_WaitToBeginFrame: This function waits until surfaces are available and it is time to begin rendering the frame
	+ ovr\_BeginFrame: This function should be called from render thread before application begins rendering.
	+ ovr\_EndFrame: This function should be called from render thread after application has finished rendering, in order to submit the rendered frame to the Oculus compositor.
	
## Known SDK Issues

* If you encounter intermittent tracking issues, remove the batteries from any Engineering Sample Oculus Remotes that you paired with your headset and contact Developer Relations for replacement remotes.
* If you bypass the shim and communicate with the DLL directly, without specifying a version to ovr\_Initialize, the DLL has no way of knowing the SDK version with which the application was built. This can result in unpredictable or erratic behavior which might cause the application to crash.
