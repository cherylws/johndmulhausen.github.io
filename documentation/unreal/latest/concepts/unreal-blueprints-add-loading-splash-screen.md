---
title: Add Loading Splash Screen
---
Adds a splash screen with parameters to the application.

## Overview

This blueprint adds a splash screen, with a set of parameters, to the application. Note that you can add multiple splash screens, in which case they will all be visible whenever a splash screen is displayed. Thus, you can think of the individual splash screens as components of the actual splash screen that the user will see.

The currently added splash screens are displayed whenever the user moves from one level to another, if you have called [Enable Auto-Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-enable-auto-loading-splash-screen/ "Enables/disables the splash screen to be automatically shown when loading a new level.")

For more information about splash screens, see:

* [Add Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-add-loading-splash-screen/ "Adds a splash screen with parameters to the application.")
* [Clear Loading Splash Screens](/documentation/unreal/latest/concepts/unreal-blueprints-clear-loading-splash-screen/ "Removes all splash screens from the application.")
* [Enable Auto-Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-enable-auto-loading-splash-screen/ "Enables/disables the splash screen to be automatically shown when loading a new level.")
## Blueprint

![](/images/documentation-unreal-latest-concepts-unreal-blueprints-add-loading-splash-screen-0.png)  
## Arguments

* Texture: A texture asset to be used for the splash. Gear VR and Oculus Go use this as a path for a loading icon. All position and rotation arguments are currently ignored by Gear VR and Oculus Go. However, Oculus Rift uses all of the arguments.
* Translation in Meters (Oculus Rift only): Initial translation of the center of the splash screen (in meters).
* Rotation (Oculus Rift only): The initial rotation value for the splash screen, with the origin at the center of the splash screen.
* Size in Meters (Oculus Rift only): Size, in meters, of the quad that contains the splash screen.
* Delta Rotation (Oculus Rift only): This is the incremental rotation, which is added at other frame to the quad transform. This causes the quad (which contains the splash screen) to be rotated about its center.
* Clear Before Add: If true, clears splashes before adding a new one.
## Output

* No output.
