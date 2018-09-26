---
title: Track Parameters
---



## Local Track Parameters

The top section of the plugin interface contains parameters that affect the individual track.

Local track parameters are used to set up the location of a sound source in 3D space, and to shape the attenuation of the sound as it gets further away from the listener.

These parameters are stored with the project when saving and loading.

|            Bypass            |                                                                                                                                        Prevents audio from being processed through the spatializer.                                                                                                                                        |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     GAIN(dB)[0.0 - 24.0]     |                                                                                                                                              Increases processed signal volume (in decibels).                                                                                                                                              |
|     NEAR (m)[0.0 - 175.0]     | Sets the distance from the listener at which a sound source will start controlling the attenuation curve (in meters). The attenuation curve approximates an inverse square and reaches maximum attenuation when it reaches the Far parameter.In the 2D grid display, the radius is represented by an orange disk around the sound position. |
|     FAR (m)[0.0 - 175.0]     |                                                                  Sets the distance from the listener at which a sound source reaches maximum attenuation value (in meters).In the 2D grid display, the radius will be represented by a red disk around the sound position.                                                                  |
| X/Y/Z Pos (m)[-100.0 - 100.0] |                                                              Sets the location of the sound relative to the listener (in meters). The co-ordinate system is right-handed, with Y-axis pointing up and the Z-axis pointing toward the screen (a.k.a. Oculus coordinate system).                                                              |
|    SCALE (m)[20.0 - 200.0]    |                                                                                                     Sets the scale of the 2D grid display (in meters). This allows the user to have greater control over the sound position placement.                                                                                                     |

## Global Track Parameters

These parameters are global to all instances of the plugin within the DAW. Any parameter changed in one global parameter plugin instance will be reflected in all global parameter plugin instances, allowing the user to easily set global parameters for all tracks.

 These parameters are stored with the project when saving and loading.

|                      REFLECTIONS                      |                                                                                                                                          Toggles the reflection engine, as defined by the reflection global parameters. This enhances the spatialization effect but incurs a commensurate performance penalty.                                                                                                                                          |
|--------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                         REVERB                         | When enabled, a fixed reverberation is mixed into the output, providing a more natural-sounding spatialization effect. Based on room size and reflection values (see *X/Y/Z Size* and *Left/Right*, *Forward/Backward*, *Up/Down Refl.*). If *X/Y/Z Size*, *Near*, *Far*, or *Refl.* parameters are changed, reverb must be turned on and off again for the changes to take effect (this avoids hitching artifacts). Reflections must be enabled to use. |
|              X/Y/Z Size (m)[1.0 - 200.0]              |                                                                                             Sets the dimensions of the theoretical room used to calculate reflections. The greater the dimensions, the further apart the reflections.In the 2D grid display, the room will be represented by a cyan box (this will only display if Reflections are enabled).                                                                                             |
| LEFT/RIGHT, FORWARD/BACKWARD,UP/DOWN REFL.[0.0 - 0.97] |                                                                                        Sets the percentage of sound reflected by each wall in a room with the dimensions specified by the *X/Y/Z SIZE* parameters. At 0, the reflection is fully absorbed. At 1.0, the reflection bounces from the wall without any absorption. Capped at 0.97 to avoid feedback.                                                                                        |

## Other Buttons and Toggles

|     ABOUT     |                                     Displays the current version (which matches the version of the Oculus Audio SDK being used). The *Update* button navigates to the latest Audio SDK in the Oculus developer site.                                     |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XZ/XY (toggle) | Changes the 2D grid display from top-down (XZ) to front-face (XY). The head model in the center of the grid will change to indicate which view you are in, making it easier to understand the relationship between the sound location and head position. |
