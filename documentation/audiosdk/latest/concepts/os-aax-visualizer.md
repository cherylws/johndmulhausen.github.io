---
title: 3D Visualizer
---
This guide describes how to install and use the Oculus Spatializer AAX plugin with the Oculus Rift.

The Oculus 3D Audio Visualizer with HMD interface allows users to optionally visualize and manipulate sound parameters within VR, using either Oculus Touch or Xbox controllers.

Using Touch, a user can control two sounds at the same time.

The sound locations of all Visualizer channels are visible with the HMD display. Users can change the position of sounds relative to the listener, adjust volume attenuation parameters, and enable/disable room and wall parameters within VR.

## Use

Note: Be sure your Oculus Rift software and firmware are up to date and running properly.To begin visualization of the VST parameters within the HMD, add a plugin to a channel.

![](/images/documentation-audiosdk-latest-concepts-os-aax-visualizer-0.png)  
Touch controllers are visualized as blue (left controller) and red (right controller) spheres which track with controller movement. The Xbox controller may be visualized as a selection sphere directly in front of the user by pressing the left index trigger - it is stationary, as the controller is not tracked.

Use the index triggers to initiate a selection pointer. Some settings respond to the strength of the pointer (see below for details). The strength value is controlled by the amount the trigger is pressed.

The Reset Rift button found in the About window tears down and re-initializes the HMD and returns users to an initial position. If you move away from the sound sources and want to ’teleport’ back to the center of the audio space, use this button.

Press the Set Color button in the About window to bring up a color selector. This selector assigns the color to the sound location assigned to the currently-selected instance of the spatializer in the DAW. This is used to differentiate each sound within the HMD.

A beats-per-minute (BPM) metronome sphere is located at the center of origin. Above the sphere is a message that indicates the current BPM and the current DAW measure:beat.

## Moving the Camera

Movement within the audio space is controlled via joysticks on either the Xbox controller or Touch controllers:

The left joystick moves your camera parallel to your viewing direction. The x-axis of the right joystick rotates you around the y-axis. The y-axis of the right joystick moves the camera up or down.

## Modifying Sound Objects

Audio sources are initially displayed as yellow spheres in the HMD which modulate (or pulse) while audio is on.

To select a sound, squeeze the index-finger trigger. If you are using a Touch controller, a beam will shoot out that can be used to select a sound. If you are using the Xbox controller, a green sphere cursor will display at the center of the screen, which can be used to select a sound.

Once you have locked onto a sound, you may move it around to position it. The joystick will stop functioning as a camera controller.

Partially release the index-finger trigger to cause the sound to lag towards the position that it is being placed in. This can be used for smooth sound movement (e.g., if you want to have softer curves when automating location).

Click the joystick button of the Touch controller or the left joystick on the Xbox controller to cycle through the available setting controls. To change parameters, you must keep the index trigger pressed to keep the sound captured.

The first setting adjusts sound fall-off. Two spheres, each representing the near/far fall-off value, will appear. Your controller will now control the values of each sphere and will no longer control the camera. The x-axis changes the near fall-off, and the y-axis changes the far fall-off.

A floating message follows the direction of the selected sound, allowing user to see the actual parameter values.

Click on the joystick button again to cycle to distance and gain, the next parameter change mode.

Use joystick up/down to change distance - the sound will move closer or farther away from you.

Use joystick left/right to adjust gain - a green sphere will change representing the attenuation of the sound (-90/+24 db).

A floating message will follow the direction of the selected sound, allowing user to see actual parameter values.

Click on the joystick button again to turn off parameter change mode, or release the index trigger to release the sound and place you back into movement mode.

## Modifying Room Reflection Parameters

Use the left Touch or Xbox controller.

The y button toggles reflections on/off and causes a dimly-colored grid cube to appear, representing the room. Each notch in the cube represents one meter. The x button enables reverb (brightly-colored).

If pressing the left trigger on either controller does not capture a sound but intersects with a room wall, that wall will turn bright green.

Clicking on the joystick will it in room parameter mode, and it will stop controlling the camera. The selected wall will turn white, and a solid transparent wall will overlay the wall grid. The intensity of the opacity on that wall represents the reflection coefficient value of that wall.

The joystick y-axis controls the size of the room. The x-axis controls the reflection coefficient. Note that you can select other walls without having to manually switch modes, provided the index finger is still down.

Click on the joystick button again to turn off room parameter mode, or release the index trigger to release the sound and return to movement mode.

## Automation

Automation is supported for audio position only. In your DAW, enable automation record (varies with each DAW) and move the sounds around using your controller of choice. The sequence will be recorded and can be played back. Automated sequences are stored with the DAW project.

