---
title: Is Auto-Loading Splash Screen Enabled
---
Determines whether or not splash screens are automatically displayed when the user transitions to a new level.

## Overview

This blueprint determines whether or not splash screens are automatically displayed when the user transitions to a new level. You may have multiple splash screens. You can add them using [Add Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-add-loading-splash-screen/ "Adds a splash screen with parameters to the application."). You cannot reference a splash screen individually after you add them. You can simply hide, remove, or show all of the splash screens you have added. So, essentially, you can create a splash screen out of multiple elements. 

When your application has multiple levels, then when the user moves from one level to another, the application enters loading mode. You can set it up so that the splash screen automatically appears during loading mode. This is called auto loading. Note that you can also explicitly show/hide splash screens. You can hide an auto loaded screen by calling [Hide Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-hide-loading-splash-screen/) or [Hide Loading Icon](/documentation/unreal/latest/concepts/unreal-blueprints-hide-loading-icon/). 

For more information about splash screens, see:

* [Add Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-add-loading-splash-screen/ "Adds a splash screen with parameters to the application.")
* [Clear Loading Splash Screens](/documentation/unreal/latest/concepts/unreal-blueprints-clear-loading-splash-screen/ "Removes all splash screens from the application.")
* [Enable Auto-Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-enable-auto-loading-splash-screen/ "Enables/disables the splash screen to be automatically shown when loading a new level.")
* [Hide Loading Icon](/documentation/unreal/latest/concepts/unreal-blueprints-hide-loading-icon/)
* [Hide Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-hide-loading-splash-screen/)
* [Is Auto-Loading Splash Screen Enabled](/documentation/unreal/latest/concepts/unreal-blueprints-is-auto-loading-splash-screen-enabled/ "Determines whether or not splash screens are automatically displayed when the user transitions to a new level.")
* [Is Loading Icon Enabled](/documentation/unreal/latest/concepts/unreal-blueprints-is-loading-icon-enabled/)
* [Show Loading Icon](/documentation/unreal/latest/concepts/unreal-blueprints-show-loading-icon/ "Immediately displays a specified defined texture as a splash screen.")
* [Show Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-show-loading-splash-screen/ "Immediately displays the currently defined splash screen.")
## Blueprint

![](/images/documentation-unreal-latest-concepts-unreal-blueprints-is-auto-loading-splash-screen-enabled-0.png)  
## Arguments

* No arguments.
## Output

* Return Value: A boolean that is True if auto-loading of splash screens is enabled, and is False otherwise. 
