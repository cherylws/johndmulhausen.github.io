---
title: Compositor Mirror
---
The Compositor Mirror tool displays the content that appears within the Rift headset on your computer monitor. It has several display options that are useful for development, troubleshooting, and presentations.

Anything that appears in the Rift headset can be shown in the Compositor Mirror tool, including Oculus Home, Guardian System boundaries, in-game notifications, and transition fades. It is compatible with all games and experiences regardless whether they are developed using the native PC SDK or a game engine.

## Finding the Tool

The Compositor Mirror tool is located in C:\Program Files\Oculus\Support\oculus-diagnostics\OculusMirror.exe

## Image Display Options

The Compositor Mirror tool provides several display options.

The default mode is recommended for live presentations and demos. If you double-click OculusMirror from Windows Explorer or run from the command line without specifying any options, the tool displays a 1366x768 (pixel) window showing a rectilinear view of the right eye image, along with the Guardian System boundary layer and the Oculus notification layer.

The other display modes are as follows:

OculusMirror.exe --LeftEyeOnly Display the left eye image in rectilinear view:![](/images/documentation-pcsdk-latest-concepts-dg-compositor-mirror-0.jpg)  
OculusMirror.exe --RightEyeOnly Display the right eye image in rectilinear view:![](/images/documentation-pcsdk-latest-concepts-dg-compositor-mirror-1.jpg)  
OculusMirror.exe --RectilinearBothEyes Display both eye images in rectilinear view:![](/images/documentation-pcsdk-latest-concepts-dg-compositor-mirror-2.jpg)  
OculusMirror.exe --RectilinearBothEyes --IncludeGuardian  Display both eye images in rectilinear view along with the Guardian System boundary. In the following example, the user's hands have protruded through the Guardian System boundary in two locations, as indicated by the circular holes in the boundary:![](/images/documentation-pcsdk-latest-concepts-dg-compositor-mirror-3.jpg)  
OculusMirror.exe --PostDistortionDisplay both eye images corrected for lens distortion and chromatic aberration. This will also display any other options that appear within the headset. For example, the following output is produced with --PostDistortion, but also shows the Guardian system boundary, since it is visible within the headset. No additional options are allowed in conjunction with --PostDistortion. For example, you cannot explicitly exclude notifications or the Guardian system boundary, if they are visible within the headset.

![](/images/documentation-pcsdk-latest-concepts-dg-compositor-mirror-4.jpg)  
## Changing the Window Size

You can change the size of the window by dragging the window borders on the desktop. You can also use the --Size width height command to set the size of the window (in pixels) from the command line. If you exceed the resolution of your main display, the window size is reduced to fit. For example:

OculusMirror.exe --Size 2160 2160 --RightEyeOnly## Displaying Notifications

You can display the Oculus notifications layer by using --IncludeNotifications. For example:

OculusMirror.exe --RectilinearBothEyes --IncludeNotifications## Flash on Frame Drops

It is possible that the CompositorMirror tool may drop frames that are displayed within the Rift headset. If you wish to clearly see when this happens, use the --FlashFrameDrops command. This will cause the display in the CompositorMirror to flash whenever a frame is dropped. For example:

OculusMirror.exe --FlashFrameDrops --RectilinearBothEyes