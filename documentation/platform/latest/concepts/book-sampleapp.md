---
title: Sample Apps
---

The Oculus Platform SDK sample apps are provided examples of how to initialize the SDK, perform the entitlement check, and implement some of the platform features.

These sample apps can be used either as a reference for integrating the Platform SDK in your app, or as a foundation that you can use to build your VR experience.

The features implementations are similar with native and Unity apps, so review all of the apps below, even if they are using a different development platform. 

This guide describes the sample apps at a very high-level, each app contains inline comments that provide more detail. 

## Get Started

To get started using the sample apps, download the latest version of the Platform SDK from the [downloads page](/downloads/). The sample apps are in each SDK download in a samples folder (`OVRPlatformSDK_vX.XX.X`/Samples). The three Unity apps described on this page are in the Unity folder (`OVRPlatformSDK_vX.XX.X`/Samples/Unity). Each sample contains a readme file to help you get started with the sample app. 

Then, if you have not done so already, [create a publisher account](/publish-guidelines/) on the Developer Console. In your publisher account create an application and retrieve the App Id from the [API](https://dashboard.oculus.com/app/api) tab. See [Creating and Managing Apps](/distribute/latest/concepts/publish-create-app/) for information about how to create a new application.

Before using the sample apps, you'll need to configure your development environment. Please see the [Getting Started Guide](/documentation/platform/latest/concepts/book-pgsg/) for information about configuring your development environment. 

**Grouping Gear VR and Rift Apps**

If you’re creating both a Rift and Gear VR application, you can move the Gear VR application into the Rift application’s [App Grouping](/distribute/latest/concepts/publish-create-app/). Then, copy the OSIG files for the Gear VR devices you are testing to `Assets\Plugins\Android\Assets`. This will allow cross-platform interactions between Rift and Gear VR users. The VRHoops, VRVoiceChat, and VRBoardGame apps below support cross-platform interaction. 

## Unity Sample Apps

**Social Starter**

The Unity Social Starter example scene demonstrates using Oculus Avatars together with Oculus Platform features such as invites, peer-to-peer networking, and VoIP. Please see the [Unity Social Starter Example](/documentation/avatarsdk/latest/concepts/legacy-avatars-sdk-unity-example-social/) page for details.

**VRHoops**

VRHoops uses [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/) (Quickmatch) and [Peer-to-Peer Networking](/documentation/platform/latest/concepts/dg-p2p/) to create a cross-platform ball shooting game. Quickmatch is used to find other players for a match and P2P is used to synchronize player state such as movement of the balls. Also, VRHoops also includes [Leaderboards](/documentation/platform/latest/concepts/dg-cc-leaderboards/) to track player scores and [Achievements](/documentation/platform/latest/concepts/dg-achievements/) to track how many times a player has won.

Please see the readme file included with VRHoops for information on how to configure Matchmaking, Achievements, and Leaderboards in the sample app. 

**VRVoiceChat**

VRVoiceChat is a simple app that demonstrates voice chat using [Rooms](/documentation/platform/latest/concepts/dg-rooms/) (invites), [Voice Chat](/documentation/platform/latest/concepts/dg-cc-voip/) (sending and receiving voice chat) and [Peer-to-Peer Networking](/documentation/platform/latest/concepts/dg-p2p/) (sharing headset positions and rotations).

**VRBoardGame**

VRBoardGame demonstrates the use of [Commerce (IAP)](/documentation/platform/latest/concepts/dg-iap/) and skill-based [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/). VRBoardGame is a simple two player game set on a 3x3 grid with two pieces and a special 'power-piece' that can be acquired with an in-app purchase through the Oculus Store. After an online match is completed, the ranking is sent to the matchmaking service so future match selections will take the user's skill level into account.

## Native Sample Apps

**CloudStorageExample**

The CloudStorageExample demonstrates how to use [Cloud Storage](/documentation/platform/latest/concepts/dg-cc-cloud-storage/) to save game information.

Gameplay in the app is a simple game of chance, encountering the largest random integer. See `RandomGame::Tick` for the details.

 Three different saves are stored in the cloud and loaded at startup:

* The highest score ever recorded.
* The most recent high score.
* The highest score on each device.


In this app, the `PlatformManager` class polls the `LibOVRPlatform` message queue for messages, and forwards all the Cloud Storage messages to the `CloudStorageManager` class.

`CloudStorageManager` transitions the game to running over after it loads all the saved metadata and data. The data in the "Latest High Score" and "Overall Highest Score" buckets are simple to deal with since you don’t need to perform any conflict resolution from multiple devices.

The save stored in the "Local High Scores" bucket is more complicated because it demonstrates handling conflicts that arise from loading both saved files and merging them together.

## Unreal Sample App

The Unreal **OculusPlatformSample** demonstrates how to use a number of platform features in Unreal, using both blueprints and code. **OculusPlatformSample** includes [Achievements](/documentation/platform/latest/concepts/dg-achievements/),[Leaderboards](/documentation/platform/latest/concepts/dg-cc-leaderboards/), [OSS Sessions - Rooms and Matchmaking](/documentation/platform/latest/concepts/dg-oss-sessions/), and [Voice Chat (VoIP)](/documentation/platform/latest/concepts/dg-cc-voip/).
