---
title: Release Channels
---
Release channels let you distribute early versions of your builds to limited audiences for testing or other purposes. You can invite different groups of people to different channels. When you are confident your app is ready for release, you can copy your build to the Store channel and then submit it for Oculus Store review. 

## Overview of Release Channels

Oculus provides three default release channels: Alpha, Beta, and Release Candidate. There is also a special channel named "Store". The first time you upload a build for your app, it goes into the Alpha release channel. After this first build, you are free to select different channel destinations when you upload builds. 

Initially, the Alpha, Beta, and Release Candidate channels are empty and contain no users, not even yourself. But, by going to each channel and inviting Oculus users into them, you can allow different groups of people to access the builds that you upload or copy into each channel.

Apps distributed through release channels appear in the **My Preview Apps** section of Oculus Home.

Note: All uploaded apps, even alpha builds, must meet the release packaging requirements for your platform. Uploading an app to a release channel signifies that you are ready to release it to an audience even if that audience is a group of internal testers.## The Store Channel is Special

The Store channel does not have subscribers. When you place a build in this channel for the first time, nothing happens until enter all your Submission Info and click "Submit for Review".

After your app is approved for Oculus Store distribution, the build in your Store channel becomes the live build for all Oculus Home users. If your app was approved for the Oculus Store or the Oculus Gallery, users can now browse and find your app in the Store. If your app was approved for Oculus keys, users who have keys can download your app. 

Any new builds of an approved app that you copy to the Store channel triggers an update for all users who are entitled to download the release version of your app. See [Updating Published Apps](/distribute/latest/concepts/publish-content-updating/#publish-content-updating "You can upload new versions of your app and update its product details at any time after your app is published to the Oculus Store.").

* **[Viewing Release Channels](/distribute/latest/tasks/publish-release-channels-view/)**  
You can view the state of your release channels at any time.
* **[Uploading Builds to a Release Channel](/distribute/latest/tasks/publish-release-channels-upload/)**  
You can upload new builds to any release channel. New builds must have a higher version number than the last uploaded build.
* **[Inviting Users to a Release Channel](/distribute/latest/tasks/publish-release-channels-add-users/)**  
You can invite up to 100 Oculus users to release channels by email invitation. In the case where users are subscribed to more than one release channel, they get access to the build with the highest version number.
* **[Copying Builds Between Release Channels](/distribute/latest/tasks/publish-release-channels-migrate/)**  
After you are satisfied with the exposure and testing a build has received in a release channel, you can copy the build to another release channel to expose it to a new set of testers or users.
* **[Adding Custom Release Channels](/distribute/latest/tasks/publish-release-channels-add-custom/)**  
You can create additional release channels if you need more.
