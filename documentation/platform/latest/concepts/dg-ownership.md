---
title: User Verification
---

User Verification validates the identity of each user accessing your application.

In addition to the basic Entitlement Check, this feature uses a client-provided nonce that is used by your trusted server to verify that the Oculus ID provided by the client is valid for the user providing it. This user verification does not replace the Entitlement Check.



![](/images/documentationplatformlatestconceptsdg-ownership-0.png)



Your application will call `ovr_User_GetUserProof()`, or `Platform.User.GetUserProof()` if you’re using Unity, to retrieve the nonce. Then after passing to your server, make a S2S call to verify that the user is who they claim to be.

## Integrate User Verification

Minimal integration is required for User Verification, the only function you have to integrate is to retrieve the nonce. The end-to-end flow for User Verification can be found in the diagram above. 

**Generate nonce:**

Native - `ovr_User_GetUserProof()`

Unity - `Platform.User.GetUserProof()`

Detail about this function can be found in the Platform SDK [Reference Content](/documentation/platform/latest/concepts/book-reference/). Unreal developers can use the native API by using following the steps listed in the [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/) guide. 

**Validate Nonce (POST)**

The next step requires to you send a S2S API request. See the [Server-to-Server API Basics](/documentation/platform/latest/concepts/pgsg-s2s-basics/) page for information about interacting with our APIs.

Verify that the Oculus ID that is being sent from the client valid by sending the nonce and Oculus ID to the following S2S API. Please see the [Users, Friends, and Relationships](/documentation/platform/latest/concepts/dg-presence/) page for more information on retrieving the Oculus ID.

```
$ curl -d "access_token=$APP_ACCESSTOKEN" -d "nonce=$NONCE" -d “user_id=$USER_ID”
https://graph.oculus.com/user_nonce_validate
```

The request returns a verification of the nonce. For example:

```
{"is_valid":true}
```

## Retrieve a Verified Org Scoped ID

Once you've used `ovr_User_GetUserProof()` and the S2S API to verify the Oculus ID being sent from the client is valid, you can then use that information to retrieve a verified Org Scoped ID.

```
$ curl -d "access_token=$APP_ACCESSTOKEN" -d “fields=org_scoped_id”
https://graph.oculus.com/&lt;userID&gt;
```

The request returns a verified Org Scoped ID:

```
{"org_scoped_id":"&lt;ID&gt;"}
```
