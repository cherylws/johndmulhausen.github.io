---
title: OVRInput
---

OVRInput exposes a unified input API for multiple controller types.

It may be used to query virtual or raw controller state, such as buttons, thumbsticks, triggers, and capacitive touch data. It currently supports the Oculus Touch and Microsoft Xbox controllers on desktop platforms. Gamepads compatible with Samsung Gear VR, such as the Samsung EI-GP20 and Moga Pro, must be Android compatible and support Bluetooth 3.0. For more details on supported mobile gamepad features, see [System and Hardware Requirements](/documentation/mobilesdk/latest/concepts/mobile-reqs/) in our Mobile SDK documentation.

When used with tracked controllers such as Oculus Touch, OVRInput also provides position and orientation data through `GetLocalControllerPosition()` and `GetLocalControllerRotation()`, which return a Vector3 and Quaternion, respectively.

Controller poses are returned by the constellation tracking system and are predicted simultaneously with the headset. These poses are reported in the same coordinate frame as the headset, relative to the initial center eye pose, and may be used for rendering hands or objects in the 3D world. They are also reset by `OVRManager.display.RecenterPose()`, similar to the head and eye poses.

OVRInput provides control of haptic vibration feedback on compatible controllers. For example, `SetControllerVibration()` sets vibration frequency and amplitude.

Mobile input bindings are now automatically added to InputManager.asset if they do not already exist. 

