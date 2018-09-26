---
title: "Oculus Go: Quick Start"
---

This guide covers everything you need to know to get started developing Unreal applications for the Oculus Go.

## Setup the Oculus Go

Setup the headset, as described in [Getting Started With Your Oculus Go](https://support.oculus.com/183135912238400/)

![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-0.png)

## Select an Unreal Engine Distribution

There are a number of ways that you can obtain the Oculus Unreal distributions:

* A binary distribution is provided through the [Epic Game Launcher](https://www.unrealengine.com/download?sessionInvalidated=true). This Oculus code may be a version or two behind the latest Oculus SDK. We recommend that beginning developers use this binary distribution. It is stable, and does not require pulling the source from GitHub, setting up Visual Studio, and performing a lengthy compilation of the entire Unreal game engine source code. 
* A source distribution is provided through the [Epic GitHub Repository](https://github.com/EpicGames). This Oculus code may be a version or two behind the latest Oculus SDK. Please see the Epic GitHub Repository table in [Version Compatibility Reference](/documentation/unreal/latest/concepts/unreal-compatibility-matrix/ "This section provides compatibility information for Oculus OVRPlugin and UE4 versions. To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository. If you are not subscribed and logged into your GitHub account, you will get a 404 error. An Unreal license is not required."), in order to choose the specific downloads that best suit your development criteria. 
* A source distribution is provided through the [Oculus GitHub Repository](https://github.com/Oculus-VR/UnrealEngine.git). These distributions are always up to date with the latest Oculus SDKs. We support the current release of UE4 and any preview of the next release of UE4. Please see the Oculus GitHub Repository table in [Version Compatibility Reference](/documentation/unreal/latest/concepts/unreal-compatibility-matrix/ "This section provides compatibility information for Oculus OVRPlugin and UE4 versions. To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository. If you are not subscribed and logged into your GitHub account, you will get a 404 error. An Unreal license is not required."), in order to choose the specific downloads that best suit your development criteria. While new Oculus features ship first to the Oculus GitHub versions, API changes may occur when these branches are merged back into Epicâ€™s version of the engine. We recommend these distributions for professional developers who would like to access the latest Oculus SDK features. In order to build this source base, see [Building UE4 from Source](/documentation/unreal/latest/concepts/unreal-building-ue4-from-source/ "The following section describes how to download, compile, and launch UE4 from the Oculus GitHub repository using Visual Studio 2015 or 2017."). 


![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-1.png)

To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository (see [UE4 of GitHub](https://www.unrealengine.com/ue4-on-github) for details). If you are not subscribed and logged into your GitHub account, you will receive a 404 error. An Unreal license is not required.

## Prerequisites

* All versions of the Oculus Unreal SDK require Windows 7 or later.
* Setup the Oculus Go for running, debugging, and testing applications, as described in [ Device Setup - Oculus Go](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-device-setup-go/).
* Install CodeWorks for Android 1R6u1, which can be found in Engine\Extras\AndroidWorks\platform].


## Enabling Unknown Sources

In order to play an in-development application, you must enable the Oculus system to run applications from unknown sources by using the Oculus application settings, available through the gear icon in the upper-right. Select **Settings &gt; General** and turn on **Unknown Sources** to allow this. 

The first time you run an application that you have not downloaded from the Oculus Store, you must launch it directly. Once you have run an application from an unknown source at least once, it will then appear in the Library section of Home and the Oculus application, and may be launched normally, as long as **Unknown Sources** is enabled.

## Developing Applications with the UE4 Editor

1. Download and setup the Unreal engine that you wish to use. Make sure you are using a compatible set of SDKs, as shown in the [Version Compatibility Reference](/documentation/unreal/latest/concepts/unreal-compatibility-matrix/ "This section provides compatibility information for Oculus OVRPlugin and UE4 versions. To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository. If you are not subscribed and logged into your GitHub account, you will get a 404 error. An Unreal license is not required.").
2. From the Unreal Engine Launcher, press the Launch button to open the Unreal Project Browser.
3. From the **New Project** tab of the Unreal Project Browser, create a new Blueprint project, with the following settings: * Blank project * Mobile / Tablet * Scalable 3D / 2D * No Starter Content * Set the folder location * Set the project name 

 Your screen should look like this: ![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-2.png)


4. Press the **Create Project** button to create the project and load the UE4 Editor. A blank project appears in the editor:![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-3.png)


5. Select **Edit &gt; Plugins**, choose the Virtual Reality section, and make sure that the OculusVR Plugin is enabled. ![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-4.png)


6. In order to be able to run any Unreal Engine project when it is deployed to a device, including the Oculus Go, you must save at least one UE4 Level. To keep the current Level, press the Save icon in the toolbar to save it. Give it a name, such as GoQSMap.
7. Select **Edit &gt; Project Settings**. Then, under **Project**, select the **Maps &amp; Modes** section: ![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-5.png)


8. Under **Default Maps**, set both the **Editor Startup Map** and the **Game Default Map** to the Level that you just saved: ![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-6.png)


9. Scroll down and select **Engine &gt; Input**. Locate the **Mobile** section: ![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-7.png)


10. Set the **Default Touch Interface** to **None**:![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-8.png)

 The result should look like this: ![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-9.png)


11. Scroll down to the **Platforms** section, select **Android**. Then scroll down on the right-hand side to the **APK Packaging** section, and if necessary click **Configure Now**:![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-10.png)


12. Set the following settings:* Minimum SDK Version: 19 * Target SDK Version: 19 * Enable FullScreen Immersive on KitKat and above devices: True 

![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-11.png)


13.  Scroll down to the **Advanced APK Packaging** section, and enable **Configure the AndroidManifest for deployment to Gear VR**:![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-12.png)

Note: Oculus Go uses the same Android manifest settings as Gear VR. In Unreal 4.20 and later, this option has been renamed to reference Oculus Mobile (rather than Gear VR).
14. Click on the **Android SDK** section, and make sure that Android SDK tools that are needed to build your project point to the correct folder on your PC and set to the following API levels:![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-13.png)


15. Scroll to the **Engine** section, select **Rendering**, and make sure **Mobile HDR** is turned off: ![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-14.png)


16. You should now be able to develop your Unreal application for the Oculus Go!


## Launch the Unreal Project on the Oculus Go

This section describes how to launch your UE4 project so that it can be viewed in the Oculus Go headset.

1. Make sure your Oculus Go is connected to your development PC via the USB cable.
2. Make sure you have installed and can run the Android Debug Bridge (ADB), and that your PC can see the Oculus Go using the ADB command adb devices. For more information, see [Adb](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-adb/) in the Mobile SDK Developer Guide.
3. In the UE4 Editor, click beside the **Launch** icon to open **Options for Launching on a Device**:![](/images/documentationunreallatestconceptsunreal-quick-start-guide-go-15.png)


4. From the drop down list, select the device you want to deploy to. If you are prompted to save the project, make sure to do so even if you recently saved it. This will ensure that the latest content resides on your Oculus Go.
5. In the lower corner of the UE4 Editor, a progress bar indicates the status of the packaging process. If this is the first time you are packaging your project, it could take a few minutes, depending on the size of your project.
6. When the process is complete, you should be able to launch the project and view it within your Oculus Go headset.


## Application Distribution Requirements and Guidelines

Before building your final release package, create a new Android keystore as described in the section “Manually Sign an APK” in Android's [Sign your Applications](https://developer.android.com/tools/publishing/app-signing.html) guide. Once you have generated your distribution keystore, in the Unreal Editor, go to **Edit** &gt; **Project Settings** &gt; **Platforms** &gt; **Android**, scroll down to **Distribution Signing**, and enter the required information.

See the [Application Signing](/documentation/mobilesdk/latest/concepts/mobile-submission-sig-file/) section of the Mobile SDK documentation for more information.

* **[Oculus Go: Getting Started â€“ Additional Tasks](/documentation/unreal/latest/concepts/unreal-ide-guide-go/)**  
This section provides in-depth information for getting started developing Unreal applications that target Oculus Go.

