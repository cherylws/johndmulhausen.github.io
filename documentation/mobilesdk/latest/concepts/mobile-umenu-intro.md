---
title: Reserved User Interactions
---

This section describes input actions that are reserved for system level functionality. This includes the following physical buttons: Volume, Back, and Home.

## Reserved User Interactions

The Back button, Home button, and Volume button behaviors must conform to specific requirements.

### Volume Button Interactions

Volume adjustment on the Samsung Gear VR and Oculus Go devices are handled automatically. The volume control dialog display is also handled automatically by the VrApi as of Mobile SDK 1.0.3. Do not implement your own volume display handling, or users will see two juxtaposed displays.

You may override automatic volume display handling if necessary by setting VRAPI_FRAME_FLAG_INHIBIT_VOLUME_LAYER as an ovrFrameParm flag.

Volume buttons are not exposed through VrApi interfaces. 

### Back Button Interactions

Back button presses are of three types: long-press, short-press, and aborted long-press.

Short-press back button behavior is determined by the application. It is typically (but not necessarily) treated as a generic back action appropriate to the application’s current state.

Back actions usually prompt apps to navigate one level up in an interface hierarchy. For example, a short-press on the back button may bring up the application’s menu. In another application, a short-press may act as a generic back navigation in the UI hierarchy until the root is reached, at which point it may bring up an application-specific menu, or enter the Quit Confirmation dialog, allowing the user to exit the application.

In applications built with Unity, if no satisfactory stateful condition is identified by the application, the short-press opens the Quit Confirmation dialog allowing the user to exit the app and return to Oculus Home. Applications built with other engines must implement this handling - see the VrCubeWorld_NativeActivity sample for an example.

An aborted long-press results in no action, and when a timer is being shown cancels the timer.

When using the VrApi interfaces, the Back button will be shown to be down for a short press only on the frame that it is actually released. This prevents the app from having to implement its own short press detection.

### Home Button Interactions

A Home button press always opens a dialog to return the user to Oculus Home. As of Mobile SDK 1.0.4, this behavior is handled automatically by the VrApi.

If the Home button is held down on a 3DoF controller, it will start a timer for a controller recenter. The Home button must be held down for 0.75 seconds for the recenter action to complete.

The Home button is not exposed through the VrApi interfaces, and no Android events will be passed to the app for the Home button.

### Hardware Platform Differences

**Oculus Go**

* A short-press occurs when the button is down less than 0.5 seconds.
* There is no response to a long-press on the Back button and no animation timer is shown.


**Samsung Gear VR**

* A short-press occurs when the button is down less than 0.25 seconds.
* A timer animation is displayed from 0.25 to 0.75 seconds, indicating to the user that a long-press in underway.
* A long-press occurs when the back button is held longer than 0.75 seconds.
* Long-press on the Back button is reserved, and always opens the Settings menu. As of Mobile SDK 1.0.4, this behavior is handled automatically by the VrApi. You should no longer implement your own long-press Back button handling, including the gaze timer.

