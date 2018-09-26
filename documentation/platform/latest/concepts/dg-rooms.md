---
title: Rooms
---

Rooms are virtual places where users come together to interact in your app.

Once together in a room, users can navigate your VR application together, chat, and even launch a matchmaking session from certain types of rooms (chat and matchmaking will require separate integrations with [Voice Chat (VoIP)](/documentation/platform/latest/concepts/dg-cc-voip/) and [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/)). You can use `ovr_Room_GetInvitableUsers2()`, described below, to retrieve a list of invitable friends and recently met non-friend users available to be invited to a room for an engaging social experience. Additionally, you can use the recently met users APIs in [Users, Friends, and Relationships](/documentation/platform/latest/concepts/dg-presence/) to display a list of users that the logged-in user recently met in VR. 

* User-created private rooms are created by users to interact in VR. These rooms are created and owned by a user. They invite friends to join the room, where they interact, and when everyone has left, the room is destroyed.
* User-created matchmaking rooms are used by the [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/ "Matchmaking places users together in a shared multiplayer experience. User matching can be done by common skill or other criteria that you define. The Matchmaking service offers two modes, Quickmatch and Browse.") service to bring users together to interact and enqueue in the matchmaking service to find a multiplayer game session.
* Moderated rooms are persistent, application-hosted rooms that your application creates and maintains.


After you’ve created the rooms, or allowed your users to create rooms themselves, use the room invites methods to help users find their friends and add them to the rooms.

**Cross Platform Rooms**

Rooms are capable of supporting users on different platforms in the same room. All that's required to support this is to have the rooms in the same application grouping. See the [Managing Apps](/distribute/latest/concepts/publish-create-app/) page for information about application groupings.

## Integrating Rooms

The process to integrate rooms is different depending on what kind of experience you want your users to have. We’ll review the integration for both user-created private rooms and system-owned moderated rooms in this section. Information about integrating user-created matchmaking rooms can be found in the [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/) guide. Then we'll introduce the methods you can call to interact with all rooms. 

When integrating rooms, be sure to familiarize yourself with how [Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/) work in the Platform SDK. Notifications are how you'll receive updates about user activities in the room.

## Integrate User-Created Private Rooms

This section details the methods that are available when creating and updating private user-generated rooms. Additional detail about each function can be found in the Platform SDK [Reference Content](/documentation/platform/latest/concepts/book-reference/).

Some methods listed below can only be called by the room owner. The owner is the user who created the room. If the user who created the room leaves, ownership of the room will be transferred to the person who has been in the room the longest. Room ownership can also be transferred by calling `ovr_Room_UpdateOwner()`. 

* **Create a private user-generated room:**

Native - ovr\_Room\_CreateAndJoinPrivate2()

Unity - Platform.Room.CreateAndJoinPrivate2()

Rooms created with this method can't be promoted to a matchmaking room. If you want to allow users to enqueue the room as a matchmaking room, you should use the ovr\_Matchmaking\_CreateRoom2 method. Please see [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/ "Matchmaking places users together in a shared multiplayer experience. User matching can be done by common skill or other criteria that you define. The Matchmaking service offers two modes, Quickmatch and Browse.") for more information about creating matchmaking rooms.


* **Kick a user out of a room:**

Native - ovr\_Room\_KickUser()

Unity - Platform.Room.KickUser()

Remove a user from a room. This method can only be called by the room owner.


* **Update a room's datastore:**

Native - ovr\_Room\_UpdateDataStore()

Unity - Platform.Room.UpdateDataStore()

Add up to 2,000 key/value pairs to the room metadata. This method can only be called by the room owner. 


* **Update room join policy:**

Native - ovr\_Room\_UpdatePrivateRoomJoinPolicy()

Unity - Platform.Room.UpdatePrivateRoomJoinPolicy()

Update the room join policy, or the definition of who can join the room. This method can only be called by the room owner.


* **Update room membership lock status:**

Native - ovr\_Room\_UpdateMembershipLockStatus()

Unity - Platform.Room.UpdateMembershipLockStatus()

Call this method to lock the membership of the room. Calling this and setting it to true will prevent additional users from joining the room. This method can only be called by the room owner. 


* **Update room owner:**

Native - ovr\_Room\_UpdateOwner()

Unity - Platform.Room.UpdateOwner()

Transfer ownership of the room to another user. This method can only be called by the current room owner. 


* **Update room description:**

Native - ovr\_Room\_SetDescription()

Unity - Platform.Room.SetDescription()

Set or change the description of the room. This method can only be called by the room owner.




## Integrate User-Created Matchmaking Rooms

Information about how to configure the matchmaking service and integrate user-created matchmaking rooms can be found in the [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/) guide. 

## Integrate Moderated Rooms

Moderated rooms are created through S2S REST calls. The client app should not have any interaction with creating or maintaining the moderated room. Please review the [Server-to-Server API Basics](/documentation/platform/latest/concepts/pgsg-s2s-basics/) for information about making S2S API calls, specifically about using the access tokens. 

With moderated rooms, only your trusted servers can create or make changes to the rooms.

**Create a Moderated Room**

