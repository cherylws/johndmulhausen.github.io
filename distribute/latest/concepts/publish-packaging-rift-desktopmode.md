---
title: Rift Apps with Non-VR Desktop Modes
---

This topic describes how to support apps that can be launched in a non-VR desktop modes.

There are three methods for delivering apps that have both VR and desktop modes:

* **Select at startup**(preferred)—the app automatically boots into VR mode or desktop mode depending on command line arguments or whether it can detect a VR headset.
* **Multiple binaries**—the app provides two different executable files for VR and desktop modes.
* **Runtime mode switching**—the app switches between VR and desktop modes depending on whether the VR headset is in use.


## Setting Web Interface Options for App Builds with Non-VR Desktop Modes

For apps that use the Select at Startup method: 

1. In **Launch File**, enter the executable file name.
2. In **Launch Parameters**, enter the command line option that boots your app in VR mode.


For apps that use Multiple binaries: 

1. In **Launch File**, enter the 3D executable file name.
2. Select the **App is launchable in 2D mode** checkbox.
3. In **In Launch File (2D Mode)**, enter the 2D executable file name.


For apps that use runtime mode switching, upload as a regular Rift build. 

## Implementing the Select at Startup Method

To support the Select at Startup method, ship a single executable file that toggles between VR and desktop mode at startup, based on the availability of a working VR headset and command line parameters.

**Sample startup code and logic**

The common logic for this startup method is as follows:

1. If the command line argument specifies desktop mode, then start in desktop mode.
2. If no VR headset is available, then start in Desktop mode.
3. Otherwise, start in VR mode.


The following samples describe how to detect if a VR headset is available in Unity, Unreal, and native C++ applications.

## Detecting a VR Headset in Unity

In Unity, the command line option `-vrmode none` disables VR. The variable `VRSettings.enabled` indicates whether VR is running and the variable `VRSettings.loadedDevice` indicates whether the VR headset is available. Putting these components together gives us a way to check if the game should start in VR or desktop mode.

```
private static bool CheckForVRDevice()
{
  bool isVR = false;
  if (VRSettings.enabled)
  { 
    // VR is enabled, make sure the device is available
    if (VRSettings.loadedDevice == VRDeviceType.Oculus)
    {
      // VR is enabled and we have a connected VR device.
      // go forward with VR!
      isVR = true;
    }
    else
    {
      // no loaded device, so turn VR support off
      VRSettings.enabled = false;
    }
  }   
return isVR;    
}
```

## Detecting a VR Headset in Unreal Engine

In Unreal Engine apps, you can activate VR mode by passing the command line option `-vr` at launch, or by setting the value of the ConsoleVariables.ini variable `vr.BStartInVR` to 1. To activate desktop mode, use the command line option `-nohmd`. `GEngine-&gt;HMDDevice-&gt;IsHMDConnected()` indicates whether the VR headset is available. `GEngine-&gt;HMDDevice.IsValid()` indicates whether the app was started in VR mode.

```
bool CheckForVRDevice()

}
```

## Detecting a VR Headset with the Oculus PC SDK

In the Oculus PC SDK, the function `ovr_Create()` returns `false` if the VR headset is not available.

```
#include &lt;OVR_CAPI.h&gt;
void Application()
{
  ovrResult result = ovr_Initialize(nullptr);
  if (OVR_FAILURE(result))
  {
    return;
  }

  ovrSession session;

  bool isVR = YourArgumentCheckHere("-vrmode", "none");
  if (isVR)
  {
    // expecting VR mode, but need a valid device.
    ovrGraphicsLuid luid;
    result = ovr_Create(&amp;session, &amp;luid);
    if (OVR_FAILURE(result))
    {
      // no headset connected, fall back to Desktop mode.
      isVR = false;
    }
  }

  // run game loop here
  RunGameLoop(isVR);

  if (isVR)
  {
    ovr_Destroy(session);    
  }
  ovr_Shutdown();
}
```
