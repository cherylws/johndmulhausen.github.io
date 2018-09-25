---
title: OVRInput
---
OVRInput exposes a unified input API for multiple controller types.

It may be used to query virtual or raw controller state, such as buttons, thumbsticks, triggers, and capacitive touch data. It currently supports the Oculus Touch, Microsoft Xbox controllers, and the Oculus remote on desktop platforms. For mobile development, it supports the Gear VR Controller and Oculus Go Controller as well as the touchpad and back button on the Gear VR headset. Gamepads must be Android compatible and support Bluetooth 3.0.

For keyboard and mouse control, we recommend using the UnityEngine.Input scripting API (see Unity’s [Input scripting reference](http://docs.unity3d.com/ScriptReference/Input.html) for more information).

Mobile input bindings are automatically added to InputManager.asset if they do not already exist.

For more information, see **OVRInput** in the [Unity Scripting Reference](/documentation/unity/latest/concepts/unity-reference-scripting/ "The Unity Scripting Reference contains detailed information about the data structures and files included with the Utilities and Legacy Integration packages."). For more information on Unity’s input system and Input Manager, documented here: <http://docs.unity3d.com/Manual/Input.html> and <http://docs.unity3d.com/ScriptReference/Input.html>.

## Requirements

To use OVRInput, you must either: 

1. Include an instance of OVRManger anywhere in your scene; or
2. Call OVRInput.Update() and OVRInput.FixedUpdate() once per frame at the beginning of any component’s Update and FixedUpdate methods, respectively.
## Oculus Touch Tracking

OVRInput provides Touch position and orientation data through GetLocalControllerPosition() and GetLocalControllerRotation(), which return a Vector3 and Quaternion, respectively.

Controller poses are returned by the constellation tracking system and are predicted simultaneously with the headset. These poses are reported in the same coordinate frame as the headset, relative to the initial center eye pose, and may be used for rendering hands or objects in the 3D world. They are also reset by OVRManager.display.RecenterPose(), similar to the head and eye poses.

## Gear VR and Oculus Go Controllers

The Oculus Go and Gear VR Controller provide orientation data through GetLocalControllerRotation(), which returns a quaternion.

The controller is positioned relative to the user by using a body model to estimate the controller’s position. Whether the controller is visualized on the left or right side of the body is determined by left-handedness versus right-handedness, which is specified by users during controller pairing.

To query handedness of a paired controller, use IsControllerConnected() or GetActiveController() to query for RTrackedRemote or LTrackedRemote.

For example: 

// returns true if right-handed controller connected OVRInput.IsControllerConnected(OVRInput.Controller.RTrackedRemote);Use OVRInput.Get() to query controller touchpad input. You may query the input position with Axis2D:

OVRInput.Get(OVRInput.Axis2D.PrimaryTouchpad, OVRInput.Controller.RTrackedRemote);A controller touchpad touch occurs when the user’s finger makes contact with the touchpad without actively clicking it. Touches may be queried with OVRInput.Get(OVRInput.Touch.PrimaryTouchpad). Controller touchpad clicks are aliased to virtual button One clicks, and may be queried with OVRInput.Get(OVRInput.Button.PrimaryTouchpad).

The volume and home buttons are reserved on the Gear VR Controller. The Oculus button is reserved on the Oculus Go Controller.

## OVRInput Usage

The primary usage of OVRInput is to access controller input state through Get(), GetDown(), and GetUp().

* Get() queries the current state of a control.
* GetDown() queries if a control was pressed this frame.
* GetUp() queries if a control was released this frame.
### Gear VR and Go Controller Swiping Gestures

For Gear VR and Go Controllers, the user interface of your VR experience should follow these natural scrolling and swiping gestures:

* Swipe up: Pull content upward. Equivalent to scrolling down.
* Swipe down: Pull content downward. Equivalent to scrolling up.
* Swipe left: Pull content left or go to the next item or page. 
* Swipe right: Pull content right or go to the previous item or page.
### Control Input Enumerations

There are multiple variations of Get() that provide access to different sets of controls. These sets of controls are exposed through enumerations defined by OVRInput as follows:

ControlEnumeratesOVRInput.Button

Traditional buttons found on gamepads, Touch controllers, the Gear VR Controller touchpad and back button, the Gear VR headset touchpad and back button, and the Oculus Go Controller touchpad and back button.

OVRInput.Touch

Capacitive-sensitive control surfaces found on the Oculus Touch, Oculus Go Controller, and Gear VR Controller.

OVRInput.NearTouch

Proximity-sensitive control surfaces found on the Oculus Touch controllers.

OVRInput.Axis1D

One-dimensional controls such as triggers that report a floating point state.

OVRInput.Axis2D

Two-dimensional controls including thumbsticks, the Gear VR Controller touchpad, and the Oculus Go Controller touchpad. Report a Vector2 state.

A secondary set of enumerations mirror the first, defined as follows:

OVRInput.RawButton

OVRInput.RawTouch

OVRInput.RawNearTouch

OVRInput.RawAxis1D

OVRInput.RawAxis2D

The first set of enumerations provides a virtualized input mapping that is intended to assist developers with creating control schemes that work across different types of controllers. The second set of enumerations provides raw unmodified access to the underlying state of the controllers. We recommend using the first set of enumerations, since the virtual mapping provides useful functionality, as demonstrated below.

### Button, Touch, and NearTouch

In addition to traditional gamepad buttons, the Oculus Touch controllers feature capacitive-sensitive control surfaces which detect when the user's fingers or thumbs make physical contact (a “touch”), as well as when they are in close proximity (a “near touch”). This allows for detecting several distinct states of a user’s interaction with a specific control surface. For example, if a user’s index finger is fully removed from a control surface, the NearTouch for that control will report false. As the user’s finger approaches the control and gets within close proximity to it, the NearTouch will report true prior to the user making physical contact. When the user makes physical contact, the Touch for that control will report true. When the user pushes the index trigger down, the Button for that control will report true. These distinct states can be used to accurately detect the user’s interaction with the controller and enable a variety of control schemes.

The Gear VR Controller touchpad may be queried for both touch status and click status, where “touch” refers to the user’s finger making contact with the touchpad without actively clicking it.

### Example Usage

// returns true if the primary button (typically “A”) is currently pressed. OVRInput.Get(OVRInput.Button.One); // returns true if the primary button (typically “A”) was pressed this frame. OVRInput.GetDown(OVRInput.Button.One); // returns true if the “X” button was released this frame. OVRInput.GetUp(OVRInput.RawButton.X); // returns a Vector2 of the primary (typically the Left) thumbstick’s current state. // (X/Y range of -1.0f to 1.0f) OVRInput.Get(OVRInput.Axis2D.PrimaryThumbstick); // returns true if the primary thumbstick is currently pressed (clicked as a button) OVRInput.Get(OVRInput.Button.PrimaryThumbstick); // returns true if the primary thumbstick has been moved upwards more than halfway. // (Up/Down/Left/Right - Interpret the thumbstick as a D-pad). OVRInput.Get(OVRInput.Button.PrimaryThumbstickUp); // returns a float of the secondary (typically the Right) index finger trigger’s current state. // (range of 0.0f to 1.0f) OVRInput.Get(OVRInput.Axis1D.SecondaryIndexTrigger); // returns a float of the left index finger trigger’s current state. // (range of 0.0f to 1.0f) OVRInput.Get(OVRInput.RawAxis1D.LIndexTrigger); // returns true if the left index finger trigger has been pressed more than halfway. // (Interpret the trigger as a button). OVRInput.Get(OVRInput.RawButton.LIndexTrigger); // returns true if the secondary gamepad button, typically “B”, is currently touched by the user. OVRInput.Get(OVRInput.Touch.Two); // returns true after a Gear VR touchpad tap OVRInput.GetDown(OVRInput.Button.One); // returns true on the frame when a user’s finger pulled off Gear VR touchpad controller on a swipe down OVRInput.GetDown(OVRInput.Button.DpadDown); // returns true the frame AFTER user’s finger pulled off Gear VR touchpad controller on a swipe right OVRInput.GetUp(OVRInput.RawButton.DpadRight); // returns true if the Gear VR back button is pressed OVRInput.Get(OVRInput.Button.Two); // Returns true if the the Gear VR Controller trigger is pressed down OVRInput.Get(OVRInput.Button.PrimaryIndexTrigger); // Queries active Gear VR Controller touchpad click position // (normalized to a -1.0, 1.0 range, where -1.0, -1.0 is the lower-left corner) OVRInput.Get(OVRInput.Axis2D.PrimaryTouchpad, OVRInput.Controller.RTrackedRemote); // If no controller is specified, queries the touchpad position of the active Gear VR Controller OVRInput.Get(OVRInput.Axis2D.PrimaryTouchpad); // returns true if the Gear VR Controller back button is pressed OVRInput.Get(OVRInput.Button.Back); // recenters the active Gear VR Controller. Has no effect for other controller types. OVRInput.RecenterController(); // recenters right Gear VR Controller (even if it is not active) OVRInput.RecenterController(Controller.RTrackedRemote); // returns true on the frame when a user’s finger pulled off Gear VR Controller back button OVRInput.GetDown(OVRInput.Button.Back);In addition to specifying a control, Get() also takes an optional controller parameter. The list of supported controllers is defined by the OVRInput.Controller enumeration (for details, refer to **OVRInput** in the [Unity Scripting Reference](/documentation/unity/latest/concepts/unity-reference-scripting/ "The Unity Scripting Reference contains detailed information about the data structures and files included with the Utilities and Legacy Integration packages.").

Specifying a controller can be used if a particular control scheme is intended only for a certain controller type. If no controller parameter is provided to Get(), the default is to use the Active controller, which corresponds to the controller that most recently reported user input. For example, a user may use a pair of Oculus Touch controllers, set them down, and pick up an Xbox controller, in which case the Active controller will switch to the Xbox controller once the user provides input with it. The current Active controller can be queried with OVRInput.GetActiveController() and a bitmask of all the connected Controllers can be queried with OVRInput.GetConnectedControllers().

Example Usage:

// returns true if the Xbox controller’s D-pad is pressed up. OVRInput.Get(OVRInput.Button.DpadUp, OVRInput.Controller.Gamepad); // returns a float of the Hand Trigger’s current state on the Left Oculus Touch controller. OVRInput.Get(OVRInput.Axis1D.PrimaryHandTrigger, OVRInput.Controller.Touch); // returns a float of the Hand Trigger’s current state on the Right Oculus Touch controller. OVRInput.Get(OVRInput.Axis1D.SecondaryHandTrigger, OVRInput.Controller.Touch);Querying the controller type can also be useful for distinguishing between equivalent buttons on different controllers. For example, if you want code to execute on input from a gamepad or Touch controller, but not on a Gear VR Touchpad, you could implement it as follows:

if (OVRInput.GetActiveController() != OVRInput.Controller.Touchpad) { /* do input handling */ }Note that the Oculus Touch controllers may be specified either as the combined pair (with OVRInput.Controller.Touch), or individually (with OVRInput.Controller.LTouch and RTouch). This is significant because specifying LTouch or RTouch uses a different set of virtual input mappings that allow more convenient development of hand-agnostic input code. See the virtual mapping diagrams in [Touch Input Mapping](/documentation/unity/latest/concepts/unity-ovrinput/#unity-ovrinput-touch) for an illustration.

Example Usage:

// returns a float of the Hand Trigger’s current state on the Left Oculus Touch controller. OVRInput.Get(OVRInput.Axis1D.PrimaryHandTrigger, OVRInput.Controller.LTouch); // returns a float of the Hand Trigger’s current state on the Right Oculus Touch controller. OVRInput.Get(OVRInput.Axis1D.PrimaryHandTrigger, OVRInput.Controller.RTouch);This can be taken a step further to allow the same code to be used for either hand by specifying the controller in a variable that is set externally, such as on a public variable in the Unity Editor.

Example Usage:

// public variable that can be set to LTouch or RTouch in the Unity Inspector public Controller controller; … // returns a float of the Hand Trigger’s current state on the Oculus Touch controller // specified by the controller variable. OVRInput.Get(OVRInput.Axis1D.PrimaryHandTrigger, controller); // returns true if the primary button (“A” or “X”) is pressed on the Oculus Touch controller // specified by the controller variable. OVRInput.Get(OVRInput.Button.One, controller); This is convenient since it avoids the common pattern of if/else checks for Left/Right hand input mappings.

## OVRInput Haptics

Use SetControllerVibration() provided in OVRInput to start and stop haptics for the controller. Expected values for amplitude and frequency are between 0-1. The greater the value, the stronger or more frequent the vibration in the controller. To end the vibration, set both amplitude and frequency to 0. Controller vibration automatically end 2 seconds after the last input. See the OVRInput reference in the [Unity Scripting Reference](/documentation/unity/latest/concepts/unity-reference-scripting/ "The Unity Scripting Reference contains detailed information about the data structures and files included with the Utilities and Legacy Integration packages.") for more information. 

Note: If you're designing your app for Touch, consider using the updated [OVRHaptics for Oculus Touch](/documentation/unity/latest/concepts/unity-ovrhaptics/ "This guide reviews OVRHaptics and OVRHapticsClip, two C# scripts that programmatically control haptics feedback for Touch.") instead.## Touch Input Mapping

The following diagrams illustrate common input mappings for Oculus Touch controllers. For more information on additional mappings that are available, refer to **OVRInput** in the [Unity Scripting Reference](/documentation/unity/latest/concepts/unity-reference-scripting/ "The Unity Scripting Reference contains detailed information about the data structures and files included with the Utilities and Legacy Integration packages.").

### Virtual Mapping (Accessed as a Combined Controller)

When accessing the Touch controllers as a combined pair with OVRInput.Controller.Touch, the virtual mapping closely matches the layout of a typical gamepad split across the Left and Right hands.

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-0.png)  
### Virtual Mapping (Accessed as Individual Controllers)

When accessing the Left or Right Touch controllers individually with OVRInput.Controller.LTouch or OVRInput.Controller.RTouch, the virtual mapping changes to allow for hand-agnostic input bindings. For example, the same script can dynamically query the Left or Right Touch controller depending on which hand it is attached to, and Button.One will be mapped appropriately to either the A or X button.

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-1.png)  
### Raw Mapping

The raw mapping directly exposes the Touch controllers. The layout of the Touch controllers closely matches the layout of a typical gamepad split across the Left and Right hands.

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-2.png)  
## Rift Remote Input Mapping

