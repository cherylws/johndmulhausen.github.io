---
title: Coordinated App Launch (CAL)
---

Coordinated App Launch (CAL) allows users to launch your social app together from Oculus Home.

There are two steps to using CAL in your game, integrating the CAL API and configuring CAL on the Oculus Developer Dashboard. 

## Integrate CAL API

When users launch a CAL-enabled app, your app will receive information about the users in the room, as well as the unique roomID. This information is sent with the launch intent. You can also retrieve this information from the following method: 

```
ovrLaunchDetailsHandle handle = ovr_ApplicationLifecycle_GetLaunchDetails();
if (ovr_LaunchDetails_GetLaunchType(handle) == ovrLaunchType_Coordinated) {
    ovrID roomID = ovr_LaunchDetails_GetRoomID(handle);
    ovrUserArrayHandle usersHandle = ovr_LaunchDetails_GetUsers(handle);
    ...
}
```

If you're using Unity:

```
LaunchDetails launchDetails =
    LaunchDetails(CAPI.ovr_ApplicationLifecycle_GetLaunchDetails());
if (launchDetails.LaunchType == LaunchType.Coordinated) {
    UInt64 roomID = launchDetails.RoomID;
    UserList users = launchDetails.Users;
    ...
}
```

These methods are synchronous and will return results immediately.

You can use the information returned in the launch detail, like the `RoomID` and users in the room, to place the group in a shared VR session.

If you plan to use [Voice Chat (VoIP)](/documentation/platform/latest/concepts/dg-cc-voip/) in your app, you'll need handle the transition to your app. Please see [Parties](/documentation/platform/latest/concepts/dg-cc-parties/) for more information.

**Unreal Development**

If you're using Unreal, please use the native C API using the information found in [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/).

**Testing CAL**

```
adb shell "am start -n com.your.package.name/.YourMainActivity -e intent_cmd \
'"'{"ovr_social_launch":{"type":"COORDINATED","room_id":"123","users" \
:[{"id":"4","alias":"janedoe1234"},{"id":"7","alias":"johndoe5678" \
}]}}'"'"
```

## Configure CAL

To configure CAL, select your app in the [Developer Dashboard](https://dashboard.oculus.com/) and navigate to **Coordinated App Launch (CAL)** under **Platform Services** tab.

Select **Supported** to enable CAL and choose the **Minimum Users** and **Maximum Users** to allow in the launch of an app session. The number of users allowed will depend on the type of app you are creating. For example, a game of Chess should require both a minimum and maximum of 2, while an open-ended multiplayer game could have groups between 2 and 4.

Enter the **Minimum Version Code** for the first build that supports the CAL API. For the approval process, the build may be in a testing or development channel.

Once CAL support is enabled and a supported build is uploaded, any account on that release channel will be able to test the feature in Rooms.

After the configuration is complete and API integrated, you can submit the app for CAL review. Please send an email requesting review to [submissions@oculus.com](mailto:submissions@oculus.com). When the app is approved you will have the option of setting the **Public** field to **Yes** enabling the feature.

## User Experience Recommendations

We recommend that you place users immediately into a social experience when they launch an app by CAL. If your app offers multiple game modes or options, we recommend that you choose a default mode so users are taken to a social VR experience as quickly as possible. If session or game customization is available, present these choices after the users can hear and see each other.
