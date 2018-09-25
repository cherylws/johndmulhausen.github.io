---
title: Testing and Tuning
---
To debug what's going on with your matchmaking pool, you can get snapshots of the queues using ovr\_Matchmaking\_GetAdminSnapshot, which returns the state of the queue at whatever time this request is made. This endpoint is not intended to be called in production.

// In your code, do a matchmaking enqueue first // We can now inspect the queue to debug it. ovr\_Matchmaking\_GetAdminSnapshot(); // In your handler case ovrMessage\_Matchmaking\_GetAdminSnapshot: if (!ovr\_Message\_IsError(message)) { auto snapshot = ovr\_Message\_GetMatchmakingAdminSnapshot(message); auto candidates = ovr\_MatchmakingAdminSnapshot\_GetCandidates(snapshot); auto firstCandidate = ovr\_MatchmakingAdminSnapshotCandidateArray\_GetElement(candidates, 0); if (ovr\_MatchmakingAdminSnapshotCandidate\_GetCanMatch(firstCandidate)) { cout << "Yay!" << endl; } } You can also view a snapshot of the queue at enqueue time:

ovrMatchmakingOptionsHandle matchmakingOptions = ovr\_MatchmakingOptions\_Create(); ovr\_MatchmakingOptions\_SetIsDebug(matchmakingOptions, true); // set other matchmaking options here ... ovr\_Matchmaking\_Enqueue2("my\_pool", matchmakingOptions); ovr\_MatchmakingOptions\_Destroy(matchmakingOptions); // In your handler case ovrMessage\_Matchmaking\_Enqueue2: if (!ovr\_Message\_IsError(message)) { auto enqueueResults = ovr\_Message\_GetMatchmakingEnqueueResult(message); auto snapshot = ovr\_MatchmakingEnqueueResult\_GetAdminSnapshot(enqueueResults); auto candidates = ovr\_MatchmakingAdminSnapshot\_GetCandidates(snapshot); auto firstCandidate = ovr\_MatchmakingAdminSnapshotCandidateArray\_GetElement(candidates, 0); if (ovr\_MatchmakingAdminSnapshotCandidate\_GetCanMatch(firstCandidate)) { cout << "Yay!" << endl; } }## Tuning Your Matches

After you've finished implementing Matchmaking and have the desired configurations in place, you may wish to tune the Matchmaking service. We introduced the concept of Advanced Tuning and Match Quality in [Configuration Overview](/documentation/platform/latest/concepts/dg-matchmaking-2a_platform_overview/) where you can choose the 'Minimum Quality Bar'. We recommend leaving this value at the default 0.5 when you were implementing Matchmaking. However, now it may be appropriate to tune this value. 

To tune your Matchmaking implementation, we recommend the following adjustments:

* Small user pool - If your pool of available matchmaking players is small, you may want to reduce the Minimum Quality Bar to allow for more matches.
* Match process takes too long - If the matchmaking service is taking too long to match users, you may want to reduce the Minimum Quality Bar to allow more, less optimal, matches to be made.
* Large user pool - If your pool of available matchmaking players is large, you may want to increase the Minimum Quality Bar to search for better quality matches.
* Match quality is low - If low-quality matches are impacting the user experience, you may want to increase the Minimum Quality Bar to search for better quality matches.
## Test Using the Rooms and Matchmaking Debugger

The [Room and Matchmaking Debugger](https://dashboard.oculus.com/tools/rooms-and-matchmaking-debugger/) is available to help developers identifying what connections and interactions a user or room makes with a room or matchmaking pool. Enter the id of a user or room to get a list of the recent connections. 

The table will display a chronological list of events for that user or room. Each row represents a single event with additional information about the occurrence. The results show what event occurred, when it occurred, what user initiated the event, and the room in which the event happened (if in a room). You can select any room or user id returned in the table to retrieve the connection or interaction information about that user or room. 

To retrieve the user and room id's:

* Retrieve the User Id - Please see the [Users, Friends, and Relationships](/documentation/platform/latest/concepts/dg-presence/ "Users, friends, and relationships manages information about each user's unique persona, their relationship with their friends, and their recent encounters in VR.") page for information about the SDK requests you can use to retrieve a User Id. Please note that this id is not the same as the Org Scoped Id.
* Retrieve the Room Id - Please see the [Rooms](/documentation/platform/latest/concepts/dg-rooms/ "Rooms are virtual places where users come together to interact in your app.") page for information about the SDK requests you can use to retrieve a User Id.
## Test Multiplayer Integrations Locally

The Platform SDK allows you to test your Multiplayer integration by initializing multiple copies of the app locally, without making any external connections. Please see the [Native Development Getting Started](/documentation/platform/latest/concepts/pgsg-native-gsg/ "The native getting started guide will walk you through the basics of setting up your development environment, initializing the SDK, and checking the user's entitlement.") or [Unity Development Getting Started](/documentation/platform/latest/concepts/pgsg-unity-gsg/ "The Unity getting started guide will walk you through the basics of setting up your development environment, initializing the SDK, and checking the user's entitlement.") for information about initializing in standalone mode.

Create test users in the [Developer Center](https://dashboard.oculus.com/) under the **Settings** tab, to test matching of users into a match locally. 

## Analytics for Matchmaking Pools

Matchmaking pool analytics allow you to review stats and the overall health of your matchmaking pools. If you've implemented any public facing pools you'll be able to review the stats by logging in to [https://dashboard.oculus.com](https://dashboard.oculus.com/), selecting the app you'd like to review, then select **Analytics** and **Matchmaking Pools**.

Note: To see the Matchmaking Pools analytics, you'll need to have permission as either a Developer or Admin for the app. Information about different user roles can be found on the [Manage your Organization and Users](/distribute/latest/concepts/publish-account-management-intro/) page.On that page you'll see the overall statistics of all your matchmaking pools. The filter allows you to review stats for a particular time period scaled by day or hour.

The analytics available are:

* **Match Made Percentage**: How often a user was successfully matched vs canceling out of the queue.
* **Average Wait Time Until Match Made**: How long a user waited for a successful match, in seconds. 
* **Matches Made Count**: A count of how many users were matched.
* **Average Wait Time Until Cancellation**: How long a user waited until they canceled the matchmaking process.
* **Cancellation Count**: How many users canceled out of the matchmaking process before finding a successful match.
