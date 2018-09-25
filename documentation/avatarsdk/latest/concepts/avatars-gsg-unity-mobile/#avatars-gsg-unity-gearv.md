---
title: Unity Developer Guide - Mobile
---
The Avatar Unity packages contain several prefabs you can drop into your existing Unity projects. This tutorial shows you how to start using them.

## Configure the Unity Editor

Setup includes importing the Oculus Unity packages and also setting up Unity for Android development and debugging.

1. Create a new project in Unity.
2. Click **File > Build Settings** and select **Android**. Download and install Unity Android Support and then restart Unity if necessary.
3. Click **Switch Platform** to switch to Android platform.
4. Click **Add Open Scenes**.
5. Set **Texture Compression** to **ASTC**.
6. Click **Edit > Project Settings > Player**, click the little Android Settings robot, and then set the following options: 
	1. Select the **Virtual Reality Supported** check box.
	2. In **Bundle Identifier**, enter a unique package name.
	3. Set **Minimum API Level** to **Android 5.0 'Lollipop' (API level 21)**.
	4. Set **Install Location** to **Automatic**.
	
7. There are two ways to import the Oculus APIs into the Unity Editor. You can either: 
	* Navigate to the [Oculus Integration](https://www.assetstore.unity3d.com/en/#!/content/82022) page and select **Import**.
	* In the Editor, select the **Asset Store** tab, Search for "Oculus Integration", and select **Import**. Note: We recommend importing the complete integration package. This enables the core Oculus APIs, the Platform and Avatar APIs, and the Social Starter sample scene. Read about the [Social Starter](/documentation/avatarsdk/latest/concepts/legacy-avatars-sdk-unity-example-social), a sample scene that demonstrates how the Avatar and Platform APIs compliment each other to create an engaging social experience. If you don't import the Oculus Integration and instead use the Unity package included with the [Avatar SDK](/downloads/package/oculus-avatar-sdk/), you must also import the Unity package included with the [Platform SDK](/downloads/package/oculus-platform-sdk/). If the Platform SDK package is not included, the SocialStarter project can cause errors and must be deleted.
	
8. (Only required for Gear VR development.) Create an Oculus Signature File for your Android device at <https://dashboard.oculus.com/tools/osig-generator/> and then copy it to the folder gearvr-avatar/Assets/Plugins/Android/assets. Create this folder if it doesn't exist.
## Adding the VR Camera

Because the Avatar has a default height of 170 cm, we must raise our VR camera rig to the same height.

1. Delete **Main Camera** from your scene and then drag **OVRCameraRig** from **OVR > PreFabs**.
2. Set the **Position** transform on OVRCameraRig to **X:0,****Y:1.70**, **Z:0**.
## Adding an Avatar

As the player cannot see his or her own Avatar, all mobile Avatars should all be of the "third person" type. To make sure the Avatar is visible, place it 50 cm in front of the camera and rotate it 180 degrees so that its front faces us.

Note: The "Local" in the prefab name "LocalAvatar" refers to how the Avatar object gets its motion data. "Local" means the avatar object is driven by the local headset orientation.1. Drag **OvrAvatar > Content > Prefabs > LocalAvatar** to the Hierarchy window.
2. In the **Inspector**, clear the **Show First Person** check box and select the **Show Third Person** check box.
3. Set the **Position** transform on LocalAvatar to **X:0**, **Y:0,****Z:0.50**.
4. Set the **Rotation** transform on LocalAvatar to **X:0**, **Y:180**, **Z:0**.
5. Click **File > Build & Run** to build an .apk from this scene and have Unity launch it on your Android device.
**Add an Avatar with the Gear VR or Oculus Go Controller**

In addition to the steps above, select the **Start With Controllers** check box in the Inspector. If a Gear VR controller is connected as the main controller, the controller will be rendered in the scene with the corresponding hand animations.

## Loading Personalized Avatars

You can replace the default blue avatar with a personalized Avatar using the Oculus Platform package. The base Avatar SDK OvrAvatar.cs class is already set up to load the Avatar specifications of users, but we need to call Oculus Platform functions to get valid user IDs.

After getting a user ID, we then can set the oculusUserID of the Avatar accordingly. The timing is important, because we have to set the user ID before the Start() function in OvrAvatar.cs gets called.

Note: For security reasons, Oculus Avatars and Oculus Platform must be initialized with a valid App ID before accessing user ID information. You can create a new application and obtain an App ID from the developer dashboard. For more information, see [Oculus Platform Setup](http://developer.prod.oculus.com/documentation/platform/latest/concepts/pgsg-s2s-basics/).The example below shows one way of doing this. It defines a new class that controls the platform. After modifying the sample with our new class, the Avatar SDK shows you the personalized Avatar of the current Oculus Home user instead of the default blue Avatar.

1. Import the [Oculus Platform SDK](/downloads/) Unity package into your Unity project.
2. Specify valid App IDs for both the Oculus Avatars and Oculus Platform plugins: 
	1. Click **Oculus Avatars > Edit Configuration** and paste your App ID into the field.
	2. Click **Oculus Platform > Edit Settings** and paste your App ID into the field.
	
3. Create an empty game object called <objectname>:
	1. Click **GameObject > Create Empty**.
	2. Rename the game object <objectname>.
	
4. Click **Add Component**, enter **New Script** in the search field, and then select **New Script**.
5. Name the script <filename> and set **Language** to **C Sharp.**
6. Save the text below as Assets\<filename>.cs. using UnityEngine; using Oculus.Avatar; using Oculus.Platform; using Oculus.Platform.Models; using System.Collections; public class <classname> : MonoBehaviour { public OvrAvatar myAvatar; void Awake () { Oculus.Platform.Core.Initialize(); Oculus.Platform.Users.GetLoggedInUser().OnComplete(GetLoggedInUserCallback); Oculus.Platform.Request.RunCallbacks(); //avoids race condition with OvrAvatar.cs Start(). } private void GetLoggedInUserCallback(Message<User> message) { if (!message.IsError) { myAvatar.oculusUserID = message.Data.ID; } } }
7. In the Unity Editor, select the game object you created from the Hierarchy. The **My Avatar** field appears in the Inspector.
8. Drag **LocalAvatar** from the Hierarchy to the **My Avatar** field.
**Handling Multiple Personalized Avatars**

In a multi-user scene where each Avatar has different personalizations, you already have the user IDs of all the users in your scene because you had to retrieve that data to invite them in the first place. Set the oculusUserID for each user 's Avatar accordingly.

If your scene contains multiple Avatars of the same person, such as in our **LocalAvatar** and **RemoteLoopback** sample scenes, you can iterate through all the Avatar objects in the scene to change all their oculusUserID values. Here is an example of how to modify the callback of our new class to personalize the Avatars in those two sample scenes:

using UnityEngine; using Oculus.Avatar; using Oculus.Platform; using Oculus.Platform.Models; using System.Collections; public class <classname> : MonoBehaviour { void Awake () { Oculus.Platform.Core.Initialize(); Oculus.Platform.Users.GetLoggedInUser().OnComplete(GetLoggedInUserCallback); Oculus.Platform.Request.RunCallbacks(); //avoids race condition with OvrAvatar.cs Start(). } private void GetLoggedInUserCallback(Message<User> message) { if (!message.IsError) { OvrAvatar[] avatars = FindObjectsOfType(typeof(OvrAvatar)) as OvrAvatar[]; foreach (OvrAvatar avatar in avatars) { avatar.oculusUserID = message.Data.ID; } } } }  
## Implementing Subtle Mouth Movement

Avatars now implement a simple vertex offset to drive subtle mouth movement, providing a more natural feel than the previous "mouth ripple" visualization. The vertex shader animates the vertices around the mouth area according to the \_Voice value. This should be set according to local microphone value range between 0-1.

public virtual void Update() { // Look for updates from remote users p2pManager.GetRemotePackets(); // update avatar mouths to match voip volume foreach (KeyValuePair<ulong, RemotePlayer> kvp in remoteUsers) { float remoteVoiceCurrent = Mathf.Clamp(kvp.Value.voipSource.peakAmplitude * VOIP\_SCALE, 0f, 1f); kvp.Value.RemoteAvatar.VoiceAmplitude = remoteVoiceCurrent; } if (localAvatar != null) { localAvatar.VoiceAmplitude = Mathf.Clamp(voiceCurrent * VOIP\_SCALE, 0f, 1f); } }   
## Ensuring Proper Lighting

Dynamic lighting of your Avatar ensures that your user’s Avatar looks and feels at home in your scene. The primary light in your scene is used to calculate lighting.

For optimal performance on mobile, you would generally want to bake lighting and have only a small number of dynamically “lit” objects, such as Avatars. You would then have a single directional light in your scene enabled.

If you must have multiple real-time light sources, which is highly discouraged, you can set the primary light source in Unity’s lighting settings.

The \_Cubemap texture is designed to work with reflection probes and applies the reflection according to the alpha channel of the roughness map.

## Avatar Prefabs

The Avatar Unity package contains two prefabs for Avatars: LocalAvatar and RemoteAvatar.

They are located in **OvrAvatar > Content > PreFabs**. The difference between LocalAvatar and RemoteAvatar is in the *driver*, the control mechanism behind Avatar movements.

The LocalAvatar driver is the OvrAvatarDriver script, which derives Avatar movement from the logged-in user's controllers and HMD.

The RemoteAvatar driver is the OvrAvatarRemoteDriver script, which gets its Avatar movement from the packet recording and playback system.

## Getting the Position of Avatar Components

You can use our accessor functions to get the transforms for the Avatar hands and mouth without having to walk the hierarchy. 

You can specify the hand and joint you want and then use GetHandTransform() to get its transform.

public Transform GetHandTransform(HandType hand, HandJoint joint)The enums for HandType are:

* Right
* Left
The enums for HandJoint are:

* HandBase
* IndexBase
* IndexTip
* ThumbBase
* ThumbTip
You can also get the forwards and upwards directions of an Avatar hand as a vector so you know where the hand is pointing. Use GetPointingDirection(). Forwards and Up are perpendicular to each other.

public void GetPointingDirection(HandType hand, ref Vector3 forward, ref Vector3 up)To get the transform of the Avatar's mouth, use GetMouthTransform(). This is useful when you want to spatialize Avatar speech as point-source audio located at the mouth.

public Transform GetMouthTransform()  
## Testing Your Integration

Once you’ve completed your integration, you can test by retrieving some Avatars in-engine. Use the following user IDs to test:

* 10150022857785745


* 10150022857770130


* 10150022857753417


* 10150022857731826


