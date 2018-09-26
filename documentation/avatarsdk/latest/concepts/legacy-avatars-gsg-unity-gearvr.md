---
title: Unity (Gear VR) Getting Started
---

The Avatar Unity packages contain several prefabs you can drop into your existing Unity projects. This tutorial shows you how to start using them.

## Set Up the Unity Project for Oculus VR and Avatars

The set up includes importing the Oculus Unity packages and also setting up Unity for Android development and debugging.

1. Create a new project in Unity named gearvr-avatar.
2. Click **File &gt; Build Settings** and select **Android**. Download and install Unity Android Support and then restart Unity if necessary.
3. Click **Switch Platform** to switch to Android platform.
4. Click **Add Open Scenes**.
5. Set **Texture Compression** to **ASTC**.
6. Click **Edit &gt; Project Settings &gt; Player**, click the little Android Settings robot, and then set the following options: 
	1. Select the **Virtual Reality Supported** check box.
	2. In **Bundle Identifier,** enter a unique package name.
	3. Set **Minimum API Level **to **Android 5.0 'Lollipop' (API level 21)**.
	4. Set **Install Location** to **Automatic**.
	
7. There are two ways to import the Oculus APIs into the Unity Editor. You can either: * Navigate to the [Oculus Integration](https://www.assetstore.unity3d.com/en/#!/content/82022) page and select **Import**. * In the Editor, select the **Asset Store** tab, Search for 'Oculus Integration', and select **Import**. Note: We recommend importing the complete integration package. This enables the core Oculus APIs, the Platform and Avatar APIs, and the Social Starter sample scene. Read about the [Social Starter](https://developer.oculus.com/documentation/avatarsdk/latest/concepts/avatars-sdk-unity-example-social), a sample scene that demonstrates how the Avatar and Platform APIs compliment each-other to create an engaging social experience. 


8. Connect your Android device to your computer.
9. Create an Oculus Signature File for your Android device at &lt;https://dashboard.oculus.com/tools/osig-generator/&gt;and then copy it to the folder gearvr-avatar/Assets/Plugins/Android/assets. Create this folder if it doesn't exist.


## Adding the VR Camera

Because the avatar has a default height of 170 cm, we must raise our VR camera rig to the same height.

1. Delete **Main Camera** from your scene and then drag **OVRCameraRig** from **OVR &gt; PreFabs**.
2. Set the **Position** transform on OVRCameraRig to **X:0,****Y:1.70**, **Z:0**.


## Adding an Avatar

As the player cannot see his or her own Gear VR avatar, Gear VR avatars should all be of the "third person" type. To make sure the avatar is visible, we can place the avatar 50cm in front of the camera, and rotate the avatar 180 degrees so that its front faces us.

1. Drag **OvrAvatar &gt; Content &gt; Prefabs &gt; LocalAvatar** to the Hierarchy window.
2. In the Inspector, clear the **Show First Person** check box and select the **Show Third Person** check box.
3. Select the **Combine Meshes** check box. This reduces total draw calls per frame per avatar to 6 from 22. Gear VR apps typically need to stay within 50 to 100 draw calls per frame. 
4. Set the **Position** transform on LocalAvatar to **X:0**, **Y:0,****Z:0.50**.
5. Set the **Rotation** transform on LocalAvatar to **X:0**, **Y:180**, **Z:0**.
6. Click **File &gt; Build &amp; Run** to build an .apk from this scene and have Unity launch it on your Android device.




![](/images/documentationavatarsdklatestconceptslegacy-avatars-gsg-unity-gearvr-0.jpg)



**Add an Avatar with the Gear VR Controller:**

In addition to the steps above, select the **Start With Controllers** check box in the Inspector. If a Gear VR Controller is connected as the main controller, the controller will be rendered in the scene with the corresponding hand animations.

## What to Explore Next?

* **Loading Personalized Avatars**

See [Using Unity Features](/documentation/avatarsdk/latest/concepts/legacy-avatars-sdk-unity/#avatars-sdk-unity "These topics describe the contents and features of Oculus Avatars for Unity development.") for instructions on how to modify the sample scenes to retrieve Oculus User IDs and display personalized avatars.


* **Recording and Playing Back Avatar Pose Updates**

Build our RemoteLoopback example scene and read the accompanying write-up in our [Unity Developer Guide - Rift](/documentation/avatarsdk/latest/concepts/avatars-gsg-unity/#avatars-gsg-unity "The Avatar Unity package contains several prefabs you can drop into your existing Unity projects. This tutorial shows you how to start using them.") topic.



