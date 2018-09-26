---
title: Controller Data
---

The Oculus SDK provides APIs that return the position and state for each Oculus Touch controller. 

This data is exposed through two locations:

* ovrTrackingState::HandPoses[2]—returns the pose and tracking state for each Oculus Touch controller.
* ovrInputState—structure returned by ovr\_GetInputState that contains the Oculus Touch button, joystick, trigger, and capacitive touch sensor state. 


The controller hand pose data is separated from the input state because it comes from a different system and is reported at separate points in time. Controller poses are returned by the constellation tracking system and are predicted simultaneously with the headset, based on the absolute time passed into GetTrackingState. Having both hand and headset data reported together provides a consistent snapshot of the system state. 
