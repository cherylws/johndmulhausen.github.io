---
title: Achievements
---
Create trophies, badges, awards, and more to challenge your users to reach a goal or objective. Users can see the achievements their friends have earned creating a competition among friends.

Achievements earned in your app can also be displayed in Oculus Home to show a user's progress in and progression through a game.

This guide shows you how to define global achievements, the SDK methods and Server-to-Server calls you can make to interact with the achievements service, and an example Unity implementation you can review. 

The Oculus Platform supports three types of achievements: simple, count and bitfield. Each achievement type has a different unlock mechanism.

* **Simple** achievements are all-or-nothing. They are unlocked by a single event or objective completion. For example, a simple achievement is unlocked when Frodo reaches Mount Doom.
* **Count** achievements are unlocked when a counter reaches a defined target. Define the **Target** to reach that triggers the achievement. For example, a target achievement is unlocked when Darth Vader chokes 3 disappointing Imperial officers.
* **Bitfield** achievements are unlocked when a target number of bits in a bitfield are set. Define the Target and Bitfield Length that triggers the achievement. For example, a bitfield achievement is unlocked when Harry destroys 5 of the 7 Horcruxes.
The Oculus Platform tracks and manages achievements. The platform displays a toast notification and plays a sound when an achievement is unlocked. Your app manages the triggers and updates for achievements and displays achievements to the user.

## Create Your Achievements