### Virtual Mapping

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-3.png)  
### Raw Mapping

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-4.png)  
## Xbox Input Handling

### Virtual Mapping

This diagram shows a common implementation of Xbox controller input bindings using OVRInput.Controller.Gamepad.

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-5.png)  
### Raw Mapping

The raw mapping directly exposes the Xbox controller.

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-6.png)  
## Gear VR Controller Input Handling

For a discussion of best practices, see [Gear VR Controller Best Practices](/design/latest/concepts/bp-userinput/) in Oculus Best Practices.

### Virtual Mapping

This diagram shows a common implementation of Gear VR Controller input bindings using OVRInput.Controller.RTrackedRemote.

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-7.png)  
### Raw Mapping

The raw mapping directly exposes the Gear VR Controller. Note that this assumes a right-handed controller.

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-8.png)  
## Oculus Go Controller Input Handling

For a discussion of best practices, see [User Input Best Practices](/design/latest/concepts/bp-userinput/) in Oculus Best Practices.

### Virtual Mapping

This diagram shows a common implementation of Oculus Go Controller input bindings using OVRInput.Controller.RTrackedRemote.

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-9.png)  
### Raw Mapping

The raw mapping directly exposes the Oculus Go Controller. Note that this assumes a right-handed controller.

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-10.png)  
## Gear VR Headset Input Handling

