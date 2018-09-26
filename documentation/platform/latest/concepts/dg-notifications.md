---
title: Notifications
---

Create targeted messages that Oculus will deliver to your users’ Notification Feed. Notifications allow you to interact with your users outside of your app.

Congratulate them for unlocking a rare achievement with an XP boost, notify them of an upcoming in-game event, or remind them that they have unused gems. The message you send is up to you.

Notifications that you generate are displayed in the Notification Feed with the other Oculus notifications. Users are made aware of the notification by badging both on and in the Gear VR Oculus app. Then when the user interacts with your notification, your app will be launched for a deeper experience.



![](/images/documentationplatformlatestconceptsdg-notifications-0.png)



**(Badging on the Oculus app)**



![](/images/documentationplatformlatestconceptsdg-notifications-1.png)



**(Badging in the Oculus app)**

## Writing Notifications

When creating your content, we recommend that each notification has a personalized element and a clear call to action. Concise, actionable notifications are most effective, especially those that are a result of some in-app action.

Notification titles of 30 characters (or less) fit on one line and notification messages of 70 characters (or less) on two lines.



![](/images/documentationplatformlatestconceptsdg-notifications-2.png)



Users have the ability to unsubscribe from notifications, so it is your responsibility to create high-quality and interesting notifications at a reasonable cadence. Notifications that users find spammy or uninteresting may result in them unsubscribing from your app’s notifications.



![](/images/documentationplatformlatestconceptsdg-notifications-3.png)



All notifications must conform to the Oculus [Content and Design Guidelines](/distribute/latest/concepts/publish-content-guidelines/). Apps that violate these guidelines or otherwise create a poor user experience (for example, by sending an excessive volume of notifications) may be blocked from sending notifications. 

## Targeting Notifications

When creating your notification you’ll have the option of sending the notification to a list of users you define, or to a targeted audience of your users.

**Target by `recipient_ids`**

Please note that this is not the user's Org Scoped ID. Users will have different IDs for each app.

**Target by `target_audience`**

You can also target users by sending notifications to predefined audience. To send to a predefined audience, send `"ALL"` or `“LAST_30_DAY_ACTIVE”` as the `target_audience`. When using `target_audience` the `recipient_ids` parameter should be omitted from your API call.

`"ALL"` will send the notification to every user entitled to your app. In other words, every user who has ever installed your app through the Oculus Store. 

`“LAST_30_DAY_ACTIVE”` will send the notification to all users who are entitled to your app and have used their VR device in the last 30 days. This targeting will include users who have been active in any VR app, not just your app, in the last 30 days. 

When using `target_audience`, users’ time zones will be taken into account so notifications will send at the same local time for each user. In the 24 hours following `send_time` (or, if omitted, the Unix timestamp at time of send), users will receive the notification at a consistent time in their respective time zones. This enables you to maximize the impact of notifications by choosing the most relevant local time for them to be received. 

For example, if `send_time` is 1527883200 (8:00pm UTC, June 1, 2018), each user will receive the notification at 8:00pm in their respective time zone. If `send_time` is omitted, notifications are sent to users in the UTC time zone immediately, and users in other time zones will receive it at the same respective local time over the next 24 hours. 

**A small percentage of any notifications sent to a target audience will be held out as a control.**

## Creating and Integrating Notifications

Once you’ve written your notification message and determined who will receive the notification, you can create and schedule the message to be sent.

Notification are created by REST API call. Please review the information on the [Server-to-Server API Basics](/documentation/platform/latest/concepts/pgsg-s2s-basics/) page for information about interacting with the Oculus S2S APIs. 

The format of the POST is:

```
curl https://graph.oculus.com/notification_request -d access_token='OC|&lt;APP_ID&gt;|&lt;APP_SECRET&gt;' 
-d app_id=&lt;APP_ID&gt; -d title='Title' -d message='Message' -d uri='url' 
-d recipient_ids=["&lt;USER_ID&gt;","&lt;USER_ID&gt;","&lt;USER_ID&gt;"]
```

|  **Parameter**  |                   **Required Y/N**                   |                                                                 **Description**                                                                 |             **Type**             |         **Example**         |
|-----------------|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|------------------------------|
|  access_token  |                          Y                          | Auth token. See `Server-to-Server API Basics`_ page.  .. _Server-to-Server API Basics: /documentation/platform/latest/concepts/pgsg-s2s-basics/ |              string              |  "OC|&lt;APP_ID&gt;|&lt;APP_SECRET&gt;"  |
|     app_id     |                          Y                          |              Your apps unique id. Found on the API_ page of the Oculus Dashboard.  .. _API: https://dashboard.oculus.com/app/api/              |             integer             |       1269926316430214       |
|     message     |                          Y                          |                                                              Notification message.                                                              |              string              | "Youve won a brand new car!" |
| recipient_ids[] | Y, unless targeting an audience with target_audience |                                                          Array of targeted Oculus IDs.                                                          |         array of strings         |     ["123","456","789"]     |
|      title      |                          Y                          |                                                               Notification title.                                                               |              string              | "Tell them what theyve won." |
|       uri       |                          Y                          |                                                      Deeplink URI. More information below.                                                      |              string              |          See below.          |
|    send_time    |                          N                          |             Unix timestamp of the date and time to send the notification. If omitted, notifications will begin to send immediately.             |              string              |         "1529598630"         |
| target_audience |                          N                          |                                              Defines the audience grouping to receive the message.                                              | enum - "ALL", LAST_30_DAY_ACTIVE |            "ALL"            |

**Using the URI Parameter**

The URI parameter allows you to deeplink into your app. When a user clicks on the notification, your app will be launched and the URI defined in your notification will be passed in the launch intent.

In your app, you’ll need to be able to handle the deeplink message you’ve defined. Native apps will receive a notification of type `ovrMessage_Notification_ApplicationLifecycle_LaunchIntentChanged` on the message queue when the app is launched from a notification.

On startup, check for this notification and call `ovr_ApplicationLifecycle_GetLaunchDetails()` (or `Platform.ApplicationLifecycle.GetLaunchDetails()` in Unity) to retrieve information about how the app was launched. All app launches by this API will have a launch type of `DEEPLINK`. This information allows you to direct the user to the proper app experience.

If the user does not currently have the app installed, they will be directed to the product information page in the Gear VR Oculus app where they can download the app.

## Test Your Notification

Before you send your notification broadly to an audience using the `target_audience` option, you may wish to test your notification and URI integration by sending to yourself or your team using `recipient_ids[]`. Once you're happy with the notification message and deeplink, you may change the targeting to a more broad audience.

## Track Notification Performance

Track the lifetime performance of the notifications you send. To access the Notification analytics, navigate to the [Analytics](https://dashboard.oculus.com/app/analytics/) page for your app, and select the **Notifications** tab.
