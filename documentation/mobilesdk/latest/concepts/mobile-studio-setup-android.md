---
title: Android Development Software Setup
---
This guide describes how to install the Android Studio Development Bundle that you'll use to build mobile VR apps.

The Android Studio Development Bundle includes all the necessary tools you need to begin developing Android Applications:

* Android Studio IDE (recommended IDE)
* Android Platforms
* Android SDK tools
* Android NDK
* Open JDK
## Getting Started

If you're planning to use a Mac for development, first install Xcode - <https://developer.apple.com/xcode/download/>. If you're using another platform you may skip this installation.

To get started, download Android Studio - <https://developer.android.com/studio/index.html>. Please refer to the Install Android Studio (<https://developer.android.com/studio/install.html?pkg=studio>) guide for detailed installation steps.

## Install Additional Packages and Tools

Once Android Studio has been installed, you can then install the following packages:

* Android SDK Platform, API level 21
* Android SDK Build Tools, v 27.0.3
* Android NDK
* LLDB
* Open JDK
These packages are installed through the **Android SDK Manager**. To access the manager, either navigate to **Tools > Android > SDK Manager** or click the SDK Manager icon in the toolbar (

![](/images/documentation-mobilesdk-latest-concepts-mobile-studio-setup-android-0.png)  
). If you do not have a project loaded you may navigate to **Configure > SDK Manager**.**Verify that the correct packages and versions have been installed**

In the **Android SDK Manager**, select the **SDK Platforms** tab. Verify the following Android platform is installed, as it is the minimum version required by the SDK: **Android 5.0 (Lollipop)**.

Then select the **SDK Tools** tab. Verify that the following components are installed: **NDK** and **LLDB**, and that the following tool versions are installed: **Android SDK Build Tools 27.0.3**.

Note: A copy of the latest OpenJDK comes bundled with Android Studio. No additional installation is necessary.Please refer to the following pages for information about **Android NDK** (<https://developer.android.com/studio/projects/add-native-code.html#download-ndk>) and **OpenJDK** (<https://developer.android.com/studio/intro/studio-config.html#jdk>).

## Configure Android Studio

Once you've finished installing the required packages, you can configure your development environment.

**Android Studio Project Structure**

To verify your settings in Android Studio, navigate to **File > Project Structure > SDK Location**. If you do not have a project loaded, navigate to **Configure > Project Defaults > Project Structure > SDK Location**.

Verify that *Use embedded JDK* is checked and that the following properties are set to appropriate values:

* Android SDK location
* JDK location
* Android NDK location
Make note of these locations, you'll use them to set your environmental variables in the next section.

**Environment Variables and Path**

With the locations recorded in the previous step, set the following environment variables:

* Set the environment variable **JAVA\_HOME** to the JDK location, typically C:\Program Files\Android\Android Studio\jre.
* Set the environment variable **ANDROID\_HOME** to the Android SDK location, typically C:\Users\[username]\AppData\Local\Android\Sdk.
* Set the environment variable **ANDROID\_NDK\_HOME** to the Android NDK location, typically C:\Users\[username]\AppData\Local\Android\Sdk\ndk-bundle.
* Add the JDK tools directory to your **PATH**, typically C:\Program Files\Android\Android Studio\jre\bin.
* Add the Android SDK platform-tools directory to your **PATH**, typically C:\Users\[username]\AppData\Local\Android\Sdk\platform-tools.
* Add the Android SDK tools directory to your **PATH**, typically C:\Users\[username]\AppData\Local\Android\Sdk\tools.
## Setting up your System to Detect your Android Device (Windows Only)

You must set up your system to detect your Android device over USB in order to run, debug, and test your application on an Android device.

If you are developing on Windows, you may need to install a USB driver for adb after installing the Android SDK. For an installation guide and links to OEM drivers, see the Android [OEM USB Drivers](https://developer.android.com/tools/extras/oem-usb.html) document.

Samsung Android drivers may be found on their developer site: <http://developer.samsung.com/android/tools-sdks/Samsung-Android-USB-Driver-for-Windows>

Windows may automatically detect the correct device and install the appropriate driver when you connect your device to a USB port on your computer. 

Access the Device Manager through the Windows Control Panel. If the device was automatically detected, it will show up under *Portable Devices* in the Device Manager. Otherwise, look under *Other Devices* in the Device Manager and select the device to manually update the driver.

To verify that the driver successfully recognized the device, open a command prompt and type the command:adb devicesNote: You will need to successfully setup your Android development environment in order to use this command. For more information, see the next section: Android Development Environment SetupIf the device does not show up, verify that the device is turned on with enough battery power, and that the driver is installed properly.

