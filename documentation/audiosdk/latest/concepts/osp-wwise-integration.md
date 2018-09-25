---
title: Integrating the Oculus Spatializer
---
This section is for programmers who are integrating Wwise libraries and plugin registration within their application code base.

Add the commented-out code at the bottom of the file OculusSpatializer.h file to the code where the Wwise run-time is being initialized. This step is only required for applications that use the PC-SDK. For applications that use Unity, please follow the standard Wwise/Unity integration steps for third party plug-ins which is defined by Audiokinetic. Please see:[https://www.audiokinetic.com/library/edge/?source=Unity&id=pg\_\_install\_\_addlicensedplugins.html](https://www.audiokinetic.com/library/edge/?source=Unity&id=pg__install__addlicensedplugins.html).

Copy OculusSpatializerWwise.dll found within <platform>\bin\plugins folder into the folder where the Wwise-enabled application .exe resides. This allows the Wwise run-time to load the plugin when Wwise initialization and registration calls are executed. For example, if you are using UE4, place the plugin into the following folder: UE4\Engine\Binaries\<Win32 or Win64>.

The spatializer assumes that only one listener is being used to drive the spatialization. The listener is equivalent to the user's head location in space, so please be sure to update as quickly as possible. See Wwise documentation for any caveats on placing a listener update to an alternative thread from the main thread.

Provided that the listener and sounds are properly updated within the application, the sounds that have been set to the OSP bus will have a greater sense of 3D presence!

