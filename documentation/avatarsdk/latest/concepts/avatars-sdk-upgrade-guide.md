---
title: Avatars Upgrade Guide
---

**Unity**

Upgrading from previous versions of Avatars is easy. Simply update your Unity engine to one of the [recommended Unity versions](/documentation/unity/latest/concepts/unity-req/) and rebuild your app. The Oculus integration will take care of the rest. 

Depending on the version of Unity from which you are updating, you may have to switch the UserID field to use a string value instead of an unsigned 64-bit int.

When upgrading from a previous version, your App ID might be cleared when importing the new package. Be sure to check this in the **Unity &gt; Oculus Avatars &gt; Edit Configuration** menu.

**Unreal**

Upgrading from the previous version of Avatars is easy. Simply update to Oculus Unreal build 1.26, or later, and rebuild your project. Avatars is currently only supported in C++ projects.

## What Happens If I Don’t Upgrade?

Not much. While we strongly encourage upgrading to the new Avatars service, existing Avatar implementations will continue to work as they do now.

If you choose to not update your Avatars integration, any user who has created an avatar using the old visual style will still have their preferred avatar returned.

Any users who had not created an avatar, or who had created an avatar only using the new visual style, will be represented using the old default avatar.
