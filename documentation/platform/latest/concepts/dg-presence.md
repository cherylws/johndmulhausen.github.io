---
title: Users, Friends, and Relationships
---
Users, friends, and relationships manages information about each user's unique persona, their relationship with their friends, and their recent encounters in VR.

Use the user and friends APIs to retrieve information about your players to customize their experience, help them find their friends, and then join them in social VR experiences with [Rooms](/documentation/platform/latest/concepts/dg-rooms/ "Rooms are virtual places where users come together to interact in your app."). The relationships APIs help users find new friends from their recent VR encounters. 

## User and Friends - Native & Unity

The following SDK methods can be called from your client app. Detail about each function can be found in the Platform SDK [Reference Content](/documentation/platform/latest/concepts/book-reference/ "The Platform SDK developer reference contains a complete list of the Platform SDK headers, functions, and data structures.").

* **Retrieve information about the current user:**

Native - ovr\_User\_GetLoggedInUser()

Unity - Platform.User.GetLoggedInUser()

This method retrieves the unique ID, Oculus username, and a URL profile image for the current user. The user ID returned by this method is specific only to this application. To retrieve an ID that can be used across applications in your organization, please see ovr\_User\_GetOrgScopedID.


* **Retrieve a list of the user’s friends:**

Native - ovr\_User\_GetLoggedInUserFriends()

Unity - Platform.User.GetLoggedInUserFriends()

Retrieves an array of the current user's friends who are also entitled to your app. The list of friends is ordered by presence, friends currently active within your app will be returned first. 

If there are a large number of values being returned, you may need to call ovr\_User\_GetNextUserArrayPage and paginate the data.


* **Retrieve a list of the user’s friends and the room they are currently in:**

Native - ovr\_User\_GetLoggedInUserFriendsAndRooms()

Unity - Platform.User.GetLoggedInUserFriendsAndRooms()

Retrieves an array of the current user's friends who are also entitled to your app. The array will also contain the room ID for users who are currently in a room. The list of friends will is ordered by presence, friends currently active within your app will be returned first. 

If there are a large number of values being returned, you may need to call ovr\_User\_GetNextUserAndRoomArrayPage and paginate the data.


* **Retrieve a list of recently met users:**

Native - ovr\_User\_GetLoggedInUserRecentlyMetUsersAndRooms()

Unity - Platform.User.GetLoggedInUserRecentlyMetUsersAndRooms()

Returns a list of users who the logged-in user recently interacted with in your app. Interesting users, users who interact frequently or for a long duration, will be returned first. Oculus tracks the number of times users meet in VR, their most recent encounter, and the amount of time they spend together. Customize the results returned using UserOptions.


* **Retrieve information about a specified user:**

Native - ovr\_User\_Get()

Unity - Platform.User.Get()

This method retrieves the unique ID, Oculus username, and a URL profile image for a specified user. The user ID returned by this method is specific only to this application. To retrieve an ID that can be used across applications in your organization, please see ovr\_User\_GetOrgScopedID.
* **Retrieve the Org Scoped ID for a user:**

Native - ovr\_User\_GetOrgScopedID()

Unity - Platform.User.GetOrgScopedID()

This method returns an ID that can be used to identify this user across all applications in your organization. Please note that the OrgScopedID is not the same as the userID in an app.


* **Display user profile (Gear VR only):**

Native - ovr\_User\_LaunchProfile()

Unity - Platform.User.LaunchProfile()

![](/images/documentation-platform-latest-concepts-dg-presence-0.png)  
Launch a profile that displays the Oculus name, ID, online status, recent interactions, and mutual friends for a specified user. The modal also allows a friend request to be sent to the user.


## User and Friends - Unreal

To retrieve the user's Oculus Id and Oculus Name to display, add the **Get Oculus Identity** node to your blueprint. The Oculus Id is available synchronously after Login() is called, while the Oculus Name is available asynchronously after OnLoginComplete() returns.

For all other actions on this page, please use the native C API with the information found in [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/ "The Unreal getting started guide will walk you through the basics of setting up your development environment and checking the user's entitlement.").

