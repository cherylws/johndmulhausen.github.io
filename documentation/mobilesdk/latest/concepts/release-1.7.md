---
title: 1.7 Release Notes
---
This document provides an overview of new features, improvements, and fixes included in the latest version of the Oculus Mobile SDK.

## 1.7.0

## Overview of Major Changes

Mobile SDK 1.7.0 provides a new VrApi interface method for obtaining predicted tracking information, build system improvements, and native debugging support with externalNativeBuild.

For details on migrating to Mobile SDK 1.7.0 from previous versions, see [Migrating to Mobile SDK 1.7.0](/documentation/mobilesdk/latest/concepts/mobile-native-migration/#mobile-native-migration-1-7-0 "This section is intended to help you upgrade from the Oculus Mobile SDK version 1.5.0 to 1.7.0.").

## New Features

* The build tools versions have changed to: 
	+ Android NDK r14b
	+ Gradle 3.3
	+ Android Plugin for Gradle 2.3.3
	+ Android SDK Build-Tools 25.0.1 
	
* Added the system status enumeration *VRAPI\_SYS\_STATUS\_SYSTEM\_UX\_ACTIVE* to detect if the either the **long press timer** or **recenter timer** system layers are active. 
* vrapi\_Initialize now returns an error code if the system driver is not found on the device instead of terminating the app with an exit(0).
## API Changes

* Added a new entry point, vrapi\_GetPredictedTracking2, for querying the predicted tracking information along with corresponding view and projection matrices for each eye.
* A default head model is now automatically applied in both vrapi\_GetPredictedTracking() and vrapi\_GetPredictedTracking2() for apps targeting SDK 1.7.0 and later. Because these tracking methods no longer explicitly apply the head model or manage head model parameters, we've removed the following methods from the VrAppFramework library: 
	+ const ovrHeadModelParms & GetHeadModelParms() const;
	+ void SetHeadModelParms( const ovrHeadModelParms & parms );
	
* The predicted tracking methods now return the head pose Y translation as height above the floor. Previously, the Y translation was relative to the head position in its canonical pose, that is, it generally hovered around 0.0m. Apps that previously applied a bias to place the view in the virtual world space must be adjusted if targeting SDK 1.7.0 or later.
* The vrapi\_GetCenterEye() helper functions have been removed and replaced with vrapi\_GetFromPose()* helper functions to remove the notion of a 'center eye'.
* VRAPI\_FRAME\_LAYER\_FLAG\_WRITE\_ALPHA from ovrFrameFlags has been deprecated. 
* DST\_ALPHA from ovrLayerType has been deprecated.
* VrApi\_LocalPrefs.h has been removed. Applications can use Android system properties for any development debug needs.
* ovr\_GetLocalPreferenceValueForKey and ovr\_SetLocalPreferenceValueForKey are no longer provided on the interface. Applications that need similar development testing functionality should instead use Android system properties directly.
