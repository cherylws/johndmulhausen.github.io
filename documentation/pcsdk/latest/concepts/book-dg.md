---
title: PC SDK Developer Guide
---

Welcome to the PC SDK Developer Guide.

This guide describes how to use the PC SDK and covers the following topics:

* Sensor initialization
* Rendering and advanced rendering
* VR focus management
* Spatialized audio
* Oculus Touch


Additionally, it contains information on the SDK samples, the Oculus Debug Tool, and the Performance HUD.

* **[LibOVR Integration](/documentation/pcsdk/latest/concepts/dg-libovr/#dg_libovr)**  
The Oculus SDK is designed to be as easy to integrate as possible. This guide outlines a basic Oculus integration with a C/C++ game engine or application.
* **[Initialization and Sensor Enumeration](/documentation/pcsdk/latest/concepts/dg-sensor/#dg_sensor)**  
This example initializes LibOVR and requests information about the available HMD.
* **[Rendering to the Oculus Rift](/documentation/pcsdk/latest/concepts/dg-render/#dg_render)**  
The Oculus Rift requires split-screen stereo with distortion correction for each eye to cancel lens-related distortion.
* **[Advanced Rendering Configuration](/documentation/pcsdk/latest/concepts/dg-render-advanced/#dg_render_advanced)**  
By default, the SDK generates configuration values that optimize for rendering quality. 
* **[Oculus Dash](/documentation/pcsdk/latest/concepts/dg-dash/)**  
This section introduces Oculus Dash for the PC-SDK.
* **[VR Focus Management](/documentation/pcsdk/latest/concepts/dg-vr-focus/)**  
 When you submit your application to Oculus, you provide the application and metadata necessary to list it in the Oculus Store and launch it from Oculus Home. 
* **[Oculus Guardian System](/documentation/pcsdk/latest/concepts/dg-guardian-system/)**  
The Oculus Guardian System is designed to display in-application wall and floor markers when users get near boundaries they defined. When the user gets too close to the edge of a boundary, translucent boundary markers are displayed in a layer that is superimposed over the game or experience. 
* **[Rift Audio](/documentation/pcsdk/latest/concepts/dg-vr-audio/)**  
When setting up audio for the Rift, you need to determine whether the Rift headphones are active and pause the audio when your app doesnâ€™t have focus.
* **[Oculus Touch Controllers](/documentation/pcsdk/latest/concepts/dg-input-touch-overview/)**  
This section describes Oculus Touch best practices gathered from developing and reviewing large numbers of games and experiences. These are not requirements and we expect them to evolve over time. 
* **[SDK Samples and Gamepad Usage](/documentation/pcsdk/latest/concepts/dg-sdk-samples/)**  
Some of the Oculus SDK samples use gamepad controllers to enable movement around the virtual world.
* **[Oculus Debug Tool](/documentation/pcsdk/latest/concepts/dg-debug-tool/)**  
The Oculus Debug Tool (IDT) enables you to view performance or debugging information within your game or experience. It also enables you to tune or configure related parameters, such as the field of view (FOV) size for a mirrored flat-screen view of the VR experience (which could be streamed to an audience in a more comfortable viewing format).
* **[Optimizing Your Application](/documentation/pcsdk/latest/concepts/dg-performance/)**  
To provide the best user experience, your application must meet or exceed the minimum requirements to be considered for publication on the Oculus Store. 
* **[Pairing the Oculus Touch Controllers](/documentation/pcsdk/latest/concepts/pairing-touch-controllers/)**  
After you receive your Touch Controllers, you need to pair them with the headset.
* **[Asynchronous SpaceWarp](/documentation/pcsdk/latest/concepts/asynchronous-spacewarp/)**  
Asynchronous Spacewarp (ASW) is a frame-rate smoothing technique that almost halves the CPU/GPU time required to produce nearly the same output from the same content.
* **[Mixed Reality Capture](/documentation/pcsdk/latest/concepts/dg-mrc/)**  
Mixed reality capture places real-world people and objects in VR. This guide will review how to add support for mixed reality capture in your native Rift app. 
* **[VRC Validator](/documentation/pcsdk/latest/concepts/dg-vrcvalidator/)**  
The Virtual Reality Check (VRC) Validator utility runs automated tests to determine if your Rift app is ready for Oculus Store technical review. The VRC Validator can reveal shortcomings that need to be addressed before your app can pass the Oculus Store review process. The VRC Validator has a command line interface as well as a GUI interface. 

