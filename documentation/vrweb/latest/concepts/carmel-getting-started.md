---
title: Getting Started
---

The basics of developing for Oculus Browser.

## User-agent string

The user-agent (UA) string for Oculus Browser is:

```
Mozilla/5.0 (Linux; Android 7.1.1; Pacific Build/N9F27L)
AppleWebKit/537.36 (KHTML, like Gecko)
OculusBrowser/4.0.0.17
SamsungBrowser/4.0
Chrome/61.0.3163.109
Mobile VR
Safari/537.36
```

The UA string should not be used for feature detection.

The UA string has a different token on different devices:

* **Oculus Go**: Pacific
* **Gear VR**: SAMSUNG SM-G920F for S6, for example.


## Display name and refresh rate for Oculus Go

The WebVR `VRDisplay.displayName` property for Oculus Go is `Oculus Go`.

On Oculus Go, Oculus Browser renders 2D web page content at 72Hz refresh rate by default, and WebVR content at 60Hz refresh rate by default.

## Debugging Your Experiences

Oculus Browser is based on [Chromium](https://www.chromium.org/). You can use Chrome's remote debugging feature to target your Oculus Go or Gear VR device. This lets you access all of your familiar tools including the console, timeline, profiler, DOM viewer, access to the address bar, and refresh features.

If you have not set up your device or have never connected your Oculus Go or Android phone to your development machine, see [Debugging Your Content](/documentation/vrweb/latest/concepts/carmel-remote-debugging/).

Alternatively, most experiences can be debugged before you ever launch the Oculus Browser. Here are some quick tips to debugging your experience locally before you enter VR:

* Know how to set up your camera to match that of your device. This means figuring out a common eye buffer size and field of view. We recommend using a 90 degree field of view and a buffer size of 1024 by 1024 (a single eye).
* You only need to render one eye, but have an adjustment so you can pick which eye to render. This can allow you to swap between the left and right eye and look for bugs. Alternatively render both eyes.
* Mouse and Device Orientation can be used to mimic head orientation so you can change your view dynamically as well.


## What's Next?

Now, with a WebVR capable device in hand, the easiest way to start developing is to start building on top of WebGL, or the WebGL framework of your choice. These experiences will run on most devices and will be very easy to enhance for use by the WebVR APIs.
