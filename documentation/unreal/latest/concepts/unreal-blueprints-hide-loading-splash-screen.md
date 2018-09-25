---
title: Hide Loading Splash Screen
---
## Overview

By default, this blueprint only hides the splash screens. If you select Clear, the splash screens are removed as well. If you don't clear the splash screens, you can subsequently call [Show Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-show-loading-splash-screen/ "Immediately displays the currently defined splash screen."), and the splash screens will appear again. But, if you clear the splash screens, you cannot show them again. 

You may have multiple splash screens. You can add them using [Add Loading Splash Screen](/documentation/unreal/latest/concepts/unreal-blueprints-add-loading-splash-screen/ "Adds a splash screen with parameters to the application."). You cannot reference a splash screen individually after you add them. You can simply hide, remove, or show all of the splash screens you have added. So, essentially, you can create a splash screen out of multiple elements. 

When your app has multiple levels, and the user moves from one level to another, then the app goes into a loading mode. You can set it up so that the splash screen automatically appears when it goes into loading mode. This is auto loading. Or, you can explicitly use show/hide splash screens. You can hide an auto loaded screen by simply calling this blueprint (Hide Loading Splash Screen) or [Hide Loading Icon](/documentation/unreal/latest/concepts/unreal-blueprints-hide-loading-icon/). 

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

![](/images/documentation-unreal-latest-concepts-unreal-blueprints-hide-loading-splash-screen-0.png)  
## Arguments

* Clear: A boolean value that removes all splash screens (in addition to hiding them) when set to True.
## Output

* No output.
