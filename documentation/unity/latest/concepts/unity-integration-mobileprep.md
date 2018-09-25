---
title: Preparing for Development: Mobile
---
This guide describes setup requirements for Oculus mobile VR development with Unity.

## Android SDK Setup and Oculus Mobile SDK

The Android SDK is required for mobile development with Unity. However, most Unity developers do not need to install Android Studio or NDK. Unity developers should follow the instructions in our [Device Setup guide](/documentation/mobilesdk/latest/concepts/mobile-device-setup/), and install the Java Development Kit (JDK) and Android SDK before beginning development. See Unityâ€™s [Getting Started with Android Development](http://docs.unity3d.com/Manual/android-GettingStarted.html) for more information. 

OVRMonitor is available to Unity 4 developers as a separate download. However, Unity 4 developers must download the Oculus Mobile SDK for the SDK Examples. 

When developing for mobile, please be sure to fully review all of the relevant performance and design documentation, especially the [Unity Best Practices: Mobile](/documentation/unity/latest/concepts/unity-integration-mobile-performance-intro/#unity-integration-mobile-performance-intro "This section provides simple guidelines to help your Unity app perform well with Samsung Gear VR."). Mobile apps are subject to more stringent limitations and requirements and computational limitations which should be taken into consideration from the ground up.

## Application Signing

Mobile applications require two different signatures at different stages of development. Be sure to read the [Application Signing](/documentation/mobilesdk/latest/concepts/mobile-submission-sig-file/) section of the Mobile SDK documentation for more information.

## Application Entitlement Checking

Entitlement checking, used to protect apps from unauthorized distribution, is disabled by default in Unity. For more information and instructions, see [Getting Started with the SDK](https://developer3.oculus.com/documentation/platform/latest/concepts/pgsg-get-started-with-sdk/) in our Platform guide.

