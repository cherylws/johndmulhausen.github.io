---
title: User Verification
---
User Verification validates the identity of each user accessing your application.

In addition to the basic Entitlement Check, this feature uses a client-provided nonce that is used by your trusted server to verify that the Oculus ID provided by the client is valid for the user providing it. This user verification does not replace the Entitlement Check.

![](/images/documentation-platform-latest-concepts-dg-ownership-0.png)  
Your application will call ovr\_User\_GetUserProof(), or Platform.User.GetUserProof() if you’re using Unity, to retrieve the nonce. Then after passing to your server, make a S2S call to verify that the user is who they claim to be.

## Integrate User Verification

Minimal integration is required for User Verification, the only function you have to integrate is to retrieve the nonce. The end-to-end flow for User Verification can be found in the diagram above. 

**Generate nonce:**

Native - ovr\_User\_GetUserProof()

Unity - Platform.User.GetUserProof()

Detail about this function can be found in the Platform SDK [Reference Content](/documentation/platform/latest/concepts/book-reference/ "The Platform SDK developer reference contains a complete list of the Platform SDK headers, functions, and data structures."). Unreal developers can use the native API by using following the steps listed in the [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/ "The Unreal getting started guide will walk you through the basics of setting up your development environment and checking the user's entitlement.") guide. 

**Validate Nonce (POST)**

The next step requires to you send a S2S API request. See the [Server-to-Server API Basics](/documentation/platform/latest/concepts/pgsg-s2s-basics/ "Some platform features use server-to-server (S2S) REST API calls to perform actions not appropriate to be sent from client devices. These APIs are provided to ensure a secure interaction between your back-end servers and the Oculus Platform.") page for information about interacting with our APIs.

Verify that the Oculus ID that is being sent from the client valid by sending the nonce and Oculus ID to the following S2S API. Please see the [Users, Friends, and Relationships](/documentation/platform/latest/concepts/dg-presence/ "Users, friends, and relationships manages information about each user's unique persona, their relationship with their friends, and their recent encounters in VR.") page for more information on retrieving the Oculus ID.

$ curl -d "access\_token=$APP\_ACCESSTOKEN" -d "nonce=$NONCE" -d “user\_id=$USER\_ID” https://graph.oculus.com/user\_nonce\_validateThe request returns a verification of the nonce. For example:

{"is\_valid":true}## Retrieve a Verified Org Scoped ID

Once you've used ovr\_User\_GetUserProof() and the S2S API to verify the Oculus ID being sent from the client is valid, you can then use that information to retrieve a verified Org Scoped ID.

$ curl -d "access\_token=$APP\_ACCESSTOKEN" -d “fields=org\_scoped\_id” https://graph.oculus.com/<userID>The request returns a verified Org Scoped ID:

{"org\_scoped\_id":"<ID>"}