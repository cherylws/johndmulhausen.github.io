---
title: 1.3 Oculus Utilities for Unity 5 Release Notes
---
## Oculus Utilities for Unity 5 version 1.3.2

This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Utilities for Unity 5. For information on first-party changes to Unity VR support for Oculus, see the Unity Release Notes for the appropriate version. You will find an updated scripting reference for the included C# scripts in our [Unity Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/).

## Unity Versions and OVRPlugin

Oculus Utilities for Unity 5 version 1.3.2 is for use with Unity 5.3 or Unity 5.4. It may only be used with **Unity 5.3.3p3 or later, or 5.4.0b11 or later**. You **must** download and install our OVRPlugin for Unity 1.3.2, available from our Downloads Page, to use these versions. For more information, see [Utilities 1.3.2 and OVRPlugin](/documentation/unity/latest/concepts/release-archive-unity-ovrplugin-132/ "Some versions of Unity require special handling to enable built-in VR support. This will not be required in future versions of Unity.").

## New Features

* OVRInput may now be used without an OVRManager instance in the scene.
## API Changes

* Restored OVRVolumeControl.
## Bug Fixes

* OVRManager.instance.usePositionTracking now toggles the head model on Gear VR.
* Fixed incorrect fog interaction with transparent UI shader.
* Fixed crash on start with Unity 5.4.0b14 and b15 on Gear VR.
* Restored OVRVolumeControl, which was accidentally removed in 1.3.0.
## Known Issues

* **Utilities 1.3.0**: Volume control will be missing on mobile applications until the release of Mobile SDK 1.0.2. OVRVolumeControl is available with Utilities v 0.1.3.0 and earlier. It was also restored in Utilities v 1.3.2.
## Oculus Utilities for Unity 5 version 1.3.0

Note: Oculus Utilities for Unity 5 version 1.3.0 is for use with **Unity 5.3.4p1 only**. To use Unity 5.3.4p1 with the Oculus Rift or Samsung Gear VR, **you must download and install our OVRPlugin for Unity 1.3.0**, available from our [Downloads page](/downloads/). For more information, see [Unity 5.3.4p1 and OVRPlugin 1.3.0](/documentation/unity/latest/concepts/release-archive-unity-ovrplugin-132/ "Some versions of Unity require special handling to enable built-in VR support. This will not be required in future versions of Unity.").## Overview of Major Changes

This public release incorporates all changes from Utilities private releases 0.2.0 through 1.3.0. 

We no longer include the deprecated InputManager.asset file.

## Rift Floor-Level Tracking

OVR Manager now includes Tracking Origin Type, which defaults to Eye Level (i.e., tracking origin is handled as in previous releases). When set to Floor Level, tracking origin will be calculated relative to the user’s standing height as specified during Rift setup or with the Oculus app.

Note: Floor-level tracking will often be used with standing experiences, but there may be situations in which eye-level tracking is a better fit for a standing experience, or floor-level tracking is a better fit for a seated experience.Any application running Unity should now be able to pull the correct height information.

## New Features

* Added support for PC SDK 1.3, including support for Rift consumer version hardware.
* Added support for Asynchronous TimeWarp and Phase Sync.
* Added Rift Remote controller support.
* Added application lifecycle management, including VR-initiated backgrounding and exit.
* Exposed proximity sensor.
* Added support for multiple trackers.
* Exposed velocity and acceleration for all tracked nodes.
* Added support for EyeLevel and FloorLevel tracking origins.
* Audio input and output now automatically use the Rift microphone and headphones (if enabled in the Oculus app).
* Rift’s inter-axial distance slider now affects the distance between Unity’s eye poses.
* Splash screen now uses Asynchronous TimeWarp for smooth tracking during load.
* Added experimental D3D 12 rendering support.
* Added events for focus change.
* Added events for audio device changes requiring sound restart.
* Added ControllerTracked state.
* Reduced head tracking latency on Gear VR by updating on render thread
* Improved performance by reducing lock contention.
* Exposed power management (CPU and GPU levels) on Android.
* Exposed queue-ahead on Android to trade latency for CPU-GPU parallelism.
## API Changes

