---
title: Oculus Dash
---
This guide describes how to add Oculus Dash support to Unreal applications.

## Overview of Oculus Dash

Oculus Dash rolls up all of the Oculus menus and UI into a central hub that is instantly accessible from anywhere within the VR experience. Dash runs as an overlay inside your current VR experience, so you’ll be able to quickly switch from one application to the next, open your library, connect with friends, and even use the rest of your PC without any extra steps. Not only does this make VR more intuitive and convenient, it also lets you multitask like never before—a huge plus for creators and developers who use VR while they work.

For general information about Dash, please see the Dash announcement: [Introducing Rift Core 2.0—Our Biggest Software Update Yet!](https://www.oculus.com/blog/introducing-rift-core/). Also see the "Introducing Oculus Dash" video in our [Welcome to Rift Core 2.0](https://www.oculus.com/blog/welcome-to-rift-core-beta-now-available/) blog post to get a sense of how Dash works. 

 When users pause an application, one of two things will happen 

* If the application includes Dash support, the application will pause and the Dash menu UI will be drawn over the paused application.
* If the application does not include Dash support, the application will be paused by the runtime and the user will be presented with the Dash menu UI in an empty room, similar to the way the Universal Menu is displayed in earlier runtimes.
## Oculus Dash Support in Unreal

The Oculus Unreal integration provides Dash support in three areas: 

* Input focus handling
* Depth buffer support
* Declaring to the Oculus runtime that the application is input focus aware.
## Input Focus Handling

When the Dash UI is active, the running application loses input focus and the HasInputFocus flag will return false. The runtime renders tracked controllers in the scene to interact with the menu.

Your application should pause, mute, and hide any tracked controllers in the scene so there will not be a duplicate pair of hands. Depending on the application, additional action may also be warranted when input focus is lost (e.g., during a multiplayer combat game, you may wish to indicate that the player is unavailable and take any other appropriate action).

Note that HasInputFocus returns false under any other conditions in which the application loses input focus, such as when the HMD is removed from the head.

Input focus status may be queried using a Blueprint or in code. This query should be performed once during every frame render cycle.

Use OculusLibrary::HasInputFocus to query input status using Blueprints. For an illustration of a typical implementation of hiding tracked controllers when input focus is lost, see the VRCharacter Blueprint in our Touch sample (illustrated below).

![](/images/documentation-unreal-latest-concepts-unreal-dash-0.png)  
To query input focus status in C++, use code similar to the following:

ovrpBool HasFocus = ovrpBool\_False; if (OVRP\_SUCCESS(ovrp\_GetAppHasInputFocus(&HasFocus))) { return HasFocus == ovrpBool\_True; } else { return false; }## Depth Buffer Support

By default, Dash-compatible Unreal versions automatically submit depth information for scene geometry to help avoid depth conflicts between the Dash UI rendered in the scene and objects in the scene. It also enables compositor layer depth testing.

You can disable depth buffer support. We do not recommend doing so, unless you have a good reason. There are two ways you can do this.

* If you have the latest version of the Oculus Unreal integration (that you downloaded and compiled from the Oculus GitHub repo), you can simply uncheck Composites Depth under Edit / Project Settings / Plugins / OculusVR / PC. ![](/images/documentation-unreal-latest-concepts-unreal-dash-1.png)  

* If you are using the Epic release of Unreal 4.21 or earlier, you can do this by adding bCompositeDepth=False under Oculus.Settings in Engine.ini. 
## Declaring an Application is Input Focus Aware

If you have the latest version of the Oculus Unreal integration (that you downloaded and compiled from the Oculus GitHub repo), you can declare that your application is input focus aware by simply checking Supports Dash under Edit / Project Settings / Plugins / OculusVR / PC (as shown in the screenshot, above).

If you are using the Epic release of Unreal 4.21 or earlier, you can declare that your application is input focus aware by adding bSupportsDash=True under Oculus.Settings in Engine.ini (default is false).

When your application supports Dash, the Dash menu will be drawn over your paused application instead of in an empty room.

Alternatively, you can launch the application with the parameter -oculus-focus-aware. This will indicate that your application is Dash aware during that invocation of the application.

Do not specify that your application supports Dash unless it properly handles input focus loss.

[Previous: Splash Screens](/documentation/unreal/latest/concepts/unreal-loading-screens/)[Next: Oculus Go: Testing and Performance Analysis](/documentation/unreal/latest/concepts/unreal-debug-go/)