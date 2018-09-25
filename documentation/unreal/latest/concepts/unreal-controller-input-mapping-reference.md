---
title: Mapping Oculus Controller Input to Blueprint Events
---
This reference section describes how Oculus controller actions (such as thumbstick presses) map to the corresponding events that can be handled via blueprints.

## Overview

When a user invokes an action on the Oculus Touch, Oculus Go controller, or Gear VR controller, such as pressing a button, your application can handle the resulting events by using the blueprints described in this section. 

The most common controller actions can be accessed via the standard Unreal MotionController API. These types of controller input tend to be supported across VR platforms from difference vendors. 

In addition, Oculus provides several Oculus-specific controller actions. For example, the Oculus Touch (L) Thumb Up CapTouch event uses a capacitive touch sensor to measure how far the user's thumb is from the thumbstick. The Oculus-specific events can be accessed via the Oculus-specific blueprints. 

Both the Unreal MotionController blueprints and the Oculus-specific blueprints are covered in the following reference sections.

Note: The Oculus Go and GearVR controllers work in ways that are fundamentally the same. The two controllers have the same number of buttons and the same layout, by design, so that you can develop applications that easily work on both controllers. Please note, however, that the Oculus Go controller has a trigger, which is not present on the Gear VR controller. However, from a technical point of view, Oculus Go and Gear VR are a single platform: the store is the same, and the APK is the same, by design. The Oculus Store actually does not allow dual APKs for an application that targets both the Oculus Go and the Gear VR. Such applications must consist of only one APK. For example, an application may not target Vulkan on Oculus Go, and GLES on Gear VR, since the choice between these two rendering systems is determined by setting that applies to the entire APK, and it must be the same APK across the entire application.## Oculus Go Controller

Oculus Go Action

Blueprint Event

Thumbstick touch, press, and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-0.png)  
* MotionController (L) Thumbstick - The thumbstick Pressed and Released events, if the Oculus Go controller is associated with the left hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-1.png)  

* MotionController (R) Thumbstick - The thumbstick Pressed and Released events, if the Oculus Go controller is associated with the right hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-2.png)  

* Oculus Touch (L) Thumbstick CapTouch - The thumbstick capacitive touch event, if the Oculus Go controller is associated with the left hand. The Axis Value returns 1 if the user is touching the thumbstick, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-3.png)  

* Oculus Touch (R) Thumbstick CapTouch - The thumbstick capacitive touch event, if the Oculus Go controller is associated with the right hand. The Axis Value returns 1 if the user is touching the thumbstick, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-4.png)  

Trigger press and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-5.png)  
* MotionController (L) Trigger - The trigger Pressed and Released events, if the Oculus Go controller is associated with the left hand ![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-6.png)  

* MotionController (R) Trigger - The trigger Pressed and Released events, if the Oculus Go controller is associated with the right hand ![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-7.png)  

Back button touch, press, and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-8.png)  
* MotionController (L) FaceButton1 - The Back button Pressed and Released events, if the Oculus Go controller is associated with the left hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-9.png)  

* MotionController (R) FaceButton1 - The Back button Pressed and Released events, if the Oculus Go controller is associated with the right hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-10.png)  

Thumbstick click and release actions at the 12:00 position

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-11.png)  
* MotionController (L) Thumbstick Up - The thumbstick 12:00 position Pressed and Released events, if the Oculus Go controller is associated with the left hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-12.png)  

* MotionController (R) Thumbstick Up - The thumbstick 12:00 position Pressed and Released events, if the Oculus Go controller is associated with the right hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-13.png)  

Thumbstick click and release actions at the 6:00 position

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-14.png)  
* MotionController (L) Thumbstick Down - The thumbstick 6:00 position Pressed and Released events, if the Oculus Go controller is associated with the left hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-15.png)  

* MotionController (R) Thumbstick Down - The thumbstick 6:00 position Pressed and Released events, if the Oculus Go controller is associated with the right hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-16.png)  

Thumbstick click and release actions at the 9:00 position

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-17.png)  
* MotionController (L) Thumbstick Left - The thumbstick 9:00 position Pressed and Released events, if the Oculus Go controller is associated with the left hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-18.png)  

