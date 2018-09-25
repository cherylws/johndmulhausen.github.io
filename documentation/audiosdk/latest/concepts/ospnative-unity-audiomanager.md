---
title: Managing Sound FX with Oculus Audio Manager
---
The Oculus Audio Manager provides sound fx management that is external to Unity scene files. This has audio workflow benefits as well as providing you with the ability to group sound FX events together for greater flexibility. 

The Oculus Audio Manager provides greater control over your audio compared to using AudioSource components:

* You can group sound FX together for volume control and other collective sound parameters and functions. 
* You can trigger sound events by an external reference instead of a Unity scene object. The advantage of this is that as an audio designer, you can develop and iterate upon a sound event without interruption while other developers are actively working on the scene. You do not have to merge and resolve your changes with those of other developers because your changes are external to the scene.
* When firing a sound event, you have more variety in control options, for example, different volume curves that behave differently from the ones available in the stock AudioSource component. 
The basic premise is that you create sound effect groups as collections of sound effects that share common parameters. Each sound effect you define is then a sound event that you can play back using the class SoundFXRef.

To create sound effects groups and events:

1. Add the script **AudioManager.cs** to a static game object.
2. In the **Inspector** window, click **+** under **Sound FX Groups** to add a new sound effects group. ![](/images/documentation-audiosdk-latest-concepts-ospnative-unity-audiomanager-0.png)  

3. Double-click the sound FX group's name to rename the group.
4. Select the sound FX group â€“ the **Properties** and **Sound Effects** options for that group appears.
5. Expand **Sound Effects** and then click **Add FX**. ![](/images/documentation-audiosdk-latest-concepts-ospnative-unity-audiomanager-1.png)  

6. Expand the new sound FX and provide a name in the **Name** field.
7. Expand **Sound Clips** and then use the **Size** and **Element** controls to select the audio files.
## Exploring the Audio Manager Sample Scene

Run the **Test** scene located in **Assets/OVRAudioManager/Scenes** to try out basic audio manager functionality. Browsing through the OVRAudioManager scene object should give you a basic understanding of the Audio Manager data architecture. 

Press **1** and **2** on your keyboard to trigger different sound events. Take a look at the example scene script TestScript.cs to see how we use public SoundFXRef *soundName* and *soundName*.PlaySoundAt(*position*) to trigger the sound events. 

