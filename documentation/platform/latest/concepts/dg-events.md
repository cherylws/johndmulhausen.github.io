---
title: Events
---
Use Events to host time-specific gatherings for your users to attend, like a viewing party, social mixer, or game tournament. Events may be shown in Explore if the post matches a user's interests. Events will be shown in the Oculus Events section of Home and Oculus Explore if deeplinks are implemented. 

Users can subscribe to upcoming VR events and receive a reminder before the event begins. Users can also see which events friends have subscribed to and join them to create a social experience. 

In VR, when a user clicks **Interested** to subscribe to a future event or **Join Now** for an event in progress, they will be prompted to install the app if they have not done so already. Users can also explore and subscribe to events in the Oculus app on Gear VR and Oculus Go.

To help promote your event on social channels, a web site will be created at https://www.oculus.com/experience/events/eventID once the event has been approved.

![](/images/documentation-platform-latest-concepts-dg-events-0.png)  
## Create an Event

To create an event, go to your app's Oculus dashboard in the [Developer Center](https://dashboard.oculus.com/) and select **Discoverability > Events**.

Enter the following information to create your event:

1. **Title** - The title is the short description of the event that will be shown with the event's image. 
2. **Description** - A description of the event. This will be used throughout the platform. The description should be in plain text. 
3. **Image** - The image that will be displayed in association with the event. The uploaded image should meet the asset guidelines, and be 2560 x 1440 24bit .png format.
4. **Start** Time - Start time of the event in your local time zone.
5. **End Time** - End time of the event in your local time zone.
6. **Deeplink Message** (optional) - The deeplink message is a message we will include with apps launched from an event. We'll include the deeplink message with the app launch detail. Information on handling the deeplink message can be found in the section below. The deeplink message should not exceed 1,500 characters. 
A 2D trailer video is required for an event to be shown in Oculus Explore. Trailer videos can be added to the Assets page in the Oculus store.

## Duplicate an Event

You may wish to create a reoccurring event. To duplicate an event, select the options menu next to the event you wish to duplicate, update the information for the new event, and submit the new event for review.

## Integrate Events

Integrating deeplink support into your app is optional. If you do not use deeplinks, the app will be launched from an event by the normal launch process.

You'll integrate a hook into your app that listens for a specific launch detail when the app is started, ovrLaunchType\_Deeplink on Native Android and Launchtype.Deeplink on Unity. When you see these details in the launch event, your app will retrieve the deeplink that you defined to direct the user to the appropriate location in your app. 

For example, on Native Android:

ovrLaunchDetailsHandle handle = ovr\_ApplicationLifecycle\_GetLaunchDetails(); if (ovr\_LaunchDetails\_GetLaunchType(handle) == ovrLaunchType\_Deeplink) { string deeplink = ovr\_LaunchDetails\_GetDeeplinkMessage(handle); // ... }On Unity:

using Oculus.Platform.Models; LaunchDetails launchDetails = new LaunchDetails(CAPI. ovr\_ApplicationLifecycle\_GetLaunchDetails()); if (launchDetails.LaunchType == LaunchType.Deeplink) { String deeplinkMessage = launchDetails.DeeplinkMessage; ... }If you're using Unreal, please use the native API using the information found in [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/ "The Unreal getting started guide will walk you through the basics of setting up your development environment and checking the user's entitlement.").

## Content Review

All posts and stories will reviewed by the Oculus team for content approval and compliance with the [Oculus Code of Conduct](https://support.oculus.com/1694069410806625/). If the submission does not comply, it will be rejected.

## Preview Your Events

Want to see how your event will look before releasing to the public? To test your event:

1. Create an event and save it as a draft.
2. Subscribe yourself to the event by selecting **Subscribe Me To Event**.
3. Launch your mobile VR device. At the bottom of Home, select the gear icon to open the settings menu. In the settings menu select **Developer Settings**, and then choose **View Developer Feed**. You'll need to be a Developer or Admin in your organization to see this menu.
4. Select the **Home** tab, and preview your event in **Explore**.
5. (Optional) If you've chosen to integrate deeplinks, you may select the event link to launch your app and test the deeplink.
6. When you're satisfied with the event and deeplink, you can submit the event for review and public release.
