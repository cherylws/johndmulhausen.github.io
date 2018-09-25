---
title: Leaderboards
---
Leaderboards create competition and increase engagement among your users.

The Oculus Platform will manage your leaderboard data. However, your app will be responsible for displaying, reporting, and verifying the data.

This page will walk you through how to create your global leaderboards, interact with the leaderboards service, and provide an example Unity implementation you can review or use as a leaderboard template.

## Create Your Leaderboards

The first step in adding leaderboards to your game is defining them in the Developer Center. To get started, navigate to [Leaderboards](https://dashboard.oculus.com/app/leaderboards) in the Developer Center and select the app that you would like to create a leaderboard for.

Select **Create Leaderboard** and enter the following information:

* **API Name** - This is the unique string that you will allow you to reference this leaderboard in your app. The API Name is case-sensitive, the name you define in the Dashboard must exactly match the name you reference in your code. 
* **Sort Order** - There are two options for Sort Order depending on your use-case: 
	+ **Higher is Better** will rank users in descending order, from highest to lowest score.
	+ **Lower is Better** will rank users in ascending order, from lowest to highest score.
	
Select **Submit** when finished to save the leaderboard. You can update leaderboard settings at any time in the Developer Center. You may also clear the results in a leaderboard and reset the scores.

## Integrating Leaderboards - Native & Unity

Once you’re finished creating the achievements, you can begin to integrate them in your game. When calling the SDK methods in this section use the API Name you defined in the Developer Center. 

Detail about each function can be found in the Platform SDK [Reference Content](/documentation/platform/latest/concepts/book-reference/ "The Platform SDK developer reference contains a complete list of the Platform SDK headers, functions, and data structures.").

* **Retrieve a list of leaderboard entries:**

Native - ovr\_Leaderboard\_GetEntries()

Unity - Platform.Leaderboard.GetEntries()

Retrieves an array of leaderboard entries for a specified leaderboard. 


* **Retrieve a list of leaderboard entries after a rank:**

Native - ovr\_Leaderboard\_GetEntriesAfterRank()

Unity - Platform.Leaderboard.GetEntriesAfterRank()

Retrieves a list of entries starting after a rank that you define. For example, if you specify a list with an 'afterRank' of 10, you’ll get a list starting with the 11th position.


* **Retrieve the next list of entries:**

Native - ovr\_Leaderboard\_GetNextEntries()

Unity - Platform.Leaderboard.GetNextEntries()

Retrieves the next group of leaderboard entries. This can be used to paginate the leaderboard data. 


* **Retrieve the previous list of entries:**

Native - ovr\_Leaderboard\_GetPreviousEntries()

Unity - Platform.Leaderboard.GetPreviousEntries()

Retrieves the previous group of leaderboard entries. This can be used to paginate the leaderboard data.


* **Write leaderboard entry:**

Native - ovr\_Leaderboard\_WriteEntry()

Unity - Platform.Leaderboard.WriteEntry()

This method will write a new leaderboard entry to a specified leaderboard for the current user. It is not an incremental update, it will overwrite the existing entry.


At a high level, there are two processes to implement when integrating leaderboards. 

1. Retrieve and Display Leaderboards - Display the current leaderboard state before a game begins. For example, ovr\_Leaderboard\_GetEntries for a native app, or Platform.Leaderboards.GetEntries for Unity. There are other methods you can use to get a subset of leaderboard entries based on input criteria.
2. Update Leaderboard Entries - Write the results of the current game to your leaderboard. For example, ovr\_Leaderboard\_WriteEntry for a native app, or Platform.Leaderboards.WriteEntry for a Unity app. A user may only have one entry on each leaderboard, subsequent entries will overwrite the existing entry on the specified leaderboard. 
**Example Implementation - Unity**

The following Unity example demonstrates retrieving information from a leaderboard called 'MOST\_MATCHES\_WON' and writing a new leaderboard entry after a win for the current user. The following example is taken from the VRHoops sample app, please [download](/downloads/) the full app for the full example with other features. and see the [Sample Apps](/documentation/platform/latest/concepts/book-sampleapp/) page for more information about the apps that are available.

using UnityEngine; using System.Collections.Generic; using Oculus.Platform; using Oculus.Platform.Models; // Coordinates updating leaderboard scores and polling for leaderboard updates. public class LeaderboardManager { // API NAME for the leaderboard where we store how many matches the user has won private const string MOST\_MATCHES\_WON = "MOST\_MATCHES\_WON"; ///... // the top number of entries to query private const int TOP\_N\_COUNT = 5; // how often to poll the service for leaderboard updates private const float LEADERBOARD\_POLL\_FREQ = 30.0f; // the next time to check for leaderboard updates private float m\_nextCheckTime; ///... // whether we've found the local user's entry yet private bool m\_foundLocalUserMostWinsEntry; // number of times the local user has won private long m\_numWins; // callback to deliver the most-wins leaderboard entries private OnMostWinsLeaderboardUpdated m\_mostWinsCallback; ///... public void CheckForUpdates() { if (Time.time >= m\_nextCheckTime && PlatformManager.CurrentState == PlatformManager.State.WAITING\_TO\_PRACTICE\_OR\_MATCHMAKE) { m\_nextCheckTime = Time.time + LEADERBOARD\_POLL\_FREQ; QueryMostWinsLeaderboard(); QueryHighScoreLeaderboard(); } } #region Most Wins Leaderboard public delegate void OnMostWinsLeaderboardUpdated(SortedDictionary<int, LeaderboardEntry> entries); public OnMostWinsLeaderboardUpdated MostWinsLeaderboardUpdatedCallback { set { m\_mostWinsCallback = value; } } void QueryMostWinsLeaderboard() { // if a query is already in progress, don't start a new one. if (m\_mostWins != null) return; m\_mostWins = new SortedDictionary<int, LeaderboardEntry>(); m\_foundLocalUserMostWinsEntry = false; Leaderboards.GetEntries(MOST\_MATCHES\_WON, TOP\_N\_COUNT, LeaderboardFilterType.None, LeaderboardStartAt.Top).OnComplete(MostWinsGetEntriesCallback); } void MostWinsGetEntriesCallback(Message<LeaderboardEntryList> msg) { if (!msg.IsError) { foreach (LeaderboardEntry entry in msg.Data) { m\_mostWins[entry.Rank] = entry; if (entry.User.ID == PlatformManager.MyID) { m\_foundLocalUserMostWinsEntry = true; m\_numWins = entry.Score; } } // results might be paged for large requests if (msg.Data.HasNextPage) { Leaderboards.GetNextEntries(msg.Data).OnComplete(MostWinsGetEntriesCallback); return; } // if local user not in the top, get their position specifically if (!m\_foundLocalUserMostWinsEntry) { Leaderboards.GetEntries(MOST\_MATCHES\_WON, 1, LeaderboardFilterType.None, LeaderboardStartAt.CenteredOnViewer).OnComplete(MostWinsGetEntriesCallback); return; } } // else an error is returned if the local player isn't ranked - we can ignore that if (m\_mostWinsCallback != null) { m\_mostWinsCallback(m\_mostWins); } m\_mostWins = null; } #endregion // submit the local player's match score to the leaderboard service public void SubmitMatchScores(bool wonMatch, uint score) { if (wonMatch) { m\_numWins += 1; Leaderboards.WriteEntry(MOST\_MATCHES\_WON, m\_numWins); } if (score > 0) { Leaderboards.WriteEntry(HIGHEST\_MATCH\_SCORE, score); } } }**Implementation Tips**

When implementing leaderboards, there are two common scenarios you should be aware of. They are:

* To retrieve leaderboard entries centered around the current user, use the LeaderboardStartAt enum to define where the values returned start or are centered. To retrieve only the current user, center on the viewer and limit results returned to 1.
* To return only the user's friends, you can use the LeaderboardFilterType enum to define the results returned.
## Integration - Unreal

After you've created your leaderboards on the Oculus Dashboard, as described above, integrating in Unreal is done by using OSS nodes in your game blueprint.

**Read leaderboard entry:**

Add the **Read Leaderboard Integer** node. There are 2 ways to query the leaderboard using this node. Pass an array of a single entry, the current user's id, to retrieve the user's rank on the leaderboard. Passing an empty array will return the top 100 players on the leaderboard.

**Write leaderboard entry:**

To write to a leaderboard, add the **Write Leaderboard Integer** node and pass the stat that you use to rank players on the leaderboard.

## S2S REST Requests

Certain actions require to your back-end servers to interact directly with our platform. For example, update a leaderboard after a server-hosted multiplayer match. See the [Server-to-Server API Basics](/documentation/platform/latest/concepts/pgsg-s2s-basics/ "Some platform features use server-to-server (S2S) REST API calls to perform actions not appropriate to be sent from client devices. These APIs are provided to ensure a secure interaction between your back-end servers and the Oculus Platform.") page for information about interacting with our APIs.

**Leaderboards S2S Parameters**

ParameterRequiredDescriptionTypeExampleapi\_nameY

The unique string that you will allow you to reference this leaderboard in your app.

string

“top\_players1”scoreY for 'Create and Update Leaderboard Entry'

The leaderboard value or score.

integer

78645earliest\_allowed\_entry\_timeY for 'Create and Update Leaderboard'Unix timestamp for the earliest time to allow leaderboard entries to post. integer1464480000entry\_write\_policyY for 'Create and Update Leaderboard'See 'Create Your Leaderboard' section above for description. enum: "CLIENT\_AUTHORITATIVE", "SERVER\_AUTHORITATIVE" extra\_data\_base64N

Extra metadata to store with the leaderboard entry. This can be used to specify information about the score. For example, in a driving game this may be what car was used. Decoded length can be, at most, 2048 bytes.

string

 “T2N1bHVz”latest\_allowed\_entry\_timeY for 'Create and Update Leaderboard'Unix timestamp for the latest time to allow leaderboard entries to post. integer1464480000force\_updateN - default is false

If you already have an entry on the leaderboard and the user receives a worse score than the existing leaderboard entry, the existing entry will not be updated unless force\_update is true. Set as true to overwrite the entry even if the new score being posted is worse than the old one.

boolean

“false”sort\_orderY for 'Create and Update Leaderboard'See 'Create Your Leaderboard' section above for description. enum: "HIGHER\_IS\_BETTER", "LOWER\_IS\_BETTER" user\_idOnly if you use the App Access Token to authenticate to the API.

Indicate which user you are posting on behalf of. That user must have an entitlement to your app. When using a User Access Token, this field must not be set. See the [Users, Friends, and Relationships](/documentation/platform/latest/concepts/dg-presence/ "Users, friends, and relationships manages information about each user's unique persona, their relationship with their friends, and their recent encounters in VR.") page for information about retrieving the User Id.

string

“12345”**Create or Update a Leaderboard (POST)**

Example Request

$ curl -d "access\_token=$APP\_ACCESSTOKEN" -d "api\_name=MY\_NEW\_LEADERBOARD" -d "sort\_order=HIGHER\_IS\_BETTER" -d "entry\_write\_policy=CLIENT\_AUTHORITATIVE" -d "earliest\_allowed\_entry\_time=1463875200" -d "latest\_allowed\_entry\_time=1464480000" https://graph.oculus.com/$APPID/leaderboardsExample Response

{"id":"10742336355960170"}**Create or Update a Leaderboard Entry (POST)**

Example Request

$ curl -d "access\_token=$APP\_ACCESSTOKEN|$USER\_ACCESSTOKEN" -d "api\_name=MY\_NEW\_LEADERBOARD" -d "score=12345" -d "extra\_data\_base64=T271bHVz" -d "force\_update=true" -d "user\_id=865302235207175" https://graph.oculus.com/leaderboard\_submit\_entryExample Response

{"success": true, "did\_update": true}The response contains a status, did\_update indicates whether the entry was recorded or not. Entries will not be recorded if the user already has an entry on the leaderboard, the new score is worse than the old score, and force\_update is false.

**Retrieve Data about a Leaderboard (GET)**

Example Request

$ curl -G -d "access\_token=$APP\_ACCESSTOKEN|$USER\_ACCESSTOKEN" -d "api\_name=MY\_NEW\_LEADERBOARD" -d 'fields' => 'sort\_order,entry\_write\_policy,entry\_count' https://graph.oculus.com/$APPID/leaderboardsExample Response

{"data":[{"id":"1074273245960170", "sort\_order":"HIGHER\_IS\_BETTER", "entry\_write\_policy":"CLIENT\_AUTHORITATIVE","entry\_count":2500}]}**Retrieve Data about a User's Leaderboard Entry (GET)**

Example Request

$ curl -G -d "access\_token=$APP\_ACCESSTOKEN|$USER\_ACCESSTOKEN" -d "api\_name=MY\_NEW\_LEADERBOARD" -d "filter=NONE" -d "start\_at=OFFSET" -d "offset=10" -d "summary=true" -d "limit=2" -d "fields=user{id,alias,profile\_url},rank,score,timestamp,extra\_data\_base64" https://graph.oculus.com/leaderboard\_entriesExample Response

{"data":[{"id":"1074233745529170", "user":{"id:865307770207175,"alias":"UnknownXuid","profile\_url":"..."},"rank":25,"score":12345,"timestamp":1456523020,"extra\_data\_base64":"T2N1bHVz"}, ...] "summary":{"total\_count":45}, "paging":{"next":"...","previous":"..."}}The first "id" returned in the response above is the entry id, which can be referenced and used to delete the user's leaderboard entry.

**Delete a Single User's Leaderboard Entry (DELETE)**

Example Request

$ curl -X DELETE -d "access\_token=$APP\_ACCESSTOKEN" https://graph.oculus.com/$entry-idThe entry-id is the id returned from the 'Retrieve Data about a User's Leaderboard Entry' GET above.

Example Response

{"success":true}**Delete All Leaderboard Entries (DELETE)**

Example Request

$ curl -d "access\_token=$APP\_ACCESSTOKEN" -d "api\_name=MY\_NEW\_LEADERBOARD" https://graph.oculus.com/leaderboard\_remove\_all\_entriesExample Response

{"success":true}Once deleted, a leaderboard entry cannot be recovered.

**Delete a Leaderboard (DELETE)**

Example Request

curl -X "DELETE" -d "access\_token=$APP\_ACCESSTOKEN" https://graph.oculus.com/$leaderboard-idThe leaderboard-id is the id returned from the 'Create or Update a Leaderboard' POST above.

Example Response

{"success":true}Once deleted, a leaderboard entry cannot be recovered.

