---
title: Oculus Go: Getting Started – Additional Tasks
---
This section provides in-depth information for getting started developing Unreal applications that target Oculus Go.

## Overview

Once your environment is set up with the appropriate tools and your project settings are configured properly, you may build virtual reality projects targeting Android, load APKs onto the Oculus Go, and play them on the Oculus Mobile platform.

Note: Mobile applications are subject to more stringent computational limitations compared to Rift applications, and this should be taken into consideration beginning in the early design phase.## Oculus Mobile SDK

Oculus provides a mobile SDK with native C/C++ libraries for Android development in addition to supporting mobile development for game engines such as Unreal. It is not necessary for Unreal developers to download or install the Mobile SDK, but you may wish to look through our [Mobile SDK Developer Guide](/documentation/mobilesdk/latest/) for general information on mobile development such as basic mobile development tools, including Android Debug Bridge (ADB) and Oculus Remote Monitor. Performance guidelines are also provided.

We recommend that Unreal mobile developers review the following sections:

* [Mobile SDK Getting Started Guide](/documentation/mobilesdk/latest/concepts/book-intro/)
* [Mobile Development Basics](/documentation/mobilesdk/latest/concepts/book-mobile-basics/)
* [Testing and Troubleshooting](/documentation/mobilesdk/latest/concepts/book-testing/)
* You may also wish to reference the [VR Performance Optimization Guide](/documentation/pcsdk/latest/concepts/dg-performance-opt-guide/), which goes into depth about performance optimization techniques for native PC-SDK applications, but which contains a lot of generally applicable information that can be applied to mobile applications as well.
Developers interested in lower-level details about how the mobile VR rendering pipeline is handled by our native libraries may wish to download the mobile SDK and review the headers, particularly for the [VrApi](/documentation/mobilesdk/latest/concepts/book-engine-integration/), which is responsible for returning headset orientation data and applying distortion, sensor fusion, and compositing.

## Mobile Environment Setup

Use the Codeworks for Android installation package, not the stock Android SDK. (If you have any other projects that require different Android SDK/NDK versions, be sure to point their environment variables to the proper locations.) The Codeworks installer is bundled with the Unreal installation in Engine\Extras\AndroidWorks. Using this package simplifies Unreal setup and is usually necessary to successfully build mobile projects. To install Codeworks for Android 1R4, follow the instructions in Epicâ€™s [Required Android Setup](https://api.unrealengine.com/INT/Platforms/Android/GettingStarted/1/index.html) guide.

Unreal developers do not need to install Android Studio. Our Unreal SDK does not currently support OS X or Linux.

Once you have installed the required Android tools, follow the setup instructions described in the [Device Setup - Oculus Go](/documentation/mobilesdk/latest/concepts/mobile-device-setup-go/) guide in the Mobile SDK documentation. In this process you will enable Developer Options on your mobile device and make device configuration settings.

## Configure Unreal for Android SDK

If you do not have a project prepared but would like to try out the process, you may create a scene with starter content such as the C++ First Person project.

Once you have installed the Android SDK and required tools, configure Unreal for Android development.

1. Select **Edit** > **Project Settings**.
2. In the **Project Settings** menu on the left, go to **Platforms** and select **Android SDK** (not **Android**).
3. Configure all fields in **SDKConfig** with the appropriate paths to the necessary tools. **Note**: if you installed Codeworks for Android, these fields should be populated automatically.
## Project Configuration

This section describes how to configure any C++ or Blueprints Unreal project targeting desktop or mobile for use with Oculus mobile devices.

If you do not have a project prepared but would like to try out the process, you may create a scene with starter content such as the C++ First Person project.

1. Select **Edit** > **Plugins**.
2. Select **Virtual Reality**. 
3. Verify that the **Enabled** check box is checked for **OculusVR**. If you need to select it, click **Restart Now** in the lower-right afterward. Close Plugins configuration.
4. Select **Edit** > **Project Settings**.
5. Fill in any other desired information in **Project** > **Description**.
6. In the **Project Settings** menu on the left, go to **Platforms** and select **Android**.
7. Under **APKPackaging**, set the **Minimum SDK Version** to **19**, and set the **Target SDK Version** to **19**.
8. Scroll down to **Advanced APKPackaging**. Then:
	1. Check **Configure the AndroidManifest for deployment to Gear VR**.
	2. Verify that **Remove Oculus Signature Files from Distribution APK** is unchecked, unless you are building a package to release.
	
9. In **Engine** > **Rendering**, uncheck **Mobile HDR** in the **Mobile** section. Restart project if prompted to do so. 
10. Close the **Project Settings** configuration window.
## Building and Running Projects

1. Connect your Oculus Go headset to your PC via USB.
2. Open a shell terminal and verify that your device is communicating with your PC using adb devices. Note that depending on the device you are using, you may need to configure your connection for software installation. For more information, see [Adb](/documentation/mobilesdk/latest/concepts/mobile-adb/) in our Mobile SDK Developer Guide.
3. We recommend using ASTC compression, though ETC2 will also work. Select **File** > **Package Project** > **Android** > **Android (ASTC)**. 
4. When prompted, browse to the destination folder where you would like your APK to be installed.
5. Once the build process is completed, navigate to the destination folder. Run the .bat file beginning with Install\_ to install the application to your phone.
6. Click the application to launch. You will be prompted to insert it into your Oculus Go headset.
Note: You may also set your phone to [Developer Mode](/documentation/mobilesdk/latest/concepts/mobile-troublesh-device-run-app-outside/), which allows you to run VR applications on your mobile device without inserting it into an HMD.## Launching a Project Directly onto your Headset or Phone

You may also directly build and launch an application to your Oculus Go headset without saving the APK locally.

1. Connect your device to your PC by USB. 
2. Select the **Launch** menu from the Unreal toolbar and select your phone/headset under Devices. If you do not see your device listed, verify your USB connection, and check if you need to set your connection to **Connected as an Installer**. Note that some Samsung phones default to **Charge Only** connection.
3. Your application will build and install to your Android device. When the build is complete, you will be prompted to insert the phone into your headset to launch.
## Preview Content on a PC

You may launch the Unreal Engine with a configuration option to use the Oculus Go plugin in conjunction with the Mobile renderer on the PC. This allows you to preview mobile development from the desktop using an Oculus Rift. To do so, disable OculusRift and SteamVR plugins for your project, and add -OpenGL -FeatureLevelES2 to your command line.

Although it is possible to preview mobile applications in the Oculus Rift during development, it is not generally useful to do so, because Rift applications are subject to substantially different performance requirements (see "Performance Targets" in [Oculus Go: Testing and Performance Analysis](/documentation/unreal/latest/concepts/unreal-debug-go/ "This guide describes basic testing and performance analysis for Oculus Go development in Unreal.")). You may find it easiest to use the 2D preview in Unreal, and then either build an APK or use Launch on Device when you need to view the app in VR.Note: Mobile Content Scale Factor is not currently supported for Oculus development.## Blueprints

Oculus provides Blueprints for common Oculus Go operations such as querying battery level and headphone connection status. 

For more information, see [Blueprints Reference](/documentation/unreal/latest/concepts/unreal-blueprints/ "This section serves as a reference guide for the Blueprints in the Online Subsystem Oculus library.").

## Advanced Rendering Features for Mobile

The Oculus SDK offers advanced mobile rendering feature such as multi-view and hybrid monoscopic rendering. Under some conditions these features can significantly improve performance.

For more information, see [Rendering](/documentation/unreal/latest/concepts/unreal-advanced-rendering/ "This section describes important rendering options and tools that can significantly improve your application.")

