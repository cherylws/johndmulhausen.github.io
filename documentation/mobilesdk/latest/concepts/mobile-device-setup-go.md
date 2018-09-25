---
title: Device Setup - Oculus Go
---
This section will provide information on how to set up your Oculus Go device for running, debugging, and testing your application.

To begin development locally for Oculus Go, you must enable Developer Mode in the companion app. Before you can put your device in Developer Mode, you need to have created (or belong to) a developer organization on the [Oculus Dashboard](https://dashboard.oculus.com/).

To join an existing organization:

1. You'll need to request access to the existing Organization from the admin.
2. You'll receive an email invite. Once accepted, you'll be a member of the Organization.
To create a new organization:

1. Go to: <https://dashboard.oculus.com/organization/create>
2. Fill in the appropriate information.
**Enable Developer Mode**

Then, to put your Oculus Go in developer mode:

1. Open the Oculus app on your mobile device.
2. In the Settings menu, select your Oculus Go headset that you're using for development.
3. Select **More Settings**.
4. Toggle **Developer Mode** on.
**Install the Oculus Go ADB Driver (Windows only)**

If you are going to be pushing builds from a Windows machine, you'll need the Oculus Go ADB Driver.

1. Download [the zip file containing the driver](/downloads/package/oculus-go-adb-drivers/).
2. Unzip the file.
3. Right-click on the .inf file and select **Install**.
Once complete, you'll be able to use Android Debug Bridge ([adb](/documentation/mobilesdk/latest/concepts/mobile-adb/#mobile-android-debug-intro)) to push builds to your Oculus Go. 

