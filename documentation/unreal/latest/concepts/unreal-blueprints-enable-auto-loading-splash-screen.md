---
title: Enable Auto Loading Splash Screen
---

Enables/disables the splash screen to be automatically shown when loading a new level. 

## Overview

This blueprint enables/disables splash screen auto-loading. When auto-loading is enabled, the splash screen will automatically be loaded whenever the user transitions from one level to another. When auto-loading is disabled, the splash screen is never automatically loaded. 

You can add multiple splash screens by calling [Add Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-add-loading-splash-screen/). If you enable splash screen auto-loading, all of the splash screens that you have added will be auto-loaded whenever the user transitions from one level to another. Thus, you can think of the individual splash screens as components of the actual splash screen that will be visible to the user.

For more information, see [Add Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-add-loading-splash-screen/). When you call Enable Auto Loading Splash Screens, it will enable/disable the auto-loading of all splash screens that have previously been added.

For more information about splash screens, see:

* [Add Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-add-loading-splash-screen/ "Adds a splash screen with parameters to the application.")
* [Clear Loading Splash Screens](/documentation/unreal/latest/concepts/unreal-blueprints-clear-loading-splash-screen/ "Removes all splash screens from the application.")
* [Enable Auto-Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-enable-auto-loading-splash-screen/ "Enables/disables the splash screen to be automatically shown when loading a new level.")


## Blueprint

![](/images/documentationunreallatestconceptsunreal-blueprints-enable-auto-loading-splash-screen-0.png)

## Arguments

* Auto Show Enabled: Check the box, or supply a boolean input of True, to turn on splash screen auto-loading.


## Output
