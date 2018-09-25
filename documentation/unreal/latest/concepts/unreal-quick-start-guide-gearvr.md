---
title: "Gear VR: Quick Start"
---
This guide covers everything you need to know to get started developing Unreal applications for Gear VR.

## Setup Development Environment

See [ Gear VR Software Setup](https://support.oculus.com/guides/gear-vr/latest/concepts/gsg-b-sw-software-setup/)

## Creating Your First Project

See [ Samsung Gear VR UE4 Quick Start](https://docs.unrealengine.com/en-us/Platforms/GearVR/QuickStart) step-by-step guide from Epic.

## Select an Unreal Engine Distribution

There are a number of ways that you can obtain the Oculus Unreal distributions:

* A binary distribution is provided through the [Epic Game Launcher](https://www.unrealengine.com/download?sessionInvalidated=true). This Oculus code may be a version or two behind the latest Oculus SDK. We recommend that beginning developers use this binary distribution. It is stable, and does not require pulling the source from GitHub, setting up Visual Studio, and performing a lengthy compilation of the entire Unreal game engine source code.
* A source distribution is provided through the [Epic GitHub Repository](https://github.com/EpicGames). This Oculus code may be a version or two behind the latest Oculus SDK. Please see the Epic GitHub Repository table in [Version Compatibility Reference](/documentation/unreal/latest/concepts/unreal-compatibility-matrix/ "This section provides compatibility information for Oculus OVRPlugin and UE4 versions. To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository. If you are not subscribed and logged into your GitHub account, you will get a 404 error. An Unreal license is not required."), in order to choose the specific downloads that best suit your development criteria.
* A source distribution is provided through the [Oculus GitHub Repository](https://github.com/Oculus-VR/UnrealEngine.git). These distributions are always up to date with the latest Oculus SDKs. We support the current release of UE4 and any preview of the next release of UE4. Please see the Oculus GitHub Repository table in [Version Compatibility Reference](/documentation/unreal/latest/concepts/unreal-compatibility-matrix/ "This section provides compatibility information for Oculus OVRPlugin and UE4 versions. To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository. If you are not subscribed and logged into your GitHub account, you will get a 404 error. An Unreal license is not required."), in order to choose the specific downloads that best suit your development criteria. While new Oculus features ship first to the Oculus GitHub versions, API changes may occur when these branches are merged back into Epic’s version of the engine. We recommend these distributions for professional developers who would like to access the latest Oculus SDK features. In order to build this source, see [Building UE4 from Source](/documentation/unreal/latest/concepts/unreal-building-ue4-from-source/ "The following section describes how to download, compile, and launch UE4 from the Oculus GitHub repository using Visual Studio 2015 or 2017."). ![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-0.png)  

To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository (see [UE4 of GitHub](https://www.unrealengine.com/ue4-on-github) for details). If you are not subscribed and logged into your GitHub account, you will receive a 404 error. An Unreal license is not required.

## Prerequisites

* All versions of the Oculus Unreal SDK require Windows 7 or later.
* Setup the Gear VR for running, debugging, and testing applications, as described in [ Device Setup - Gear VR](/documentation/mobilesdk/latest/concepts/mobile-device-setup/).
* Install CodeWorks for Android 1R6u1, which can be found in Engine\Extras\Android.
## Application Signing: OSIG and Android Distribution Keystore

There are two types of signatures that are required for your Gear VR application:

* An Oculus Signature File (OSIG) is required for your application to run on Gear VR.
* An Android Distribution Keystore is required for submission to the Oculus Store.
Note: An Oculus Signature File (OSIG) is **not** required for Oculus Go or Oculus Rift.During development, your application must be signed with an Oculus-issued Oculus Signature File (OSIG). This signature comes in the form of a file that you include in your application in order to access protected low-level VR functionality on your mobile device. Each signature file is tied to a specific device, so you will need to generate OSIG files for each device that you use for development. When your application is submitted and approved, Oculus will modify the APK so that it can be used on all devices.

To add your OSIG to Unreal for development:

1. Follow the instructions in [Application Signing](/documentation/mobilesdk/latest/concepts/mobile-submission-sig-file/) to download your OSIG.
2. Navigate to the directory <Unreal-directory>\Engine\Build\Android\Java\.
3. Create a new directory inside \Engine\Build\Android\Java\ and name it assets (entirely lower case).
4. Copy your OSIG to this directory.
When you are ready to build an APK for submission to release, we recommend that you exclude the OSIG in your APK. To do so, select **Edit** > **Project Settings** > **Android**, scroll down to **Advanced APKPackaging**, and verify that **Remove Oculus Signature Files from Distribution APK** is checked.

![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-1.png)  
Before building your final release, create a new Android keystore by following the “Manually Sign an APK” instructions in Android's [Sign your Applications](https://developer.android.com/tools/publishing/app-signing.html) guide. Once you have generated your distribution keystore, go to **Edit** > **Project Settings** > **Platforms** > **Android**, scroll down to **Distribution Signing**, and enter the required information.

See the [Application Signing](/documentation/mobilesdk/latest/concepts/mobile-submission-sig-file/) section of the Mobile SDK documentation for more information.

It is important to review [Distribute](/distribute/), which covers Oculus Store submission requirements and guidelines.

## Enabling Unknown Sources

In order to play an in-development application, you will need to enable the Oculus system to run applications from unknown sources by using the Oculus app settings, available through the gear icon in the upper-right. Select **Settings > General** and turn on **Unknown Sources** on to allow this.

The first time you run an application that you have not downloaded from the Oculus Store, you will need to launch it directly. Once you have run an application from an unknown source at least once, it will then appear in the Library section of Home and the Oculus app, and may be launched normally, as long as **Unknown Sources** is enabled.

## Developing Applications with the UE4 Editor

1. Download and setup the Unreal engine that you wish to use. Make sure you are using a compatible set of SDKs, as shown in the [Version Compatibility Reference](/documentation/unreal/latest/concepts/unreal-compatibility-matrix/ "This section provides compatibility information for Oculus OVRPlugin and UE4 versions. To access these GitHub repositories, you must be subscribed to the private EpicGames/UnrealEngine repository. If you are not subscribed and logged into your GitHub account, you will get a 404 error. An Unreal license is not required.").
2. From the Unreal Engine Launcher, press the Launch button to open the Unreal Project Browser.
3. From the **New Project** tab of the Unreal Project Browser, create a new Blueprint project, with the following settings:
	* Blank project
	* Mobile / Tablet
	* Scalable 3D / 2D
	* No Starter Content
	* Set the folder location
	* Set the project name
	 Your screen should look like this: ![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-2.png)  

4. Press the **Create Project** button to create the project and load the UE4 Editor. A blank project appears in the editor:![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-3.png)  

5. Select **Edit > Plugins**, choose the Virtual Reality section, and make sure that the OculusVR Plugin is enabled. ![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-4.png)  

6. In order to be able to run any Unreal Engine project when it is deployed to a device, including the Gear VR, you must save at least one level. To keep the current level, press the Save icon in the toolbar to save it. Give it a name, such as GearVRQSMap.
7. Select **Edit > Project Settings**. Then, under **Project**, select the **Maps & Modes** section: ![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-5.png)  

8. Under **Default Maps**, set both the **Editor Startup Map** and the **Game Default Map** to the level that you just saved: ![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-6.png)  

9. Scroll down and select **Engine > Input**. Locate the **Mobile** section: ![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-7.png)  

10. Set the **Default Touch Interface** to **None**:![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-8.png)  
 The result should look like this: ![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-9.png)  

11. Scroll down to the **Platforms** section, select **Android**, and on the right scroll down to the **APK Packaging** section, and click **Configure Now**:![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-10.png)  

12. Set the following settings:
	* Minimum SDK Version: 19
	* Target SDK Version: 19
	* Enable FullScreen Immersive on KitKat and above devices: True
	![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-11.png)  

13.  Scroll down to the **Advanced APK Packaging** section, and enable the **Configure the AndroidManifest for deployment to Gear VR** check mark box:![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-12.png)  
Note: Since Oculus Go uses the same Android manifest settings as Gear VR, in Unreal 4.20 and later, this option has been renamed to reference Oculus Mobile (rather than Gear VR).
14. Click on the **Android SDK** section, and make sure that Android SDK tools that are needed to build your project point to the correct folder on your PC and set to the following API levels:![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-13.png)  

15. Scroll to the **Engine** section, select **Rendering**, and make sure **Mobile HDR** is turned off: ![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-14.png)  

16. You should now be able to develop your Unreal application for the Gear VR!
## Launch the UE4 Project on the Gear VR

This section describes how to launch your UE4 project so that it can be viewed in the Gear VR headset.

1. Connect your Samsung phone to your PC via USB.
2. Open a shell terminal and verify that your device is communicating with your PC using adb devices. Note that depending on the device you are using, you may need to configure your connection for software installation. For more information, see [Adb](/documentation/mobilesdk/latest/concepts/mobile-adb/) in our Mobile SDK Developer Guide.
3. In the UE4 Editor, click on the small white triangle next to the **Launch** icon to open the **Options for Launching on a Device**.![](/images/documentation-unreal-latest-concepts-unreal-quick-start-guide-gearvr-15.png)  

4. From the drop down list, select the device you want to deploy to. If you are prompted to save the project, make sure to do so even if you recently saved it. This will ensure that the latest content resides on your Android phone.
5. In the lower corner of the UE4 Editor, a progress bar indicates the status of the packaging process. If this is the first time you are packaging your project, it could take a few minutes depending on the size of your project.
6. When the process is complete, you should be able to launch the project and view it within your Gear VR headset.
* **[Gear VR: Getting Started – Additional Tasks](/documentation/unreal/latest/concepts/unreal-ide-guide-gearvr/)**  
This section provides in-depth information for getting started developing Unreal applications that target Gear VR.
