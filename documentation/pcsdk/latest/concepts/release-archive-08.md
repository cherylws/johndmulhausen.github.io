---
title: Changes For Release 0.8.0
---

The Oculus SDK 0.8 release changes the SDK from an HMD-based model to a session-based model and adds several new features. 

## New Features

The following are new features for the Oculus SDK and runtime:

* Improved support for Windows 10.
* Added ovr\_GetSessionStatus, which returns whether the headset is present and whether it has VR focus and can render to the headset.
* Added ovr\_Detect to OVR\_CAPI\_Util.h, which enables you to detect the presence of a headset without initializing LibOVR. This can be useful when a game has VR and non-VR modes.
* Added HandStatusFlags to ovrTrackingState, which specifies whether the Oculus Touch controllers are being tracked. Status includes orientation and position.
* Added SensorSampleTime to ovrLayerEyeFov, which specifies when the render pose was calculated. This is useful for measuring application tracking latency.
* Added ovr\_GetTrackingCaps to get the tracking capabilities of the device.
*  Usage of ovr\_ConfigureTracking is no longer needed unless you want to disable tracking features. By default, ovr\_Create enables the full tracking capabilities supported by any given device.
* Added ovrLayerHudMode, which enables the headset user to see information about a layer.
* Added ovrControllerType\_None and ovrControllerType\_XBox to ovrControllerType.
* The Oculus Debug Tool was added to simplify troubleshooting. For more information see [Oculus Debug Tool](/documentation/pcsdk/latest/concepts/dg-debug-tool/ "The Oculus Debug Tool (IDT) enables you to view performance or debugging information within your game or experience. It also enables you to tune or configure related parameters, such as the field of view (FOV) size for a mirrored flat-screen view of the VR experience (which could be streamed to an audience in a more comfortable viewing format).").


## Runtime Changes

Changes include:

* If you have an NVIDIA GPU, make sure to upgrade to the 358.70 driver or later. To get the driver, go to &lt;https://developer.nvidia.com/gameworks-vr-driver-support&gt;.
* If you have an AMD GPU, we recommend the Catalyst 15.10 Beta or later. To get the driver, go to &lt;http://support.amd.com/en-us/kb-articles/Pages/latest-catalyst-windows-beta.aspx&gt;.


## API Changes

This release represents a major revision of the API. Changes to the API include:

* Applications no longer need to call ovr\_ConfigureTracking. ovr\_Create automatically enables the full tracking capabilities supported by any given device.
* Replaced ovr\_GetFrameTiming with ovr\_GetPredictedDisplayTime.
* Added latencyMarker to ovrTrackingState. When set to ovrTrue, this indicates that it will be used in the rendering loop and will be used to calculate latency.
* To emphasize the session model, renamed ovrHmd to ovrSession and hmd to session.
* ovrLayerType\_QuadInWorld and ovrLayerType\_QuadHeadLocked were renamed to ovrLayerType\_Quad and are now differentiated by the ovrLayerFlag\_HeadLocked flag.
* Added ovrMaxLayerCount, which sets the maximum number of layers to 32.
* Removed ovrInit\_ServerOptional. If you use this to detect whether the OVRService is available, periodically call ovr\_Initialize or poll ovr\_Detect instead.
* Removed ovrTrackingCap\_Idle from ovrTrackingCaps. 


## Known Issues

The following are known issues:

* The Oculus service might crash when gathering diagnostic logs from the Oculus Config Util. If this happens, the service will automatically restart and the logs will be retained.
* The Oculus service and Config Util might hang when running the demo scene and another VR app at the same time"


## Migrating from SDK 0.7.x to SDK 0.8

To migrate:

1. Update calls to ovr\_GetFrameTiming with ovr\_GetPredictedDisplayTime using the new syntax.
2. Update instances of ovrHmd hmd to ovrSession session.
3. Remove any code that uses ovrInit\_ServerOptional. If you use this to detect whether the OVRService is available, periodically call ovr\_Initialize or poll ovr\_Detect instead.
4. Remove calls to ovr\_ConfigureTracking as the SDK enables all existing tracking features by default.
5. For ovrLayerType\_EyeFov layers, fill in the SensorSampleTime with timestamps captured when ovr\_GetTrackingState is being called in the same frame just before generating the view matrix to render the two eye textures.

