---
title: OSS Sessions - Rooms and Matchmaking
---
 Matchmaking and Rooms in Unreal uses the OSS Sessions interface.

The Oculus OSS Sessions integration is based on the concepts introduced in Epic's [Sessions and Matchmaking](https://docs.unrealengine.com/latest/INT/Programming/Online/Interfaces/Session/index.html) guide. Most of the functionality for Rooms and Matchmaking build on Epic's [IOnlineSession](https://docs.unrealengine.com/latest/INT/API/Plugins/OnlineSubsystem/Interfaces/IOnlineSession/) APIs. 

Both the Rooms and Matchmaking integrations using the OSS Sessions interface are limited in scope. For a full-featured Room and Matchmaking integration, please use the native C APIs.

Please note that when a session is created, either Room or Matchmaking, a VoIP connection is not created. You'll have to integrate [Voice Chat (VoIP)](/documentation/platform/latest/concepts/dg-cc-voip/ "Use the Platform VoIP service to add voice chat to your app.") if you want to enable voice chat in your app.

## About Rooms

Oculus uses Rooms as a place for players to gather, these Rooms map to Sessions in Unreal. Oculus Rooms can be expressed in your app in multiple ways: user rooms, matchmaking rooms, and moderated rooms. We'll discuss how to add matchmaking rooms in the next section, while moderated rooms are created by the server-to-server API calls defined on the [Rooms](/documentation/platform/latest/concepts/dg-rooms/ "Rooms are virtual places where users come together to interact in your app.") page.

 User rooms are not enqueued in the matchmaking service and can not later be promoted.

**Integrate User Rooms**

The following steps describe a basic Rooms integration.

**Blueprint**

1. User wants to join a room:
	* Add the **Join Session** blueprint Node. 
	
2. User wants to create a room:
	* Add **Create Session** to your app blueprint. Leave the name of **Oculus Matchmaking Pool** blank.
	
**Code**

1. User wants to join a room:
	* Call JoinSession().
	
2. User wants to create a room:
	* Call CreateSession() with NewSessionSettings.Settings as null.
	
## About Matchmaking

The process to add matchmaking requires that you first create the matchmaking pools, then add the matchmaking service to your app. This guide will review some of the basics and background required for the Unreal integration, but we recommend that you review the complete native [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/ "Matchmaking places users together in a shared multiplayer experience. User matching can be done by common skill or other criteria that you define. The Matchmaking service offers two modes, Quickmatch and Browse.") guide for a complete overview of the matchmaking service as well as how to create and manage Moderated Rooms. 

**Matchmaking Modes**

There are two supported matchmaking modes, Quickmatch and Browse. Choose the multiplayer experience that you want your players to have.

* **Quickmatch** - Quickmatch allows players to join a matchmaking queue, and be automatically matched into a room for a multiplayer session. There are two types of Quickmatch:


	+ **Simple Quickmatch** - In Simple Quickmatch, rooms are created for players once a match has been made. Simple Quickmatch is designed for 2 player games, like chess or checkers, where users don't need the ability to join matches in progress.
	+ **Advanced Quickmatch** - Advanced Quickmatch can be configured where rooms are created by the user, by the Matchmaking service, or both. This allows the matchmaking service to host two matchmaking queues, one for rooms supporting multiple game settings and one for users looking for rooms. Use this mode for more complicated games with multiple match options or settings, and where users may join, or leave, during the course of a match. 
	
* **Browse** - In Browse, users can create and host rooms or choose from a list of rooms to join. Browse also supports more complicated games with multiple match options or settings, and where users may want to join, and leave, a match in progress. 
Before integrating Matchmaking, you'll need to create your pools of users. Please see the **Pools** section of the [Configuration Overview](/documentation/platform/latest/concepts/dg-matchmaking-2a_platform_overview/) page for information about creating Matchmaking and Skill Pools. Please note that the Data Settings and Matchmaking Queries described on that page are not available through the OSS interface.

**Integrate Matchmaking - Quickmatch**

The following steps describe a basic Quickmatch integration.

**Blueprint**

1. Create a Quickmatch Matchmaking pool. Example pools can be found on the [Matchmaking Quickstart w/Advanced Options](/documentation/platform/latest/concepts/dg-matchmaking-3quickstart/) page.
2. User wants to join a match:
	* Add **Join Session** to your app blueprint to enqueue the player in the Matchmaking service. 
	
3. User wants to create a match (Advanced Quickmatch only):
	* Add **Create Session** to your app blueprint, pass the name of the Matchmaking pool you created. The room will be automatically enqueued in the Matchmaking service.
	
4. (Optional) At any time, you may use the **Set Session Enqueue** to enqueue or dequeue the current session in the matchmaking pool.
**Code**

1. Create a Quickmatch Matchmaking pool. Example pools can be found on the [Matchmaking Quickstart w/Advanced Options](/documentation/platform/latest/concepts/dg-matchmaking-3quickstart/) page.
2. User wants to join a match:
	* Call StartMatchmaking() to enqueue the user in the Matchmaking service. Pass the key for the matchmaking pool you created to start matchmaking. 
	
3. User wants to create a match (Advanced Quickmatch only):
	* Call CreateSession() with NewSessionSettings.Settings as the key for the matchmaking pool you created and NewSessionSettings.bShouldAdvertise as true to enqueue the session in the Matchmaking service. If the user wants to remove the room from the Matchmaking service, call UpdateSession() with UpdatedSessionSettings.bShouldAdvertise as false. 
	
**Integrate Matchmaking - Browse**

The following steps describe a basic Browse integration.

**Blueprint**

1. Create a Browse Matchmaking pool. Example pools can be found on the [Matchmaking Quickstart w/Advanced Options](/documentation/platform/latest/concepts/dg-matchmaking-3quickstart/) page.
2. User wants to join a match:
	* Add **Find Matchmaking Sessions** to your app blueprint and pass the name of your Matchmaking pool to retrieve a list of available sessions. If using Moderated rooms, add **Find Moderated Sessions** instead.
	* Then when the user has selected their desired session, pass the SessionName to the **Join Session** blueprint Node. 
	* Optional - When you display the list of rooms to the user, you can retrieve metadata about the room by adding the **Get Current Players**, **Get Max Players**, **Get Ping in MS**, and **Get Server Name** nodes.
	
3. User wants to create a match (if supported):
	* Add **Create Session** to your app blueprint, pass the name of the matchmaking pool you created. The room will be automatically enqueued.
	
4. (Optional) At any time, you may use the **Set Session Enqueue** to enqueue or dequeue the current session in the matchmaking pool.
**Code**

1. Create a Browse Matchmaking pool Example pools can be found on the [Matchmaking Quickstart w/Advanced Options](/documentation/platform/latest/concepts/dg-matchmaking-3quickstart/) page.
2. User wants to join a match: 
	* First call FindSessions() and pass the name of your matchmaking pool to retrieve a list of available sessions. Define QuerySettings as OCULUSPOOL in the SearchSettings if finding Matchmaking rooms or define QuerySettings as OCULUSMODERATEDROOMSONLY if using Moderated rooms.
	* Then when the user has selected their desired session, call JoinSession().
	
3. User wants to create a match (if supported): 
	* Call CreateSession() with NewSessionSettings.Settings as the key of your matchmaking pool and NewSessionSettings.bShouldAdvertise as true to enqueue the session in the Matchmaking service. If the user wants to remove the room from the matchmaking service, call UpdateSession() with UpdatedSessionSettings.bShouldAdvertise as false. 
	