There are special considerations when handling Gear VR headset input in regard to how queries work and headset touchpad input behavior.

When handling Gear VR headset touchpad input, queries work differently than on other controllers. Both Get() and GetDown() return true on the frame that the user’s finger is released from the headset touchpad, and GetUp() returns true on the next frame.

OVRInput.Button is normally used when querying traditional buttons and Oculus Go and Gear VR Controller touchpad clicks. Since the Gear VR headset touchpad can be touched, but not pressed like a button or clicked, there can be confusion on whether OVRInput.Button or OVRInput.Touch should be used for certain input events. The following information on when to use each also applies to OVRInput.RawButton and OVRInput.RawTouch, respectively.

To query for taps on the Gear VR headset touchpad, use OVRInput.Button.One. Queries on OVRInput.Button.One report true only when the user lifts their finger on completion of a zero-length swipe (tap). This is because the headset touchpad is unable to distinguish a non-zero-length swipe from a tap until the user releases their finger, and also because false positives could be generated by swipes if taps were reported on initial contact.

To query for swipes, use OVRInput.Button along with the desired direction (Up/Down/Left/Right or DpadUp/DpadDown/DpadLeft/DpadRight). Like taps, swipes are not reported until the user releases their finger.

To query for Back button presses, use OVRInput.Button.Two. Reporting behavior is similar to other Gear VR headset OVRInput.Button input events. Note that a Back button long-press is reserved and automatically handled by the Gear VR VrApi. For more information, see [Reserved User Interactions](/documentation/mobilesdk/latest/concepts/mobile-umenu-intro/) in our Mobile SDK Developer Guide.

To query on whether the user’s finger is on the headset touchpad, use OVRInput.Touch.One. Unlike OVRInput.Button, queries on OVRInput.Touch.One immediately report true when the user’s finger makes contact with the headset touchpad.

### Virtual Mapping

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-11.png)  
### Raw Mapping

![](/images/documentation-unity-latest-concepts-unity-ovrinput-unity-ovrinput-12.png)  
