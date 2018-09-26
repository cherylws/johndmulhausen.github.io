---
title: Changes For Release 0.4 Since Release 0.2.5
---

In addition, the 0.4 Oculus API has been significantly redesigned since the 0.2.5 release, with the goals of improving ease of use, correctness and supporting a new driver model.

The following is the summary of changes in the API:

* All of the HMD and sensor interfaces have been organized into a C API. This makes it easy to bind from other languages.
* The new Oculus API introduces two distinct approaches to rendering distortion: SDK Rendered and Client Rendered. As before, the application is expected to render stereo scenes onto one or more render targets. With the SDK rendered approach, the Oculus SDK then takes care of distortion rendering, frame present, and timing within the SDK. This means that developers donâ€™t need to setup pixel and vertex shaders or worry about the details of distortion rendering, they simply provide the device and texture pointers to the SDK. In client rendered mode, distortion rendering is handled by the application as with previous versions of the SDK. SDK Rendering is the preferred approach for future versions of the SDK.


* The method of rendering distortion in client rendered mode is now mesh based. The SDK returns a mesh which includes vertices and UV coordinates which are then used to warp the source render target image to the final buffer. Mesh based distortion is more efficient and flexible than pixel shader approaches.


* The Oculus SDK now keeps track of game frame timing and uses this information to accurately predict orientation and motion.


* A new technique called Timewarp is introduced to reduce motion-to-photon latency. This technique re-projects the scene to a more recently measured orientation during the distortion rendering phase.




The table on the next page briefly summarizes differences between the 0.2.5 and 0.4 API versions.

|    Functionality    |                                                             0.2 SDK APIs                                                             |                                                                              0.4 SDK C APIs                                                                              |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    Initialization    |                                         OVR::System::Init, DeviceManager, HMDDevice, HMDInfo.                                         |                                                        ovr_Initialize, ovr_Create, ovrHmd handle and ovrHmdDesc.                                                        |
|  Sensor Interaction  | OVR::SensorFusion class, with GetOrientation returning Quatf. Prediction amounts are specified manually relative to the current time. |                    ovr_ConfigureTracking, ovr_GetTrackingState returning ovrTrackingState. ovr_GetEyePoses returns head pose based on correct timing.                    |
|   Rendering Setup   |            Util::Render::StereoConfig helper class creating StereoEyeParams, or manual setup based on members of HMDInfo.            | ovr_ConfigureRendering populates ovrEyeRenderDesc based on the field of view. Alternatively, ovr_GetRenderDesc supports rendering setup for client distortion rendering. |
| Distortion Rendering |                                      App-provided pixel shader based on distortion coefficients.                                      |                Client rendered: based on the distortion mesh returned by ovr_CreateDistortionMesh. (or) SDK rendered: done automatically in ovr_EndFrame.                |
|     Frame Timing     |                                         Manual timing with current-time relative prediction.                                         |                                  Frame timing is tied to vsync with absolute values reported by ovr_BeginFrame or ovr_BeginFrameTiming.                                  |
