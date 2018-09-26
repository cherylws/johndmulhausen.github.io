---
title: Requirements and Setup
---



## Requirements

* Windows 7/8/10
* Unity 5.2 Professional or Personal, or later. See [Unity Compatibility and Requirements](https://developer.oculus.com/documentation/unity/latest/concepts/unity-req/) for details on our recommended versions.


## Download and Setup

To download the ONSP and import it into a Unity project: 

1. Download the **Oculus Spatializer Unity** package from the [Audio Packages](https://developer.oculus.com/downloads/audio/) page.
2. Extract the zip. 
3. Open your project in the Unity Editor, or create a new project. 
4. Select *Assets* &gt; *Import Package* &gt; *Custom Packageâ€¦*. 
5. Select OculusNativeSpatializer.unitypackage and import.
6. When the *Importing Package* dialog opens, leave all assets selected and click *Import*.


To turn on the Native Spatializer:

1. Go to *Edit* &gt; *Project Settings* &gt; *Audio* in Unity Editor
2. Select *OculusSpatializer* in the *Spatializer Plugin* drop-down setting in the AudioManager Inspector panel as shown below.


We recommend Rift developers set **DSP Buffer Size** to **Best latency** to set up the minimum buffer size for the platform that is supported, reducing overall audio latency.

Gear VR developers should set **DSP Buffer Size** to **Good** or **Default** to avoid audio distortion.

![](/images/documentationaudiosdklatestconceptsospnative-unity-req-setup-0.png)

## Updating to Oculus Native Spatializer for Unity from previous OSP for Unity Versions

1. Note the settings used in OSPManager in your project.
2. Replace OSPAudioSource.cs (from previous OSP) on AudioSources with ONSPAudioSource.cs in &lt;project&gt;/Assets/OSP.
3. Set the appropriate values previously used in OSPManager in the plugin effect found on the mixer channel. Note that the native plugin adds functionality, so you will need to adjust to this new set of parameters.
4. Remove OSPManager from the project by deleting OSPManager*.* from &lt;project&gt;/Assets/OSP **except** your newly-added ONSPAudioSource.cs.
5. Verify that OculusSpatializer is set in the Audio Manager and that Spatialization is enabled for that voice.


Use the functions on AudioSource to start, stop and modify sounds as required.
