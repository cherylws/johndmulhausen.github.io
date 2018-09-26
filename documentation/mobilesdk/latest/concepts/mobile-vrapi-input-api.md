---
title: VrApi Input API
---

This document describes using the VrApi Input API.

The VrApi Input API allows applications linked to VrApi to enumerate and query the state of devices connected to a Samsung Gear VR or Oculus Go. When a device is enumerated, its current state can be queried using the input API.

The Input API is defined in VrApi/Src/VrApi_Input.h. For sample usage, see VrSamples/Native/VrController.

## System Input and SIGILL

The mobile VR runtime reserves the Back, Home, Volume Up, and Volume Down buttons for system input. Applications will never see Home and volume buttons, while Back button presses are deferred and may be consumed in the case of long-presses. In order to capture this input from all input devices, the VR runtime uses a SIGILL interrupt handler to hook input in the VR application process. If your engine uses a SIGILL handler, it may conflict with the mobile VR runtime's SIGILL handler and cause undefined behavior.

## Input Devices Supported

For all devices listed below, there are buttons and interactions that are unavailable or require specific interactions. The Home, Back button long-press, Volume Up and Volume Down buttons on the controller and headset are reserved for system use and will not appear in the button state on either input device. Please see the [Reserved User Interactions](/documentation/mobilesdk/latest/concepts/mobile-umenu-intro/#mobile-umenu-intro) page for more information about reserved interactions. 

**Samsung Gear VR Headset**

Gear VR Headset controls include the touchpad and Back button short-press.

**Samsung Gear VR Controller and Oculus Go Controller**

The controllers are orientation-tracked input devices. The controller is positioned relative to the user by using a body model to estimate the location based upon the orientation of the device.

Left-handedness versus right-handedness is specified by users during controller pairing, and is used to determine which side of the user’s body to position the controller.

Both controllers have a touchpad, a trigger, a home and back button. The Samsung Gear VR Controller also has volume up and down buttons.

**Bluetooth Gamepads**

Bluetooth gamepads are exposed through the Input VrApi, attempting to map the device to the classic gamepad model of a X Y B A buttons, left and right triggers, left and right bumpers, a d-pad, and 2 joysticks.

## Enumerating Devices

In order to find a device, an application should call vrapi_EnumerateInputDevices. This function takes a pointer to the ovrMobile context, and an index and a pointer to an ovrInputCapabilityHeader structure. If a device exists for the specified index, the ovrInputCapabilityHeader’s Type and DeviceID members are set upon return.

Once a device is enumerated, its full capabilities can be queried with vrapi_GetInputDeviceCapabilities. This function also takes a pointer to an ovrInputCapabilityHeader structure, but the caller must pass a structure that is appropriate for the ovrControllerType that was returned by vrapi_EnumerateInputDevices.

For instance, if vrapi_EnumerateInputDevices returns a Type of ovrControllerType_TrackedRemote when passed an index of 0, then the call to vrapi_GetInputDeviceCapabilities should pass a pointer to the Header field inside of a ovrInputTrackedRemoteCapabilities structure. For example:

```
ovrInputCapabilityHeader capsHeader;
if ( vrapi_EnumerateInputDevices( ovr, 0, &amp;capsHeader ) &gt;= 0 )
{
   if ( capsHeader.Type == ovrControllerType_TrackedRemote )
   {
      ovrInputTrackedRemoteCapabilities remoteCaps;
      remoteCaps.Header = capsHeader;
      if ( vrapi_GetInputDeviceCapabilities( ovr, &amp;remoteCaps.Header ) &gt;= 0 )
      {
            // remote is connected
      }
   }
}
```

After successful enumeration, the ovrInputCapabilityHeader structure that was passed to vrapi_EnumerateInputDevices will have its DeviceID field set to the device ID of the enumerated controller.

The device state can then be queried by calling vrapi_GetInputTrackingState as described below.

## Device Connection and Disconnection

Devices are considered connected once they are enumerated through vrapi_EnumerateInputDevices, and when vrapi_GetInputTrackingState and vrapi_GetCurrentInputState return valid results.

vrapi_EnumerateInputDevices does not do any significant work and may be called each frame to check if a device is present or not.

## Querying Device Input State

The state of the input device can be queried via the vrapi_GetCurrentInputState function.

Both functions take deviceIDs and pointers to ovrInputStateHeader structures. Before calling these functions, fill in the header’s Type field with the type of device that is associated with the passed deviceID. Make sure the structure passed to these functions is not just a header, but the appropriate structure for the device type. For instance, when querying a controller, pass an ovrInputTrackedRemoteCapabilities structure with the Header.Type field set to ovrControllerType_TrackedRemote.

```
ovrInputStateTrackedRemote remoteState;
remoteState.Header.Type = ovrControllerType_TrackedRemote;
if ( vrapi_GetCurrentInputState( ovr, controllerDeviceID, &amp;remoteState.Header ) &gt;= 0 )
{
// act on device state returned in remoteState
}
```

vrapi_GetCurrentInputState returns the controller’s current button and trackpad state.

## Querying Device Tracking State

To query the orientation tracking state of a device, call vrapi_GetInputTrackingState and pass it a predicted pose time. Passing a predicted pose time of 0 will return the most recently-sampled pose.

```
ovrTracking trackingState;
if ( vrapi_GetInputTrackingState( ovr, controllerDeviceID, &amp;trackingState ) &gt;= 0 )
```

VrApi implements an arm model that uses the controller’s orientation to synthesize a plausible hand position each frame. The tracking state will return this position in the Position field of the predicted tracking state’s HeadPose.Pose member.

Controller handedness may be queried using vrapi_GetInputDeviceCapabilities as described in Enumerating Devices above.

Applications that implement their own arm models are free to ignore this position and calculate a position based on the Orientation field that is returned in the predicted tracking state’s pose.

## Recentering the Controller

Users may experience some orientation drift in the yaw axis, causing the physical controller's orientation to go out of alignment with its VR representation.

To synchronize the physical controller’s orientation with the VR representation, users should:

1. Point the controller in the direction of the forward axis of their headset, and
2. Press and hold the Home button for one second.


When a recenter occurs, the VrApi arm model is notified and the arm model’s shoulders are repositioned to align to the headset’s forward vector. This is necessary because the shoulders do not automatically rotate with the head.

Applications that implement their own arm models can poll the device input state’s RecenterCount field to determine when the controller is recentered. RecenterCount increments only when a recenter is performed. We recommend recentering arm models based on the head pose when this field changes.

## Headset Emulation

Emulation mode is convenient for applications that have not been rebuilt to use the new controller API. When enabled, Gear VR and Oculus Go Controller touch values send Android touch events using the same mapping as Gear Vr headset touch values, and applications cannot distinguish headset inputs from controller inputs.

Headset emulation for the controller can be toggled on or off by calling vrapi_SetRemoteEmulation. It is disabled by default.

When emulation is enabled, applications that load a new VrApi with Gear VR Controller support will receive input from the controller through Android Activity’s dispatchKeyEventx and dispatchTouchEvent methods.

New applications and applications that are specifically updated to use the controller should use the VrApi Input API to enumerate the controller and query its state directly. Applications may also want to enumerate the headset and query its state through the same API.

## Touchpad Swiping Gestures

For touchpads, the user interface of your VR experience should follow these natural scrolling and swiping gestures:

* Swipe up: Pull content upward. Equivalent to scrolling down.
* Swipe down: Pull content downward. Equivalent to scrolling up.
* Swipe left: Pull content left or go to the next item or page. 
* Swipe right: Pull content right or go to the previous item or page.

