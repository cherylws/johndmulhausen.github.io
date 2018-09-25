---
title: Using the controller
---
You can use window.navigator.getGamepads() to query for the Oculus Go controller, the Gear VR gamepad, and any Bluetooth gamepads.

 On Oculus Go devices, the controller is exposed as a gamepad with a Gamepad.id property of "Oculus Go Controller".

On Gear VR devices, the controller is exposed as a gamepad with the Gamepad.id property of "Gear VR".

Rendering the correct controller model and position is vital to help with user immersion. 

Gamepad.hand returns which hand the controller is held in; always draw the controller in the correct location.

The [Mobile SDK](http://developer.prod.oculus.com/downloads/package/oculus-mobile-sdk/) has a great example (OVR\_ArmModel.cpp) of an arm model that can be used for 3DoF controllers such as the Gear VR and Oculus Go controllers.

var state = { lastButtons: {}, lastAxes: {} }; Array.prototype.forEach.call(navigator.getGamepads(), function (activePad, padIndex) { if (activePad.connected) { if (activePad.id.includes("Gear VR")) { // Process buttons and axes for the Gear VR touch panel activePad.buttons.forEach(function (gamepadButton, buttonIndex) { if (buttonIndex === 0 && gamepadButton.pressed && !lastButtons[buttonIndex]) { // Handle tap } state.lastButtons[buttonIndex] = gamepadButton.pressed; }); activePad.axes.forEach(function (axisValue, axisIndex) { if (axisIndex === 0 && axisValue < 0 && lastAxes[axisIndex] >= 0) { // Handle swipe right } else if (axisIndex === 0 && axisValue > 0 && lastAxes[axisIndex] <= 0) { // Handle swipe left } else if (axisIndex === 1 && axisValue < 0 && lastAxes[axisIndex] >= 0) { // Handle swipe up } else if (axisIndex === 1 && axisValue > 0 && lastAxes[axisIndex] <= 0) { // Handle swipe down } state.lastAxes[axisIndex] = axisValue; }); } else { // This is a connected Bluetooth gamepad which you may want to support in your VR experience } } });The Gear VR gamepadâ€™s button 0 will press for a short time whenever the user taps the touchpad. There are also two axes on the gamepad, which always have the value of 0, 1, or -1. The following table indicates how these values map to swipes.

AxisIf Value = 1If Value = -10Swipe leftSwipe right1Swipe downSwipe upBy recording the last button press state and last axis value you can detect when the corresponding action occurs. Try out an interactive Gamepad sample which demonstrates the Gear VR gamepad values in VR [here](https://s3.amazonaws.com/static.oculus.com/carmel/WebVRSamples/Gamepad/index.html).

