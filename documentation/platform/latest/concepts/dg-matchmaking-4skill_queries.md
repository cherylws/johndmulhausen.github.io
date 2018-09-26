---
title: Adding Skill and Using Queries
---

Once you have your basic matchmaking integration working as expected, you can start adding the other aspects of the matchmaking service to ensure that you are bringing the right users together.

This page will walk you through how to use add Skill and Matchmaking Queries to your game. We introduced the concept of both in the [Configuration Overview](/documentation/platform/latest/concepts/dg-matchmaking-2a_platform_overview/), with a description of the capability. This page will review the high-level implementation. 

## Adding Skill Matches

Adding the Skill component to the matchmaking service is straightforward. In the Developer Center, navigate to the [Matchmaking](https://dashboard.oculus.com/app/matchmaking) page and create your skill pool as described in the matchmaking overview. 

Once you’ve entered the information for your skill pool, the next step is to add it to your matchmaking pool. Navigate to the pool you created for your game and select **View/Edit Pool**, then select the skill pool you created from the dropdown and save your matchmaking pool.

Once you've added the skill pool to your pool, you can integrate the skill component into your game. To do this you'll need to integrate two SDK methods to your game.

* Native - ovr\_Matchmaking\_StartMatch()
* Unity - Platform.Matchmaking.StartMatch()


* Native - ovr\_Matchmaking\_ReportResultInsecure()
* Unity - Platform.Matchmaking.ReportResultInsecure()


The matchmaking service will now track and account for the user’s skills when determining the quality of a match.

## Adding Matchmaking Queries and Other Enqueue-Time Data

You can further configure the matchmaking service and use the Matchmaking Queries to compare potential matches. Some Matchmaking requests accept an optional `ovrMatchmakingOptionsHandle` that allow you to pass Data Settings and other enqueue specifics to be used when finding matches. 

**Defining Data Settings and Matchmaking Queries**

First, we’ll create the Data Setting and Matchmaking Queries that we want to use to match users. Navigate to [Matchmaking](https://dashboard.oculus.com/app/matchmaking) in the Developer Center and select ‘Manage Queries’ as described in [Configuration Overview](/documentation/platform/latest/concepts/dg-matchmaking-2a_platform_overview/).

We’ll use an example to demonstrate how Data Settings and Matchmaking Queries can be used. In the Developer Center we’ll navigate to our matchmaking pool, which for the detailed example below we’ll call ‘my_pool’, and enter the following Data Settings:

* player\_level (INTEGER)
* game\_mode (STRING)
* map\_size (INTEGER\_BITSET)


Then we’ll create a Matchmaking Query called ‘my_query’, also in ‘my_pool’, with the following query expressions:

* Their "player\_level" is equal to my "player\_level". Importance: Medium
* Their "game\_mode" is equal to my "game\_mode". Importance: Required
* Their "map\_size" is a bitmask AND of my "map\_size". Importance: Required


In the game, "map_size" bitmask has the following bit meanings:

* 0x4: large map size
* 0x2: medium map size
* 0x1: small map size


**Integrating the Matchmaking Queries**

First you’ll need to create an instance of the `ovrMatchmakingOptionsHandle` by calling `ovr_MatchmakingOptions_Create()`. When you’re finished with the handle, you can call `ovr_MatchmakingOptions_Destroy()` to free the memory.

After you’ve created the handle, you’ll populate the user or room enqueue message with the data settings for the room or user. The available data settings for users and rooms are:

**Setting Data for a Room**

Setting data for a Room during the create room process is available when calling `CreateRoom2` and `CreateAndEnqueueRoom2`.

* ovr\_MatchmakingOptions\_SetCreateRoomMaxUsers will override the value of "Max Users" for a Pool of the Developer Dashboard. Note: You can not exceed the ‘Max Users’ value that you set when creating your Pool.
* ovr\_MatchmakingOptions\_SetCreateRoomJoinPolicy will specify a join policy for the created room. If not provided, the join policy defaults to everyone. 


**Setting Data for a User**

Setting data for a user during the enqueue processes is available when calling `Enqueue2`, `EnqueueRoom2`, and `Browse2`. 

* ovr\_MatchmakingOptions\_AddEnqueueAdditionalUser sets additional users, using their userID, at enqueue-time as users to be added to a multiplayer session. Additional users will not receive notifications when they are enqueued, only when a match is made. Note: Once the users are matched, you may then want to team people up based on their original groupings. You would loop through the matched users using ovr\_Room\_GetMatchedUsers. Then, within each of those, call ovr\_MatchmakingEnqueuedUser\_GetAdditionalUserIDsSize. If anybody has more than 1, loop through those using ovr\_MatchmakingEnqueuedUser\_GetAdditionalUserID, and place those users on the same team.
* ovr\_MatchmakingOptions\_SetEnqueueDataSettingsInt sets an integer Data Setting.
* ovr\_MatchmakingOptions\_SetEnqueueDataSettingsDouble sets a double Data Setting.
* ovr\_MatchmakingOptions\_SetEnqueueDataSettingsString sets a string Data setting.
* ovr\_MatchmakingOptions\_SetEnqueueIsDebug if true, debug information is returned with the response payload. See "Debugging" section for more information.
* ovr\_MatchmakingOptions\_SetEnqueueQueryKey specifies a specific Matchmaking Query for filtering potential matches.


**Example Integration Setting Enqueue-Time Data**

Using the example data we defined earlier, the following example shows a user enqueueing in the matchmaking service and looking to be matched with other players with Data Settings `player_level=10`, `game_mode="CaptureTheFlag"`, and `map_size` is large, medium, or both.

```
ovrMatchmakingOptionsHandle matchmakingOptions = ovr_MatchmakingOptions_Create();
ovr_MatchmakingOptions_SetEnqueueDataSettingsInt(matchmakingOptions, "player_level", 10);
ovr_MatchmakingOptions_SetEnqueueDataSettingsString(matchmakingOptions, "game_mode", "CaptureTheFlag");

// I want large or medium map size
ovr_MatchmakingOptions_SetEnqueueDataSettingsInt(matchmakingOptions, "map_size", 0x4 &amp; 0x2);

// Specify which Matchmaking Query to use with the Data Settings we provided
ovr_MatchmakingOptions_SetEnqueueQueryKey(matchmakingOptions, "my_query");

ovr_Matchmaking_Enqueue2("my_pool", matchmakingOptions);

// Destroy the matchmaking options now that we are done with it
ovr_MatchmakingOptions_Destroy(matchmakingOptions);       
```

**Testing your Matchmaking integration**

When you're finished configuring your matchmaking integration, you may need to do some troubleshooting to make sure that the service is making the matches you want it to. Please review [Testing and Tuning](/documentation/platform/latest/concepts/dg-matchmaking-5debugging/) page for more information. 
