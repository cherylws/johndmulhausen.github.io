---
title: Preparing for Mobile Development
---
To prepare for Unity mobile development for Oculus Go and Samsung Gear VR, you must set up the Unity Editor for Android development and install the Android SDK. The Oculus Mobile SDK is not required.

Note: If you are developing with a Unity Professional license, you will need an Android Pro Unity license to build Android applications with Unity. The Free license includes basic Android support. For more information, see [License Comparisons](http://download.unity3d.com/unity/licenses) Unity’s documentation.We recommend reviewing Unity’s [Getting started with Android development](https://docs.unity3d.com/Manual/android-GettingStarted.html) for general information on Android development, but the essential setup steps are described below.

Once you have set up the Unity Editor for Android development, VR support is enabled by checking the **Virtual Reality Supported** checkbox in **Player Settings**. Applications targeting the Android Platform will then run on Gear VR.

Unity automatically applies orientation tracking, stereoscopic rendering, and distortion correction to your main camera when VR support is enabled. For more details, see [Unity VR Support](/documentation/unity/latest/concepts/book-unity-dg/ "Welcome to the Oculus Unity Developer Guide.").

If you are already prepared for Unity Android development, you are nearly ready to begin mobile development.

## Mobile Device Setup

Follow the instructions in the [Gear VR Device Setup](/documentation/mobilesdk/latest/concepts/mobile-device-setup/) and [Oculus Go Device Setup](/documentation/mobilesdk/latest/concepts/mobile-device-setup-go/) sections of our Mobile SDK Developer Guide to prepare to run, debug, and test your mobile applications.

## Android SDK

The Android SDK is required for mobile development with Unity. For setup instructions, [Android Development Software Setup](/documentation/mobilesdk/latest/concepts/mobile-studio-setup-android/) in our Mobile SDK Developer Guide. Most Unity developers do not need to install Android Studio or NDK.

Once you have installed the Standalone Android SDK tools, you may continue with this guide. 

Once you have installed the Android SDK, you may wish to familiarize yourself with adb (Android Debug Bridge), a useful tool used for communicating with your Android phone. For more information, see [Adb](/documentation/mobilesdk/latest/concepts/mobile-adb/) in our Mobile Developer Guide.

## Sign your App with an Oculus Signature File

All Gear VR applications must be signed with an Oculus Signature File (osig) during development to access low-level VR functionality on your mobile device. This signature comes in the form of an Oculus-issued file that you include in your application. 

Each signature file is associated with a specific mobile device, so you will need an osig file for each device that you use for development. 

Please see our osig self-service portal for more information and instructions on how to request an osig for development: <https://dashboard.oculus.com/tools/osig-generator/>

Once you have downloaded an osig, be sure to keep a copy in a convenient location for reuse. You will only need one osig per device for any number of applications.

Make a copy of the osig and copy it to the following directory: <project>/Assets/Plugins/Android/assets/If that directory does not exist, create it and copy the osig file to it. Note that the folder names are **caps sensitive** and must be exactly as stated above.

If you attempt to run an Oculus mobile APK that has not been correctly signed with an osig, you will get the error message “thread priority security exception make sure the apk is signed”.

We recommend removing your osig before building a final APK for submission to the Oculus Store. When your application is approved, Oculus will modify the APK so that it can be used on all devices. See [Building Mobile Apps for Submission to the Oculus Store](/documentation/unity/latest/concepts/unity-build-android/#unity-build-android-store "If you are building an application for the Oculus Store, you will need to take a few extra steps.") for more information.

## Application Entitlement Checking

Entitlement checking is used to protect apps from unauthorized distribution. It is disabled by default in Unity. Entitlement checking is not required for development, but it is required for submitting an application to the Oculus Store.

For more information and instructions, see [Getting Started and Checking Entitlements](/documentation/platform/latest/concepts/pgsg-get-started-with-sdk/) in our Platform guide.

## Getting Started with Mobile Development

Mobile applications are subject to more stringent limitations and requirements and computational limitations than Rift applications.

We strongly recommend carefully reviewing [Mobile Development](/documentation/unity/latest/concepts/unity-mobile-performance-intro/#unity-mobile-performance-intro "This section provides guidelines to help your Unity app perform well with Samsung Gear VR.") and [Best Practices for Rift and Mobile](/documentation/unity/latest/concepts/unity-best-practices-intro/ "This section describes performance targets and offers recommendations for developers.") in our Developer Guide to be sure you understand our performance targets and recommendations for mobile development. These sections contain important information that can help you avoid mistakes that we see frequently.

## Previewing Mobile apps in Rift

You may find it useful to preview mobile applications using the Oculus Rift during development, but use caution when doing so. The rendering path for Android applications differs substantially from the rendering path used for Rift application previews and builds, and you may notice important differences in the look-and-feel and performance.

## Designing Apps for Both Rift and Mobile

When developing for both Rift and mobile platforms, keep in mind that their requirements differ substantially. If you would like to generate builds for both PC and mobile from a single project, it is important to follow the more stringent mobile development best practices, as well as meeting the required 90 FPS required by the Rift. This approach is not often taken in practice. 

## Additional Sources of Information

For information on Oculus tools to assist with mobile development, such as our Sample Framework or the Oculus Remote Monitor for performance debugging, please see [Other Oculus Resources for Unity Developers](/documentation/unity/latest/concepts/unity-resources/ "This guide describes useful tools Oculus provides for Unity developers.").

For information on core VR development concepts, see the [Intro to VR](/documentation/intro-vr/latest/concepts/book-bp/) in our PC Developer Guide. It is written from the perspective of Rift development, but many contents apply equally well to mobile design.

Most Unity developers do not need to install the Oculus Mobile SDK. However, advanced developers may find it useful to review our Mobile SDK Developer Guide for insight into the underlying logic. Developers interested in the Android lifecycle and rendering path of Oculus mobile applications should review our documentation on [VrApi](/documentation/mobilesdk/latest/concepts/mobile-vrapi/). [Mobile Best Practices](/documentation/game-engines/latest/concepts/unity-mobile-performance-intro/#unity-mobile-performance-intro) and [General Recommendations](/documentation/game-engines/latest/concepts/unity-mobile-performance-intro/#unity-mobile-best-practices) may also be of interest.

If you are interested in submitting an application to the Oculus Store, please see our [Distribute Guide](/distribute/). We recommend doing so before beginning development in earnest so you have a realistic sense of our guidelines and requirements. 

