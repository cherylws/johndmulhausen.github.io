---
title: 3D Visualizer
---
This guide describes how to install and use the Oculus Spatializer VST plugin with the Oculus Rift.

The Oculus 3D Audio Visualizer with HMD interface allows users to optionally visualize and manipulate sound parameters within VR, using either Oculus Touch or Xbox controllers.

Using Touch, a user can control two sounds at the same time.

The sound locations of all Visualizer channels are visible with the HMD display. Users can change the position of sounds relative to the listener, adjust volume attenuation parameters, and enable/disable room and wall parameters within VR.

## Use

Note: Be sure your Oculus Rift software and firmware are up to date and running properly.To start visualization of the VST parameters within the HMD, add a plugin to a track/channel.

![](/images/documentation-audiosdk-latest-concepts-os-vst-visualizer-0.png)  
And then, put on the HMD.

![](/images/documentation-audiosdk-latest-concepts-os-vst-visualizer-1.png)  
The Touch controllers are visualized as blue (left controller) and red (right controller) spheres which track with controller movement. The Xbox controller may be visualized as a selection sphere directly in front of the user by squeezing the left trigger - it is stationary, as the controller is not tracked.

Squeezing the trigger on your controller initiates the selection pointers. Some settings increase in intensity as you squeeze the trigger.

The Reset Rift button found in the Config window returns you to your initial position. If you move away from the audio track sources and want to ’teleport’ back to the center of the audio space, use this button.

Use the Label field and Color picker tool in the Config Window to assign a label and color to the currently-selected instance of the spatializer. This is used to differentiate each audio source within the HMD.

A beats-per-minute (BPM) metronome sphere is located at the center of origin. Above the sphere is a message that indicates the current BPM and the current DAW measure:beat.

## Moving the Camera

The sticks on the controllers control movement within the audio space.

The left joystick moves your camera parallel to your viewing direction. The x-axis of the right joystick rotates you around the y-axis. The y-axis of the right joystick moves the camera up or down.

Left Stick

Pan left and right, move forwards and back.

Right Stick

Pan up and down, rotate left and right.

## Modifying Audio Track Objects

Audio sources are initially displayed as yellow spheres in the HMD which modulate (or pulse) while audio is on.

To select a sound, squeeze the trigger. If you are using a Touch controller, squeezing the trigger activates a laser beam you use to lock onto a source. If you are using the Xbox controller, a green sphere cursor will display at the center of the screen, which can be used to lock onto a source.

After you lock onto a source, squeeze the grip to move it around and position it.

Partial squeezes of the trigger cause the track to lag towards the position that it is being placed in. This can be used for smooth sound movement (for example, if you want to have softer curves when automating location).

Press the Stick on the Touch controller or the left joystick on the Xbox controller to cycle through the available setting controls. To change parameters, you must keep the index trigger squeezed to keep the object captured.

The first setting adjusts sound fall-off. Two spheres, each representing the near/far fall-off value, will appear. Your controller controls the values of each sphere and will no longer control the camera. The x-axis changes the near fall-off, and the y-axis changes the far fall-off.

A floating message follows the direction of the selected sound, allowing user to see the actual parameter values.

Click on the joystick button again to cycle to distance and gain, the next parameter change mode.

Use joystick up/down to change distance - the sound will move closer or farther away from you.

Use joystick left/right to adjust gain - a green sphere will change representing the attenuation of the sound (-90/+24 db).

A floating message follows the direction of the selected sound, allowing user to see actual parameter values.

Press the Stick again to turn off parameter change mode, or release the Trigger to release the sound and return to movement mode.

## Modifying Room Reflection Parameters

Use the left Touch or Xbox controller.

The y button toggles reflections on/off and causes a dimly-colored grid cube to appear, representing the room. Each notch in the cube represents one meter. The x button enables reverb (brightly-colored).

If pressing the left trigger on either controller does not capture a sound but intersects with a room wall, that wall will turn bright green.

Clicking on the joystick will it in room parameter mode, and it will stop controlling the camera. The selected wall will turn white, and a solid transparent wall will overlay the wall grid. The intensity of the opacity on that wall represents the reflection coefficient value of that wall.

The joystick y-axis controls the size of the room. The x-axis controls the reflection coefficient. Note that you can select other walls without having to manually switch modes, provided the index finger is still down.

Click on the joystick button again to turn off room parameter mode, or release the index trigger to release the sound and return to movement mode.

## Automation

Automation is supported for audio position only. In your DAW, enable automation record (varies with each DAW) and move the sounds around using your controller of choice. The sequence will be recorded and can be played back. Automated sequences are stored with the DAW project.

