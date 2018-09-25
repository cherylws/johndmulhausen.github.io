---
title: Unity (Rift) Getting Started
---
The Avatar Unity package contains several prefabs you can drop into your existing Unity projects. This tutorial shows you how to start using them.

## Set Up the Unity Project for Oculus VR and Avatars

1. Create a New Project in Unity named "Unity Avatar Demo Project".
2. There are two ways to import the Oculus APIs into the Unity Editor. You can either:
	* Navigate to the [Oculus Integration](https://www.assetstore.unity3d.com/en/#!/content/82022) page and select **Import**.
	* In the Editor, select the **Asset Store** tab, Search for 'Oculus Integration', and select **Import**.
	Note: We recommend importing the complete integration package. This enables the core Oculus APIs, the Platform and Avatar APIs, and the Social Starter sample scene. Read about the [Social Starter](/documentation/avatarsdk/latest/concepts/avatars-sdk-unity-example-social), a sample scene that demonstrates how the Avatar and Platform APIs complement each-other to create an engaging social experience.
3. Select the **Virtual Reality Supported** check box in **Edit > Project Settings > Player**.
4. Delete **Main Camera** from your scene and then drag **OVRCameraRig** from **OVR > PreFabs**.
5. Reset the transform on OVRCameraRig.
Note: You may ignore any **No Oculus Rift App ID** warnings you see during development. While an App ID is required to retrieve Oculus avatars for specific users, you can prototype and test experiences that make use of Touch and Avatars with just the default blue avatar.## Adding an Avatar to the Scene

The **LocalAvatar** prefab renders the player's avatar and hands. You can choose which parts of the avatar you want to render: body, hands, and Touch controllers.

To render avatar hands with controllers:

1. Drag **OvrAvatar > Content > Prefabs > LocalAvatar** to the Unity **Hierarchy** window.
2. In the Unity **Inspector** window, select the **Start With Controllers** check box.
Click **Play** to test. Try out the built-in hand poses and animations by playing with the Touch controllers. 

![](/images/documentation-avatarsdk-latest-concepts-legacy-avatars-gsg-unity-0.jpg)  
To render avatar hands without controllers:1. In the **Hierarchy** window, select **LocalAvatar**.
2. In the **Inspector** window, clear the **Start With Controllers** check box.
Click **Play** to test. Squeeze and release the grips and triggers on the Touch controllers and observe how the finger joints transform to change hand poses. It is possible to add hand poses outside the range of these movements; we talk more about this in [Custom Touch Grip Poses](/documentation/avatarsdk/latest/concepts/avatars-gsg-unity/#avatars-sdk-unity-custom-grip-poses "The GripPoses sample lets you change the hand poses by rotating the finger joints until you get the pose you want. You can then save these finger joint positions as a Unity prefab that you can load at a later time.").

![](/images/documentation-avatarsdk-latest-concepts-legacy-avatars-gsg-unity-1.jpg)  
To render an avatar body:1. In the **Hierarchy** window, select **LocalAvatar**.
2. In the **Inspector** window, select the **Show Third Person** check box.
3. Change **Transform > Position** to X:0 Y:0 Z:1.5
4. Change **Transform > Rotation** to X:0 Y:180 Z:0
![](/images/documentation-avatarsdk-latest-concepts-legacy-avatars-gsg-unity-2.jpg)  
## Recording and Playing Back Avatar Pose Updates

The avatar packet recording system saves avatar movement data as packets you can send across a network to play back on a remote system. Lets take a quick tour of the RemoteLoopbackManager script.

Open the **RemoteLoopback** scene in **OvrAvatar > Samples > RemoteLoopback**.

We set RecordPackets to true to start the avatar packet recording system. We also subscribe to the event handler PacketRecorded so that we can trigger other actions each time a packet is recorded.

void Start () { LocalAvatar.RecordPackets = true; LocalAvatar.PacketRecorded += OnLocalAvatarPacketRecorded; }Each time a packet is recorded, our code places the packet into a memory stream we are using as a stand-in for a real network layer.

void OnLocalAvatarPacketRecorded(object sender, args) { using (MemoryStream outputStream = new MemoryStream()) { BinaryWriter writer = new BinaryWriter(outputStream); writer.Write(packetSequence++); args.Packet.Write(outputStream); SendPacketData(outputStream.ToArray()); } }The remainder of our code receives the packet from the memory stream for playback on our loopback avatar object.

void SendPacketData(byte[] data) { ReceivePacketData(data); } void ReceivePacketData(byte[] data) { using (MemoryStream inputStream = new MemoryStream(data)) { BinaryReader reader = new BinaryReader(inputStream); int sequence = reader.ReadInt32(); OvrAvatarPacket packet = OvrAvatarPacket.Read(inputStream); LoopbackAvatar.GetComponent<OvrAvatarRemoteDriver>().QueuePacket(sequence, packet); } }