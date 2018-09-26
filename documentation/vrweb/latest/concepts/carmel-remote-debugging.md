---
title: Debugging Your Content
---

Oculus Browser is based on Chromium, so you can use the Chrome Developer Tools to debug and inspect your WebVR application. You can debug remotely either over USB or Wi-Fi.

## Enabling USB Debugging on Oculus Go

To configure your device for USB debugging:

1. Open the Oculus VR app on your phone.
2. Select your Pacific Go device in *Settings*.
3. Tap on **More Settings**
4. Tap on **Developer Mode**
5. Turn on **Developer Mode**


## Enabling USB debugging on Gear VR devices:

 To configure your device for USB debugging:

1. Open the **Settings** menu on your device.
2. Select **About device**.
3. Locate **Build Number**.
4. Tap **Build Number** seven times. The developer options notification appears.
5. Return to the top level of device settings, and then select **Developer Options**.
6. Turn on **USB Debugging**.


## Enabling Gear VR Developer Mode

Gear VR Developer mode speeds up your development workflow by letting you run VR applications without inserting your device into the Gear VR headset.

To enable Gear VR Developer mode:

1. Build an apk signed with your osig file and install it to your device. For more information, see &lt;https://dashboard.oculus.com/tools/osig-generator/&gt;.
2. Open the **Settings** menu on your device.
3. Select **Applications &gt; Application Manager**.
4. Select **Gear VR Service**.
5. Select **Manage Storage**.
6. Tap **VR Service Version** several times until the **Developer Mode** switch appears.
7. Turn on **Developer Mode**.


## Enabling Wi-Fi Debugging

If you want to debug while your device is plugged into the Gear VR headset, use Wi-Fi debugging. Wi-Fi is necessary because USB debugging does not work when your device is plugged into Gear VR.

To set up Wi-Fi debugging:

1. Complete the **Enabling USB Debugging** procedure and then connect your device to your computer with a USB cable.
2. Install Android Studio.
3. Open a terminal or Windows command prompt window.
4. Locate the adb tool if it is not already in your path. On Windows, it is typically located in C:\Users\*&lt;user&gt;*\AppData\Local\Android\sdk\platform-tools.
5. In the terminal window, enter adb tcpip 5555
6. Open the Settings menu on your device.
7. Select **About device &gt; Status** and obtain the IP address of your device.
8. In the terminal window, enter adb connect *x.x.x.x*:5555 where *x.x.x.x *is the IP address.


## Starting a Remote Debugging Session with Chrome Developer Tools

After you have your application loaded and running in Oculus Browser, you can debug it remotely using the Chrome Developer tools.

To start a remote debugging session:

1. Load and run your application in Oculus Browser.
2. Launch Chrome and then open the Chrome developer tools.
3. Select **More tools &gt; Remote devices** to open the Remote devices tab.

![](/images/documentationvrweblatestconceptscarmel-remote-debugging-0.png)


4. Select your device from the list on the left.
5. Click the **Inspect** button next to **com.oculus.carmel.player\_apk**.


 For more information about remote debugging with Chrome Developer Tools, see: [https://developers.google.com/web/tools/chrome-devtools/remote-debugging/](https://developers.google.com/web/tools/chrome-devtools/remote-debugging/)
