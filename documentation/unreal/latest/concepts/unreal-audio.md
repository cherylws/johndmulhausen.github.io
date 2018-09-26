---
title: Audio
---

Audio is critical for creating a persuasive VR experience and can contribute strongly to the user's sense of immersion.

## Audio Basics (Oculus Rift)

When Unreal PC applications are launched, if the OculusVR plugin is enabled and the Oculus VR Runtime Service is installed, then the application will automatically override the default Windows graphics and audio devices and target the Rift. The Oculus VR Runtime Service is installed with the Oculus app.

Unless your application is intended to run in VR, do not enable the OculusVR plugin. Otherwise, it is possible that audio and/or video will be incorrectly targeted to the Oculus Rift when the application is run.

Alternatively, users can disable loading all HMD plugins by specifying "-nohmd" on the command line.

## Audio Spatialization (Oculus Go, Oculus Rift, Gear VR)

The Oculus Audio SDK includes spatialization plugins (OSPs) that provide Head-related Transfer Function (HRTF) spatialization and reverb modeling for audio editing tools commonly used with Unreal, including Audiokinetic Wwise and FMOD Studio.

FMOD supports Oculus Go, Oculus Rift, and Gear VR development. Wwise supports Oculus Rift development. For more details on integrating our spatialization plugins with FMOD and Wwise for use in Unreal, see [Rift Audio](/documentation/pcsdk/latest/concepts/dg-vr-audio/) and [Introduction to Virtual Reality Audio](/documentation/audiosdk/latest/concepts/book-audio-intro/).

We recommend using FMOD or Wwise with the appropriate OSP, which will provide access to our full spatialization feature set as well as the full functionality of the audio tools themselves. Epic also offers built-in audio spatialization for Rift with HRTF-spatialization only. Epic offers support for Oculus Go and Gear VR which does not support some features such as ducking and filtering. For an example of how to implement it, see AmbientSound Spatialize in the Unreal [Audio Content Example](https://docs.unrealengine.com/latest/INT/Resources/ContentExamples/Audio/index.html).

For more information on our plugins, and for general information about audio design for VR, please see our [Audio SDK Developer Guide](/documentation/audiosdk/latest/). 
