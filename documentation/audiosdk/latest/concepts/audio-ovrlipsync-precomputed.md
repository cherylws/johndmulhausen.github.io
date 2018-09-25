---
title: Precomputing Visemes to Save CPU Processing
---
 You can save a lot of processing power by pre-computing the visemes for recorded audio instead of generating the visemes in real-time. This is particularly useful for lip synced animations on non-playable characters or in mobile apps as there is less processing power available. 

 We provide both a tool in Unity for generating pre-computed visemes for an audio source and a context called **OVRLipSyncContextCanned**. It works much the same as **OVRLipSyncContext **but reads the visemes from a pre-computed viseme asset file instead of generating them in real-time. 

## Precomputing viseme assets from an audio file

 You can generate viseme assets files for audio clips that meet these requirements: 

* **Preload Audio** check box is selected.
* **Compression Mode** is set to **Decompress on Load**.
Note: You do not have to ship the audio clips with these settings, but you do need to have them set up as such to generate viseme assets files.

[![](/images/documentation-audiosdk-latest-concepts-audio-ovrlipsync-precomputed-0.png "Audio clip settings to enable precomputing")  
](https://scontent.xx.fbcdn.net/v/t39.2365-6/37074096_206935720015511_1256283242659577856_n.png?_nc_cat=102&oh=d5fa226a7e08b9ada3232e31df18ff96&oe=5C299C6C)

To generate a viseme assets file:

1. Select one or more audio clips in the Unity project window.
2. Click **Tools > Oculus > Generate Lip Sync Assets**.
The viseme assets files are saved in the same folder as the audio clips, with the file name: ***audioClipName*\_lipSync.asset**. 

## Playing back precomputed visemes

[![](/images/documentation-audiosdk-latest-concepts-audio-ovrlipsync-precomputed-1.png "Settings for a canned playback geometry morph target")  
](https://scontent.xx.fbcdn.net/v/t39.2365-6/37357368_208149839846153_8973881247805734912_n.png?_nc_cat=108&oh=d397f395f73abf2734c749276e45aa82&oe=5C5EE5F0)

1. On your Unity object, pair an **OVRLipSyncContextCanned** script component with both an **Audio Source** component and either an **OVRLipSyncContextTextureFlip** or a **OVRLipSyncContextMorphTarget** script component setup as described in [Using Lip Sync Integration](/documentation/audiosdk/latest/concepts/audio-ovrlipsync-sample-details/).
2. Drag the viseme asset file to **OVRLipSyncContextCanned** component's **Current Sequence** field.
3. Play the source audio file on the attached **Audio Source** component.
