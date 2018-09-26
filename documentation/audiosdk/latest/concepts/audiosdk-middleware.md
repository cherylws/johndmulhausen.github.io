---
title: Middleware Support
---



Very few Oculus developers will use the Oculus Audio C/C++ SDK directly. Most developers use a middleware framework, such as Audiokinetic Wwise or FMOD, and/or an engine such as Unity or Epic's Unreal. For this reason, we support middleware packages and engines commonly used by developers.

* **Audiokinetic Wwise**: Oculus provides a Wwise compatible plugin for Windows. More information about this plugin can be found in the [Oculus Spatializer for Wwise Integration Guide](/documentation/audiosdk/latest/concepts/osp-wwise-overview/ "The Oculus Spatializer Plugin (OSP) is an add-on plugin for the Audiokinetic Wwise tool set that allows monophonic sound sources to be spatialized in 3D relative to the user's head location. This integration guide describes how to install and use OSP in both the Wwise application and the end-user application.").
* **FMOD**: The Oculus Audio SDK supports FMOD on the Windows, Mac and Android platforms. More information about this plugin can be found in the [Oculus Spatializer for FMOD Integration Guide](/documentation/audiosdk/latest/concepts/osp-fmod-overview/ "The Oculus Spatializer Plugin (OSP) is an add-on plugin for FMOD Studio for Windows and Mac OS X that allows monophonic sound sources to be properly spatialized in 3D relative to the user's head location. This plugin requires FMOD Studio version 1.08.16 or later.").
* **Unity3D**: The Oculus Audio SDK supports Unity 5 on Android, Mac OS X and Windows. More information about this plugin can be found in the [Oculus Native Spatializer for Unity](/documentation/audiosdk/latest/concepts/book-ospnative-unity/ "Welcome to this guide to using the Oculus Native Spatializer plugin in Unity.").
* **Unreal Engine**: Epic's Unreal Engine 4 supports numerous different audio subsystems. The Wwise integration (available directly from Audiokinetic) has been tested with our Wwise Spatializer plugin (see above).

