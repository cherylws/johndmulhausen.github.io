---
title: In-App Content
---
Promote self-contained experiences in your app, like a video, photo set, or standalone experience with In-App Content. 

Note: These posts are only shown to English speaking users and on Gear VR and Oculus Go at this time.## Create an In-App Content Post

To create an In-App Content post, go to your app's Oculus dashboard in the [Developer Center](https://dashboard.oculus.com/) and select **Discoverability / In-App Content**.

Enter the following information to create your announcement or story.

1. **Tagline** - A 2-5 word sentence about your In-App Content post. 
2. **Description** - A longer form detail about the content. The description should be 2-3 sentences about your post and cannot include HTML or other markup. This should be specific to your story content, and not just a copy of your app description.
3. **Image** - Image for the content. This should be different than your cover art. It should reflect your story and should be 16:9 Aspect Ratio and a 2560 x 1440 24-bit .png file.
4. **Facebook Trailer Video URL** (optional) - After uploading a 2D or 360 video (preferred) to your Facebook page, copy and paste the video URL and provide it here. Details about creating the trailer can be found in the 'Create a Trailer Video' section below.
5. **Start Time** - The time you would like your story to start showing up in Oculus Home.
6. **Deeplink Message** - A string that you create that will be provided as a parameter in the app launch intent. If a user does not have your app installed when clicking on the deep-link, we will prompt them to purchase your app. Deeplink messages are required for In-App Content posts. 
## Integrate In-App Content

Integrating deeplink support is required to create an In-App Content post.

You'll integrate a hook into your app that listens for a specific launch detail when the app is started, ovrLaunchType\_Deeplink on Native Android and Launchtype.Deeplink on Unity. When you see these details in the launch event, your app will retrieve the deeplink that you defined to direct the user to the appropriate location in your app. 

For example, on Native Android:

ovrLaunchDetailsHandle handle = ovr\_ApplicationLifecycle\_GetLaunchDetails(); if (ovr\_LaunchDetails\_GetLaunchType(handle) == ovrLaunchType\_Deeplink) { string deeplink = ovr\_LaunchDetails\_GetDeeplinkMessage(handle); // ... }On Unity:

using Oculus.Platform.Models; LaunchDetails launchDetails = new LaunchDetails(CAPI. ovr\_ApplicationLifecycle\_GetLaunchDetails()); if (launchDetails.LaunchType == LaunchType.Deeplink) { String deeplinkMessage = launchDetails.DeeplinkMessage; ... }If you're using Unreal, please use the native API using the information found in [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/ "The Unreal getting started guide will walk you through the basics of setting up your development environment and checking the user's entitlement.").

## Create a Trailer Video

A 2D video trailer is recommended for In-App Content. The easiest way is to create a secret Facebook 2D video using the process described below, but we also support streaming videos not on Facebook and photo albums. Please contact us at [exploreapi@oculus.com](mailto:exploreapi@oculus.com) if you'd like to use a photo or video not hosted on Facebook.

**Add a Secret Facebook Video**

You can publish a 2D video to FB as a 'Secret' video and use that for your story if you don't want to share the video outside the Oculus environment.

1. Go to **Publishing Tools** / **Video Library**. Information about this process can be found in the Facebook [Publishing FAQ](https://www.facebook.com/help/1533298140275888?helpref=faq_content).
2. Select the video.
3. In the **Video Details** dialog box, click **Create Post With Video**.
4. Select the **Advanced** tab.
5. Change **Distribution** to **Custom**.
6. Select **Add as secret video**.
Then, once you've created the video, retrieve the URL.

1. Go to **Publishing Tools** / **Video Library**.
2. Select the video.
3. In the **Video Details** dialog box, select the post you just created (at the bottom).
4. Click **View Permalink**.
## Content Review

All posts and stories will reviewed by the Oculus team for content approval and compliance with the [Oculus Code of Conduct](https://support.oculus.com/1694069410806625/). If the submission does not comply, it will be rejected.

## Preview Your In-App Content

Want to see how your in-app content will look before releasing to the public? To test:

1. Create a post and save it as a draft.
2. Launch your mobile VR device. At the bottom of Home, select the gear icon to open the settings menu. In the settings menu select **Developer Settings**, and then choose **View Developer Feed**. You'll need to be a Developer or Admin in your organization to see this menu.
3. Select the **Home** tab, and preview your in-app content in **Home**.
4. Select the link to launch your app and test the deeplink.
5. When you're satisfied with the announcement and deeplink, you can submit the announcement for review and public release.
