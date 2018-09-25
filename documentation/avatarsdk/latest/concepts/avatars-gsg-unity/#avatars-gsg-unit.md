---
title: Unity Developer Guide - Rift
---
The Avatar Unity package contains several prefabs you can drop into your existing Unity projects. This tutorial shows you how to start using them.

## Configure Your Unity Project

1. Create a new project in Unity.
2. There are two ways to import the Oculus APIs into the Unity Editor. You can either:
	* Navigate to the [Oculus Integration](https://www.assetstore.unity3d.com/en/#!/content/82022) page and select **Import**.
	* In the Editor, select the **Asset Store** tab, search for "Oculus Integration", and select **Import**.
	Note: We recommend importing the complete integration package. This enables the core Oculus APIs, the Platform and Avatar APIs, and the Social Starter sample scene. Read about the [Social Starter](/documentation/avatarsdk/latest/concepts/legacy-avatars-sdk-unity-example-social), a sample scene that demonstrates how the Avatar and Platform APIs complement each other to create an engaging social experience.If you don't import the Oculus Integration and instead use the Unity package included with the [Avatar SDK](/downloads/package/oculus-avatar-sdk/), you must also import the Unity package included with the [Platform SDK](/downloads/package/oculus-platform-sdk/). If the Platform SDK package is not included, the Social Starter project can cause errors and must be deleted.
3. Select the **Virtual Reality Supported** check box in **Edit > Project Settings > Player**.
4. Delete **Main Camera** from your scene and then drag **OVRCameraRig** from **OVR > PreFabs**.
5. Reset the transform on OVRCameraRig.
Note: You may ignore any **No Oculus Rift App ID** warnings you see during development. While an App ID is required to retrieve Oculus Avatars for specific users, you can prototype and test experiences that make use of Touch and Avatars with just the default blue Avatar.## Adding an Avatar to the Scene

The **LocalAvatar** prefab renders the user's Avatar and hands. You can choose which parts of the Avatar you want to render: body, hands, and Touch controllers.

To render Avatar hands with Touch controllers:

1. Drag **OvrAvatar > Content > Prefabs > LocalAvatar** to the Unity **Hierarchy** window.
2. In the Unity **Inspector** window, select the **Start With Controllers** check box.
Click **Play** to test. Try out the built-in hand poses and animations by playing with the Touch controllers. 

To render Avatar hands without controllers:1. In the **Hierarchy** window, select **LocalAvatar**.
2. In the **Inspector** window, clear the **Start With Controllers** check box.
Click **Play** to test. Squeeze and release the grips and triggers on the Touch controllers and observe how the finger joints transform to change hand poses.

To render an avatar body:1. In the **Hierarchy** window, select **LocalAvatar**.
2. In the **Inspector** window, select the **Show Third Person** check box.
3. Change **Transform > Position** to X:0 Y:0 Z:1.5.
4. Change **Transform > Rotation** to X:0 Y:180 Z:0.
## Recording and Playing Back Avatar Pose Updates

The Avatar packet recording system saves Avatar movement data as packets you can send across a network to play back on a remote system. Lets take a quick tour of the RemoteLoopbackManager script.

Open the **RemoteLoopback** scene in **OvrAvatar > Samples > RemoteLoopback**.

Set RecordPackets to true to start the Avatar packet recording system. Also, subscribe to the event handler PacketRecorded so that you can trigger other actions each time a packet is recorded.

void Start () { LocalAvatar.RecordPackets = true; LocalAvatar.PacketRecorded += OnLocalAvatarPacketRecorded; }Each time a packet is recorded, the code places the packet into a memory stream being used as a stand-in for a real network layer.

void OnLocalAvatarPacketRecorded(object sender, args) { using (MemoryStream outputStream = new MemoryStream()) { BinaryWriter writer = new BinaryWriter(outputStream); writer.Write(packetSequence++); args.Packet.Write(outputStream); SendPacketData(outputStream.ToArray()); } }The remainder of the code receives the packet from the memory stream for playback on the loopback avatar object.

void SendPacketData(byte[] data) { ReceivePacketData(data); } void ReceivePacketData(byte[] data) { using (MemoryStream inputStream = new MemoryStream(data)) { BinaryReader reader = new BinaryReader(inputStream); int sequence = reader.ReadInt32(); OvrAvatarPacket packet = OvrAvatarPacket.Read(inputStream); LoopbackAvatar.GetComponent<OvrAvatarRemoteDriver>().QueuePacket(sequence, packet); } }  
## Loading Personalized Avatars

You can replace the default blue Avatar with a personalized Avatar using the Oculus Platform package. The base Avatar SDK OvrAvatar.cs class is already set up to load the avatar specifications of users, but we need to call Oculus Platform functions to get valid user IDs.

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
5. Name the script <filename> and set **Language** to **C Sharp**.
6. Save the text below as Assets\<filename>.cs. using UnityEngine; using Oculus.Avatar; using Oculus.Platform; using Oculus.Platform.Models; using System.Collections; public class <classname> : MonoBehaviour { public OvrAvatar myAvatar; void Awake () { Oculus.Platform.Core.Initialize(); Oculus.Platform.Users.GetLoggedInUser().OnComplete(GetLoggedInUserCallback); Oculus.Platform.Request.RunCallbacks(); //avoids race condition with OvrAvatar.cs Start(). } private void GetLoggedInUserCallback(Message<User> message) { if (!message.IsError) { myAvatar.oculusUserID = message.Data.ID; } } }
7. In the Unity Editor, select the game object you created from the Hierarchy. The **My Avatar** field appears in the Inspector.
8. Drag **LocalAvatar** from the Hierarchy to the **My Avatar** field.
**Handling Multiple Personalized Avatars**

In a multi-user scene where each avatar has different personalizations, you already have the user IDs of all the users in your scene because you had to retrieve that data to invite them in the first place. Set the oculusUserID for each user's Avatar accordingly.

If your scene contains multiple Avatars of the same person, such as in our **LocalAvatar** and **RemoteLoopback** sample scenes, you can iterate through all the Avatar objects in the scene to change all their oculusUserID values. Here is an example of how to modify the callback of our new class to personalize the Avatars in those two sample scenes:

using UnityEngine; using Oculus.Avatar; using Oculus.Platform; using Oculus.Platform.Models; using System.Collections; public class <classname> : MonoBehaviour { void Awake () { Oculus.Platform.Core.Initialize(); Oculus.Platform.Users.GetLoggedInUser().OnComplete(GetLoggedInUserCallback); Oculus.Platform.Request.RunCallbacks(); //avoids race condition with OvrAvatar.cs Start(). } private void GetLoggedInUserCallback(Message<User> message) { if (!message.IsError) { OvrAvatar[] avatars = FindObjectsOfType(typeof(OvrAvatar)) as OvrAvatar[]; foreach (OvrAvatar avatar in avatars) { avatar.oculusUserID = message.Data.ID; } } } }  
** Cross-Platform Avatar Support**

The removal of dependencies on the Oculus runtime enables developers making multi-platform apps to use Oculus Avatars on any platform that can use the Avatar SDK. To see a demo of this functionality, see the Unity CrossPlatform sample included with the SDK.

Keep the following information in mind concerning cross-platform avatars:

* There is presently no support for non-Oculus users to customize their avatars. However, there are 12 avatar IDs (Oculus User ID on each LocalAvatar) included in the sample to enable you to provide these users with a few choices.
* A network connection is required for full functionality.
* Distribution of a cross-platform app with avatar support requires including libovravatar.dll and OvrAvatarAssets.zip in a Plugins folder of your Unity project’s Assets folder. By default, these files can be found at C:\Program Files\Oculus\Support\oculus-runtime. 
* Distribution also requires including the [Oculus Avatar SDK](/licenses/avatar-sdk-1.0/) license with your app.
Note: Unity's build only copies DLL files in a project's Plugins directory to the output Plugins directory. You must manually copy OvrAvatarAssets.zip to the output Plugins directory. You can automate this process with a script adding a custom build command. For more information, see <https://docs.unity3d.com/Manual/BuildPlayerPipeline.html>## Avatar Prefabs

The Avatar Unity package contains two prefabs for Avatars: LocalAvatar and RemoteAvatar.

They are located in **OvrAvatar > Content > PreFabs**. The difference between LocalAvatar and RemoteAvatar is in the *driver*, the control mechanism behind avatar movements.

The LocalAvatar driver is the OvrAvatarDriver script, which derives Avatar movement from the logged-in user's controllers and HMD.

The RemoteAvatar driver is the OvrAvatarRemoteDriver script, which gets its Avatar movement from the packet recording and playback system.

## Ensuring Proper Lighting

Dynamic lighting of your Avatar ensures that your user’s Avatar looks and feels at home in your scene. The primary light in your scene is used to calculate lighting.

If you must have multiple real-time light sources, which is highly discouraged, then can set the primary light source in Unity’s lighting settings.

The \_Cubemap texture is designed to work with reflection probes and applies the reflection according to the alpha channel of the roughness map.

## Custom Touch Grip Poses

The GripPoses sample lets you change the hand poses by rotating the finger joints until you get the pose you want. You can then save these finger joint positions as a Unity prefab that you can load at a later time.

In this example, we pose the left hand to make it look like a scissors or bunny rabbit gesture.

Creating the left hand pose: 

1. Open the **Samples > GripPoses > GripPoses** scene.
2. Click **Play**.
3. Press E to select the **Rotate** transform tool.
4. In the **Hierarchy** window, expand **LocalAvatar > hand\_left > LeftHandPoseEditHelp > hands\_l\_hand\_world > hands:b\_l\_hand**.

![](/images/documentation-avatarsdk-latest-concepts-avatars-gsg-unity-avatars-gsg-unity-0.png)  

5. Locate all the joints of the fingers you want to adjust. Joint 0 is closest to the palm, subsequent joints are towards the finger tip. To adjust the pinky finger joints for example, expand **hands:b\_l\_pinky0 > hands:b\_l\_pinky1 > hands:b\_l\_pinky2 > hands:b\_l\_pinky3**.


6. In the **Hierarchy** window, select the joint you want to rotate.

![](/images/documentation-avatarsdk-latest-concepts-avatars-gsg-unity-avatars-gsg-unity-1.png)  

7. In the **Scene** window, click a rotation orbit and drag the joint to the desired angle.

![](/images/documentation-avatarsdk-latest-concepts-avatars-gsg-unity-avatars-gsg-unity-2.png)  

8. Repeat these two steps until you achieve the desired pose.
Saving the left hand pose:

1. In the **Hierarchy** window, drag **hand\_l\_hand\_world** to the Project window.
2. In the **Project** window, rename this transform to something descriptive, for example: poseBunnyRabbitLeft.
Using the left hand pose:

1. In the **Hierarchy** window, select **LocalAvatar**.
2. Drag **poseBunnyRabbitLeft** from the **Project** window to the **Left Hand Custom Pose** field in the **Inspector** window.
Click **Play** again. You see that the left hand is now frozen in our custom bunny grip pose. 

## Grabbing Objects with Rift Hands

To let avatars interact with objects in their environment, use the OVRGrabber and OVRGrabble components. For a working example, see the **AvatarWithGrab** sample scene included in the [Oculus Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/).

## Making Rift Stand-alone Builds

To make Rift Avatars appear in stand-alone executable builds, you need to change two settings.

* Add the Avatar shaders to the Always Included Shaders list in your project settings: 
	1. Click **Edit > Project Settings > Graphics**.
	2. Under **Always Included Shaders**, add **+3** to the **Size** and then press Enter.
	
* Build as a 64-bit application: 
	1. Click **File > Build Settings**.
	2. Set **Architecture** to **x86\_x64**.
	
## Testing Your Integration

Once you’ve completed your integration, you can test by retrieving some Avatars in-engine. Use the following user IDs to test:

* 10150022857785745


* 10150022857770130


* 10150022857753417


* 10150022857731826


