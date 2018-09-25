---
title: Matchmaking Quickstart w/Advanced Options
---
Now that you’ve familiarized yourself with the Platform and SDK configurations, we can start to implement Matchmaking in your game. We recommend integrating the Matchmaking service in steps, starting with the basics and then introducing the additional configurations like Data Settings, Queries, and Skill. We'll review how to add those on the [Adding Skill and Using Queries](/documentation/platform/latest/concepts/dg-matchmaking-4skill_queries/) page.

The first step is to determine what type of game you’re making. We introduced the different modes in [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/ "Matchmaking places users together in a shared multiplayer experience. User matching can be done by common skill or other criteria that you define. The Matchmaking service offers two modes, Quickmatch and Browse."), and different game types call for different Matchmaking modes.

We’ll review a basic implementation for Simple Quickmatch, Advanced Quickmatch, and Browse. Details about Pool configurations were introduced on the [Configuration Overview](/documentation/platform/latest/concepts/dg-matchmaking-2a_platform_overview/) page.

## Simple Quickmatch

Let's start with the most basic Matchmaking scenario and make a 2 player game where we won't match based on skill. For example, a board game like checkers or tic-tac-toe may want to use Simple Quickmatch. Simple Quickmatch will match users into system-generated rooms. 

1. Create your matchmaking pool, in the [Matchmaking](https://dashboard.oculus.com/app/matchmaking) section of the Developer Center, with the following configurations: 
	* **Pool Key** = TicTacToe\_BestOfThree or any value you'd like to use in your game.
	* **Mode** = Quickmatch
	* **Users per Match** = 2 for all fields. 
	* **Skill Pool** = None
	* **Advanced Quickmatch** = No
	* **Should Consider Ping Time?** = No
	* When you're finished entering the pool configurations, select **Save and Deploy** to save the pool.
	
2. After you've created your pool, you can begin integrating into your client-side app. To add the user to the matchmaking queue, call ovr\_Matchmaking\_Enqueue2() from the client app. The user will be continually re-enqueued until they are successfully matched or cancel the process. After enqueueing the user, listen for the match notification ovrMessage\_Notification\_Matchmaking\_MatchFound. Information about how the Platform SDK uses notifications can be found on the [Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/ "The Platform SDK uses a message queue to interact with Native apps. This page describes the concept of the queue and how to retrieve messages and information.") page. 
3. (Optional) Review the methods in the OVR\_MatchmakingEnqueueResult.h file for a list of methods you can call for information about the health of the queue that you may display to the user at this time. 
4. In your notification handler, call ovr\_Room\_Join2 with the roomID from the notification to place the user into the room.
5. Your game will be listening for ovrNotification\_Room\_RoomUpdate for the number of users in the room. When the desired number of users is reached, your app will launch the game. 
6. At any time in the matchmaking process, the user can call ovr\_Matchmaking\_Cancel2() to remove themselves from the queue and exit the matchmaking process. 
**Example Implementation**

Our Unity sample app, VRHoops, is a simple ball shooting game that uses Simple Quickmatch. Please see the [Sample Apps](/documentation/platform/latest/concepts/book-sampleapp/) page for more information about the available sample apps.

## Advanced Quickmatch

If we're building a multiplayer game that involves more players (2-8) and has multiple modes, using Advanced Quickmatch will allows both users and the Matchmaking service to create rooms and matches for multiple users. For example, a first-person shooter may want to use Advanced Quickmatch as there may be multiple maps or users may wish to join matches already in progress. 

1. Create your matchmaking pool, in the [Matchmaking](https://dashboard.oculus.com/app/matchmaking) section of the Developer Center, with the following configurations: 
	* **Pool Key** = CaptureTheFlag\_TwoVsTwo or any value you'd like to use in your game.
	* **Mode** = Quickmatch
	* **Users per Match** = 2 for Min Users. 4 for Min Preferred. 6 for Max Preferred. 8 for Max Users.
	* **Skill Pool** = None
	* **Advanced Quickmatch** = Yes
		1. **Can people create and enqueue rooms themselves?** - Yes
		2. **Can the system create rooms to match people into?** - Yes
		3. **Can unmatched people join matchmaking rooms?** - Yes
		4. **Can the matchmaking service keep matching into the same room?** - Yes
		5. **Enable host migration when the room owner leaves the room?** - No (Please review the Room Ownership section below for more information about host migration. This feature requires an additional integration.)
		
	* **Should Consider Ping Time?** - No
	* When you're finished entering the pool configurations, select **Save and Deploy** to save the pool.
	
2. After you've created your pool, you can begin integrating into your client-side app. You may need to support multiple scenarios depending on the configuration settings you chose when creating your Pool and how the user wants to use the matchmaking service. Our pool configuration allows both users and the system to create rooms, so we'll need to be able to handle both scenarios. 
	* If a user wants to join a match: 
		1. Call ovr\_Matchmaking\_Enqueue2. The user will be continually re-enqueued until they are successfully matched or cancel the process.
		2. Handle the notification that the user was enqueued, ovrMessage\_Matchmaking\_Enqueue2. Information about how the Platform SDK uses notifications can be found on the [Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/ "The Platform SDK uses a message queue to interact with Native apps. This page describes the concept of the queue and how to retrieve messages and information.") page. 
		3. (Optional) Review the methods in the OVR\_MatchmakingEnqueueResult.h file for a list of methods you can call for information about the health of the queue to display to the user. 
		4. Be listening for the match notification, ovrMessage\_Notification\_Matchmaking\_MatchFound.
		5. In your notification handler, call ovr\_Room\_Join2 to place the user into the room identified in the MatchFound notification.
		
	* If the user wants to create a room and host a match: 
		1. To create and enqueue the user and room, call either ovr\_Matchmaking\_CreateAndEnqueueRoom2 or ovr\_Matchmaking\_CreateRoom2, handle the response, and then call ovr\_Matchmaking\_EnqueueRoom2. The Room will be continually re-enqueued until canceled or a match is found.
		2. Handle the ovrMessage\_Matchmaking\_CreateAndEnqueueRoom2 or ovrMessage\_Matchmaking\_EnqueueRoom2 response. 
		3. (Optional) Review the methods in the OVR\_MatchmakingEnqueueResult.h file for a list of methods you can call for information about the health of the queue to display to the user. 
		4. The Matchmaking service will search for matches. 
		
	
3. Your game will be listening for ovrNotification\_Room\_RoomUpdate for the number of users in the room. When the desired number of users is reached, your app will launch the game.
4. At any time in the matchmaking process, the user can call ovr\_Matchmaking\_Cancel2() to remove themselves from the queue and exit the matchmaking process. 
## Browse

Finally, lets create a simple game where you allow users to browse and select the match that they want to join.

1. Create your matchmaking pool, in the [Matchmaking](https://dashboard.oculus.com/app/matchmaking) section of the Developer Center, with the following configurations: 
	* **Pool Key** = FreeForAll\_Browse or any value you'd like to use in your game.
	* **Mode** = Browse
	* **Users per Match** = 2 for Min Users. 8 for Max Users. (We don't specify Min or Max Preferred users for browse. The user will define this when they create the room.)
	* **Skill Pool** = None
	* **Should Consider Ping Time?** = No
	* When you're finished entering the pool configurations, select **Save and Deploy** to save the pool.
	
2. After you've created your pool, you can begin integrating into your client-side app. Your Browse integration will need to support multiple scenarios depending on the configuration settings you chose when creating your Pool and how the user wants to use the service. 
	* If the user wants to join a match: 
		1. Call ovr\_Matchmaking\_Browse2 to get a list of the available rooms. 
		2. Handle the ovrMessage\_Matchmaking\_Browse2 response and display the list of rooms to the user. You may wish to periodically refresh the list by periodically calling the browse method.
		3. Call ovr\_Room\_Join2 when the user has chosen a room.
		
	* If the user wants to create a room and host a match: 
		1. To create and enqueue the user and room, call either ovr\_Matchmaking\_CreateAndEnqueueRoom2 or call ovr\_Matchmaking\_CreateRoom2, handle the response, and then call ovr\_Matchmaking\_EnqueueRoom2. 
		2. Handle the ovrMessage\_Matchmaking\_CreateAndEnqueueRoom2 or ovrMessage\_Matchmaking\_EnqueueRoom2 response. 
		3. (Optional) Review the methods in the OVR\_MatchmakingEnqueueResult.h file for a list of methods you can call for information about the health of the queue to display to the user.
		
	
3. Your game will be listening for ovrNotification\_Room\_RoomUpdate for the number of users in the room. When the desired number of users is reached, your app will launch the game.
4. At any time in the matchmaking process, the user can call ovr\_Matchmaking\_Cancel2() to remove themselves from the queue and exit the matchmaking process. 
**Room Ownership**

Each user-generated matchmaking room is associated with the user who created the room. That user who created the room becomes the room's owner. This role may have the permission to update the settings of the room, if you have configured the pool to allow this. During the course of the multiplayer session, it may be necessary to transfer ownership of the room. The requests to update room data and transfer ownership can be found on the [Rooms](/documentation/platform/latest/concepts/dg-rooms/ "Rooms are virtual places where users come together to interact in your app.") page.

If the room owner leaves without transferring ownership, your pool may be configured to automatically transfer ownership to the user who has been in the room the longest. Enable this setting by choosing Yes for **Enable host migration when the room owner leaves the room?** when creating your pool. 

**What's next?**

Once you've finished the basic Matchmaking integration, please review the [Adding Skill and Using Queries](/documentation/platform/latest/concepts/dg-matchmaking-4skill_queries/) page for information on more advanced Matchmaking integrations. 

