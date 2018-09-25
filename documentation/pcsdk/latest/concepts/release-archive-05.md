---
title: Changes For Release 0.5
---
A number of changes were made to the API since the 0.4 release. 

The Oculus SDK 0.5 moves from static linking to a dynamic link library (DLL) model. Using a DLL offers several advantages:

* As long as the arguments and return values are the same, experiences do not need to be recompiled to take advantage of the updated library.
* Localization into new languages is easier because the functions remain consistent across languages.
* The DLL can be updated to take advantage of new features and headsets without affecting current games and experiences.
In addition to moving to a DLL model, the following changes were made:

* SDK versions now use a *product*.*major*.*minor*.*patch* format. The product value is currently set to 0 as this is a pre-release product. For example, 0.5.0.1 means Product 0, Major 5, Minor 0, Patch 1.
* Significant improvements were made to tracking behavior and performance.
* Improvements were made to the samples.
* The SDK now provides better reporting of display driver incompatibility.
* Support for DX10 was removed.
* DX9 support is deprecated and will be removed in a future version of the SDK.
* A bug was fixed where full persistence was inadvertently enabled due to device initialization races.
* Improvements were made to headset USB sleep management.
* Uncommon deadlocks were fixed in the runtime service.
* Diagnostics and configuration capture were improved.
* Monitor rotation is now supported in the legacy Extended mode.
* Default time warp scheduling is improved, which should reduce frame drops.
The following SDK changes were made:

* Moved and renamed LibOVR/Src/OVR\_CAPI.h to LibOVR/Include/OVR\_CAPI\_0\_5\_0.h. Some additional public headers such as OVR\_Version.h have been moved to LibOVR/Include/. Any other previously public headers are now private to LibOVR.
* Added enum ovrHmdCaps::ovrHmdCap\_DebugDevice.
* Renamed enum ovrDistortionCaps::ovrDistortionCap\_ProfileNoTimewarpSpinWaits to ovrDistortionCap\_ProfileNoSpinWaits.
* Removed enum ovrDistortionCaps::ovrDistortionCap\_NoTimewarpJit.
* Added enum ovrDistortionCaps::ovrDistortionCap\_TimewarpJitDelay.
* Removed ovrTrackingState::LastVisionProcessingTime.
* Removed ovrTrackingState::LastVisionFrameLatency.
* ovr\_Initialize now takes a params argument. See the in-code documentation for details.
* ovr\_Initialize now returns false for additional reasons.
* No API functions can be called after ovr\_Shutdown except ovr\_Initialize.
* The hmdToEyeViewOffset argument for ovr\_GetEyePosess is now const.
* Added the ovrQuatf playerTorsoMotion argument to ovr\_GetEyeTimewarpMatricesDebug.
* Added ovr\_TraceMessage.