* MotionController (R) Thumbstick Left - The thumbstick 9:00 position Pressed and Released events, if the Oculus Go controller is associated with the right hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-19.png)  

Thumbstick click and release actions at the 3:00 position

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-20.png)  
* MotionController (L) Thumbstick Right - The thumbstick 3:00 position Pressed and Released events, if the Oculus Go controller is associated with the left hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-21.png)  

* MotionController (R) Thumbstick Right - The thumbstick 3:00 position Pressed and Released events, if the Oculus Go controller is associated with the right hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-22.png)  

## Oculus Touch

Oculus Touch Action

Blueprint Event

Thumbstick touch, press, and thumb up actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-23.png)  
* MotionController (L) Thumbstick - The left controller thumbstick Pressed and Released events. In order for the Pressed event to fire, the thumbstick must be pressed to the point of clicking.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-24.png)  

* MotionController (R) Thumbstick - The right controller thumbstick Pressed and Released events. In order for the Pressed event to fire, the thumbstick must be pressed to the point of clicking.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-25.png)  

* Oculus Touch (L) Thumbstick CapTouch - The left controller thumbstick capacitive touch event. The Axis Value returns 1 if the user is touching the thumbstick, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-26.png)  

* Oculus Touch (R) Thumbstick CapTouch - The right controller thumbstick capacitive touch event. The Axis Value returns 1 if the user is touching the thumbstick, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-27.png)  

* Oculus Touch (L) Thumb Up CapTouch - The left controller thumbstick capacitive touch event. The Axis Value returns a floating point value, from 0.0 to 1.0, that expresses how far the user's thumb is from the thumbstick, where 0.0 is as close as possible, and 1.0 is as far away as can be measured by the thumbstick. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-28.png)  

* Oculus Touch (R) Thumb Up CapTouch - The right controller thumbstick capacitive touch event. The Axis Value returns a floating point value, from 0.0 to 1.0, that expresses how far the user's thumb is from the thumbstick, where 0.0 is as close as possible, and 1.0 is as far away as can be measured by the thumbstick. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-29.png)  

Trigger touch, press, release, and pointing finger actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-30.png)  
* MotionController (L) Trigger - The left controller trigger Pressed and Released events. ![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-31.png)  

* MotionController (R) Trigger - The right controller trigger Pressed and Released events. ![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-32.png)  

* Oculus Touch (L) Trigger CapTouch - The left controller trigger capacitive touch event. The Axis Value returns 1 if the user is touching the trigger, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time. ![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-33.png)  

* Oculus Touch (R) Trigger CapTouch - The right controller trigger capacitive touch event. The Axis Value returns 1 if the user is touching the trigger, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time. ![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-34.png)  

* Oculus Touch (L) Pointing CapTouch - The left controller pointing capacitive touch event. The Axis Value returns a floating point value, from 0.0 to 1.0, that expresses how far away the user's finger is pointing from the trigger, where 0.0 is as close as possible, and 1.0 is as far away as can be measured by the trigger. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time. ![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-35.png)  

* Oculus Touch (R) Pointing CapTouch - The right controller pointing capacitive touch event. The Axis Value returns a floating point value, from 0.0 to 1.0, that expresses how far away the user's finger is pointing from the trigger, where 0.0 is as close as possible, and 1.0 is as far away as can be measured by the trigger. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-36.png)  

Grip press and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-37.png)  
* MotionController (L) Grip1 - The left controller grip Pressed and Released events.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-38.png)  

* MotionController (R) Grip1 - The right controller grip Pressed and Released events.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-39.png)  

X or A button press and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-40.png)  
* MotionController (L) FaceButton1 - The left controller X button Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-41.png)  

* MotionController (R) FaceButton1 - The right controller A button Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-42.png)  

* Oculus Touch (L) X Button CapTouch - The left controller X button capacitive touch event. The Axis Value returns 1 if the user is touching the X button, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time. ![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-43.png)  

* Oculus Touch (R) A Button CapTouch - The right controller A button capacitive touch event. The Axis Value returns 1 if the user is touching the A button, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time. ![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-44.png)  

Y or B button press and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-45.png)  
* MotionController (L) FaceButton2 - The left controller Y button Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-46.png)  

* MotionController (R) FaceButton2 - The right controller B button Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-47.png)  

