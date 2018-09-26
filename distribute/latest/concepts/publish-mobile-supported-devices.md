---
title: Managing Supported Devices
---

Your mobile app may not run on all devices supported Oculus. Select the devices your app will support. 

After you've uploaded a build to a release channel, you can update the build information to specify the devices that your app supports. For example, you may know that your app will not maintain framerate on the Samsung Galaxy S6, so you can remove support for that device. The app will then be hidden from users who are on excluded devices in the Oculus Store. 

Each upload defaults to supporting all devices.

## Manage Device Support

1. To select your devices, first navigate to the app on the [Oculus Dashboard](https://dashboard.oculus.com/). 
2. Hover over the app panel and select **Manage Build**.
3. Open the options menu for the channel that you want to update.
4. Click **View Channel Builds**.
5. Next, open the options menu for the build that you want to update. The most recent and active build will be listed on top. Select **View Build Details**.
6. Scroll down to the **Supported Devices** section and select **Edit**.
7. Check the box by all devices that your app supports and select **Save**.


Your app will now be only shown to users who are using the devices you've chosen to support.

You will also be prompted to manage this list when submitting your app to the store team for review. This list can also be accessed by selecting **Submit Your App** and then Edit or Fix the app **Specifications** in the app submission flow.

## Unsupported Devices

As described on the [Uploading Gear VR and Go Apps](/distribute/latest/concepts/publish-uploading-mobile/) page, APKs will be scanned to ensure they support the platforms that you've selected the app to run on. If they do not, you will be notified that updates are required.



![](/images/distributelatestconceptspublish-mobile-supported-devices-0.png)


