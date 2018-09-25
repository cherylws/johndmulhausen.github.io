---
title: Server-to-Server API Basics
---
Some platform features use server-to-server (S2S) REST API calls to perform actions not appropriate to be sent from client devices. These APIs are provided to ensure a secure interaction between your back-end servers and the Oculus Platform.

For example, we use these APIs to make [in-app purchases](/documentation/platform/latest/concepts/dg-iap/ "In-app purchases (IAP) allow users to purchase items without leaving your app.") more secure and prevent fraud.

Details about individual S2S calls can be found in the features pages of the [Developer Guide](/documentation/platform/latest/concepts/book-dg/). This page describes the two types of access tokens required to make S2S calls, the User Access and App Access tokens.

Note: Unity editor incompatibility. Older versions of Unity use .NET 3.5 or earlier, which does not support SSL certificates that use SHA2. Modern SSL certs use SHA2 because SHA1 has been compromised. Unity clients that attempt to use the S2S APIs directly can not trust the response message because they can't decrypt the SHA2-based SSL certs that the API uses.## App Access Token

The App Access Token is a string that your back-end uses to identify itself as a trusted resource. The App Access Token should never be shared with the client-side app.

The string is (OC|$APPID|$APPSECRET) where $APPID and $APPSECRET are application specific values found on the [API](https://dashboard.oculus.com/app/api) tab in the Developer Console.

The $APPSECRET may be changed in the event that your credentials are compromised or you need a fresh set of API credentials. Changing the App Secret will revoke permissions from the previous App Secret.

When calls originate from a trusted server and are in reference to specific user, the App Access Token will be used and the Oculus ID will be passed as a URI parameter. For example, during gameplay a user may unlock a rare achievement. Due to the achievement's desirability you have configured the achievement as Server Authoritative, meaning only your trusted server can unlock the achievement. In this scenario your trusted server will make a S2S call, using the App Access Token and Oculus ID, to unlock the achievement on behalf of the user.

## User Access Token

The User Access Token is user-specific string that identifies a user and allows your back-end server to act on their behalf.

The User Access Token is retrieved by sending a request to ovr\_User\_GetAccessToken(). The token will be returned as a response. This token can be passed from the client to your backend.

The User Access Token can be used when interacting on behalf of a user, or in reference to a specific user. For example, after a server-hosted multiplayer match may want to update a leaderboard with the results of the match. In this scenario, your server would make a call to update the leaderboard entry for each user with the results of the match using the User Access Token to identify the user.

## Forming the API Calls

Each API call made to the Oculus APIs should be formed based on the information on the features pages, but there are some general similarities to be aware of.

Most calls will ask you to reference the $AppID in the URI of the call. For example, when verifying that a user owns an IAP item:

curl -X POST -d https://graph.oculus.com/$APPID/verify\_entitlement?sku=$SKU-TO-CHECK&access\_token=$USER-ACCESS-TOKENThis is the same App Id that is found in the [API](https://dashboard.oculus.com/app/api) tab of Developer Center.

## Example S2S Call

Let's review the process to form an S2S REST call using the information on this page. 

For this example, we'll use the Oculus S2S API to unlock a client-authoritative achievement that a user has earned. This example assumes that you have already created the achievement and integrated the hooks into your app, additional information can be found on the [Achievements](/documentation/platform/latest/concepts/dg-achievements/ "Create trophies, badges, awards, and more to challenge your users to reach a goal or objective. Users can see the achievements their friends have earned creating a competition among friends.") page.

1. Retrieve the user's id - To call the Oculus APIs on behalf of a user you need to include the Oculus Id identifying that user. Call ovr\_User\_GetLoggedInUser on Native or Platform.User.GetLoggedInUser on Unity to retrieve the ID. It will be returned as the ovrID of the user. 
2. Pass the information to your trusted server - Once you've retrieved the Oculus ID, pass the ID and the api\_name of the achievement you wish to update or unlock from the client device to your server.
3. Form the App Access Token - Use the following credentials that we retrieved from the API section of the Developer Center:
	* App Id - 1120829788014273.
	* App Secret - 5f8730a4n51c5f8v8122aaf971b937e7.
	You can then form the App Access Token as: OC|1120829788014273|5f8730a4n51c5f8v8122aaf971b937e7.


4. Call the API to unlock the achievement - Once you've retrieved the information from the client device and formed the App Access Token, send the API call to unlock the achievement. $ curl -d "access\_token=OC|1120829788014273|5f8730a4n51c5f8v8122aaf971b937e7" -d "api\_name=MY\_SIMPLE\_ACHIEVEMENT" -d "force\_unlock=true" https://graph.oculus.com/$USERID/achievements The API will respond with:

{ "id":"$USERID", "api\_name":"MY\_SIMPLE\_ACHIEVEMENT", "just\_unlocked":true } Letting you know that your request was successful. Pass a message back to the client indicating that the achievement has been successfully unlocked. 


## HTTP Status Codes

The Oculus S2S REST APIs support the standard HTTP status codes to let you know, in the event of an issue, what went wrong.

CodeStatus400Bad Request401Unauthorized Request403Forbidden Request404Not Found500Internal Server Error