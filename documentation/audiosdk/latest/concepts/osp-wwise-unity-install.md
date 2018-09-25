---
title: Adding Target Platform Plugins to Wwise Unity Projects
---
Add the Oculus Spatializer plugin after installing the Wwise Integration Package to your Unity projects. 

Audiokinetic provides Wwise integration for Unity projects through the Wwise Integration Package, allowing Wwise to be used in Unity games (see Audiokineticâ€™s documentation [here](https://www.audiokinetic.com/library/edge/?source=Unity&id=pg__installation.html)). Before you can add Wwise sound banks to your Unity scene that include Oculus spatialized audio, you must add the appropriate Oculus spatializer plugin to your Unity project.

Each Unity target platform (Android, macOS, x86, x86\_64) has its own plugin you must add.

## x86 Target Platform

1. Navigate to the Oculus Spatializer Wwise download package folder that matches your version of Wwise.
2. Copy \Win32\bin\plugins\OculusSpatializerWwise.dll to the {Unity Project}\Assets\Wwise\Deployment\Plugins\Windows\x86\DSP\ folder.
## x86\_64 Target Platform

1. Navigate to the Oculus Spatializer Wwise download package folder that matches your version of Wwise.
2. Copy \x64\bin\plugins\OculusSpatializerWwise.dll to the {Unity Project}\Assets\Wwise\Deployment\Plugins\Windows\x86\_64\DSP\ folder.
## macOS Target Platform

1. Navigate to the Wwise20xx/Mac folder in your Oculus Spatializer Wwise download package.
2. Copy libOculusSpatializerWwise.dylib to the {Unity Project}/Assets/Wwise/Deployment/Plugins/Mac/DSP/ folder.
## Android Target Platform

1. Navigate to the Wwise20xx\Android folder in your Oculus Spatializer Wwise download package.
2. Copy libOculusSpatializerWwise.so to the {Unity Project}\Assets\Wwise\Deployment\Plugins\Android\armeabi-v7a\DSP\ folder.
