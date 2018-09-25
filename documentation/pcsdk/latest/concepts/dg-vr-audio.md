---
title: Rift Audio
---
When setting up audio for the Rift, you need to determine whether the Rift headphones are active and pause the audio when your app doesn’t have focus.

The user can enable the Rift headphones and microphone in the Oculus app or use the default Windows audio devices. Configuration is made the Oculus app in Settings -> Devices -> Headset. The following screenshot shows the Rift headphones disabled and the microphone enabled: 

![](/images/documentation-pcsdk-latest-concepts-dg-vr-audio-0.png)  
Audio ConfigurationThe headphone setting is handled automatically by the function ovr\_GetAudioDeviceOutGuid (located in OVR\_CAPI\_Audio.h), which returns the GUID for the device to target when playing audio. Similarly, use ovr\_GetAudioDeviceInGuid to identify the microphone device used for input. 

## FMOD D for Native Rift Development

If you detect that the Rift headphones are enabled, use code similar to the following for FMOD: 

ERRCHECK(FMOD::System\_Create(&sys)); GUIDguid; ovr\_GetAudioDeviceOutGuid(&guid); intdriverCount=0; sys->getNumDrivers(&driverCount); intdriver=0; while(driver<driverCount) { charname[256]={0}; FMOD\_GUIDfmodGuid={0}; sys->getDriverInfo(driver,name,256,&fmodGuid,nullptr,nullptr,nullptr); if(guid.Data1==fmodGuid.Data1&& guid.Data2==fmodGuid.Data2&& guid.Data3==fmodGuid.Data3&& memcmp(guid.Data4,fmodGuid.Data4,8)==0) { break; } ++driver; } if(driver<driverCount) { sys->setDriver(driver); } else { // error rift not connected } For instructions on using FMOD with Unreal Engine, see “Unreal and FMOD” below. 

## Wwise for Native Rift Development

If you detect that the Rift headphones are enabled, use code similar to the following for Wwise: 

AkInitSettings initSettings; AkPlatformInitSettings platformInitSettings; AK::SoundEngine::GetDefaultInitSettings( initSettings ); AK::SoundEngine::GetDefaultPlatformInitSettings( platformInitSettings ); // Configure initSettings and platformInitSettings... WCHAR outStr[128]; if (OVR\_SUCCESS(ovr\_GetAudioDeviceOutGuidStr(outStr))) { initSettings.eMainOutputType = AkAudioAPI::AkAPI\_Wasapi; platformInitSettings.idAudioDevice = AK::GetDeviceIDFromName(outStr); } For instructions on using Wwise with Unity 5, see “Unity 5 and Wwise” below. For instructions on using Wwise with Unreal Engine, see “Unreal and FMOD” below. 

## Unity 5

Audio input and output automatically use the Rift microphone and headphones unless configured to use the Windows default audio device by the user in the Oculus app. Events OVRManager.AudioOutChanged and AudioInChanged occur when audio devices change, making audio playback impossible without a restart.

## Unity 5 and Wwise

To configure Wwise to use to configured audio device in Unity 5, pass the user-configured audio device name/GUID (set in the Oculus app) into the function AkSoundEngine.GetDeviceIDFromName(), located in AkInitializer.cs.

To get the audio device GUID from libOVR, you must include the Oculus Utilities unitypackage, which exposes that string through the class OVRManager.

The following function should be called before AkSoundEngine.Init(...):

void SetRiftAudioDevice(AkPlatformInitSettings settings) { string audioDevice = OVRManager.audioOutId; uint audioOutId = AkSoundEngine.GetDeviceIDFromName (audioDevice); settings.idAudioDevice = audioOutId; }Pass AkPlatformInitSettings into the function above and use it to initialize the Ak sound engine.

Note:OVRManager.audioOutId will be deprecated in the future. This minor change should not impact the integration.VR Audio Output in Oculus Store > Settings > Devices > Rift Headset may be used to configure which input mic to use within the Ak sound engine. The GUID for this is exposed through OVRManager.audioInId.

## Unity 4

Audio input and output automatically use the Rift microphone and headphones, unless configured to use the Windows default audio device by the user in the Oculus app.

The Rift’s microphone is not used by default when calling Microphone.Start(null,..). Find the entry in Microphone.devices that contains the word Rift and use it.

## Unreal

When Unreal PC applications are launched, if the OculusRift plugin is enabled and the Oculus VR Runtime Service is installed, then the application will automatically override the default Windows graphics and audio devices and target the Rift. The Oculus VR Runtime Service is installed with the Oculus app.

Unless your application is intended to run in VR, do not enable the OculusRift plugin. Otherwise, it is possible that audio and/or video will be incorrectly targeted to the Oculus Rift when the application is run.

Alternatively, users can disable loading all HMD plugins by specifying "-nohmd" on the command line.

## Unreal and Wwise

To use Wwise with any Unreal version, use the Wwise Unreal Plug-in provided by Audiokinetic here: [https://www.audiokinetic.com/library/2016.1.0\_5775/?source=UE4&id=index.html](https://www.audiokinetic.com/library/2016.1.0_5775/?source=UE4&id=index.html).

Note: The link above links to build Wwise 2016.1 build 5775 for use with Unity 4.12. Be sure to select the appropriate build for your Unity version in the upper-left. ![](/images/documentation-pcsdk-latest-concepts-dg-vr-audio-1.png)  
## Unreal and FMOD

For an illustration of how to target the Oculus Rift headphones using FMOD in UE4, see the FMOD section above.

## Unity 5 and FMOD

To target the Oculus Rift headphones using FMOD in Unity 5, use the following code snippet:

 FMOD.System sys; FMODUnity.RuntimeManager.StudioSystem.getLowLevelSystem(out sys); int driverCount = 0; sys.getNumDrivers(out driverCount); string riftId = OVRManager.audioOutId; int driver = 0; while (driver < driverCount) { System.Guid guid; int rate, channels; FMOD.SPEAKERMODE mode; sys.getDriverInfo(driver, out guid, out rate, out mode, out channels); if (guid.ToString() == riftId) { break; } ++driver; } if(driver < driverCount) { sys.setDriver(driver); } ## Oculus Audio Spatialization

The Oculus Audio SDK, available from our Downloads page, provides free, easy-to-use spatializer plugins for engines and middleware. Our spatialization features support both Rift and Gear VR development.

For a detailed discussion of audio spatialization and virtual reality audio, we recommend beginning with our Introduction to Virtual Reality Audio and Oculus Audio SDK guides.

For additional information on using Oculus spatializer plugins with Unity and Unreal, see Unity Audio and Unreal VR Audio.

## VR Sound Level Best Practices

Audio is an important part of the virtual reality experience, and it is important that all VR apps provide a comfortable listening level for users. Developers should target a reasonable sound level that is consistent between different experiences. To achieve this, Oculus recommends the following best practices.

First, target -18 LUFS during final mix. To do this, you can use the use the Oculus Audio Loudness Meter [https://www.audiokinetic.com/library/2016.1.0\_5775/?source=UE4&id=index.html](https://www.audiokinetic.com/library/2016.1.0_5775/?source=UE4&id=index.html). Alternatively, you can use third party tools such as Avid's Pro Limited Plugin, Nugen's VisLM, Klangfreund LUFS Meter, Audacity VuMeter, or similar loudness measurement tools.

Second, measure your experience against the audio levels in published Oculus experiences, especially the ambient audio in Home and the Dreamdeck experience. Set overall system volume so that Dreamdeck and Home sound comfortable, and then adjust your experience's mix to this volume.

Finally, mix your application using the Rift headphones. This ensures that the sounds you're creating and mixing have a frequency content appropriate for the headphones most Oculus users will use.

By adhering to these guidelines, we can guarantee that our Oculus VR users will have a pleasant audio experience.

