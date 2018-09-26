---
title: 1.0.x Release Notes
---



## 1.0.3.7 Release Notes

New Features

* Added new getting started tutorial support.


## 1.0.3.6 Release Notes

Bug Fixes

* Removed VrApi interface threading restrictions when using explicit EGL objects.
* Prevent the wrong JNIEnv from being used on vrapi\_leaveVrMode when calling VrApi interface methods from different threads.


## 1.0.3.5 Release Notes

Bug Fixes

* Fixed latency and tearing issues.
* VrApiâ€™s framebuffer capture now only streams buffered layers to prevent Oculus Remote Monitor from streaming a single cursor layer.
* Modified Developer Mode to not set VRAPI\_TRACKING\_STATUS\_HMD\_CONNECTED when device is undocked with phone sensors enabled, allowing code which checks this flag to execute while undocked to run properly in Developer Mode.


## 1.0.3.4 Release Notes

New Features

* Phones in [Developer Mode](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-troublesh-device-run-app-outside/) now implement limited orientation tracking using phone sensors. This may be disabled with a setting to Local Preferences or System Properties. For more information, see [Local Preferences and Android System Properties](/documentation/mobilesdk/latest/concepts/mobile-localprefs/ "Use Android System Properties to set various device configuration options for testing and debugging.").
* Volume indicator now turns red at volume 11 when headphones detected.
* Redesigned icons for volume, Bluetooth, Wi-Fi, airplane mode, notifications, brightness, reorient, and battery.
* Moved Pass-Through Camera from Settings to Utilities in Universal Menu. 
* Reorient function now opens Pass-Through Camera and displays instructional text.
* Polished UI elements for friend request, status bar.
* Changed brightness/volume UI to a slider bar.


## 1.0.3.3 Release Notes

New Features

* The Universal Menu (UM) may now be realigned to any direction except straight down. To realign, look away from the UM and tap the touchpad when the message "Tap to reorient menu" appears.
* Added SMS text preview. To view message contents, hover over the notification and click "View."
* Game invites from friends may now be accepted from the UM notifications page. When an invite is received through a supported app, a gamepad icon will appear in the upper left corner. The user may enter the UM to see details and choose to join or clear. If ignored, game invites expire in ten minutes.
* Gamepad B button now acts as Back button.
* A notification count badge now appears over the Notifications button when new notifications are received.
* Long text is now auto-scaled or clipped to fit in UI elements.
* SMS now displays senderâ€™s phone number.
* Volume and brightness indicators can now be changed by gazing over them and swiping forward or backwards.
* Added UI for inviting users to games to System Activities and UM. This interface will be exposed to developers in a future release of the Oculus Platform SDK library.


Bug Fixes

* Fixed duplicate sounds when hovering over items.
* Fixed misaligned time when using the 24-hour time format.
* Fixed a text aliasing bug.
* Fixed a crash when receiving SMS messages.
* Improved text wrapping in Chinese, Japanese, and Korean.
* Added missing Korean translation for "incoming calls".
* All fonts now support the Unicode replacement character. This character looks like a diamond with a question mark in it and is rendered when a character is requested but not found in the font.
* Brightness level indicator no longer changes when re-entering the UM.
* Issues related to Android OS sending phantom MENU key events on a back press were fixed.


## 1.0.3.2 Release Notes

New Features

* Userâ€™s real name now displayed on profile page.


Bug Fixes

* Fixed minor word-wrapping bug.
* Fixed subtle overlay layer jittering associated with large, odd-sized textures.


## 1.0.3.1 Release Notes

New Features

* Android N compatibility update in VrApi Loader to work with library namespacing.


Bug Fixes

* Updated stb library to fix jpeg loading bugs.
* Font rendering improvements.
* Fixed automatic word wrapping for Chinese text.
* Fixed incorrect word wrapping in Japanese.


## 1.0.3.0 Release Notes

New Features

