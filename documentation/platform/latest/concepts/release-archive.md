---
title: Previous Platform SDK Version Release Notes
---

Feature updates and changes in the legacy versions of the Platform SDK.

## Overview of Oculus Platform SDK Version 1.24

The Oculus Platform SDK 1.24 release includes the following new features.

**Oculus recommends that all Unity developers who have previously used Standalone Mode upgrade to Platform 1.24. This version fixes an issue where developer credentials may be stored locally in an insecure manner. Once you have upgraded to 1.24, add your developer credentials as described in the **Use the SDK in Standalone Mode** section in [Unity Development Getting Started](/documentation/platform/latest/concepts/pgsg-unity-gsg/).**

**New Features**

* Unreal Sample - Platform SDK 1.24 contains an updated Unreal sample that demonstrates the use of many of the Platform features. See the Sample Apps page for more information. 


**Bug Fixes**

* Fixes an issue where a developer's credentials may be insecurely stored in the Unity Editor.


**API Changes**

* There are no breaking changes to version 1.24.


## Overview of Oculus Platform SDK Version 1.20

The Oculus Platform SDK 1.20 release includes the following new features.

**New Features**

* Added App Deeplinking to the Platform SDK. App Deeplinking allows you to launch users directly into an app event or gameplay mode from another app. See the [App Deeplinking](/documentation/platform/latest/concepts/dg-deeplinking/ "App Deeplinking allows you to launch users directly into an app event or gameplay mode.") page for more information.


**API Changes**

* There are no breaking changes to version 1.20.


## Overview of Oculus Platform SDK Version 1.19

The Oculus Platform SDK 1.19 release includes the following new features.

**New Features**

