---
title: Configuration Overview
---

This page will walk you through the concepts of matchmaking, and the configuration details available in the Developer Center. The [Matchmaking Quickstart](/documentation/platform/latest/concepts/dg-matchmaking-3quickstart/) and [Additional Configurations](/documentation/platform/latest/concepts/dg-matchmaking-4skill_queries/) pages will walk you through how to implement Matchmaking in your game.

## Matchmaking Configuration Options

The Oculus Developer Center allows you to define how you want to group your players and matchmaking configuration that determine how you'll bring them together. There are three Matchmaking concepts that we’ll review in this guide: Pools, Data Settings, and Queries.

## Pools

Pools are the top level groups of users in matchmaking. This is where you define the Matchmaking mode that you want to use, the baseline networking requirements necessary to match users, and the high-level criteria required to make a match.

There are two types of pools you can create, matchmaking pools and skill pool. Pools are the basic matchmaking configurations for a group of users, game-type, or game mode. The Pools define the number of users per matchmaking session, the connectivity requirements, and other high-level matchmaking tuning. Skill pools can be created and added to matchmaking pools to account for a user’s cumulative skill level when making matches.

If you create multiple pools and skill pools for the same app, each pool created will have a separate queue of users. Users in different pools cannot be matched.

**Create a Matchmaking Pool**

