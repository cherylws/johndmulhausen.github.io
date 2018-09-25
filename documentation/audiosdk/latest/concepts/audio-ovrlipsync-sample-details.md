---
title: Using Oculus Lipsync
---
This guide describes how to use the Oculus Lipsync integration within your own projects. You may find it helpful to use the [demo scene](/documentation/audiosdk/latest/concepts/audio-ovrlipsync-sample/) or the included prefabs as references. We assume that you have already completed the [download and setup](/documentation/audiosdk/latest/concepts/audio-ovrlipsync-setup/) steps to add the Oculus Lipsync integration assets into your Unity project.

## Main Lipsync interface

To use Oculus Lipsync, a scene must include the **OVRLipSync** script, which is the main interface to the Oculus Lipsync plugin. We provide the **LipSyncInterface **prefab for convenience. It is located in ***Assets > Oculus > LipSync > Prefabs***. Add this to your scene to get started.

## Driving your own objects with Lipsync

**OVRLipSyncContext **must be added to each GameObject which has a morph or texture target that you want to control. This script provides a number of options:

* *Show Visemes * displays responses on an **OVRLipSyncDebugConsole**. (Add the **LipSyncDebugConsole **prefab for an easy way to include this.)


* *Audio Loopback* replays received audio as output.


* *Enable Keyboard/Touch Input* enables keyboard and touch control for these two options.


* There are other options as well.


All options have tool-tips with more information.

**OVRLipSyncContextMorphTarget **and **OVRLipSyncContextTextureFlip **are the scripts that bridge the viseme output from **OVRLipSyncContext**, as described in the following sections. 

#### Geometry morph targets

![](/images/documentation-audiosdk-latest-concepts-audio-ovrlipsync-sample-details-0.gif "Geometry morph target saying: Welcome to the Oculus Lipsync demo")  


**OVRLipSyncContextMorphTarget **requires a Skinned Mesh Renderer, which should have blend targets assigned to it (see the **Lips** object in the **LipSyncMorphTarget\_Lips **prefab for an example). The mesh should include all 15 visemes generated by the **OVRLipSyncContext **(expand *BlendShapes* in **Lips** Inspector view to access). For example: 

[![](/images/documentation-audiosdk-latest-concepts-audio-ovrlipsync-sample-details-1.png "Skinned Mesh Renderer with all 15 viseme blendshapes")  
](https://scontent.xx.fbcdn.net/v/t39.2365-6/37299566_192126621645482_3606753281361051648_n.png?_nc_cat=101&oh=254cbeef206f307aafac946797a756bd&oe=5C5C86BA)

 Each blend target from *sil* to *ou* represents a viseme generated by the viseme engine. You may view each one by setting the blend target for a single viseme to 100.0 Note that *sil *corresponds to the *silence*, i.e. the neutral expression, and setting it to 100 with all other values 0 will have no visible effect. We provide a [reference set of viseme images here](/documentation/audiosdk/latest/concepts/audio-ovrlipsync-viseme-reference/), based on those from the [Viseme MPEG-4 Standard](http://www.visagetechnologies.com/uploads/2012/08/MPEG-4FBAOverview.pdf). 

 Visemes only capture lip shapes, and thus if you want to add expression you may want to add additional shapes. Use caution when adding mouth expressions. For example, adding a laughter expression on top of viseme shapes may look uncanny. The **OVRLipSyncContextMorphTarget **script includes options under **Viseme To Blend Targets** to assign the 15 outputs from Oculus Lipsync to blend shapes other than the first 15 if you so wish:

[![](/images/documentation-audiosdk-latest-concepts-audio-ovrlipsync-sample-details-2.png "Setting non-default blendshape targets")  
](https://scontent.xx.fbcdn.net/v/t39.2365-6/37346043_246279179500498_5646779188372307968_n.png?_nc_cat=104&oh=8ee26c520845500cfc806353383e1a98&oe=5C56B089)

By selecting the* Enable Viseme Test Keys* option you can drive each viseme to 100% using the **QWERTY** row of a US-layout keyboard by default, or set the keys by expanding *Viseme Test Keys.*

#### Texture flip targets

![](/images/documentation-audiosdk-latest-concepts-audio-ovrlipsync-sample-details-3.gif "Texture flip target saying: Welcome to the Oculus lipsync demo")  


**OVRLipSyncContextTextureFlip **requires a material target and set of textures - one for each viseme - which will be selected based on output from the **OVRLipSyncContext**. These textures must be set within the *Textures* field, and must match the texture which you want to associate with a given viseme:

[![](/images/documentation-audiosdk-latest-concepts-audio-ovrlipsync-sample-details-4.png "Setting textures for the 15 visemes in the OVR Lip Sync Context Texture Flip")  
](https://scontent.xx.fbcdn.net/v/t39.2365-6/37353468_207968436548753_3102664063730057216_n.png?_nc_cat=102&oh=444fc69445825687883a99c881965d7c&oe=5C59C467)

The logic within the **OVRLipSyncContextTextureFlip **script only chooses one texture to use on a given frame, and assigns it to the main material texture, which should be assigned to the model which is used for drawing the avatar lips.

### Other Oculus Lipsync Scripts

**OVRLipSyncMicInput **is for use with a GameObject which has an AudioSource attached to it. It takes input from any attached microphone and pipes it through the AudioSource.

 We recommend looking at the other scripts and prefabs included with this integration. They will provide more insight as to what is possible with Oculus Lipsync. We include, for example, some helper scripts to facilitate easy on-screen (in VR) debugging. 

### Using Audio Spatialization with LipSync

You can use the [Oculus Native Spatializer for Unity](/documentation/audiosdk/latest/concepts/book-ospnative-unity/) to process sound sources so that the user experiences audio in a 3D environment, relative to the user's head orientation and location. This dramatically improves the userâ€™s experience of sound within immersive experiences. However, when speech is subjected to spatial processing, it effects the integrity of the spoken signal. The spatial processing essentially adds noise to the signal, which degrades the viseme output. In order to use audio spatialization in conjunction with LipSync, you must configure the the spatializer to post process the signal so that the raw input signal drives the viseme engine. 

By default, the Oculus Native Spatializer for Unity processes the AudioSource buffers before calling OnAudioFilterRead (which invokes the LipSync functionality, if it is enabled). To change the order, set the spatializePostEffects flag on the AudioSource to True. You can set this flag in the Unity script function OnAudioFilterRead. You can also set this flag via the Inspector window. The field will show up provided the Spatialize field is checked. For more information, see [AudioSource.spatializePostEffects](https://docs.unity3d.com/ScriptReference/AudioSource-spatializePostEffects.html). 
