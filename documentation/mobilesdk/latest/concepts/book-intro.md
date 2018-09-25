---
title: Mobile SDK Getting Started Guide
---
The Oculus Mobile SDK includes libraries, tools, and resources for native development for Oculus Go and Gear VR. 

## SDK Contents

* VrApi for third-party engine integration (not required for Unity or Unreal). 
* Native application framework for building high-performance VR Applications from scratch. 
* Additional libraries providing support for GUI, locale, and other functionality. 
* Native project sample applications and source to provide reference model for creating your own VR applications.
* Tools and resources to assist with native development.
## Mobile SDK Intro Documentation

* Getting Started Guide: A one-time guide to environment setup.
* Mobile Development Basics: Information every developer should know about Oculus mobile development. Every developer should read through this guide.
## Native Developers

Most of the Mobile SDK guide is written for native developers. Complete the setup described in the Getting Started Guide, then move on to the [Native Development Overview](/documentation/mobilesdk/latest/concepts/book-native/ "Welcome to the Native Development Guide. This guide describes the libraries, tools, samples, and other material provided with this SDK for native development of mobile VR applications.").

## Unity and Unreal Developers

Mobile developers working with Unity and Unreal should begin with [Mobile Development with Unity and Unreal](/documentation/mobilesdk/latest/concepts/mobile-game-engine/#mobile-game-engine), as setup and development differ substantially from native setup and development. 

## Developing for Oculus Go and Gear VR

For the most part, developing apps for Oculus Go and Gear VR is the same. However, you should be aware of some key differences between building for the two platforms, especially if you've previously built an app for Gear VR.

Oculus Go has the following restrictions:

* **No Google Play Services. **Unlike the Samsung Galaxy devices that run Gear VR, Oculus Go does not ship with Google Play Services installed. You cannot rely on Google Play Services (e.g. Google Firebase, Google Cloud Messaging, etc) when running on Oculus Go.
* **No 2D Surface. **Oculus Go does not have a 2D phone display, and therefore some app behaviors (such as push notifications, or authentication via a separate Android application) do not make sense on Oculus Go.
* **No Camera.** Oculus Go does not have a camera, and cannot run applications that rely upon access to a camera.
* **No HMD Touchpad. **Oculus Go does not have a touchpad on the HMD. Your app should not refer to an HMD touchpad when running on Oculus Go.
* **Different Controller.** The Oculus Go Controller and Gear VR Controller share the same inputs: both are 3DOF controllers with clickable trackpads and an index finger trigger. Though these two devices provide the same inputs, the physical design of each is distinct. If your app displays a visible controller, you should change the model displayed depending on whether you are running on Gear VR or Oculus Go. Alternatively, a stylized controller model that is distinct from both the Oculus Go Controller and the Gear VR Controller is acceptable.
## Platform Features

Mobile applications may use our Platform SDK (available separately from our [Downloads](/downloads/) page) to add features related to security (e.g., entitlements), community (e.g., rooms, matchmaking), revenue (e.g., in-app purchases), and engagement (e.g., leaderboards). For more information, see our [Platform SDK documentation](/documentation/platform/latest/). 

## Application Submission

For information on preparing to submit your mobile VR application to Oculus for distribution through the Oculus Store, see our [Publishing Guide](/distribute/latest/).

Thank you for joining us at the forefront of virtual reality!

To become acquainted with Gear VR, we recommend starting with the [Gear VR Documentation](https://product-guides.oculus.com/en-us/documentation/gear-vr/latest/), which covers topics including:

* Device Features and Functionality
* Connecting the Headset
* Navigation and App Selection
## Questions?

Visit our developer support forums at <https://forums.oculusvr.com/developer/discussions>.

Our Support Center can be accessed at <https://support.oculus.com/>.

* **[Mobile Development with Unity and Unreal](/documentation/mobilesdk/latest/concepts/mobile-game-engine/#mobile-game-engine)**  

* **[System and Hardware Requirements](/documentation/mobilesdk/latest/concepts/mobile-reqs/#mobile-reqs)**  
Please begin by making sure that you are using supported hardware and devices for this release of the Oculus Mobile SDK.
* **[Device Setup - Gear VR](/documentation/mobilesdk/latest/concepts/mobile-device-setup/)**  
This section will provide information on how to set up your supported Gear VR device for running, debugging, and testing your mobile application.
* **[Device Setup - Oculus Go](/documentation/mobilesdk/latest/concepts/mobile-device-setup-go/)**  
This section will provide information on how to set up your Oculus Go device for running, debugging, and testing your application.
* **[Android Development Software Setup](/documentation/mobilesdk/latest/concepts/mobile-studio-setup-android/)**  
This guide describes how to install the Android Studio Development Bundle that you'll use to build mobile VR apps.