The first step in adding achievements to your game is to define the achievements and how they are unlocked. To create an achievement, go to the [Achievements](https://dashboard.oculus.com/app/achievements) tab on the Developer Dashboard.

When creating achievements, you can choose to localize the achievement into multiple languages. When entering the achievement information, select **Choose Languages**, check the boxes of the languages you would like to localize into, and enter the information for the languages selected. The language displayed to the user is based on the locale set for the user's device OS.

Select **Create Achievement** and enter the following information:

* **API Name** - The unique string that you use to reference the achievement in your app. The API Name is case-sensitive, the name you define in the Dashboard must exactly match the name you reference in your code. 
* **Title** - The short descriptive name that the user will see.
* **Description** - The full description of the achievement. You may wish to describe how a user can unlock or earn this achievement.
* **Unlocked Description** - (Optional) This is a description that will replace the Description after the user has unlocked the achievement.
* **Locked and Unlocked Icons** - (Optional) The icons associated with the achievement. The Locked Icon will be displayed to users who have not earned the achievement, while the Unlocked Icon will be displayed to the users who have. If only an Unlocked Icon is provided, the Locked Icon will be a grayscale version of the Unlocked Icon. If neither is provided, a default icon will be used.
* **Write Policy** - Choose one of the two Write Policy options: 
	+ **Client Authoritative** is the default setting and means that achievement progress may be written or unlocked from the client app.
	+ **Server Authoritative** means that the achievement can only be written or updated using S2S APIs listed below. This is typically used to reduce cheating when trusted servers are running the game sessions. Achievement information and progress may still be queried from the client app.
	
* **Is Achievement Secret** - Yes/No toggle that chooses whether the achievement title, description, icon, and progress will be hidden until the achievement is completely earned or unlocked. Default selection is **No**.
* **Type** - This is the type of achievement. The values are **simple**, **count**, and **bitfield**. See the description above for information about these achievement types.
Select **Submit** when you’re finished to save the achievement. You can update your achievements in the Developer Center at any time.

**Archiving Achievements**

You can archive achievements at any time. Archiving does not delete the achievement or a user's progress, it hides the achievement and any progress the user. You can unarchive an achievement to restore visibility to users.

## Integrating Achievements - Unity and Native

Once you’re finished creating the achievements, you can begin to integrate them in your game. When calling the SDK methods in this section use the **API Name** you defined in the Developer Center.

The following SDK methods can be called from your client app. Detail about each function can be found in the Platform SDK [Reference Content](/documentation/platform/latest/concepts/book-reference/ "The Platform SDK developer reference contains a complete list of the Platform SDK headers, functions, and data structures.").

* **Retrieve information about an achievement:**

Native - ovr\_Achievements\_GetDefinitionsByName()

Unity - Platform.Achievements.GetDefinitionsByName()

Retrieves information about a specific achievement; including, achievement name, type, and target or bitfield length. 


* **Retrieve information about the user’s progress on an achievement:**

Native - ovr\_Achievements\_GetProgressByName()

Unity - Platform.Achievements.GetProgressByName()

Retrieves information about a user's progress on a specific achievement; including, name, unlocked status, time the achievement was unlocked, current bitfield, and current count.


* **Retrieve information about all achievements:**

Native - ovr\_Achievements\_GetAllDefinitions()

Unity - Platform.Achievements.GetAllDefinitions()

Retrieves information about all achievements; including, achievement name, type, and target or bitfield length.
* **Retrieve information about the user’s progress on all achievements:**

Native - ovr\_Achievements\_GetAllProgress()

Unity - Platform.Achievements.GetAllProgress()

Retrieves information about a user's progress on all achievements; including, name, unlocked status, time the achievement was unlocked, current bitfield, and current count.


The following SDK methods can be called for any achievement that has a Client Authoritative write policy. If the achievement is Server Authoritative you’ll need to use the S2S REST calls in the section below to make updates from your trusted server.

* **Unlock an achievement:**

Native - ovr\_Achievements\_Unlock()

Unity - Platform.Achievements.Unlock()

Unlock a specified achievement. This will completely unlock an achievement, including Count and Bitfield achievements, even if the target has not been met.


* **Increment the count on a Count achievement:**

Native - ovr\_Achievements\_AddCount()

Unity - Platform.Achievements.AddCount()

Increment the counter on a Count type achievement. 


* **Add to a Bitfield achievement:**

Native - ovr\_Achievements\_AddFields()

Unity - Platform.Achievements.AddFields()

Unlock a bit in a Bitfield type achievement. Once a bit is unlocked it will not change from that state, e.g. if the bitfield is 10011 and an AddFields call is made with 00110, the resulting state is 10111.


## Example Implementation - Unity

The following Unity example demonstrates setting an achievement to unlock on an event that you define. The following example is taken from the VRHoops sample app. Please see the [Sample Apps](/documentation/platform/latest/concepts/book-sampleapp/) page for more information about the apps that are available.

The example first defines an achievement that was configured on the Developer Center called LIKES\_TO\_WIN. The example then checks for an update message to see if the achievement has been unlocked and, if true, sets the achievement as unlocked in the app. Otherwise, the game moves on and increments the count on the achievement if a game condition is met, in this example if a win is recorded. 

using UnityEngine; using System.Collections; using Oculus.Platform; using Oculus.Platform.Models; public class AchievementsManager : MonoBehaviour { // API NAME defined on the dashboard for the achievement private const string LIKES\_TO\_WIN = "LIKES\_TO\_WIN"; // true if the local user hit the achievement Count setup on the dashboard private bool m\_likesToWinUnlocked; public bool LikesToWin { get { return m\_likesToWinUnlocked; } } public void CheckForAchievmentUpdates() { Achievements.GetProgressByName(new string[]{ LIKES\_TO\_WIN }).OnComplete( (Message<AchievementProgressList> msg) => { foreach (var achievement in msg.Data) { if (achievement.Name == LIKES\_TO\_WIN) { m\_likesToWinUnlocked = achievement.IsUnlocked; } } } ); } public void RecordWinForLocalUser() { Achievements.AddCount(LIKES\_TO\_WIN, 1); CheckForAchievmentUpdates(); } }## Integrating Achievements - Unreal

After you've created your achievements on the Oculus Dashboard, as described above, integrating in Unreal is done by using OSS nodes in your game blueprint.

There are some differences between how Unreal and Oculus handle achievements. For example, progress for UE4 achievements counts from 0 to 100.

On app startup, or before you can call to retrieve or write any achievement information, you need to add **Cache Achievement Descriptions** and **Cache Achievements**, in that order, to your blueprint. This makes the information about the app's achievements available. 

**Read/Retrieve Achievement Progress**

To retrieve the achievement progress for a player in your app.

1. In your blueprint, add **Get Cached Achievement Description** to retrieve information about a specific achievement, including the achievement type.
2. Then add, **Get Cached Achievement Progress** to get the progress for that user.
3. Convert the value returned to the proper format to display to the user: 
	1. Simple: either 0 if locked or 100 if unlocked.
	2. Count: current count * 100 / the target value (capped at 100).
	3. Bitfield: number of '1's in the string * 100 / the target value (capped at 100).
	
**Write Achievement Progress**

To write achievement progress for a player in your app.

1. In your blueprint, add **Get Cached Achievement Description** to retrieve information about a specific achievement, including the achievement type.
2. Then add, **Write Achievement Progress** to write the progress for that user. When writing progress, convert the progress as follows: 
	1. Simple: unlock when this is called with any value.
	2. Count: will add the value from the WriteObject to the achievement progress. Only Int32, Int64, UInt32, and UInt64 values are supported.
	3. Bitfield: use a series of “0” and “1”s to the bitmask. Int32 values will be turned into their string representation: 101 → “101” and string values will be used as passed.
	
## S2S REST Requests

Certain actions require you to interact directly with our server. For example, if any achievement is set to Server Authoritative you’ll need to make API calls from your trusted server to increment and unlock achievements. See the [Server-to-Server Basics](/documentation/platform/latest/concepts/pgsg-s2s-basics/ "Some platform features use server-to-server (S2S) REST API calls to perform actions not appropriate to be sent from client devices. These APIs are provided to ensure a secure interaction between your back-end servers and the Oculus Platform.") page for information about interacting with our APIs.

**Create or Update an Achievement (POST)**

Create or update an achievement allows you to create a new achievement, or update one that already exists. This will update the achievement for all users.

**Parameter****Required Y/N****Description****Type****Example**api\_nameY

The name used to reference to the achievement in this API and in the client SDK. This alphanumeric string must be unique for the app.

string

“VISIT\_3\_CONTINENTS”achievement\_typeY

This is the achievement type. There are three types of achievement, please see the description above for information on the different types.

enum

* simple
* count
* bitfield
"simple"entry\_write\_policyY

This determines who is allowed to write achievement progress. Please see the description above for information on the two different write policies.

enum

* client\_ authoritative
* server\_ authoritative
"client\_authoritative"targetY, if achievement\_type = count or bitfield

The number of event occurrences for the achievement to be unlocked. Please see the description above for more information on target. 

integer

50bitfield\_lengthOnly if achievement\_type = bitfield

The size of the bitfield for this achievement.

integer

7is\_archivedN - Default is false.

Boolean that determines if the achievement is archived. Can also be used to unarchive an achievement. Archiving does not delete the achievement or user progress.

boolean

"false"titleY

The name of the achievement that the user sees. 

string

"Visited 3 Continents"descriptionY

The text description that the user sees. 

string

"This achievement unlocks when..."unlocked\_description \_overrideN

The text description that the user sees when the achievement is unlocked. 

string

"Congratulations! You visited 3 continents."is\_secretN - Default is false.

Boolean that indicates whether the achievement is hidden until earned. 

boolean

"false"unlocked\_image\_fileN - A default image will be used.

The local path to the icon shown after the achievement has been earned. Must be a 256x256 PNG file.

string

“@/path/to/unlocked\_icon.png; type=image/png”locked\_image\_fileN - If an unlocked image is provided, a grayscale version will be used as the locked image. Otherwise, a default is used.

The local path to the icon shown before the achievement is earned. Must be a 256x256 PNG file.

string

“@/path/to/locked\_icon.png; type=image/png”Example Create/Update Request

$ curl -F "access\_token=$APP\_ACCESSTOKEN" -F "api\_name=VISIT\_3\_CONTINENTS" -F "achievement\_type=BITFIELD" -F "achievement\_write\_policy=CLIENT\_AUTHORITATIVE" -F "target=3" -F "bitfield\_length=7" -F "is\_archived=false" -F "title=Achievement Title" -F "description=How to earn me" -F "unlocked\_description\_override=You did it" -F "is\_secret=false" -F "locked\_image\_file=@/path/to/locked\_icon.png;type=image/png" -F "unlocked\_image\_file=@/path/to/unlocked\_icon.png;type=image/png" https://graph.oculus.com/$APPID/achievement\_definitions Example Response

{ "id":"1074233745960170" } **Retrieve Achievement Definitions (GET)**

Query achievement definitions allows you to get information about achievements to display to your users. 

**Parameter****Required Y/N****Description****Type****Example**api\_namesN

The names of the achievement definitions to fetch. If omitted all achievement definitions are returned.

array of strings

["VISIT\_3\_CONTINENTS", "WALK\_500\_MILES"]include\_archivedN

Boolean that indicates whether to include archived achievements. This may only be used when an App Access Token is used to authenticate.

boolean

"false"Example Request

$ curl -G -d "access\_token=$APP\_ACCESSTOKEN|$USER\_ACCESSTOKEN" -d 'api\_names=["VISIT\_3\_CONTINENTS", "WALK\_500\_MILES"]' -d "include\_archived=true" -d 'fields=api\_name,achievement\_type,achievement\_write\_policy,target,bitfield\_length,is\_archived,title, description,unlocked\_description\_override,is\_secret,locked\_image\_uri,unlocked\_image\_uri' https://graph.oculus.com/$APPID/achievement\_definitions Note: The example above shows "access\_token=$APP\_ACCESSTOKEN|$USER\_ACCESSTOKEN", this is showing that you can use either the User Access Token or the App Access Token and retrieve the same result. It is not a combination of the two tokens.The definition of the fields are the same as in the create or update API call above. Images are locked\_image\_uri and unlocked\_image\_uri and notlocked\_image\_file and unlocked\_image\_file. This is the location of the image source and not the location of the local image file. 

Example Response

{ "data": [ { "id":"1074233745960170", "api\_name":"VISIT\_3\_CONTINENTS", "achievement\_type":"BITFIELD", "achievement\_write\_policy":"CLIENT\_AUTHORITATIVE", "target":3, "bitfield\_length":7, "is\_archived":false, "title":"Achievement Title", "description":"How to earn me", "unlocked\_description\_override":"You did it", "is\_secret":false, "locked\_image\_uri":"https://scontent.oculuscdn.com/...", "unlocked\_image\_uri":"https://scontent.oculuscdn.com/..." }, { ... } ] }**Write (and Unlock) Achievement Progress (POST)**

Write achievement progress updates a user’s progress on an achievement. This method accumulates progress, for count type achievements, instead of overwriting values. For example, add\_count=25 will increment the count by 25, not set the current count to 25. This is so that conflicts that arise from updating achievements from multiple sources simultaneously or making progress from multiple devices in offline mode can be handled gracefully.

**Parameter****Required Y/N****Description****Type****Example**api\_nameY

The names of the achievement to update.

string

"VISIT\_3\_CONTINENTS"add\_countY if the achievement is a Count type.

Value to add to the progress counter for this achievement. Only valid for COUNT achievements.

integer

25add\_bitsY if the achievement is a Bitfield type.

Bits to add to the progress of this achievement. Only valid for BITFIELD achievements.

string"110001"force\_unlockN - Default is false.

Instantly unlocks an achievement regardless of progress. This must be used to unlock SIMPLE achievements.

boolean

"false"Example Request

$ curl -d "access\_token=$APP\_ACCESSTOKEN|$USER\_ACCESSTOKEN" -d "api\_name=MY\_ACHIEVEMENT" -d "add\_bits=0011001" -d "add\_count=25" -d "force\_unlock=true" https://graph.oculus.com/$USERID/achievements Note: The example above shows "access\_token=$APP\_ACCESSTOKEN|$USER\_ACCESSTOKEN", this is showing that you can use either the User Access Token or the App Access Token and retrieve the same result. It is not a combination of the two tokens.Example Response

{ "id":"1074233745960170", "api\_name":"MY\_ACHIEVEMENT", "just\_unlocked":true } The response will contain the parameter just\_unlocked that indicates if this operation caused the achievement to unlock.

**Query Achievement Progress (GET)**

Retrieve a user’s progress for an achievement.

**Parameter****Required Y/N****Description****Type****Example**api\_namesN

The names of the achievement definitions to fetch. If omitted all achievement definitions are returned.

array of strings

["VISIT\_3\_CONTINENTS", "WALK\_500\_MILES"]Example Request

The definitions for the ‘fields’ are the same as in the Create or Update Achievement call above.

$ curl -G -d "access\_token=$APP\_ACCESSTOKEN|$USER\_ACCESSTOKEN" -d 'api\_names=["VISIT\_3\_CONTINENTS", "WALK\_500\_MILES"]' -d 'fields'='definition{api\_name,target},count\_progress,bitfield\_progress,is\_unlocked,unlock\_time' https://graph.oculus.com/$USERID/achievementsNote: The example above shows "access\_token=$APP\_ACCESSTOKEN|$USER\_ACCESSTOKEN", this is showing that you can use either the User Access Token or the App Access Token and retrieve the same result. It is not a combination of the two tokens.Example Response - The following is an example of an unlocked bitfield achievement.

 { "data": [ { "id": "1074233745960170", "definition": { "api\_name": "VISIT\_3\_CONTINENTS", "target": 3 }, "count\_progress": 0, "bitfield\_progress": "1001100", "is\_unlocked": true, "unlock\_time": 1459815726 } ] }**Remove all Achievements and Progress for a User (POST)**

This method will remove all achievement progress, both locked and unlocked, for a user.

$ curl -d "access\_token=$APP\_ACCESSTOKEN" -d "user\_id=$USERID" https://graph.oculus.com/achievement\_remove\_all Example Response

{ "success":true } 