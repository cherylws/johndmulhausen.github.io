---
title: WebVR
---
Welcome to the WebVR Guide.

WebVR is a browser API used to interface with VR headsets. Working with WebVR directly requires knowledge of JavaScript and WebGL. Interfacing with a VR headset using WebVR is typically done in two phases:

* **Setup**. The application detects the headset, described by the VRDevice object, and targets it for presentation.
* **Per-Frame Rendering**. Once setup is complete, a requestAnimationFrame handler is used to query pose data, render the WebGL scene for each eye, and submit it to the headset. 
Though WebVR is an evolving API, a configuration of the API has crystallized that most major browser vendors believe can reach general availability in 2018.

Oculus Browser targets this configuration. All of our samples and documentation explain how to use this version of the API and also where we diverge from it and why.

