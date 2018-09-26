---
title: Inviting Users to a Release Channel
---

You can invite up to 100 Oculus users to release channels by email invitation. In the case where users are subscribed to more than one release channel, they get access to the build with the highest version number.

To distribute your release channel builds to users, you must first invite them to the release channel. In the Oculus Store, the user will see the highest version published to any release channel they belong to (or published to the Store channel). You can add a user to multiple release channels.

Each Oculus user must accept your release channel invitation before we provision their Oculus Store Library with that channel’s build. This prevents users from getting signed up for apps they do not want.

Users subscribed to your release channel are granted an entitlement to download and run your build for as long as they remain subscribed to that channel. Removing a user from the channel disables their access to the build.

To add a user:

1. Log on to &lt;https://dashboard.oculus.com/&gt;.
2. On the **My Apps** page, hover the mouse over an app and then click **Manage Build**.
3. Click **+** in the **Subscribed Users** column of the channel.
4. Enter the email addresses of the Oculus users you want to invite to this channel. Enter up to 100 email addresses separated by commas.
5. Click **Add Users**.The system sends email invitations to each Oculus user you have invited.




**Subscribed Users** lists the users who have accepted your invitation.

**Pending Users** lists the users who have not yet accepted your invitation.

## Users With Multiple Release Channels Get the Highest Build Version

Users who are subscribed to more than one of your app's release channels get the version with the highest build version number available to them. For example, in the scenario below, a user with entitlements to all these channels would download build 67, as that is the highest build version.

* Alpha: build 55
* Beta: build 63
* Release Candidate: build 67
* Store: build 44