Calling this endpoint will create a new moderated room.

```
$ curl -d 'access_token=$APP_ACCESSTOKEN'  -d 'max_users=MY_MAX_USER_COUNT' 
https://graph.oculus.com/room_moderated_create
```

You’ll need to include the `max_users` parameter which identifies the max simultaneous users for the room. The maximum number of users supported per room is 1,024.

Example response:

```
{"id": 963119010431337}
```

In response the API will return the `moderated_room_id` as the id value. Call this id when adding users to the room. 

**Update a Moderated Room's Datastore**

Calling this endpoint sets up to 2,000 key/value pairs in the room datastore. Key and value data can only be accepted as string values, any other value type will return an error. The `ROOM_ID` is the value returned from the API when you created the room.

```
$ curl -d 'access_token=$APP_ACCESSTOKEN' -d 'room_id=$ROOM_ID' 
-d 'datastore=[{"key":"KEY","value":"VALUE"},{"key":"KEY2","value":"VALUE2"}]'
https://graph.oculus.com/room_update_data_store
```

Example response:

```
{"success": true}
```

**Retrieve Information about a Moderated Room**

Calling this endpoint will retrieve information about a specified moderated room. The `ROOM_ID` is the value returned from the API when you created the room. The parameters in the example below are all optional, information will only be returned for the parameters identified in the request. 

```
$ curl -d 'access_token=$APP_ACCESSTOKEN' -d 'fields=max_users,owner{id,alias,presence,presence_status,profile_url,profile_url_small},
users{id,alias,presence,presence_status,profile_url,profile_url_small},
data_store,name,description,join_policy,type,joinability,version,is_membership_locked'
https://graph.oculus.com/$ROOM_ID
```

**Delete a Moderated Room**

Calling this endpoint will delete a moderated room.

```
$ curl  -X DELETE -d 'access_token=$APP_ACCESSTOKEN' 
https://graph.oculus.com/$MODERATED_ROOM_ID
```

Example response:

```
{"success": true}
```

## Interacting with Rooms

This section describes the methods can be called to get information and interact with all types of rooms. Detail about each function can be found in the Platform SDK [Reference Content](/documentation/platform/latest/concepts/book-reference/).

* **Retrieve information about a room:**

Native - ovr\_Room\_Get()

Unity - Platform.Room.Get()

Retrieve information about a specified room. 


* **Get current room information:**

Native - ovr\_Room\_GetCurrent()

Unity - Platform.Room.GetCurrent()

Retrieve information about the current room. 


* **Get current room information for another user:**

Native - ovr\_Room\_GetCurrentForUser()

Unity - Platform.Room.GetCurrentForUser()

Retrieve information about a room that a specified user is in. 


* **Join a room:**

Native - ovr\_Room\_Join2()

Unity - Platform.Room.Join2()

Join the specified room.


* **Leave a room:**

Native - ovr\_Room\_Leave()

Unity - Platform.Room.Leave()

Leave the specified room. 




## Integrating Invites

Room invites allow users to invite others to join them in a social VR experience. Room invites can be received whether the invited person is currently in VR or not. However, users can only be invited to apps they’re entitled to. 

You can send invites by constructing your own custom UI or using the Oculus UI provided with the Platform SDK.

**Use a Custom UI**

1. Make sure the user has joined the room for which they are sending invites. You can call ‘Get Current Room Information’ to confirm.
2. Get a list of users that can be invited to that room. Call:Native - ovr\_Room\_GetInvitableUsers2()

Unity - Platform.Room.GetInvitableUsers2()

You’ll get information for each invitable person (users who are friends that own the app and non-friends who the logged-in user recently interacted with in your app) that includes the Oculus username and a user-specific invite token. We'll return users in an order of how likely they are to join the user in a room, e.g. users who are online and in the app first. Also, the invitable users returned will be for the room the calling user is currently in. You may retrieve a list of invitable users for another room by providing the room id as a parameter in the call. 