For more information, see **OVRInput** in the [Unity Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/). For more information on Unity’s input system and Input Manager, documented here: [http://docs.unity3d.com/Manual/Input.html](http://docs.unity3d.com/Manual/Input.html) and [http://docs.unity3d.com/ScriptReference/Input.html](http://docs.unity3d.com/ScriptReference/Input.html).

See OVRTouchpad.cs in Assets/OVR/Moonlight/Scripts for our interface class to the touchpad. The Gear VR HMD touchpad is not currently exposed by OVRInput.

## OVRInput Usage



The primary usage of OVRInput is to access controller input state through `Get()`, `GetDown()`, and `GetUp()`.

* Get() queries the current state of a control.
* GetDown() queries if a control was pressed this frame.
* GetUp() queries if a control was released this frame.


### Control Input Enumerations

There are multiple variations of `Get()` that provide access to different sets of controls. These sets of controls are exposed through enumerations defined by OVRInput as follows:

|      Control      |                                  Enumerates                                  |
|--------------------|-------------------------------------------------------------------------------|
|  OVRInput.Button  |    Traditional buttons found on gamepads and the Oculus Touch controllers.    |
|   OVRInput.Touch   | Capacitive-sensitive control surfaces found on the Oculus Touch controllers. |
| OVRInput.NearTouch |  Proximity-sensitive control surfaces found on the Oculus Touch controllers.  |
|  OVRInput.Axis1D  | One-dimensional controls such as triggers that report a floating point state. |
|  OVRInput.Axis2D  |   Two-dimensional controls such as thumbsticks that report a Vector2 state.   |

A secondary set of enumerations mirror the first, defined as follows:

|  OVRInput.RawButton  |
|-----------------------|
|   OVRInput.RawTouch   |
| OVRInput.RawNearTouch |
|  OVRInput.RawAxis1D  |
|  OVRInput.RawAxis2D  |

The first set of enumerations provides a virtualized input mapping that is intended to assist developers with creating control schemes that work across different types of controllers. The second set of enumerations provides raw unmodified access to the underlying state of the controllers. We recommend using the first set of enumerations, since the virtual mapping provides useful functionality, as demonstrated below.

### Button, Touch, and NearTouch

In addition to traditional gamepad buttons, the Oculus Touch controllers feature capacitive-sensitive control surfaces which detect when fingers make physical contact (a “touch”), as well as when they are in close proximity (a “near touch”). This allows for detecting several distinct states of a user’s interaction with a specific control surface. For example, if a user’s index finger is fully removed from a control surface, the NearTouch for that control will report false. As the user’s finger approaches the control and gets within close proximity to it, the NearTouch will report true prior to the user making physical contact. When the user makes physical contact, the Touch for that control will report true. When the user pushes the index trigger down, the Button for that control will report true. These distinct states can be used to accurately detect the user’s interaction with the controller and enable a variety of control schemes.

### More on Controls

Example Usage:

```
// returns true if the primary button (typically “A”) is currently pressed.
    OVRInput.Get(OVRInput.Button.One); 
    
    // returns true if the primary button (typically “A”) was pressed this frame.
    OVRInput.GetDown(OVRInput.Button.One); 
    
    // returns true if the “X” button was released this frame.
    OVRInput.GetUp(OVRInput.RawButton.X); 
    
    // returns a Vector2 of the primary (typically the Left) thumbstick’s current state. 
    // (X/Y range of -1.0f to 1.0f)
    OVRInput.Get(OVRInput.Axis2D.PrimaryThumbstick); 
    
    // returns true if the primary thumbstick is currently pressed (clicked as a button)
    OVRInput.Get(OVRInput.Button.PrimaryThumbstick); 
    
    // returns true if the primary thumbstick has been moved upwards more than halfway.  
    // (Up/Down/Left/Right - Interpret the thumbstick as a D-pad).
    OVRInput.Get(OVRInput.Button.PrimaryThumbstickUp); 
    
    // returns a float of the secondary (typically the Right) index finger trigger’s current state.  
    // (range of 0.0f to 1.0f)
    OVRInput.Get(OVRInput.Axis1D.SecondaryIndexTrigger); 
    
    // returns a float of the left index finger trigger’s current state.  
    // (range of 0.0f to 1.0f)
    OVRInput.Get(OVRInput.RawAxis1D.LIndexTrigger); 
    
    // returns true if the left index finger trigger has been pressed more than halfway.  
    // (Interpret the trigger as a button).
    OVRInput.Get(OVRInput.RawButton.LIndexTrigger); 
    
    // returns true if the secondary gamepad button, typically “B”, is currently touched by the user.
    OVRInput.Get(OVRInput.Touch.Two);
```

In addition to specifying a control, `Get()` also takes an optional controller parameter. The list of supported controllers is defined by the OVRInput.Controller enumeration (for details, refer to **OVRInput** in the [Unity Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/).

Specifying a controller can be used if a particular control scheme is intended only for a certain controller type. If no controller parameter is provided to `Get()`, the default is to use the `Active` controller, which corresponds to the controller that most recently reported user input. For example, a user may use a pair of Oculus Touch controllers, set them down, and pick up an Xbox controller, in which case the Active controller will switch to the Xbox controller once the user provides input with it. The current Active controller can be queried with `OVRInput.GetActiveController()` and a bitmask of all the connected Controllers can be queried with `OVRInput.GetConnectedControllers()`.

Example Usage:

```
// returns true if the Xbox controller’s D-pad is pressed up.
    OVRInput.Get(OVRInput.Button.DpadUp, OVRInput.Controller.Gamepad); 
    
    // returns a float of the Hand Trigger’s current state on the Left Oculus Touch controller.
    OVRInput.Get(OVRInput.Axis1D.PrimaryHandTrigger, OVRInput.Controller.Touch); 
    
    // returns a float of the Hand Trigger’s current state on the Right Oculus Touch controller.
    OVRInput.Get(OVRInput.Axis1D.SecondaryHandTrigger, OVRInput.Controller.Touch);
```

Note that the Oculus Touch controllers may be specified either as the combined pair (with `OVRInput.Controller.Touch`), or individually (with `OVRInput.Controller.LTouch` and `RTouch`). This is significant because specifying LTouch or RTouch uses a different set of virtual input mappings that allow more convenient development of hand-agnostic input code. See the virtual mapping diagrams in [Touch Input Mapping](/documentation/unity/latest/concepts/unity-ovrinput/#unity-ovrinput-touch) for an illustration.

Example Usage:

```
// returns a float of the Hand Trigger’s current state on the Left Oculus Touch controller.
    OVRInput.Get(OVRInput.Axis1D.PrimaryHandTrigger, OVRInput.Controller.LTouch);
    
    // returns a float of the Hand Trigger’s current state on the Right Oculus Touch controller.
    OVRInput.Get(OVRInput.Axis1D.PrimaryHandTrigger, OVRInput.Controller.RTouch);
```

This can be taken a step further to allow the same code to be used for either hand by specifying the controller in a variable that is set externally, such as on a public variable in the Unity Editor.

Example Usage:

```
// public variable that can be set to LTouch or RTouch in the Unity Inspector
    public Controller controller; 
    …
    // returns a float of the Hand Trigger’s current state on the Oculus Touch controller  
    // specified by the controller variable.
    OVRInput.Get(OVRInput.Axis1D.PrimaryHandTrigger, controller);
    
    // returns true if the primary button (“A” or “X”) is pressed on the Oculus Touch controller
    // specified by the controller variable.
    OVRInput.Get(OVRInput.Button.One, controller); 
```

This is convenient since it avoids the common pattern of if/else checks for Left/Right hand input mappings.

## Touch Input Mapping



The following diagrams illustrate common input mappings for Oculus Touch controllers. For more information on additional mappings that are available, refer to **OVRInput** in the [Unity Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/).

### Virtual Mapping (Accessed as a Combined Controller)

When accessing the Touch controllers as a combined pair with OVRInput.Controller.Touch, the virtual mapping closely matches the layout of a typical gamepad split across the Left and Right hands.

![](/images/documentationunitylatestconceptsunity-integration-ovrinput-0.png)

### Virtual Mapping (Accessed as Individual Controllers)

When accessing the Left or Right Touch controllers individually with OVRInput.Controller.LTouch or OVRInput.Controller.RTouch, the virtual mapping changes to allow for hand-agnostic input bindings. For example, the same script can dynamically query the Left or Right Touch controller depending on which hand it is attached to, and Button.One will be mapped appropriately to either the A or X button.

![](/images/documentationunitylatestconceptsunity-integration-ovrinput-1.png)

### Raw Mapping

The raw mapping directly exposes the Touch controllers. The layout of the Touch controllers closely matches the layout of a typical gamepad split across the Left and Right hands.

![](/images/documentationunitylatestconceptsunity-integration-ovrinput-2.png)

## Rift Remote Input Mapping



### Virtual Mapping

![](/images/documentationunitylatestconceptsunity-integration-ovrinput-3.png)

### Raw Mapping

![](/images/documentationunitylatestconceptsunity-integration-ovrinput-4.png)

## Xbox Input Handling



### Virtual Mapping

This diagram shows a common implementation of Xbox controller input bindings using OVRInput.Controller.Gamepad.

![](/images/documentationunitylatestconceptsunity-integration-ovrinput-5.png)

### Raw Mapping

The raw mapping directly exposes the Xbox controller.

![](/images/documentationunitylatestconceptsunity-integration-ovrinput-6.png)