* OVRTracker.GetPose() no longer takes a prediction time. It now takes an optional index specifying the tracker whose pose you want.
* OVRTracker.frustum has been replaced by OVRTracker.GetFrustum(), which takes an optional index specifying the tracker whose frustum you want.
* OVRManager.isUserPresent is true when the proximity sensor detects the user.
* OVRInput.GetControllerLocal[Angular]Velocity/Acceleration exposes the linear and angular velocity and rotation of each Touch controller.
* OVRDisplay.velocity exposes the head’s linear velocity.
* OVRDisplay.angularAcceleration exposes the head’s angular acceleration.
* Removed OVRGamepadController.cs and OVRInputControl.cs scripts, which have been replaced by the new OVRInput.cs script. Refer to [OVRInput](/documentation/unity/latest/concepts/unity-ovrinput/#unity-ovrinput "OVRInput exposes a unified input API for multiple controller types.") for more information.
* Added public member Tracking Origin Type to OVR Manager.
* Added “floor level” reference frame for apps that need accurate floor height.
* Removed OVRVolumeControl in favor of Universal Menu’s built-in volume meter.
* OVRManager.queueAhead now controls Gear VR latency mode, allowing you to trade latency for CPU-GPU parallelism. Queue-ahead is now automatically managed on Rift.
* Events OVRmanager.VrFocusLost and VrFocusAcquired occur when the app loses and regains VR focus (visibility on the HMD).
* Events OVRManager.AudioOutChanged and AudioInChanged occur when audio devices change and make audio playback impossible without a restart.
* OVRManager.cpuLevel controls CPU power-saving vs performance trade-off on Gear VR.
* OVRManager.gpuLevel controls GPU power-saving vs performance trade-off on Gear VR.
* Added ability to hold a named mutex throughout runtime.
## Bug Fixes

* Removed redundant axial deadzone handling from Xbox gamepad input.
* Fixed OVRManager.monoscopic to display left eye buffer to both eyes and use center eye pose.
* Application lifetime management now works, even without the Utilities.
* Fixed crash when running VR apps with Rift disconnected.
* OVRManager.isUserPresent now correctly reports proximity sensor output.
* OVRManager.isHMDPresent now correctly reports Gear VR docking state.
* We now prevent AFR SLI on NVIDIA hardware to avoid black screens/flicker.
* Fixed drift between TimeWarp start matrix and view matrix.
* Fixed crash when main monitor is on one adapter and Rift is on another.
* Fixed crash on Mac due to OVRPlugin being uninitialized before first access.
* Increased dead zone on OVRInput stick input to prevent drift.
* Fixed handedness issue with angular head velocity on Rift.
* Fixed handedness issue with rotation of OVROverlay quads. 
* Fixed crash in OVROverlay when using D3D 12 and compressed textures.
* Fixed crashes due to thread synchronization checks on Gear VR.
* Fixed loss of input handling while paused.
* Fixed artifact in which bars appeared around mirror image when using occlusion mesh.
* Fixed Android logcat spam about OVR\_TW\_SetDebugMode.
* Gear VR logs now report VRAPI loader version, not SystemActivites version.
* Statically linking MSVC runtime to avoid missing DLL dependencies.
* Fixed black screen when HMD was reconnected: notifying Unity of display lost.
## Known Issues

* Volume control will be missing on mobile applications until the release of Mobile SDK 1.0.2. To restore OVRVolumeControl, please use an older copy of the Utilities.
* **[Utilities 1.3.2 and OVRPlugin](/documentation/unity/latest/concepts/release-archive-unity-ovrplugin-132/)**  
Some versions of Unity require special handling to enable built-in VR support. This will not be required in future versions of Unity.
* **[Utilities 1.3.0 and OVRPlugin](/documentation/unity/latest/concepts/release-archive-unity-ovrplugin-130/)**  

