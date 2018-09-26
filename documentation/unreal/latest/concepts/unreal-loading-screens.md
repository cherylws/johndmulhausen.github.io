---
title: Splash Screens
---

We strongly recommend adding a loading splash screen to your Rift or mobile application. Loading splash screens are required by the Oculus Store. 

A simple loading splash screen presenting the user with a rotating texture can be easily added to your game. You will need to specify a texture for display, either with a provided Blueprint or by modifying the defaultengine.ini configuration file. In both methods, the loading splash screen is drawn to a VR Compositor Layer, and is guaranteed to render consistently at the required minimum frame rate.

We recommend favoring the configuration file approach over the Blueprint, as Blueprints must be initialized before your Loading Screen can be displayed, and there may be a delay after application launch before they are visible.

In our Unreal source using Oculus SDK 1.14 and earlier, a rotating arrow loading screen was provided by default. Versions using 1.16 and later do not provide a default loading screen.

## Create a Loading Screen with a Configuration File

Add an entry similar to the following example to your project’s defaultengine.ini file. The values given in this example work well for a typical icon.

```
[Oculus.Splash.Settings]
TexturePath=/Game/LoadingIconTexture.LoadingIconTexture
DistanceInMeters=X=6.0 Y=0.0 Z=0.0
SizeInMeters=X=0.25 Y=0.25
RotationDeltaInDegrees=1.0
RotationAxis=X=0.0 Y=0.0 Z=1.0
```

## Create a Loading Screen using a Blueprint

To display splash screens, use the Add Loading Splash Screen Blueprint:

![](/images/documentationunreallatestconceptsunreal-loading-screens-0.png)

For more information on Oculus Blueprints, see [Blueprints Reference](/documentation/unreal/latest/concepts/unreal-blueprints/). 

## Loading Splash Screen Example

This example consists of three levels: StartupLevel, Level1, and Level2. The StartupLevel configures four overlays which rotate independently. Then, Level1 is loaded after a brief delay so that you can observe the loading splash screen, which is auto loaded when a new level is being initialized.

![](/images/documentationunreallatestconceptsunreal-loading-screens-1.png)

The level blueprint for Level 1 simply waits one second and loads Level2. The loading splash screens will appear while Level2 is being loaded, because they have already been configured and remain ready for activation whenever a level is being loaded. The level blueprint for Level 1 simply waits one second and loads Level2. The loading splash screens will appear while Level2 is being loaded, because they have already been configured and remain ready for activation whenever a level is being loaded.

Level1 blueprint:

![](/images/documentationunreallatestconceptsunreal-loading-screens-2.png)

The level blueprint for Level2 is pretty much the same as Level1's level blueprint - it just waits one second and loads Level1. Again, the loading splash screens will be visible during this transition.

Level2 blueprint:

![](/images/documentationunreallatestconceptsunreal-loading-screens-3.png)

The result of running the sample will be 10 seconds of the splash screens spinning for the initial startup level, then bouncing between Level1 and Level2. The loading screens will probably only be visible for a few moments on most systems because these levels are trivially small.

The LoadingLevel blueprint shows a few extra nodes which aren't connected to the execution path. They are there to point out a common source of confusion we've heard from developers. First, the Hide Splash Screen looks like it should hide the Loading Splash Screens, but it doesn't work that way as of this writing. If the graph is modified so that Hide Splash Screen is used (as shown below) instead of Hide Loading Splash Screen, the application will never actually hide the splash screens.

![](/images/documentationunreallatestconceptsunreal-loading-screens-4.png)

The important thing to understand here is that the Oculus-specific splash screen nodes need to be used together. While they are closely related to the standard Unreal splash screen nodes, they are not the same system.

The Oculus fork of the Unreal Engine samples now includes a complete project which demonstrates everything described in this article. The sample can be found here: [https://github.com/Oculus-VR/UnrealEngine/tree/4.19/Samples/Oculus/SplashScreenSample](https://github.com/Oculus-VR/UnrealEngine/tree/4.19/Samples/Oculus/SplashScreenSample)

For more information on Oculus Blueprints, see [Blueprints Reference](/documentation/unreal/latest/concepts/unreal-blueprints/). 
