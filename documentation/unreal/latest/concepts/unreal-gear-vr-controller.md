---
title: Gear VR Controller and Headset Touchpad
---
The Gear VR Controller is an orientation-tracked input device that can be accessed through standard Unreal Blueprints, and through Oculus-specific Blueprints. The Gear VR Touchpad is mounted on the side of the headset, and can be accessed via Oculus-specific Blueprints.

## Handling Controller Input with Blueprints

Your application can use Blueprints to access every input event generated by the Gear VR controller. For a full description of these blueprints, please see [Mapping Oculus Controller Input to Blueprint Events](/documentation/unreal/latest/concepts/unreal-controller-input-mapping-reference/ "This reference section describes how Oculus controller actions (such as touchpad presses) map to the corresponding events that can be handled via blueprints.").

## Best Practices for Controller Usage

For a discussion of best practices for the Gear VR controller, see [Gear VR Controller Best Practices](/blog/gear-vr-controller-best-practices/).

For instructions on how to add a Motion Controller component to your Pawn or Character, see [Motion Controller Component Setup](https://docs.unrealengine.com/latest/INT/Platforms/VR/MotionController/) in Epic’s Unreal documentation. Epic has also provided a detailed training tutorial called [Setting Up VR Motion Controllers](https://docs.unrealengine.com/latest/INT/Videos/PLZlv_N0_O1gY7G589Z3I5-Dz7AdFSIWaG/6ALnsdQnkVQ/). 

The Gear VR locates the controller relative to the user by using a body model to estimate the controller’s position. Whether the controller is visualized on the left or right side of the body is determined by left-handedness versus right-handedness, which is specified by users during controller pairing.

Orientation tracking is handled automatically by the Motion Controller Component. If you need to query the controller orientation, you can query the Motion Controller rotation.

Motion Controller Components must be specified as either left or right controllers when they are added, and each Gear VR controller button mapping has a left/right equivalent. However, any button click sends both left and right events, so the setting you choose when you add the Motion Controller component has no effect.

## Input Sample

You will find an example of the Gear VR controller input in our Input sample available in the directory <install>/Samples/Oculus. Please see the sample and its Level Blueprint for a full illustration of how to use the controller in your game, including the button mappings. 

## Gear VR Touchpad Integration

The Gear VR touchpad is located on the side of the headset. The following Blueprints facilitate adding the Gear VR touchpad integration into your applications:

![](/images/documentation-unreal-latest-concepts-unreal-gear-vr-controller-0.png)  
The Gamepad Events include:

* Oculus Touchpad Back: The user pressed the Back button on the touchpad.
* Oculus Touchpad Press: The user pressed down on the thumbpad of the touchpad.
* Oculus Touchpad X-Axis: This event is generated when the user presses down on the touchpad. It provides the X-Axis value for the finger's position on the touchpad.
* Oculus Touchpad Y-Axis: This event is generated when the user presses down on the touchpad. It provides the Y-Axis value for the finger's position on the touchpad.
Use the following workflow when adding Gamepad Events and Gamepad Values to your applications:

![](/images/documentation-unreal-latest-concepts-unreal-gear-vr-controller-1.png)  
You should only call Get Oculus Touchpad X-Axis / Y-Axis between the Pressed and Released events.## Gear VR Controller Swiping Gestures

For the Gear VR controller, the user interface of your VR experience should follow these natural scrolling and swiping gestures:

* Swipe up: Pull content upward. Equivalent to scrolling down.
* Swipe down: Pull content downward. Equivalent to scrolling up.
* Swipe left: Pull content left or go to the next item or page. 
* Swipe right: Pull content right or go to the previous item or page.