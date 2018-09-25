---
title: Matchmaking
---
Matchmaking places users together in a shared multiplayer experience. User matching can be done by common skill or other criteria that you define. The Matchmaking service offers two modes, Quickmatch and Browse.

Note: This guide only describes how to implement Matchmaking in native and Unity applications. If you're build an app in Unreal, please see the [OSS Sessions - Rooms and Matchmaking](/documentation/platform/latest/concepts/dg-oss-sessions/ "Matchmaking and Rooms in Unreal uses the OSS Sessions interface.") page.Matchmaking works in combination with another Oculus Platform feature, [Rooms](/documentation/platform/latest/concepts/dg-rooms/ "Rooms are virtual places where users come together to interact in your app."), to provide a full multiplayer experience in VR. Matchmaking places users together in a room for a gameplay session, and the room the hosts and manages the gameplay session. Please see the [Rooms](/documentation/platform/latest/concepts/dg-rooms/ "Rooms are virtual places where users come together to interact in your app.") page for information about the different types of rooms available. For the purposes of integrating Matchmaking, you should be aware that there are two different types of matchmaking rooms that are used by the service, user-created matchmaking rooms and system-generated matchmaking rooms. As the names suggests, user-created rooms are created and owned by users, where system-generated rooms are created and owned by your app.

Matchmaking is frequently used in combination with [Leaderboards](/documentation/platform/latest/concepts/dg-cc-leaderboards/ "Leaderboards create competition and increase engagement among your users.") to rank and compare multiplayer users creating a competition among players. 

**Matchmaking Modes**

There are two supported matchmaking modes, Quickmatch and Browse. Choose the multiplayer experience that you want your players to have.

* **Quickmatch** - Quickmatch allows players to join a matchmaking queue, and be automatically matched into a room for a multiplayer session. There are two types of Quickmatch:


	+ **Simple Quickmatch** - In Simple Quickmatch, rooms are created for players once a match has been made. Simple Quickmatch is designed for 2 player games, like chess or checkers, where users don't need the ability to join matches in progress.
	+ **Advanced Quickmatch** - Advanced Quickmatch can be configured where rooms are created by the user, by the Matchmaking service, or both. This allows the matchmaking service to host two matchmaking queues, one for rooms supporting multiple game settings and one for users looking for rooms. Use this mode for more complicated games with multiple match options or settings, and where users may join, or leave, during the course of a match. 
	
* **Browse** - In Browse, users can create and host rooms or choose from a list of rooms to join. Browse also supports more complicated games with multiple match options or settings, and where users may want to join, and leave, a match in progress. 
## Using this Guide

This guide will walk you through the matchmaking configurations, SDK basics, a basic matchmaking implementation, how to add more advanced user matching, and finally how to test and tune your implementation. We recommend reading through the whole guide before you begin your integration.

* **[Configuration Overview](/documentation/platform/latest/concepts/dg-matchmaking-2a_platform_overview/)**  

* **[SDK Overview](/documentation/platform/latest/concepts/dg-matchmaking-2b_sdk_overview/)**  

* **[Matchmaking Quickstart w/Advanced Options](/documentation/platform/latest/concepts/dg-matchmaking-3quickstart/)**  

* **[Adding Skill and Using Queries](/documentation/platform/latest/concepts/dg-matchmaking-4skill_queries/)**  

* **[Testing and Tuning](/documentation/platform/latest/concepts/dg-matchmaking-5debugging/)**  