To create a matchmaking pool, navigate to [Matchmaking](https://dashboard.oculus.com/app/matchmaking) in the Developer Center, use the drop-down to select **Pool**, click **Create Pool**, and enter your pool details.

* **Pool Key** - This is the unique string that you will allow you to reference this matchmaking pool in your app. The Pool Key is case-sensitive, the name you define in the Dashboard must exactly match the key you reference in your code. 
* **Mode** - Select one of the matchmaking modes (Quickmatch or Browse) described above. 
* **Users per Match** - Users per match is four configurations that detail how many players are supported in a session. 
	+ **Min Users** - The minimum number of users required to initiate a session.
	+ **Min Preferred Users** - (Optional) The ideal minimum number of users in a session. Fewer users is supported (down to the Min Users defined), but the game experience may be degraded.
	+ **Max Preferred Users** - (Optional) The ideal maximum number of users in a session. More users are supported (up to the Max Users defined), but the game experience may be degraded.
	+ **Max Users** - The maximum number of users supported in a session.
	
* **Skill Pool** - If you would like to add a skill dimension to your matchmaking pool, please see the section below about creating a skill pool. Once the skill pool has been created you can add it to the multiplayer pool.
* **Advanced Quickmatch** - Select whether you would like this pool to support Advanced Quickmatch. Information about Advanced Quickmatch can be found on the [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/ "Matchmaking places users together in a shared multiplayer experience. User matching can be done by common skill or other criteria that you define. The Matchmaking service offers two modes, Quickmatch and Browse.") page. 
	+ **Can people create and enqueue rooms themselves?** - Select whether you would like to allow users to create their own matchmaking rooms. If disabled, only system generated rooms will be supported.
	+ **Can the system create rooms to match people into?** - Select whether you would like to allow the matchmaking service to create rooms when it finds matches. If disabled, the service will rely on users to create and enqueue rooms.
	+ **Can unmatched people join matchmaking rooms?** - Select whether to allow users not matched by the matchmaking service to join a room, i.e. members of a party or friends of the matched user. If disabled, only users matched by the service can be added to a matchmaking room. 
	+ **Can the matchmaking service keep matching into the same room?** - Select whether to allow users to be matched to the same matchmaking room multiple times. For example, enabling would allow users to join an in-progress game or trickle into a room one by one. If disabled, once a match is made, the room will be removed from the queue.
	+ **Enable host migration when the room owner leaves the room?** - Select whether you would like to transfer ownership of a user-created room in the event that the room owner leaves. The person who has been in the room the longest will become the room owner automatically if enabled.
	
* **Should Consider Ping Time?** - Choose if you would like the matchmaking service to consider peer-to-peer latency when matching users. If yes: 
	+ **Acceptable Ping Time (ms)** - The maximum acceptable ping time for users to be matched. 
	+ **Good Ping Time (ms)** -The longest ping time before multiplayer experience will be affected.
	
* **Advanced Tuning** - Advanced tuning options are available if you’d like to further refine the pools of users. Select **Show Advanced Tuning…’** to reveal these options. We'll review how to use these tuning options in the [Testing and Tuning](/documentation/platform/latest/concepts/dg-matchmaking-5debugging/) page.
	+ **Minimum Quality Bar** - (Optional) A ratio defining the minimum Match Quality where a match should be made. We recommend starting with the default 0.5 and using this value to fine-tune matches. Small multiplayer populations may wish to reduce this number to allow users to be matched more easily. See the next section for information about how we determine match quality. The multiplayer queries described below will also affect the Match Quality.
	+ **Reservation Period** - (Optional) This is the amount of time, in seconds, that a user has to accept a multiplayer session before their spot is released to another user.
	+ **Suggested Rampdown** - (Optional) Potential matches are ranked in terms of their Match Quality. When users enter the matchmaking queue the match quality the service will try to match the user with is 1, the required score gradually decreases adding incrementally less ideal matches over time. The Suggested Rampdown is the time, in seconds, for the score to decrease from 1 to your defined Minimum Quality Bar.
	


**Create a Skill Pool**

To create a skill pool, use the drop-down to select skill pool, click ‘Create Pool’, and enter the following information for your skill pool. 

* **Skill Pool Key** - This is the unique string that you will use to reference this skill pool. The Skill Pool Key is case-sensitive, the key you define in the Dashboard must exactly match the name you reference in your code. 
* **Luck Factor** - Luck Factor is a qualitative judgment about how much luck is involved in your game. Card games would have a higher Luck Factor and it would be appropriate to allow players of a wide skill range, while a skill-based game, like chess, rely more on skill and less on luck. 
* **Draw Probability** - This is a number (between 0 and 1, inclusive) that is your estimate that a match of evenly-matched players will result in a draw.
* **Skill Reset** - Skill reset allows you to reduce, or normalize, the skill ratings for all players by a certain amount at a specified time.


## Data Settings

Data Settings are the key/value pair data that the enqueuing player or room provides about itself at enqueue time. Data Settings can be used both to determine what a player is looking for in a match, as well as what a player looks like to another player. For example, if a player may be enqueued with the type of match they want to play, the map they want to play on, and the level they have achieved in the game. You may also use Data Settings to ensure that matches are only made with users who are using the same version of your app.

To add Data Settings to a matchmaking pool, navigate to [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/) in the Developer Center, click the more options selection for the pool, and then click **Manage Queries**. Then, on the Matchmaking Queries page, click **Edit Data Settings**.

* **Key** - This is the unique string that you will use to reference this Data Setting. The Key is case-sensitive, the name you define in the Dashboard must exactly match the key you reference in your code. 
* **Type** - The type of data you are entering. Options are: 
	+ **DOUBLE** - A decimal value to 2 decimal places.
	+ **INTEGER** - An integer.
	+ **INTEGER\_BITSET** - A hex bitset. 
	+ **STRING** - An enumerated string where you define the acceptable values.
	
* **Default Value** - The default value of the Data Setting if a value is not provided.


We'll review how to implement Data Settings by applying them to users or rooms at enqueue time on the [Adding Skill and Using Queries](/documentation/platform/latest/concepts/dg-matchmaking-4skill_queries/) page.

## Matchmaking Queries

Matchmaking Queries allow you to define the criteria that determines whether enqueued players and rooms can be matched with each other. These expressions compare the Data Settings of potential matches against each other. You define the Matchmaking Queries in the Developer Dashboard. At enqueue time, the Data Settings provided for the user or room will be compared with potential matches using the Matchmaking Queries.

A Matchmaking Query is composed of one or more expressions that make up a conditional statement. The Matchmaking service populates each expression with the Data Settings of the user and potential match candidate, and determines the quality of the potential match. The 'How do we determine who gets matched?' section below will review how we use this information to compare potential matches. 

To add a Matchmaking Query Expression to a Matchmaking Pool, navigate to [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/) in the Developer Center, click the more options selection for the Pool, and click **Manage Queries**. Then, in the Matchmaking Queries page, click **Create Query**.

* **Query Key** - This is the unique string that you will use to reference this Matchmaking Query. The Query Key is case-sensitive, the name you define in the Dashboard must exactly match the key you reference in your code. 
* **Importance** - You will configure an importance for the expression. When an expression passes, it evaluates to a value of 1, and otherwise (failure case) evaluates to the value of the associated importance. Note that the match-on-failure delay times below are calculated based on a rampdown time of 30 seconds. The greater the assigned importance, the less likely a match will occur if the expression fails. And in the case of expressions with **Required** importance, a failure will never result in a match. 
	+ **Required**: 0, i.e. never matches on failure.
	+ **High**: ~0.55, i.e. matches on failure after 27 seconds.
	+ **Medium**: ~0.75, i.e. matches on failure after 15 seconds.
	+ **Low**: ~0.9, i.e. matches on failure after 6 seconds.
	
* **Expression** - The Expression is where you define what criteria must be, or youâ€™d prefer to be, met in order for a match to be made. You can define that a Data Setting must be in a specified range of a defined value or the other users Data Setting. 


**How do we determine who gets matched?**

Each potential match between users is assigned a Match Quality value between 0 and 1. When determining the quality of a match between users, the criteria values of the criteria considered, like Ping Time, Skill, and Queries get multiplied together to get a single Match Quality value. A successful match is made when the Match Quality exceeds the match threshold. The match threshold decreases over time that a user is enqueued. The Match Quality value and how quickly the match threshold decreases can be configured in your matchmaking pool. We recommend leaving these values as the default until you have data to evaluate the quality of your matches. We'll review how to tune your matches in the [Testing and Tuning](/documentation/platform/latest/concepts/dg-matchmaking-5debugging/) section.

A value of 0.5 is considered to be a marginal match, while 0.9 an excellent match. A successful match occurs if the match value is greater than or equal to the match threshold. With the rampdown, a match threshold is 1.0 at enqueue time seeking a perfect match, but will decrease to 0.5 over a rampdown period of 30 seconds (default, the rampdown time can be configured in your Pools) where less ideal matches will be accepted.
