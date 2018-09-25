---
title: Adb
---
This guide describes how to perform common tasks using adb.

Android Debug Bridge (adb) is included in the Android SDK and is the main tool used to communicate with an Android device for debugging. We recommend familiarizing yourself with it by reading the official documentation located here: [http://developer.android.com/tools/help/adb.html](https://developer.android.com/tools/help/adb.html)

For a list of available commands and options, make a connection as described below and enter:

adb help## Connecting to a Device with adb

Using adb from the OS shell, it is possible to connect to and communicate with an Android device either directly through USB, or via TCP/IP over a Wi-Fi connection. You must install the Android SDK and appropriate device drivers to use adb (see [Device Setup - Gear VR](/documentation/mobilesdk/latest/concepts/mobile-device-setup/ "This section will provide information on how to set up your supported Gear VR device for running, debugging, and testing your mobile application.") for Gear VR and [Device Setup - Oculus Go](/documentation/mobilesdk/latest/concepts/mobile-device-setup-go/ "This section will provide information on how to set up your Oculus Go device for running, debugging, and testing your application.") for Oculus Go).

To connect a device via USB, plug the device into the PC with a compatible USB cable. After connecting, open up an OS shell and type:

adb devicesIf the device is connected properly, adb will show the device id list such as:

List of devices attached ce0551e7 deviceAdb may not be used if no device is detected. If your device is not listed, the most likely problem is that you do not have the correct USB driver (see [Device Setup - Gear VR](/documentation/mobilesdk/latest/concepts/mobile-device-setup/ "This section will provide information on how to set up your supported Gear VR device for running, debugging, and testing your mobile application.") or [Device Setup - Oculus Go](/documentation/mobilesdk/latest/concepts/mobile-device-setup-go/ "This section will provide information on how to set up your Oculus Go device for running, debugging, and testing your application.") for more information). You may also wish to try another USB cable and/or port.

## Connecting adb via Wi-Fi

Connecting to a device via USB is generally faster than using a TCP/IP connection, but a TCP/IP connection is sometimes indispensable, especially when debugging behavior that only occurs when the phone is placed in the Gear VR, in which case the USB connection is occupied by the Gear VR jack.

To connect via TCP/IP, first determine the IP address of the device and make sure the device is already connected via USB. You can find the IP address of the device under Settings -> About device -> Status. Then issue the following commands:

adb tcpip <port> adb connect <ipaddress>:<port>For example:

> adb tcpip 5555 restarting in TCP mode port: 5555 > adb connect 10.0.32.101:5555 connected to 10.0.32.101:5555The device may now be disconnected from the USB port. As long as adb devices shows only a single device, all adb commands will be issued for the device via Wi-Fi.

To stop using the Wi-Fi connection, issue the following adb command from the OS shell:

adb disconnect## Using adb to Install Applications

To install an APK on your mobile device using adb, connect to the target device and verify connection using adb devices as described above. Then install the APK with the following command:

adb install <apk-path>Use the -r option to overwrite an existing APK of the same name already installed on the target device. For example:

adb install -r C:\Dev\Android\MyProject\VrApp.apkFor more information, see the [Installing an Application](https://developer.android.com/studio/command-line/adb.html#move) section of Android's *Android Debug Bridge* guide. 

## Connection Troubleshooting

Note that depending on the particular device, detection may be finicky from time to time. In particular, on some devices, connecting while a VR app is running or when adb is waiting for a device, may prevent the device from being reliably detected. In those cases, try ending the app and stop adb using Ctrl-C before reconnecting the device. Alternatively the adb service can be stopped using the following command after which the adb service will be automatically restarted when executing the next command:

adb kill-serverMultiple devices may be attached at once, and this is often valuable for debugging client/server applications. Also, when connected via Wi-Fi and also plugged in via USB, adb will show a single device as two devices. In the multiple device case adb must be told which device to work with using the -s switch. For example, with two devices connected, the adb devices command might show:

List of devices attached ce0551e7 device 10.0.32.101:5555 deviceThe listed devices may be two separate devices, or one device that is connected both via Wi-Fi and plugged into USB (perhaps to charge the battery). In this case, all adb commands must take the form:

adb -s <device id> <command>where <device id> is the id reported by adb devices. So, for example, to issue a logcat command to the device connected via TCP/IP:

adb -s 10.0.32.101:55555 logcat -cand to issue the same command to the device connected via USB:

adb -s ce0551e7