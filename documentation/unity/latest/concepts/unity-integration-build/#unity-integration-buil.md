---
title: Configuring for Build
---
This section describes building your project to PC and mobile targets.

## PC Build Target: Microsoft Windows and Mac OS X

This section describes targeting Unity project builds to Microsoft Windows and Mac OS X.

## Build Settings and Player Settings

To build the demo as a standalone full screen application, you will need to change a few project settings to maximize the fidelity of the demo.

Click on **File** > **Build Settings...** and select one of the following:

For Windows, set Target Platform to Windows and set Architecture to either x86 or x86 64.

![](/images/documentation-unity-latest-concepts-unity-integration-build-unity-integration-build-0.png)  
Build Settings: PCFor Mac, set Target Platform to Mac OS X.

![](/images/documentation-unity-latest-concepts-unity-integration-build-unity-integration-build-1.png)  
Build Settings: MacWithin the **Build Settings** pop-up, click **Player Settings**. Under **Resolution and Presentation**, set the values to the following:

![](/images/documentation-unity-latest-concepts-unity-integration-build-unity-integration-build-2.png)  
Player SettingsIn the **Build Settings** pop-up, select **Build**. If prompted, specify a name and location for the build.

If you are building in the same OS, the demo should start to run in full screen mode as a standalone application.

## Quality Settings

You may notice that the graphical fidelity is not as high as the pre-built demo. You will need to change some additional project settings to get a better looking scene.

Navigate to **Edit** > **Project Settings** > **Quality**. Set the values in this menu to the following:

![](/images/documentation-unity-latest-concepts-unity-integration-build-unity-integration-build-3.png)  
Quality settings for Oculus demoThe most important value to modify is **Anti aliasing** - it must be increased to compensate for the stereo rendering, which reduces the effective horizontal resolution by 50%. An anti-aliasing value of 2X is ideal - 4x may be used if you have performance to spare, and 8x usually isn't worth it.

Note: A quality setting called **Fastest** has been added to address a potential performance issue with Unity 4.5 and OS X 10.9. This setting turns off effects and features that may cause the drop in performance.Now rebuild the project again, and the quality should be at the same level as the pre-built demo.

## Running the Build

Now that the project is properly configured for VR, itâ€™s time to install and run the application.

PC builds create a single executable file that may be used in either Direct Display or Extended Display modes.

