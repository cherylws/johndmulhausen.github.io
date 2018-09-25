---
title: Console Variables and Commands Reference
---
This document reviews useful console variables and commands available for Unreal development. 

## Unreal Console Variables (1.15 or later)

Oculus integration 1.15 and later replace our previous console command model with console variables. For a complete description of available console variables, see UE4-Oculus.txt in the root folder of your Unreal installation.

## Legacy Unreal Console Commands (1.14 or earlier)

These commands are available in Unreal versions using Oculus integration 1.14 or earlier.

**Oculus Rift**: Press the tab keys while your game is running to bring up the console. 

**Gear VR**: To bring up the console on a mobile device, set it to developer mode, launch the application, and tap the screen with four fingers.

To specify console commands to be loaded on startup, in most cases you should add them to Engine/Config/ConsoleVariables.ini. See [Loading Console Variables](https://docs.unrealengine.com/latest/INT/Programming/Development/Tools/ConsoleManager/#loadingconsolevariables) in Epicâ€™s [Console Manager: Console Variables in C++](https://docs.unrealengine.com/latest/INT/Programming/Development/Tools/ConsoleManager/) for more information.

For more information, see "Useful VR Console Commands" in Unreal's [VR Cheat Sheet](https://docs.unrealengine.com/latest/INT/Platforms/VR/CheatSheet/).

Configuration CommandsCommand

Description

stereo on|off

Enables/Disables stereo mode.

stereo e=0.064

Eye distance (m).

stereo w2m=100

Overrides default world-units-to-meters scale.

stereo ncp=10 fcp=10000

Overrides near clipping and/or far clipping planes for stereo rendering (in cm).

stereo cs=1 ps=1

Overrides camera and position scale.

stereo show

Shows current ipd and head model offset.

stereo reset

Resets stereo settings.

hmd enable|disable

Enables/Disables HMD.

hmd pd [0..3.0]

Sets pixel density in the center (default is 1.0).

hmd pdadaptive on|off

Enables/Disables adaptive pixel density (see [Oculus Rift: Adaptive Pixel Density](/documentation/unreal/latest/concepts/unreal-adaptive-viewport/ "Adaptive Pixel Density allows applications to scale down the application viewport as GPU resources exceed 85% utilization, and to scale up as they become more available. This feature is currently available for Rift development only.") for more details).

hmd pdmax [0.5..2.0]

Sets maximum adaptive pixel density (ignored if hmd pdadaptive is off).

hmd pdmin [0.5..2.0]

Sets minimum adaptive pixel density (ignored if hmd pdadaptive is off).

hmd sp [30..300]

Overrides screenpercentage for stereo mode. (Deprecated, use 'hmd pd xxx' instead).

hmd hqdistortion on|off

Enables/Disables high-quality distortion.

hmd mirror on|off

Enables/Disables mirroring to the desktop window.

hmd mirror mode [0..4]

Sets mirror mode: 0=Distorted, 1=Undistorted, 2=SingleEye, 3=SingleEye Letterboxed, 4=SingleEye Cropped

hmdpos on|off|toggle

Enables/Disables/Toggles positional tracking.

hmdpos enforce on|off

Enables/Disables head tracking even if not in stereo (for testing purposes).

hmdpos reset {yaw}

Resets position and rotation, applies yaw (in degrees) if provided.

hmdpos resetrot {yaw}

Resets rotation only, applies yaw (in degrees) if provided.

hmdpos resetpos

Resets position only.

hmdpos show

Outputs status of positional tracking to log.

hmdpos floor|eye

Selects tracking origin.

Misc CommandsCommand

Description

hmd stats

Shows HMD-related stats.

hmd grid

Toggles lens-centered grid.

hmd updateongt on|off

Enables/Disables updating HMD pose on game thread. On by default.

hmd updateonrt on|off

Enables/Disables updating HMD pose on render thread, for lower latency. On by default.

hmd cubemap [gearvr] [xoff=N] [yoff=N] [zoff=N] [yaw=N]

Generates a cube map image of your application. May be used for VR app previews in the Oculus Store. Cube map PNGs will be saved in the directory GameDir/Saved/Cubemaps.

gearvr: If specified, cube map size will be 6x1024x1024, otherwise it will be 6*2048x2048.

xoff, yoff, zoff: Offset from the current player's location.

yaw: override yaw rotation (degrees).

hmd setint PerfHUDMode [0..4]

Selects performance HUD mode, set to 0 to disable.

hmd setint DebugHudStereoMode [0..3]

Selects debug HUD stereo mode, set to 0 to disable.

hmdversion

Prints Oculus SDK version used and Oculus Plugin info.

