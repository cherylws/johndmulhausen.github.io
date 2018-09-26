---
title: 0.4 Mobile Unity Integration Release Notes
---

This document provides an overview of new features, improvements, and fixes included in the Oculus Unity Integration that shipped with version 0.4 of the Oculus Mobile SDK.

## Mobile Unity Integration 0.4.3

## New Features

* New Mobile Unity Integration Based on Oculus PC SDK 0.4.4


## Mobile Unity Integration 0.4.2

## Overview of Major Changes

If you are developing with Unity, we recommend updating to Unity 4.6.1, which contains Android 5.0 – Lollipop support.

We would like to highlight the inclusion of the new Mobile Unity Integration with full DK2 support based on the Oculus PC SDK 0.4.4. As this is a significant API refactor, please refer to the Unity Development Guide: Migrating From Earlier Versions section for information on how to upgrade projects built with previous versions of the Mobile Unity Integration.

## API Changes

* Fix for camera height discrepancies between the Editor and Gear VR device.
* Moonlight Debug Util class names now prefixed with OVR to prevent namespace pollution.
* Provide callback for configuring VR Mode Parms on OVRCameraController; see OVRModeParms.cs for an example.


## Mobile Unity Integration 0.4.1

## Overview of Major Changes

Added support for Android 5.0 (Lollipop) and Unity Free.

## New Features

* Added Unity Free support for Gear VR developers.


## Mobile Unity Integration 0.4.0

## Overview of Major Changes

First public release of the Oculus Mobile SDK.

## Bug Fixes

* Unity vignette rendering updated to match native (slightly increases effective FOV).
* Unity volume pop-up distance to match native.


## Migrating From Earlier Versions

The 0.4.3+ Unity Integration’s API is significantly different from prior versions. This section will help you upgrade.

## API Changes

The following are changes to Unity components:

|       OVRDevice  OVRManager       |         Unity foundation singleton.         |
|-----------------------------------|---------------------------------------------|
| OVRCameraController  OVRCameraRig |   Performs tracking and stereo rendering.   |
|             OVRCamera             | Removed. Use eye anchor Transforms instead. |

The following are changes to helper classes:

|    OVRDisplay    |      HMD pose and rendering status.      |
|------------------|-------------------------------------------|
|    OVRTracker    | Infrared tracking camera pose and status. |
| OVR.Hmd  Ovr.Hmd |        Pure C# wrapper for LibOVR.        |

The following are changes to events:

|    HMD added/removed    |              Fired from OVRCameraRig.Update() on HMD connect and disconnect.              |
|-------------------------|-------------------------------------------------------------------------------------------|
| Tracking acquired/lost |          Fired from OVRCameraRig.Update() when entering and exiting camera view.          |
|      HSWDismissed      | Fired from OVRCameraRig.Update() when the Health and Safety Warning is no longer visible. |
| Get/Set*(ref *) methods |                                  Replaced by properties.                                  |

## Behavior Changes

* OVRCameraRig’s position is always the initial center eye position.
* Eye anchor Transforms are tracked in OVRCameraRig’s local space.
* OVRPlayerController’s position is always at the user’s feet.
* IPD and FOV are fully determined by profile (PC only).
* Layered rendering: multiple OVRCameraRigs are fully supported (not advised for mobile).
* OVRCameraRig.*EyeAnchor Transforms give the relevant poses.


## Upgrade Procedure

To upgrade, follow these steps:

1. Ensure you didn’t modify the structure of the OVRCameraController prefab. If your eye cameras are on Game Objects named “CameraLeft” and “CameraRight” which are children of the OVRCameraController Game Object (the default), then the prefab should cleanly upgrade to OVRCameraRig and continue to work properly with the new integration.
2. Write down or take a screenshot of your settings from the inspectors for OVRCameraController, OVRPlayerController, and OVRDevice. You will have to re-apply them later.
3. Remove the old integration by deleting the following from your project:* OVR folder * OVR Internal folder (if applicable) * Any file in the Plugins folder with “Oculus” or “OVR” in the name * Android-specific assets in the Plugins/Android folder, including: vrlib.jar, libOculusPlugin.so, res/raw and res/values folders 


