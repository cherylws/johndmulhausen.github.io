---
title: Setup
---



## Installing the Profiler

Download the **Oculus Audio Profiler for Windows** package from the [ Audio Packages](/downloads/audio/) page. 

After downloading the package, extract the contents of the .zip file to the desired location.

## Activating Profiling in Your App

We ship the Oculus Spatializer with the analytics server turned off. Before you can profile your app's audio, you must activate the Oculus Spatializer analytics server in your app.

**Oculus Spatializer Plugins in Unity (Native, FMOD, Wwise)**

1. Create an empty game object.
2. Add the appropriate script component to the game object: ![](/images/documentationaudiosdklatestconceptsaudio-profiler-setup-0.png)


	1. For Unity Native Plugin, add ONSPProfiler.
	2. For FMOD Unity Plugin, add OculusSpatializerFMOD.
	3. For Wwise Unity Plugin, add OculusSpatializerWwise.
	
3. Select the **Profiler Enabled** check box.
4. (Optional) Change the network port if the default port of 2121 is not suitable for your use case.


**Oculus Spatializer Plugin for Wwise**

1. Call OSP\_Wwise\_SetProfilerEnabled(bool enabled);
2. (Optional) Change the network port if the default port of 2121 is not suitable for your use case by calling OSP\_Wwise\_SetProfilerPort(int port)


**Oculus Spatializer Plugin for FMOD**

1. Call OSP\_FMOD\_SetProfilerEnabled(bool enabled);
2. (Optional) Change the network port if the default port of 2121 is not suitable for your use case by calling OSP\_FMOD\_SetProfilerPort (int port);


**Oculus Spatializer Plugin for Native C/C++ Apps**

1. Call ovrAudio\_SetProfilerEnabled(ovrAudioContext Context, int enabled);
2. (Optional) Change the network port if the default port of 2121 is not suitable for your use case by calling ovrAudio\_SetProfilerPort(ovrAudioContext Context, int portNumber);

