---
title: Device Setup - Gear VR
---

This section will provide information on how to set up your supported Gear VR device for running, debugging, and testing your mobile application.

Please review the [System and Hardware Requirements](/documentation/mobilesdk/latest/concepts/mobile-reqs/#mobile-reqs) above for the list of supported devices for this SDK release.

## Configuring Your Device for Debugging

In order to test and debug applications on your Android device, you will need to enable specific developer options on the device:

1. Configure Developer Options in Settings * Enable USB Debugging * Allow mock locations * Verify apps via USB 


2. Configure Display Options in Settings * Disable lock screen * Set Display Timeout (optional) 




## Developer Options

Developer options may be found under: **Settings -&gt; System -&gt; Developer options**.

**Developer options** may be hidden by default. If so, you can expose these options with the following steps:

1. Locate *Build number* option in Settings. Android M and later: Go to *Settings -&gt; System -&gt; About device -&gt; Software Info*.

Earlier Android Versions: Go to *Settings -&gt; System -&gt; About device*.


2. Scroll down to *Build number*.
3. Press *Build number* seven times.


You should be informed that **Developer options** has been enabled.

Once you have found **Developer options**, enable the following:

**USB Debugging**: This will allow the tools to install and launch deployed apps over USB.

You should see the screen shown on the accompanying figure.

![](/images/documentationmobilesdklatestconceptsmobile-device-setup-0.png)

Check **Always allow this computer** and hit **OK**.

To purge the authorized whitelist for USB Debugging, press **Revoke USB debugging authorizations** from the **Developer options** menu and press **OK**.

**Allow mock locations**: This will allow you to send mock location information to the device (convenient for apps which use Location Based Services).

**Verify apps via USB**: This will check installed apps from ADB/ADT for harmful behavior.

## Display Options

The following display options are found in: **Home -&gt; Apps -&gt; Settings -&gt; Sound and Display**.

**Lock screen/Screen Security/Screen lock**: Set to **None** to make the Home screen is instantly available, without swipe or password. Useful to quickly get in and out of the phone.

**Display/Screen timeout**: Set the time to your desired duration. Useful if you are not actively accessing the device but wish to keep the screen awake longer than the default 30 seconds.

See [Android Debugging](/documentation/mobilesdk/latest/concepts/book-anddebug/) for more information.
