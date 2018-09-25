---
title: Using Unity Features
---
These topics describe the contents and features of Oculus Avatars for Unity development.

## Sample Scenes

There are four sample scenes in the Avatar Unity package.

* Controllers

Demonstrates how first-person avatars can be used to enhance the sense of presence for Touch users.


* GripPoses

A helper scene for creating custom grip poses. See [Custom Touch Grip Poses](/documentation/avatarsdk/latest/concepts/avatars-gsg-unity/#avatars-sdk-unity-custom-grip-poses "The GripPoses sample lets you change the hand poses by rotating the finger joints until you get the pose you want. You can then save these finger joint positions as a Unity prefab that you can load at a later time.").


* LocalAvatar

Demonstrates the capabilities of both first-person and third-person avatars. Does not yet include microphone voice visualization or loading an Avatar Specification using Oculus Platform.


* RemoteLoopback

Demonstrates the avatar packet recording and playback system. See [Recording and Playing Back Avatar Pose Updates](/documentation/avatarsdk/latest/concepts/avatars-gsg-unity/#avatars-gsg-unity#unity-gsg-remoteloopback-sample).


* Social Starter

Demonstrates using Oculus Avatars together with other Oculus Platform features such as invites, peer-to-peer networking, and VoIP. See [Unity Social Starter Example](/documentation/avatarsdk/latest/concepts/legacy-avatars-sdk-unity-example-social/ "The Social Starter example scene demonstrates using Oculus Avatars together with other Oculus Platform features such as invites, peer-to-peer networking, and VoIP.").


## Loading Personalized Avatars

You can replace the default blue avatar with a personalized avatar using the Oculus Platform package. The base Avatar SDK OvrAvatar.cs class is already set up to load the avatar specifications of users, but we need to call Oculus Platform functions to get valid user IDs.

After getting a user ID, we then can set the oculusUserID of the avatar accordingly. The timing is important, because we have to set the user ID before the Start() function in OvrAvatar.cs gets called.

Note: For security reasons, Oculus Avatars and Oculus Platform must be initialized with a valid App ID before accessing user ID information. You can create a new application and obtain an App ID from the developer dashboard. For more information, see [Oculus Platform Setup](http://developer.prod.oculus.com/documentation/platform/latest/concepts/pgsg-s2s-basics/).![](/images/documentation-avatarsdk-latest-concepts-legacy-avatars-sdk-unity-avatars-sdk-unity-0.jpg)  
The example below shows one way of doing this. It defines a new class called PlatformManager to extend our existing [Unity Developer Guide - Rift](/documentation/avatarsdk/latest/concepts/avatars-gsg-unity/#avatars-gsg-unity "The Avatar Unity package contains several prefabs you can drop into your existing Unity projects. This tutorial shows you how to start using them.") sample. After modifying the sample with our new class, the Avatar SDK shows you the personalized avatar of the current Oculus Home user instead of the default blue avatar.

1. Import the [Oculus Platform SDK](/downloads/) Unity package into your Unity project.
2. Specify valid App IDs for both the Oculus Avatars and Oculus Platform plugins: 
	1. Click **Oculus Avatars > Edit Configuration** and paste your **Oculus Rift App Id** or **Gear VR App Id** into the field.
	2. Click **Oculus Platform > Edit Settings** and paste your **Oculus Rift App Id** or **Gear VR app Id** into the field.
	
3. Create an empty game object named **PlatformManager**:
	1. Click **GameObject > Create Empty**.
	2. Rename the game object **PlatformManager**.
	
4. Click **Add Component, ** enter **New Script** in the search field, and then select **New Script**.
5. Name the new script **PlatformManager** and set **Language** to **C Sharp.**
6. Save the text below as Assets\PlatformManager.cs. using UnityEngine; using Oculus.Avatar; using Oculus.Platform; using Oculus.Platform.Models; using System.Collections; public class PlatformManager : MonoBehaviour { public OvrAvatar myAvatar; void Awake () { Oculus.Platform.Core.Initialize(); Oculus.Platform.Users.GetLoggedInUser().OnComplete(GetLoggedInUserCallback); Oculus.Platform.Request.RunCallbacks(); //avoids race condition with OvrAvatar.cs Start(). } private void GetLoggedInUserCallback(Message<User> message) { if (!message.IsError) { myAvatar.oculusUserID = message.Data.ID; } } }
7. In the Unity Editor, select **PlatformManager** from the Hierarchy. The **My Avatar** field appears in the Inspector.
8. Drag **LocalAvatar** from the Hierarchy to the **My Avatar** field.
**Handling Multiple Personalized Avatars**

In a multi-user scene where each avatar has different personalizations, you already have the user IDs of all the users in your scene because you had to retrieve that data to invite them in the first place. Set the oculusUserID for each user 's avatar accordingly.

If your scene contains multiple avatars of the same person, such as in our **LocalAvatar** and **RemoteLoopback** sample scenes, you can iterate through all the avatar objects in the scene to change all their oculusUserID values. Here is an example of how to modify the callback of our PlatformManager class to personalize the avatars in those two sample scenes:

using UnityEngine; using Oculus.Avatar; using Oculus.Platform; using Oculus.Platform.Models; using System.Collections; public class PlatformManager : MonoBehaviour { void Awake () { Oculus.Platform.Core.Initialize(); Oculus.Platform.Users.GetLoggedInUser().OnComplete(GetLoggedInUserCallback); Oculus.Platform.Request.RunCallbacks(); //avoids race condition with OvrAvatar.cs Start(). } private void GetLoggedInUserCallback(Message<User> message) { if (!message.IsError) { OvrAvatar[] avatars = FindObjectsOfType(typeof(OvrAvatar)) as OvrAvatar[]; foreach (OvrAvatar avatar in avatars) { avatar.oculusUserID = message.Data.ID; } } } }## Avatar Prefabs

The Avatar Unity package contains two prefabs for Avatars: LocalAvatar and RemoteAvatar.

 They are located in **OvrAvatar >Content > PreFabs**. The difference between LocalAvatar and RemoteAvatar is in the *driver*, the control mechanism behind avatar movements.

The LocalAvatar driver is the OvrAvatarDriver script which derives avatar movement from the logged in user's controllers and HMD.

The RemoteAvatar driver is the OvrAvatarRemoteDriver script which gets its avatar movement from the packet recording and playback system.

## Reducing Draw Calls with the Combine Meshes Option

Each avatar in your scene requires 11 draw calls per eye per frame (22 total). The **Combine Meshes** option reduces this to 3 draw calls per eye (6 total) by combining all the mesh parts into a single mesh. This is an important performance gain for Gear VR as most apps typically need to stay within a draw call budget of 50 to 100 draw calls per frame. Without this option, just having 4 avatars in your scene would use most or all of that budget.

You should almost always select this option when using avatars. The only drawback to using this option is that you are no longer able to access mesh parts individually, but that is a rare use case.

## Custom Touch Grip Poses

The GripPoses sample lets you change the hand poses by rotating the finger joints until you get the pose you want. You can then save these finger joint positions as a Unity prefab that you can load at a later time.

In this example, we pose the left hand to make it look like a scissors or bunny rabbit gesture.

Creating the left hand pose: 

1. Open the **Samples > GripPoses > GripPoses** scene.
2. Click **Play**.
3. Press E to select the Rotate transform tool.
4. In the Hierarchy window, expand **LocalAvatar > hand\_left > LeftHandPoseEditHelp > hands\_l\_hand\_world > hands:b\_l\_hand**.

![](/images/documentation-avatarsdk-latest-concepts-legacy-avatars-sdk-unity-avatars-sdk-unity-1.png)  

5. Locate all the joints of the fingers you want to adjust. Joint 0 is closest to the palm, subsequent joints are towards the finger tip. To adjust the pinky finger joints for example, expand **hands:b\_l\_pinky0 > hands:b\_l\_pinky1 > hands:b\_l\_pinky2 > hands:b\_l\_pinky3**.


6. In the **Hierarchy** window, select the joint you want to rotate.

![](/images/documentation-avatarsdk-latest-concepts-legacy-avatars-sdk-unity-avatars-sdk-unity-2.png)  

7. In the **Scene** window, click a rotation orbit and drag the joint to the desired angle.

![](/images/documentation-avatarsdk-latest-concepts-legacy-avatars-sdk-unity-avatars-sdk-unity-3.png)  

8. Repeat these two steps until you achieve the desired pose.
Saving the left hand pose:

1. In the Hierarchy window, drag **hand\_l\_hand\_world** to the Project window.
2. In the Project window, rename this transform to something descriptive, for example: poseBunnyRabbitLeft.
Using the left hand pose:

1. In the Hierarchy window, select **LocalAvatar**.
2. Drag **poseBunnyRabbitLeft** from the Project window to the **Left Hand Custom Pose** field in the Inspector Window.
Click **Play** again. You see that the left hand is now frozen in our custom bunny grip pose. 

## Grabbing Objects with Rift Hands

To let avatars interact with objects in their environment, use the OVRGrabber and OVRGrabble components. For a working example, see the **AvatarWithGrab** sample scene included in the [Oculus Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/).

## Making Rift Stand-alone Builds

To make Rift avatars appear in stand-alone executable builds, we need to change two settings.

* Add the Avatar shaders to the Always Included Shaders list in your project settings: 
	1. Click **Edit > Project Settings > Graphics**.
	2. Under **Always Included Shaders**, add **+3** to the **Size** and then press Enter.
	3. Add the following shader elements: AvatarSurfaceShader, AvatarSurfaceShaderPBS, AvatarSurfaceShaderSelfOccluding.
	
* Build as a 64-bit application: 
	1. Click **File > Build Settings**.
	2. Set **Architecture** to **x86\_x64**.
	
## Getting the Position of Avatar Components

You can use our accessor functions to get the transforms for the avatar hands and mouth without having to walk the hierarchy. 

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
You can also get the forwards and upwards directions of an avatar hand as a vector so you know where the avatar hand is pointing. Use GetPointingDirection(). Forwards and Up are perpendicular to each other.

public void GetPointingDirection(HandType hand, ref Vector3 forward, ref Vector3 up)To get the transform of the avatar's mouth, use GetMouthTransform(). This is useful when you want to spatialize avatar speech as point-source audio located at the mouth.

public Transform GetMouthTransform()