* Photo Sharing is available for Gear VR. Photo Sharing allows users to post screen captures they take in VR to their Facebook network. See [Sharing](/documentation/platform/latest/concepts/dg-sharing/ "The Oculus Platform allows users to share their VR experience with their Facebook network.") for more information about Photo Sharing.
* The [Matchmaking and Room Debugger](https://dashboard.oculus.com/tools/rooms-and-matchmaking-debugger/) tool is now available to help developers identify the connections and interactions made by a user or room. See the Matchmaking [Testing and Tuning](/documentation/platform/latest/concepts/dg-matchmaking-5debugging/) page for more information. 


**API Changes**

* There are no breaking changes to version 1.19.


## Overview of Oculus Platform SDK Version 1.18

The Oculus Platform SDK 1.18 release includes the following new features.

**New Features**

* Profile Card API - On Gear VR you can use ovr\_User\_LaunchProfile to launch a profile that displays the Oculus name, ID, online status, recent interactions, and mutual friends for a specified user. The profile also allows a friend request to be sent. Please see the [Users, Friends, and Relationships](/documentation/platform/latest/concepts/dg-presence/ "Users, friends, and relationships manages information about each user's unique persona, their relationship with their friends, and their recent encounters in VR.") page for additional information.
* Recently Met API - Use ovr\_User\_GetLoggedInUserRecentlyMetUsersAndRooms to retrieve a list of users who the logged-in user recently interacted with in your app. Interesting users, users who interact frequently or for a long duration, will be returned first. Oculus tracks the number of times users meet in VR, their most recent encounter, and the amount of time they spend together. Please see the [Users, Friends, and Relationships](/documentation/platform/latest/concepts/dg-presence/ "Users, friends, and relationships manages information about each user's unique persona, their relationship with their friends, and their recent encounters in VR.") page for additional information.
* Room Notifications - You'll now receive a room update notification if the user is removed from a room by Oculus. Please see the [Rooms](/documentation/platform/latest/concepts/dg-rooms/ "Rooms are virtual places where users come together to interact in your app.") guide for information about handling room updates.


**Platform Reference**

* Platform SDK Reference - The Platform SDK reference has changed. Starting with 1.18 the reference materials will be hosted in a manner similar to the other Oculus SDKs. You'll always be able to find a link to the latest version on the [Reference Content](/documentation/platform/latest/concepts/book-reference/ "The Platform SDK developer reference contains a complete list of the Platform SDK headers, functions, and data structures.") page.


**API Changes**

* There are no breaking changes to version 1.18.


## Overview of Oculus Platform SDK Version 1.17

The Oculus Platform SDK 1.17 release includes the following new features.

**New Feature**

* Standalone Initialization - Standalone initialization is now available for Unity. Read about initializing the SDK in standalone mode in [Native Development Getting Started](/documentation/platform/latest/concepts/pgsg-native-gsg/ "The native getting started guide will walk you through the basics of setting up your development environment, initializing the SDK, and checking the user's entitlement.") or [Unity Development Getting Started](/documentation/platform/latest/concepts/pgsg-unity-gsg/ "The Unity getting started guide will walk you through the basics of setting up your development environment, initializing the SDK, and checking the user's entitlement.").
* Rooms Invites Push Notifications - The Platform SDK will now send notifications to the message queue when a user has been invited to join a room. Information about room invite notifications can be found in the [Rooms](https://developer.oculus.com/documentation/platform/latest/concepts/dg-rooms) guide.
* Rift Parties - Rift now supports Parties. Parties allow users to chat wherever they are in VR, including your app. Please review the [Parties](https://developer.oculus.com/documentation/platform/latest/concepts/dg-cc-parties/) guide for information about how to handle potential conflicts with VoIP streams.


**API Changes**

* There are no breaking changes to version 1.17.


## Overview of Oculus Platform SDK Version 1.16

The Oculus Platform SDK 1.16 release includes the following new features.

**New Feature**

* User and Friends - When retrieving a list of a user's friends, the Oculus Platform will now order the friends list by online presence. Friends active within your app will be returned first. 
* VoIP - Improvements to the VoIP service to minimize network bandwidth used by the Platform VoIP service. 


**API Changes**

* There are no breaking changes to version 1.16.


## Overview of Oculus Platform SDK Version 1.15

The Oculus Platform SDK 1.15 release includes the following new feature and bug fix.

**New Feature**

* Two new Discoverability features are now available for Gear VR apps. Use targeted Announcements and In-App Content stories to bring users into your app. Review the [Discoverability](https://developer.oculus.com/documentation/platform/latest/concepts/dg-discoverability/) documentation for more information.


**API Changes**

* There are no breaking changes to version 1.15.


**Bug Fix**

* Fixed a Matchmaking deadlock issue that caused users to not be matched by the service.
* General Platform SDK performance improvements and bug fixes.


## Overview of Oculus Platform SDK Version 1.14

The Oculus Platform SDK 1.14 release includes the following new feature and bug fix.

**New Feature**

* Added ovr\_Platform\_InitializeStandaloneOculus that allows you to initialize the Platform SDK in standalone mode for local testing. See [Getting Started Guide](/documentation/platform/latest/concepts/book-pgsg/ "The Getting Started Guide will review the onboarding and basic integration process for the Platform SDK, how to configure your development environment, and how to implement the required components of the SDK.") for information about the SDK initialization methods. 


**Bug Fix**

* Multiple back-end changes to RoomsManager that improve handling of out-of-order updates. Resolves an issue where users received room updates from rooms they had previously created and joined. 


## Overview of Oculus Platform SDK Version 1.13

The Oculus Platform SDK 1.13 release includes the following new features.

**New Features**

* Asynchronous initialization API - ovr\_PlatformInitializeWindowsAsynchronous (Native Rift), ovr\_PlatformInitializeAndriodAsynchronous (Native Gear VR), and Platform.Core.AsyncInitialize (Unity). Use the asynchronous API to initialize the SDK with an intermediate state that allows your app to run other processes and make requests to the Platform SDK while initializing. Requests made to the Platform SDK while initializing will be queued to run after SDK initialization has completed. See [Getting Started Guide](/documentation/platform/latest/concepts/book-pgsg/ "The Getting Started Guide will review the onboarding and basic integration process for the Platform SDK, how to configure your development environment, and how to implement the required components of the SDK.") for more information.
* Livestream testing - New feature to test how apps will perform while a user is Livestreaming. See [Sharing](/documentation/platform/latest/concepts/dg-sharing/ "The Oculus Platform allows users to share their VR experience with their Facebook network.") for more information.


## Overview of Oculus Platform SDK Version 1.12.1

The Oculus Platform SDK 1.12 release includes the following minor improvements and bug fixes.

Version 1.12.1 fixes an issue introduced by 1.12. 

**API Changes**

* Matchmaking - Change that allows developers to change enqueue options without first having to call ovr\_Matchmaking\_Cancel2.


## Overview of Oculus Platform SDK Version 1.11

The Oculus Platform SDK 1.11 release includes minor improvements, bug fixes, and updates. These include:

**New Features**

* Turn host migration on / off when configuring Advanced Quickmatch rooms.


**API Changes**

* Matchmaking - Room\_KickUser now allows a room owner to kick other users from a matchmaking room. 
* User 
	+ User\_GetLoggedInUserFriends now returns results in improved sort order based on online status and app status. 
	+ Added User\_GetLoggedInUserFriendsAndRooms. New API to retrieve a list of a user's logged in friends and the rooms they are in. 
	
* Rooms 
	+ Room\_Join2 now allows a user to update the room metadata if they become the room owner. 
	+ Room\_GetInvitableUsers2 now returns results in improved sort order based on online status and app status. 
	


**Bug Fixes**

* Fixed bug where matchmaking room notifications may be received out of order.


## Overview of Oculus Platform SDK Version 1.10

The Oculus Platform SDK 1.10 release includes minor improvements, bug fixes, and updates. These include:

* Updated two Unity sample apps that cover matchmaking, P2P, VoIP, and rooms (Gear and Rift).
* Added VoIP support to UE4.
* Added UE4 browse mode.
* Added some private room matchmaking features to public rooms.
* Improved leaderboard support in the Dashboard (paging, reset/clear leaderboards).


## Overview of Oculus Platform SDK Version 1.9

The Oculus Platform SDK 1.9 release includes minor improvements, bug fixes, and updates.

* Simplified how to specify matchmaking queries and query variables. Additionally, introduced a new matchmaking argument request structure to make it easier to modify future versions without breaking backwards compatibility. For more information, see [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/ "Matchmaking places users together in a shared multiplayer experience. User matching can be done by common skill or other criteria that you define. The Matchmaking service offers two modes, Quickmatch and Browse.").
* Updated room invites documentation. For more information, see [Rooms](/documentation/platform/latest/concepts/dg-rooms/ "Rooms are virtual places where users come together to interact in your app.").


## Overview of Oculus Platform SDK Version 1.8

The Oculus Platform SDK 1.8 release includes minor improvements, bug fixes, and updates.

* Added a new Quickmatch matchmaking mode. For more information, see [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/ "Matchmaking places users together in a shared multiplayer experience. User matching can be done by common skill or other criteria that you define. The Matchmaking service offers two modes, Quickmatch and Browse.").
* You can now subscribe to updates to observer room joins and leaves. For more information, see [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/ "Matchmaking places users together in a shared multiplayer experience. User matching can be done by common skill or other criteria that you define. The Matchmaking service offers two modes, Quickmatch and Browse.").
* Updated matchmaking queries. For more information, see [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/ "Matchmaking places users together in a shared multiplayer experience. User matching can be done by common skill or other criteria that you define. The Matchmaking service offers two modes, Quickmatch and Browse.").


## Overview of Oculus Platform SDK Version 1.7

The Oculus Platform SDK 1.7 release includes minor improvements, bug fixes, and updates.

* **VoIP Filters:** You can now add voice effects to VoIP communications. For more information, see [Voice Chat (VoIP)](/documentation/platform/latest/concepts/dg-cc-voip/ "Use the Platform VoIP service to add voice chat to your app.").
* **Developer and Admin Entitlements:** Developers and admins automatically get entitlements to all apps within that organization.


## Overview of Oculus Platform SDK Version 1.6

The Oculus Platform SDK 1.6 release includes improvements to storing user game data in the cloud, achievements, and auto-updates for Gear VR apps.

* **Cloud Storage update:** You can now delete stored data. For example, you can let your users decide to delete saved games.
* **Achievements update:** You can now design a specific cosmetic appearance for your achievements using our API.
* **Matchmaking update:** Matchmaking now supports multiple players in all modes.
* **Separable API update:** Only the libovrplatformloader.so is required for auto-updates for native Gear VR apps.


## Overview of Oculus Platform SDK Version 1.5

The Oculus Platform SDK 1.5 release includes new functionality, including more options for room invites, an end-to-end VoIP API for multi-player voice communication, and the option to store user game data in the cloud.

* **Room Invites:** Room invites are the best way to allow the users of your app to initiate a shared game. Use the Oculus System UI, or build your own UI if you wish.
* **VoIP:** Use VoIP to permit direct voice communication among users of your app.
* **Cloud Storage** Store user data, like game-save data, in the cloud so users can access their games from any computer.
* **Separable API:** For Gear VR apps, the new Oculus platform SDK files libovrplatformloader.so and svcloader.jar will silently auto-update in the background from now on, just as currently happens with Platform SDK .dll files for Rift apps.


## Overview of Oculus Platform SDK Version 1.2.x

The 1.2.0 release adds Unreal Engine support, as well as improvements to Unity friend requests, P2P API, error messages, and matchmaking debugging. 

* Initial release of UE4 plugin, for apps made with Unreal Engine, with:


	+ OnlineSubsystemOculus
	
	
		- Entitlement and user's Oculus username — UE4 OnlineIdentityInterface
		- User's friends list — UE4 OnlineFriendsInterface
		- Achievements — UE4 OnlineAchievementsInterface
		- Rooms and Matchmaking — UE4 OnlineSessionInterface
		
	+ OculusNetDriver
	
	
		- UE4 Networking with Oculus usernames
		
	
* Unity support for friend requests:


	+ Ability to mark notifications as read, as well as retrieve RoomInvites from the server — ovr\_Notification\_GetRoomInvites
	+ Unity callback — RoomInviteNotification
	
* P2P API improvements:


	+ Check for open connections to a given peer — ovr\_Net\_IsConnected()
	+ Broadcast a single packet to all members of a room — ovr\_Net\_SendPacketToCurrentRoom()
	+ Enforce automatic acceptance of connection attempts from room members — ovr\_Net\_AcceptForCurrentRoom()
	+ Change state when a peer explicitly closes their end of the connection, or when a previously-open connection breaks — ovrPeerState\_Closed added to ovrPeerConnectionState
	
* Improved error messaging: call the function ovr\_Error\_GetDisplayableMessage to show a customized error message for Oculus Platform SDK calls
* Matchmaking debug enhancement: matchmaking\_pool\_for\_admin graph API node is now available for debugging


## Overview of Oculus Platform SDK Version 1.1.0

The 1.1.0 release focuses on performance improvements and minor bug fixes. 

* Removed exports that prevent linking with UE4 in some cases.
* Fixed message parsing resulting from ovr\_Matchmaking\_JoinRoom.


## Overview of Oculus Platform SDK Version 1.0.0

Release 1.0.0 is a maintenance release leading up to Rift launch.

* A number of new Leaderboard management web APIs were added to the REST API documentation.
* When joining a room once a match has been found, please switch from using ovr\_Room\_Join to ovr\_Matchmaking\_JoinRoom. ovr\_Room\_Join will soon be deprecated for matchmaking rooms, but will continue to work for released games and joining non-matchmaking rooms.
* When canceling an enqueuement, switch from using ovr\_Matchmaking\_Cancel to ovr\_Matchmaking\_Cancel2. You no longer need to pass in the request hash. With the new changes, you no longer need to care about request hashes at all.