* Added Universal Menu support for Profile, Friends, Notifications, and Game Invites (app must support this feature).
* No longer require an OpenGL context to be bound during vrapi\_EnterVrMode.
* Added ability to change clock levels from a background thread.
* Defer deleting texture swapchains.
* A fatal error is now triggered if vrapi\_Shutdown is called before vrapi\_LeaveVrMode.
* Made improvements to Oculus Remote Monitor - see OVRMonitor release notes for details.
* Local Preferences are now also mapped to Android system properties.


Bug Fixes

* Return NULL from vrapi\_EnterVrMode when eglCreateWindowSurface fails.
* Fix for vsync handling taking an extremely large amount of CPU time on S7+Snapdragon devices running certain OS versions.


## 1.0.2.5 Release Notes

New Features

* Enabled distortion mesh clipping by default: WARP\_MESH\_CLIP\_MODE\_SQUARE.
* Updated V-sync timing and events.
* Added support for different rendering completion fences.


## 1.0.2.3 Release Notes

Bug Fixes

* Added workaround to determine the external SDCard path if Gear VR Service version is lower than 2.4.18.


## 1.0.2.2 Release Notes

New Features

* Enabled video capture and screenshot buttons in the Utilities submenu of Universal Menu. See [Screenshot and Video Capture](/documentation/mobilesdk/latest/concepts/mobile-testing-capture/ "Full-resolution, undistorted, single-eye, full-layer-support 2D screenshots and video capture for VR apps are available through the sharing menu. Video capture is also available by configuring localprefs.") for details.
* Upgraded icon resolutions for all Universal Menu icons.


Bug Fixes

* Fix to maintain consistent text size for Passthrough Camera Off button.


## 1.0.2.1 Release Notes

This release of System Activities adds new permission requirements for features in development. This update will prompt the user to accept camera and network access.

New Features

* Added two additional weights to EFIGS font.
* Improved text word wrap integration in VRMenuObject.


Bug Fixes

* Fixed update for buttons in Universal Menu.
* Fixed VRMenuObjects to prevent freeing textures that were allocated via the texture manager.
* Fixed Universal Menu performance regression.
* Fixed out-of-range font weight making text invisible.


## 1.0.2.0 Release Notes

New Features

* Redesigned Universal Menu.
* Video Capture (Alpha) video files are now written into the app’s cache directory. If permissions permit, the video file is now moved into /sdcard with the app’s package name appended for easy sorting in the directory /sdcard/Oculus/VideoShots/.


Bug Fixes

* Fixed Unity support with Video Capture (Alpha). 
* getApplicationName no longer uses the string table to lookup application name, in the case it is not in the string table.


## 1.0.1.4 Release Notes

Bug Fixes

* Fixed HMD Device Creation Failure.
* Implemented workaround for Android abandoning the buffer queue when using a NativeActivity.


## 1.0.1.4 Release Notes

Bug Fixes

* Fixed HMD Device Creation Failure.
* Implemented workaround for Android abandoning the buffer queue when using a NativeActivity.


## 1.0.1.3 Release Notes

New Features

* Added logging for the vrapi version requested by the app, making it easier to determine which SDK a given application was built against.
* Added warning if loading the default distortion file fails.
* Modified getdevice and getgputype checks to run after vr permissions check.
* Distortion file is now loaded directly from VRSVC without requiring a temp file in /sdcard/Oculus/, eliminating need for READ\_EXTERNAL\_STORAGE Android permission (requires Mobile SDK 1.0 or later).
* "Do Not Disturb" mode in the Universal Menu only checks for change state when toggled.


Bug Fixes

* Fixed button rendering issue in Universal Menu.


Known Issues

* On a clean boot of the target device, distortion correction is missing when running a VR app outside of the headset with Developer Mode enabled. Target device must be docked to a Gear VR headset at least once after every clean boot up of the target device in order to cache the distortion file. 


## 1.0.1.2 Release Notes

Bug Fixes

* Fixed the front buffer extension on Adreno Lollipop Note 4 when the EGLSurface for the front buffer is not created by TimeWarp.


## 1.0.1.1 Release Notes

Bug Fixes

* Ensured that initial swapbuffer is called for Oculus Home.

