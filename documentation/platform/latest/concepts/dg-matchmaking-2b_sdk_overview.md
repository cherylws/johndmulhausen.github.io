---
title: SDK Overview
---
This page will walk you through the Matchmaking SDK concepts. The [Matchmaking Quickstart](/documentation/platform/latest/concepts/dg-matchmaking-3quickstart/) and [Additional Configurations](/documentation/platform/latest/concepts/dg-matchmaking-4skill_queries/) pages will walk you through how to implement these methods in your game.

The following SDK methods are available to call from your client app. With Matchmaking SDK methods listed below, we recommend waiting for response messages before making additional requests. Making a call before the previous call has been handled creates a race condition that may result in unintended actions.

We’ll review the main SDK methods in OVR\_Requests\_Matchmaking.h. You should review the other Matchmaking header files in the [Reference Content](/documentation/platform/latest/concepts/book-reference/ "The Platform SDK developer reference contains a complete list of the Platform SDK headers, functions, and data structures.") section to see all available requests.

* **Enqueue the user:**

Native - ovr\_Matchmaking\_Enqueue2()

Unity - Platform.Matchmaking.Enqueue2()

ovr\_Matchmaking\_Enqueue2 adds the user to the Quickmatch queue, the user will be continually re-enqueued until they are successfully matched or cancel the process. Match notifications will come in the form of an ovrMessage\_Notification\_Matchmaking\_MatchFound notification with the details of the match. Your app should be listening for notifications on the message queue, please see [Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/ "The Platform SDK uses a message queue to interact with Native apps. This page describes the concept of the queue and how to retrieve messages and information.") for information about the message queue.


* **Create and enqueue a Room:**

Native - ovr\_Matchmaking\_CreateAndEnqueueRoom2()

Unity - Platform.Matchmaking.CreateAndEnqueueRoom2()

ovr\_Matchmaking\_CreateAndEnqueueRoom2 creates and enqueues a user-created, multiplayer-capable, Room. Review the ovr\_Matchmaking\_CreateAndEnqueueRoom2 page for information about the parameters and return data structure. 


* **Create a Matchmaking Room:**

Native - ovr\_Matchmaking\_CreateRoom2()

Unity - Platform.Matchmaking.CreateRoom2()

ovr\_Matchmaking\_CreateRoom2 creates a user-created multiplayer-capable Room. 


* **Enqueue a Matchmaking Room:**

Native - ovr\_Matchmaking\_EnqueueRoom2()

Unity - Platform.Matchmaking.EnqueueRoom2()

ovr\_Matchmaking\_EnqueueRoom2 adds User Generated rooms previously created by ovr\_Matchmaking\_CreateRoom2 to the matchmaking queue.

Note: Private user-created rooms created by ovr\_Room\_CreateAndJoinPrivate() cannot be upgraded to a matchmaking room or enqueued in the matchmaking service. 
* **Browse the list of available Rooms to join:**

Native - ovr\_Matchmaking\_Browse2()

Unity - Platform.Matchmaking.Browse2()

ovr\_Matchmaking\_Browse2 will return a list of Rooms that the user can join. This call will not return all Rooms, only the Rooms where the user meets the join criteria.


* **Cancel the Matchmaking request:**

Native - ovr\_Matchmaking\_Cancel2()

Unity - Platform.Matchmaking.Cancel2()

Cancels the matchmaking request. This can be called at any time in the Matchmaking process. If the user has already joined the Room you will need to call ovr\_Room\_Leave to remove the user. 


* **Report results of a match (Matchmaking with skill only):**

Native - ovr\_Matchmaking\_ReportResultInsecure()

Unity - Platform.Matchmaking.ReportResultInsecure()

After the match is over, you’ll want to report the results of the match for consideration in future matches. 


* **Start a match (Matchmaking with skill only):**

Native - ovr\_Matchmaking\_StartMatch()

Unity - Platform.Matchmaking.StartMatch()

After the match is over, you’ll want to report the results of the match for consideration in future matches.


