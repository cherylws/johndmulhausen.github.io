---
title: Haptics for Rift Controllers
---
This guide describes how to use Unreal Blueprints to control haptic effects on Touch or Xbox controllers. 

You may use the standard **Play Haptic Effect** Blueprint to send a specified haptic curve to the Oculus Touch or Xbox controller. For more information, see Unrealâ€™s [Play Haptic Effect guide](https://docs.unrealengine.com/latest/INT/BlueprintAPI/Game/Feedback/PlayHapticEffect/index.html).

## Haptics in Unreal Engine 4.13 and Later

PlayHapticEffects may be configured to play haptic waves based on three types of input. Right-click Content Browser to bring up the context menu, then select Miscellaneous. and select one of the following three options:

* Haptic Feedback Buffer: Plays a buffer of bytes 0-255,
* Haptic Feedback Curve: Draw the haptic linear curve you wish to play using the Haptic Curve Editor, or
* Haptic Feedback Soundwave: Select a mono audio file to be converted into a haptic effect of corresponding amplitude.
The following Blueprint illustrates a simple haptics sequence on the Oculus Touch controller using **Play Haptic Effect**. This example sends vibrations using **Play Haptic Effect** when the left controller grip button is pressed. When the button is released, **Stop Haptic Effect** sends a stop command to the Touch controller.

When the left controller X button is pressed, a constant vibration is sent by **Set Haptics by Value** until the button is released. Note that **Set Haptics by Value** calls are limited to 30 Hz; additional calls will be disregarded.

![](/images/documentation-unreal-latest-concepts-unreal-haptics-0.png)  
## Haptics in Unreal Engine 4.12 and Earlier

In addition to Play Haptic Effects, Unreal 4.12 adds Play Haptic Soundwave.

The following Blueprint illustrates a simple haptics sequence on the Oculus Touch controller using **Play Haptic Effects** and **Play Haptic Soundwave**. This example sends vibrations using **Play Haptic Effect** when the left controller grip button is pressed. When the button is released, **Play Haptic Soundwave** sends a second vibration to the controller.

When the left controller X button is pressed, a constant vibration is sent by **Set Haptics by Value** until the button is released. Note that **Set Haptics by Value** calls are limited to 30 Hz; additional calls will be disregarded.

![](/images/documentation-unreal-latest-concepts-unreal-haptics-1.png)  
APlayerController::PlayHapticSoundWave takes a mono soundwave as an argument. It downsamples the wave into a series of bytes that serially describe the amplitude of the wave (uint8 values 0-255). Each byte is then multiplied by the factor specified in Scale (max = 255), and haptic vibrations are sent to the targeted Oculus Touch controller. Each controller must be targeted individually. Call **Stop Haptic Effect** to stop haptic playback.

## Haptics Sample

The TouchSample, available from our Unreal GitHub repository, illustrates basic use of Oculus Touch, including haptics control using PlayHapticEffect() and PlayHapticSoundWave(). For more information, see [Unreal Samples](/documentation/unreal/latest/concepts/unreal-samples/ "Oculus provides samples which illustrate basic VR concepts in Unreal such as Touch, haptics, and the Boundary Component API for interacting with the Guardian System.").

