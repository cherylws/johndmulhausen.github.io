---
title: Native SoundEffectContext
---

Use SoundEffectContext to easily play sound effects and replace sound assets without recompilation.

SoundEffectContext consists of a simple sound asset management class, SoundAssetMapping, and sound pool class, SoundPool.

```
"sv_touch_active" : "sv_touch_active.wav"
```

```
soundEffectContext-&gt;Play( "sv_touch_active" );
```

The string "sv_touch_active" is first passed to SoundEffectContext, which resolves it to an absolute path, as long as the corresponding key was found during initialization.

The following two paths specify whether the sound file is in the res/raw folder of VrAppFramework (e.g., sounds that may be played from any app, such as default sounds or Settings Menu sounds), or the assets folder of a specific app: 

```
"res/raw/ sv_touch_active.wav"
```

```
"assets/ sv_touch_active.wav"
```

If SoundEffectContext fails to resolve the passed-in string within the SoundEffectContext::Play function, the string is passed to SoundPooler.play in Java. In SoundPooler.play, we first try to play the passed-in sound from res/raw, and if that fails, from the current assets folder. If that also fails, we attempt to play it as an absolute path. The latter allows for sounds to be played from the phone’s internal memory or SD card.

The JSON file loaded by SoundAssetMapping determines which assets are used with the following scheme:

1. Try to load sounds\_assets.json in the Oculus folder on the sdcard: sdcard/Oculus/sound\_assets.json
2. If we fail to find the above file, we the load the following two files in this order: res/raw/sound\_assets.json assets/sound\_assets.json


The loading of the sound_assets.json in the first case allows for a definition file and sound assets to be placed on the SD card in the **Oculus** folder during sound development. The sounds may be placed into folders if desired, as long as the relative path is included in the definition. 

```
"sv_touch_active" : "SoundDev/my_new_sound.wav"
```

we would replace all instances of that sound being played with our new sound within the SoundDev folder.

```
"sv_touch_active" : ""
```

The above key-value pair, if defined in an app’s sound_assets.json (placed in its asset folder), will disable that sound completely, even though it is still played by other VrAppSupport code such as VrGUI.

You will find the sound effect source code in VrAppSupport/VrSound/. 