4. Import the new integration.
5. Click Assets -&gt; Import Package -&gt; Custom Package…
6. Open OculusUnityIntegration.unitypackage
7. Click Import All.
8. Fix any compiler errors in your scripts. Refer to the API changes described above. Note that the substitution of prefabs does not take place until after all script compile errors have been fixed.
9. Re-apply your previous settings to OVRCameraRig, OVRPlayerController, and OVRManager. Note that the runtime camera positions have been adjusted to better match the camera positions set in the Unity editor. If this is undesired, you can get back to the previous positions by adding a small offset to your camera:
	1. **Adjust the camera's y-position.**
		1. If you previously used an OVRCameraController without an OVRPlayerController, add 0.15 to the camera y-position.
		2. If you previously used an OVRPlayerController with **Use Player Eye Height** checked on its OVRCameraContoller, then you have two options. You may either (1) rely on the new default player eye-height (which has changed from 1.85 to 1.675); or (2) uncheck **Use Profile Data** on the converted OVRPlayerController and then manually set the height of the OVRCameraRig to 1.85 by setting its y-position. Note that if you decide to go with (1), then this height should be expected to change when profile customization is added with a later release.
		3. If you previously used an OVRPlayerController with **Use Player Eye Height** unchecked on its OVRCameraContoller, then be sure uncheck **Use Profile Data** on your converted OVRPlayerController. Then, add 0.15 to the y-position of the converted OVRCameraController.
		
	2. **Adjust the camera's x/z-position.** If you previously used an OVRCameraController without an OVRPlayerController, add 0.09 to the camera z-position relative to its y rotation (i.e. +0.09 to z if it has 0 y-rotation, -0.09 to z if it has 180 y-rotation, +0.09 to x if it has 90 y-rotation, -0.09 to x if it has 270 y-rotation). If you previously used an OVRPlayerController, no action is needed.
	
10. Re-start Unity


## Common Script Conversions

```
OVRCameraController -&gt; OVRCameraRig
   cameraController.GetCameraPosition() -&gt; cameraRig.rightEyeAnchor.position
   cameraController.GetCameraOrientation() -&gt; cameraRig.rightEyeAnchor.rotation
   cameraController.NearClipPlane -&gt; cameraRig.rightEyeCamera.nearClipPlane
   cameraController.FarClipPlane -&gt; cameraRig.rightEyeCamera.farClipPlane
   cameraController.GetCamera() -&gt; cameraRig.rightEyeCamera
   
   ----------------------------------------------------------------------
   if ( cameraController.GetCameraForward( ref cameraForward ) &amp;&amp;
   cameraController.GetCameraPosition( ref cameraPosition ) ) 
   {
   ...
   
   to
   
   if (OVRManager.display.isPresent)
   {
   
        // get the camera forward vector and position
        Vector3 cameraPosition = cameraController.centerEyeAnchor.position;
        Vector3 cameraForward = cameraController.centerEyeAnchor.forward;
   ...
  ----------------------------------------------------------------------
   
   OVRDevice.ResetOrientation();
   to
   OVRManager.display.RecenterPose();
   
   ----------------------------------------------------------------------
   
   cameraController.ReturnToLauncher();
   
   to
   
   OVRManager.instance.ReturnToLauncher();
   
   ----------------------------------------------------------------------
   
   OVRDevice.GetBatteryTemperature();
   OVRDevice.GetBatteryLevel();
   
   to
   
   OVRManager.batteryTemperature
   OVRManager.batteryLevel
   
   ----------------------------------------------------------------------
   
   OrientationOffset
   
   Set rotation on the TrackingSpace game object instead.
   
   ----------------------------------------------------------------------
   
   FollowOrientation
   
   ----------------------------------------------------------------------

   FollowOrientation is no longer necessary since OVRCameraRig applies tracking 
   in local space. You are free to script the rig’s pose or make it a child of 
   another Game Object.
```
