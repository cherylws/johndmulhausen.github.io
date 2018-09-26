---
title: Requests and Messages
---

The Platform SDK uses a message queue to interact with Native apps. This page describes the concept of the queue and how to retrieve messages and information.

## Making a Request

SDK requests are how you asynchronously send information to, or request information from, the Oculus Platform. Your client initiates these requests by calling the SDK method that corresponds to the action you want to perform. A complete list of the requests you can make are found in the [Reference Content](/documentation/platform/latest/concepts/book-reference/).

For example, let’s retrieve the Oculus Id of the user that is currently logged in. Call the following SDK method:

```
OVRP_PUBLIC_FUNCTION(ovrRequest) ovr_User_GetLoggedInUser();
```

We'll check for a response and the Oculus ID a little later on. 

## Checking the Message Queue

Your app should constantly check the message queue for notifications and messages from the Platform SDK. Messages are responses to some action from your app, while notifications are initiated external systems or other users. 

We recommend that you check the queue every frame for new messages and notifications.

To poll the message queue, call `ovr_PopMessage()`. If a message is present, an `ovrMessageHandle` object will be returned as a pointer to a message or notification.

You should poll the queue until a null value is returned.

## Retrieving Messages and Notifications Off the Queue

After you’ve checked the queue and retrieved a message pointer, you'll check what kind of data the message contains. This will determine how your app handles the information contained in the message.

**Determine the Message Type**

Call `ovr_Message_GetType` with the pointer you retrieved to check the message type.

From our earlier example, let's assume the message type returned is `ovrMessage_User_GetLoggedInUser` indicating that this message is a response to a request for the currently logged in user's Oculus Id.

A full list of message types that can be returned can be found in the `OVR_MessageType.h` SDK file.

**Retrieve the Message Data**

Once you've determined the message type, check to see if the message is an error by calling `ovr_Message_IsError()` passing the pointer to the message. If the response is an error you should handle the error in your app. Check to see if the message is an error before you retrieve any message data. 

If there was no error, our example message will contain a payload of type `ovrUserHandle`. Extract the payload from the message handle with:

```
ovr_Message_GetUser (const ovrMessageHandle obj)
```

The method to retrieve the message payload will typically follow the format '`OVR_Message_`' followed by the message type. A full list of functions to retrieve a message can be found in the `OVR_Message.h` file of the Platform SDK. 

Each message type maps to a data model type telling you exactly what data to expect in the payload. A complete list of the data models that may be returned can be found in the [Reference Content](/documentation/platform/latest/concepts/book-reference/).

Once you’ve retrieved the message payload call `ovr_FreeMessage()` to free the message from memory.

## Making Multiple Requests

If you’re making multiple requests to the same SDK method, you’ll want to be able to associate the responses with the request that you made. For example, you may wish to retrieve data from multiple leaderboards to display to a user.

In this scenario you’ll associate a request id with each call that you make. Then, when you’ve checked the queue and retrieved a message type that matches your leaderboard requests, call `ovr_Message_GetRequestID()` with the message pointer you received and compare the response to the message ids that you set when making the requests. When you match the message to the request you made, retrieve the payload and handle the data as described above.

## Example Implementation

Our [Sample Apps](/documentation/platform/latest/concepts/book-sampleapp/) contain examples of how functioning apps handle messages. CloudStorage is our native sample app that handles multiple types of messages. 