Note: Apps created after September 2017 will automatically be opted-in to include recently met users in response to ovr\_Room\_GetInvitableUsers2. Apps created prior to that date may opt in to include the recently met results on the [Rooms and Matchmaking](https://dashboard.oculus.com/app/matchmaking) page. If you don't want to include recently met users, you may use that page to opt out. You can also specify in the request, using roomOptions, to not include recently met users. 
3. Then invite the user to the Room.Native - ovr\_Room\_InviteUser()

Unity - Platform.Room.InviteUser()


4. If you request room updates for the room when calling ovr\_Room\_Join2 by using the subscribeToUpdates parameter, your app will receive a notification of type ovrMessage\_Notification\_Room\_RoomUpdate when the user joins. Be sure to listen for this notification. 


**Use the Oculus UI**

1. Make sure the user has joined the room for which he or she is sending invites. You can call ovr\_Room\_GetCurrent() to confirm.
2. To open the Oculus UI, temporarily background your app and call:Native - ovr\_Room\_LaunchInvitableUserFlow()

Unity - Platform.Room.LaunchInvitableUserFlow()


3. The user will see an interface outside of your app, in the SystemUI, that allows users to invite others. The platform will take care of the rest.


**Accepting an Invite and Joining a Room from Home**

You can configure your app to launch invites directly from Oculus Home. This allows your users to jump directly into a social session in your app.

To accept invites outside of your application:

1. Oculus will provide the invite notifications to the user in both Rift and Gear VR Home.
2. If the user accepts this notification Oculus will then launch your application.
3. To detect that the user launched from accepting an invite, you can look for an invite-accepted message when launching your app.* For a native app, when polling the message queue, look for the ovrMessage\\_Notification\\_Room\\_InviteAccepted message. For example: int messageType = ovr\\_Message\\_GetType(response); if (messageType == ovrMessage\\_Notification\\_Room\\_InviteAccepted) { const char *roomIDString = ovr\\_Message\\_GetString(response); ovrID roomID; ovrID\\_FromString(&amp;roomID, roomIDString)); // we can now try to join the room } * For a Unity app, use the following callback: Oculus.Platform.Rooms.SetRoomInviteNotificationCallback ( (Oculus.Platform.Message&lt;string&gt; msg) =&gt;{ if (msg.IsError) { // Handle error } else { string roomID = msg.GetString(); // we can now try to join the room } } ); 




## Handling Updates and Notifications

There are two ways to receive updates for rooms. 

1. You can check and pull notifications for a user by calling ovr\_Notification\_GetRoomInvites() for native apps, or Notifications.GetRoomInviteNotifications() for Unity apps. This method requires you to frequently check for invites and room updates. 
2. You can add a listener to your game loop for notifications. This will notify you any time you receive a notification or message.On native apps, you'll listen for ovrMessage\_Notification\_Room\_InviteReceived. Please see the [Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/ "The Platform SDK uses a message queue to interact with Native apps. This page describes the concept of the queue and how to retrieve messages and information.") page for an overview of notifications and the message queue.

In Unity, you'll set a callback for any time an invite is received. Your callback may resemble:

public static void SetRoomInviteReceivedNotificationCallback(Message&lt;Models.RoomInviteNotification&gt;.Callback callback) { Callback.SetNotificationCallback( Message.MessageType.Notification\_Room\_InviteReceived, callback ); }


You'll receive a notification any time a user enters, leaves, or is removed from a room. The `roomId` will be `0` if the user has left or been removed from a room.

## Rooms Quickstart

Now that we've reviewed the different types of rooms you can create and how you're able to interact with them, let's review a basic integration that supports invites.

This integration will allow users to create a private non-matchmaking room.

1. Create the Room: A user calls ovr\_Room\_CreateAndJoinPrivate2() to create and join a private user-created room. This user becomes the owner of the room.
	1. Specify the joinPolicy and maxUsers for the room when sending the create request. joinPolicy defines who is able to join the room; see RoomJoinPolicy for the available policies. maxUsers is the maximum number of users that can be added to a room. The maximum number of users supported per room is 1,024.
	2. Once created, the room owner has the ability to lock the membership of the room by calling ovr\_Room\_UpdateMembershipLockStatus(). This will prevent new members from being able to join the room. Any users that are in the room at the time of lock will be able to rejoin. 
	
2. Invite Friends: Using the pre-built Oculus invites interface is the simplest way for your app to allow users to invite their friends. The app calls ovr\_Room\_LaunchInvitableUserFlow() with the roomID of the room that was just created. The invite interface will be opened where the user may find and invite users to the room. 
3. Join the Room: Recipients of invites will receive a notification on the message queue that they have been invited to join a room. 
	1. Handle the notification on the message queue and extract the roomID from the notification payload. Please see the [Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/ "The Platform SDK uses a message queue to interact with Native apps. This page describes the concept of the queue and how to retrieve messages and information.") page for information about how the Platform SDK uses messages, notifications, and the queue. 
	2. The invitee's client can retrieve information about the room using ovr\_Room\_Get() with the roomID of the room. The response will be a Room message that contains the details about the room.
	3. If the invitee decides to join the room, add them using ovr\_Room\_Join2() with the roomID of the room.
	4. At any time the user may call ovr\_Room\_Leave() to leave the room. 
	


## Test Using the Rooms and Matchmaking Debugger

The [Room and Matchmaking Debugger](https://dashboard.oculus.com/tools/rooms-and-matchmaking-debugger/) is available to help developers identifying what connections and interactions a user or room makes with a room or matchmaking pool. Enter the id of a user or room to get a list of the recent connections. 

The table will display a chronological list of events for that user or room. Each row represents a single event with additional information about the occurrence. The results show what event occurred, when it occurred, what user initiated the event, and the room in which the event happened (if in a room). You can select any room or user id returned in the table to retrieve the connection or interaction information about that user or room. 

To retrieve the user and room id's:

* Retrieve the User Id - Please see the [Users, Friends, and Relationships](/documentation/platform/latest/concepts/dg-presence/ "Users, friends, and relationships manages information about each user's unique persona, their relationship with their friends, and their recent encounters in VR.") page for information about the SDK requests you can use to retrieve a User Id. Please note that this id is not the same as the Org Scoped Id.
* Retrieve the Room Id - Use the SDK methods listed above to retrieve the User Ids.

