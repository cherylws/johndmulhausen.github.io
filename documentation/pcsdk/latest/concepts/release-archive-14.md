---
title: Changes For Release 1.4.x
---
This section describes changes to the Oculus SDK, the Oculus App, Oculus Home, and the runtime.

## Overview of Release 1.4.0

The 1.4.0 release focuses on performance improvements and minor bug fixes. 

## New Features for 1.4.0

* The SDK now supports protected content, which is designed to prevent any mirroring of the compositor. For more information, see [Protecting Content](/documentation/pcsdk/latest/concepts/dg-render-advanced/#dg-render-advanced-protected-content "There are some cases where you only want the content to display on the headset. The protected content feature is designed to prevent any mirroring of the compositor.").
* The Touch controller pairing process has improved. For more information, see [Pairing the Oculus Touch Controllers](/documentation/pcsdk/latest/concepts/pairing-touch-controllers/ "After you receive your Touch Controllers, you need to pair them with the headset.").
## API Changes for 1.4.0

There are no breaking changes to version 1.4.0.

## Known Issues

The following are known issues:

* Version 16.5.2 of the AMD driver can cause flickering on your computer screen. If you encounter this issue, use the 16.5.1 driver.
* There are some USB chipsets that do not meet the USB 3.0 specification and are incompatible with the Oculus Rift sensor. If you receive a notification in Oculus Home or the Oculus App, plug the sensor into a different USB 3.0 port (blue). If none of the USB 3.0 ports work, plug the sensor into a USB 2.0 port (black). 
* Antivirus software, such a McAfee, can cause installation issues. To work around the issue, make sure you have the latest updates and disable real-time scanning.
* If you encounter installation issues, delete the Oculus folder and install the software again.
* If the Rift displays a message that instructs you to take off the headset, remove it and place it on a flat surface for 10-15 seconds.
* The keyboard and mouse do not work in Oculus Home. To select an item, gaze at it and select it using the Oculus Remote or Xbox controller.
* Bandwidth-intensive USB devices, such as web cams and high-end audio interfaces, might not work when using the Rift. To work around this issue, install the device on another USB host controller or a separate computer.
* For dual-boot systems using DK2 or CB1 HMDs, the OS selection screen might appear on the HMD instead of the monitor. To work around this, try plugging the HMD into a different port or unplug the HMD while booting.
* If you are running your application from the Unity Editor and you press the controller's home button to return to Oculus Home, you will be prompted to close the application. If you select OK, Unity might remain in a state where it is running, but will never get focus. To work around this, restart Unity.
## Migrating from SDK 1.3.x to SDK 1.4.0

There are no breaking SDK changes or migration requirements other than installing the new SDK.