* Oculus Touch (L) Y Button CapTouch - The left controller Y button capacitive touch event. The Axis Value returns 1 if the user is touching the Y button, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time. ![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-48.png)  

* Oculus Touch (R) B Button CapTouch - The right controller B button capacitive touch event. The Axis Value returns 1 if the user is touching the B button, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time. ![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-49.png)  

Thumbstick up press and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-50.png)  
* MotionController (L) Thumbstick Up - The left controller Thumbstick Up Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-51.png)  

* MotionController (R) Thumbstick Up - The right controller Thumbstick Up Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-52.png)  

Thumbstick down press and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-53.png)  
* MotionController (L) Thumbstick Down - The left controller Thumbstick Down Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-54.png)  

* MotionController (R) Thumbstick Down - The right controller Thumbstick Down Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-55.png)  

Thumbstick left press and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-56.png)  
* MotionController (L) Thumbstick Left - The left controller Thumbstick Left Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-57.png)  

* MotionController (R) Thumbstick Left - The right controller Thumbstick Left Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-58.png)  

Thumbstick right press and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-59.png)  
* MotionController (L) Thumbstick Right - The right controller Thumbstick Right Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-60.png)  

* MotionController (R) Thumbstick Right - The right controller Thumbstick Right Pressed and Released events![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-61.png)  

## Gear VR Controller

Gear VR Controller Action

Blueprint Event

Thumbstick touch, press, and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-62.png)  
* MotionController (L) Thumbstick - The thumbstick Pressed and Released events, if the Gear VR controller is associated with the left hand.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-63.png)  

* MotionController (R) Thumbstick - The thumbstick Pressed and Released events, if the Gear VR controller is associated with the right hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-64.png)  

* Oculus Touch (L) Thumbstick CapTouch - The thumbstick capacitive touch event, if the Gear VR controller is associated with the left hand. The Axis Value returns 1 if the user is touching the thumbstick, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-65.png)  

* Oculus Touch (R) Thumbstick CapTouch - The thumbstick capacitive touch event, if the Gear VR controller is associated with the right hand. The Axis Value returns 1 if the user is touching the thumbstick, and 0 otherwise. This event fires once per frame, when input is enabled for the containing actor. Note: There is also a corresponding gamepad value blueprint (with the same name) that can be explicitly retrieved at any time.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-66.png)  

Back button touch, press, and release actions

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-67.png)  
* MotionController (L) FaceButton1 - The Back button Pressed and Released events, if the Gear VR controller is associated with the left hand.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-68.png)  

* MotionController (R) FaceButton1 - The Back button Pressed and Released events, if the Gear VR controller is associated with the right hand.![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-69.png)  

Thumbstick click and release actions at the 12:00 position

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-70.png)  
* MotionController (L) Thumbstick Up - The thumbstick 12:00 position Pressed and Released events, if the Gear VR controller is associated with the left hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-71.png)  

* MotionController (R) Thumbstick Up - The thumbstick 12:00 position Pressed and Released events, if the Gear VR controller is associated with the right hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-72.png)  

Thumbstick click and release actions at the 6:00 position

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-73.png)  
* MotionController (L) Thumbstick Down - The thumbstick 6:00 position Pressed and Released events, if the Gear VR controller is associated with the left hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-74.png)  

* MotionController (R) Thumbstick Down - The thumbstick 6:00 position Pressed and Released events, if the Gear VR controller is associated with the right hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-75.png)  

Thumbstick click and release actions at the 9:00 position

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-76.png)  
* MotionController (L) Thumbstick Left - The thumbstick 9:00 position Pressed and Released events, if the Gear VR controller is associated with the left hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-77.png)  

* MotionController (R) Thumbstick Left - The thumbstick 9:00 position Pressed and Released events, if the Gear VR controller is associated with the right hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-78.png)  

Thumbstick click and release actions at the 3:00 position

![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-79.png)  
* MotionController (L) Thumbstick Right - The thumbstick 3:00 position Pressed and Released events, if the Gear VR controller is associated with the left hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-80.png)  

* MotionController (R) Thumbstick Right - The thumbstick 3:00 position Pressed and Released events, if the Gear VR controller is associated with the right hand![](/images/documentation-unreal-latest-concepts-unreal-controller-input-mapping-reference-81.png)  

