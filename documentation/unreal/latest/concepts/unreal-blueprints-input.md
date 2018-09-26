---
title: Input Blueprints
---

This section describes the blueprints that are used with input devices such as the Oculus Touch or the Oculus Go controller.

## Input Blueprints

The Input Blueprint provides a control interface for Touch, Oculus remote, and the Gear VR Controller.

*  Gamepad events
	+ return Oculus Remote button events (bool)
	+ return Oculus Touch button events (bool)
	![](/images/documentationunreallatestconceptsunreal-blueprints-input-0.png)


* Gamepad Values - return Oculus Touch values (floats) ![](/images/documentationunreallatestconceptsunreal-blueprints-input-1.png)




Gear VR Controller clickpad events are reported in the Input Blueprint as thumbstick events. A clickpad click is reported as a press followed by a release. You may query the x- and y-axis of the thumbstick to determine the location of clickpad presses. The Gear VR Controller Back button may be queried with Motion Controller Face Button 1.

The **Is Device Tracked?** Blueprint may be used to infer the handedness of a Gear VR Controller. If a connected input device returns true for Right Controller and false for Left Controller, it is a right-handed controller.

## Oculus Touch Haptics

The following Blueprints are not Oculus-specific, but may be used to control haptics for the Xbox or Oculus Touch controllers. For detailed information, see [Haptics for Rift Controllers](/documentation/unreal/latest/concepts/unreal-haptics/)

* Play Haptic Effect
* Stop Haptic Effect
* Set Haptics by Value
* Play Haptic Soundwave

