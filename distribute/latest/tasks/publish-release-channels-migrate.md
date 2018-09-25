---
title: Copying Builds Between Release Channels
---
After you are satisfied with the exposure and testing a build has received in a release channel, you can copy the build to another release channel to expose it to a new set of testers or users.

Only build versions with higher version numbers can be copied over lower version builds. So, if there is already a build inside a release channel, you cannot replace that channelâ€™s build with an older version. The build version numbers are indicated on the Build Dashboard.

To copy a build to another release channel:

1. Log on to <https://dashboard.oculus.com/>.
2. On the My Apps page, hover the mouse over the app and then click Manage Build. 
3. Click ... in the Action column of the channel that contains the build.
4. Select Copy to Another Channel.
5. Select the destination channel and then click Copy.

The build is copied to the new channel and is made available to all subscribed users as an update.


Note: Consider maintaining a known-stable version of your app so that you can quickly upload it and release the update to your users if you find a serious problem with the currently-published version.