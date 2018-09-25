---
title: Updating Published Apps
---
You can upload new versions of your app and update its product details at any time after your app is published to the Oculus Store.

## Upload Updates to the Store Channel

When you upload a new build of a published app to the Store channel, the update gets processed immediately. If it passes the upload validator, it is automatically deployed to all users as an update. It is our general policy not to perform technical or content review for updates. However, if you have concerns about a major update and would like us to conduct another technical review, email us at submissions@oculus.com.

## Special Gear VR Update Requirements

The upload validator rejects Gear VR updates that do not match the following specifications:

* versionCode manifest attribute must be higher than the current Store channel build.
* minSdkVersion version manifest attribute must be the same or higher than the current Store channel build.
* package manifest attribute must be the same as the current Store channel build. 
* Android cryptographic signature must be the same as the current Store channel build.
To upload a new version of your app:

* Copy or upload a new build to the Store release channel. 
If it turns out that you broke something in your new version, replace the broken version by uploading the last-known-good version of your app as if it were a new version.

## Updating Product Details

As you release new versions and updates to your app, you might want to update its screenshots, descriptions, and other product details. Such changes must pass our content review process before they are updated on the Oculus Store.

Note: If you update an app's Store channel build at the same time that you update product details, we apply the build update immediately but the product detail changes your build update still takes effect immediately. The content review applies only to the product detail changes. There are some product details that we do not let you update. We consider the category, comfort level, age rating, ratings board, and price to be fundamental properties of your app. Contact us at submissions@oculus.com if there are strong reasons for modifying those properties.

To make changes to your Oculus Store product details:

1. Log on to [https://dashboard.oculus.com](https://dashboard.oculus.com/).
2. On the My Apps page, hover the mouse over an approved app and then click View Details.
3. Click Update App Info.
4. Click the Submission Info tab.
5. Make your changes.
6. Click Submit on the left menu.
7. Click Submit For Review.
To schedule an Oculus Store content update for a specific date, email us at submissions@oculus.com.

