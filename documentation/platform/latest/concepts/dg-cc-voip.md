---
title: Voice Chat (VoIP)
---

Use the Platform VoIP service to add voice chat to your app. 

The VoIP service transmits PCM (pulse-code modulation) data between users that the Platform SDK decodes to audio.

VoIP is peer-to-peer so your app will be limited by bandwidth in most cases. In general, the VoIP service becomes unstable if you have 12, or more, connections. We recommend no more than 8 connections on Rift and 4 on Gear VR. You may be able to support more if you use push to talk or some proximity-type muting.

## Integrating VoIP - Native &amp; Unity

To integrate Application VoIP in your Native application, follow the steps below. The methods can be called from your client app. Detail about each function can be found in the Platform SDK [Reference Content](/documentation/platform/latest/concepts/book-reference/).

* **Send a VoIP connection request:**

Native - ovr\_Voip\_Start()

Unity - Platform.Voip.Start()

Initiate a VoIP connection request with a specified user.


* **Accept a VoIP connection request:**

Native - ovr\_Voip\_Accept()

Unity - Platform.Voip.Accept()

Accept a VoIP connection request. 


* **Retrieve the maximum size of the buffer:**

Native - ovr\_Voip\_GetOutputBufferMaxSize()

Unity - Platform.Voip.GetOutputBufferMaxSize()

Retrieve the size of the internal ringbuffer used by the VoIP system in elements. This size is the maximum number of elements that can ever be returned by ovr\_Voip\_GetPCM or ovr\_Voip\_GetPCMFloat.


* **Retrieve PCM data from a user (16 bit fixed point):**

Native - ovr\_Voip\_GetPCM()

Unity - Platform.Voip.GetPCM()

Retrieve all available samples of voice data from a specified user and copy them into the outputBuffer. The VoIP system will generate data at roughly the rate of 480 samples per 10ms. This function should be called every frame with 50ms (2400 elements) of buffer size to account for frame rate variations. The data format is 16 bit fixed point 48khz mono.


* **Retrieve PCM data from a user (32 bit floating point):**

Native - ovr\_Voip\_GetPCMFloat()

Unity - Platform.Voip.GetPCMFloat()

Retrieve all available samples of voice data from a specified user and copy them into the outputBuffer The VoIP system will generate data at roughly the rate of 480 samples per 10ms. This function should be called every frame with 50ms (2400 elements) of buffer size to account for frame rate variations. The data format is 32 bit floating point 48khz mono.

We do not recommend using floating point unless necessary. This operation requires additional resources when compared to the integer based process.


* **Retrieve the number of PCM data files available:**

Native - ovr\_Voip\_GetPCMSize()

Unity - Platform.Voip.GetPCMSize()

Retrieve the current number of audio samples available to read from a specified user. This function is inherently racy, it's possible that data can be added between a call to this function and a subsequent call to ovr\_Voip\_GetPCM or ovr\_Voip\_GetPCMFloat.


* **Retrieve PCM data with a timestamp from a user (16 bit fixed point):**

Native - ovr\_Voip\_GetPCMWithTimestamp()

Unity - Platform.Voip.GetPCMWithTimestamp()

Like ovr\_Voip\_GetPCM, this function copies available audio samples from a specified user into a buffer. Along with the audio samples, this function also stores the timestamp of the first sample in the output parameter timestamp. This timestamp can be used for synchronization, see ovr\_Voip\_GetSyncTimestamp for more details. The data format is 16 bit fixed point 48khz mono.

This function may return data early, even if there's more data available, to keep the batch of audio samples returned with a single timestamp small. For example, if 30ms worth of audio is in the buffer, this function may return 480 samples (10ms) each time it's called. Therefore, it's recommended to call this as long as there's data in the buffer (i.e. the function returns a non-zero result).


* **Retrieve PCM Data with a timestamp from a user (32 bit floating point):**

Native - ovr\_Voip\_GetPCMWithTimestampFloat()

Unity - Platform.Voip.GetPCMWithTimestampFloat()

Like ovr\_Voip\_GetPCMFloat, this function copies available audio samples from a specified user into a buffer. Along with the audio samples, this function also stores the timestamp of the first sample in the output parameter timestamp. This timestamp can be used for synchronization, see ovr\_Voip\_GetSyncTimestamp for more details. The data format is 32 bit floating point 48khz mono.

This function may return data early, even if there's more data available, in order to keep the batch of audio samples with a single timestamp small. For example, if there's 30ms worth of audio in the buffer, this function may return 480 samples (10ms) each time it's called. Therefore, it's recommended to call this as long as there's data in the buffer (i.e. the function returns a non-zero result).

We do not recommend using floating point unless necessary. This operation requires additional resources when compared to the integer based process.


* **Retrieve the sync timestamp for the sender:**

Native - ovr\_Voip\_GetSyncTimestamp()

Unity - Platform.Voip.GetSyncTimestamp()

Returns a timestamp used for synchronizing audio samples sent to the user with an external data stream.

Timestamps associated with audio frames are implicitly transmitted to remote peers; on the receiving side, they can be obtained by using ovr\_Voip\_GetPCMWithTimestamp. ovr\_Voip\_GetSyncTimestamp is used to fetch those timestamps on the sending side. An application can insert the value returned by this function into each data packet and compare it to the value returned by GetPCMWithTimestamp on the receiving side to determine the ordering of two events (sampling audio and composing a data packet).

Note: The timestamp is generated by an unspecified clock and won't represent wall-clock time. Use ovr\_Voip\_GetSyncTimestampDifference to determine the difference between two timestamps in microseconds.This function assumes that a voice connection to the user already exists; it returns 0 if that isn't the case.


* **Retrieve the difference (in Âµs) between two timestamps:**

Native - ovr\_Voip\_GetSyncTimestampDifference()

Unity - Platform.Voip.GetSyncTimestampDifference()

Retrieve the calculated difference between two sync timestamps, in microseconds. returned by ovr\_Voip\_GetSyncTimestamp, ovr\_Voip\_GetPCMWithTimestamp, or ovr\_Voip\_GetPCMWithTimestampFloat.

Return value will be negative if lhs is smaller than rhs, zero if both timestamps are the same, and positive otherwise. The absolute value of the result is the time in microseconds between the two sync timestamps.


* **Retrieve the mute state of the microphone:**

Native - ovr\_Voip\_GetSystemVoipMicrophoneMuted()

Unity - Platform.Voip.GetSystemVoipMicrophoneMuted()

Checks if the microphone has been muted. 


* **Retrieve the VoIP system status:**

Native - ovr\_Voip\_GetSystemVoipStatus()

Unity - Platform.Voip.GetSystemVoipStatus()

Retrieves the status of SystemVoIP. SystemVoIP is the service used by Oculus Parties. Please review the [Parties](/documentation/platform/latest/concepts/dg-cc-parties/ "Parties allow users to voice chat with friends in Oculus Home.") page for information about potential SystemVoIP conflicts. 


* **Set the microphone filter callback:**

Native - ovr\_Voip\_SetMicrophoneFilterCallback()

Unity - Platform.Voip.SetMicrophoneFilterCallback()

Set a callback that will be called every time audio data is captured by the microphone. The callback function must match this format:

void filterCallback(int16\_t pcmData[], size\_t pcmDataLength, int frequency, int numChannels);The pcmData param is used for both input and output. pcmDataLength is the size of pcmData in elements. numChannels will be 1 or 2. If numChannels is 2, then the channel data will be interleaved in pcmData. frequency is the input data sample rate in hertz.


* **Mute/unmute the microphone:**

Native - ovr\_Voip\_SetMicrophoneMuted()

Unity - Platform.Voip.SetMicrophoneMuted()

This function is used to enable or disable the local microphone. When muted, the microphone will not transmit any audio. VoIP connections are unaffected by this state. New connections can be established or closed whether the microphone is muted or not. This can be used to implement push-to-talk, or a local mute button. The default state is unmuted.


* **Set the VoIP output sample rate:**

Native - ovr\_Voip\_SetOutputSampleRate()

Unity - Platform.Voip.SetOutputSampleRate()

Set the output sample rate. Audio data will be resampled as it is placed into the internal ringbuffer. 


* **Terminate the VoIP connection:**

Native - ovr\_Voip\_Stop()

Unity - Platform.Voip.Stop()

End a VoIP session with a specified user. Note that a muting functionality should be used to temporarily stop sending audio; restarting a VoIP session after tearing it down may be an expensive operation.




## Setting VoIP Options – DTX and Bit Rate

You can optionally configure your app to use discontinuous transmission (DTX) and set the bit rate for VoIP connections.

DTX allows for temporary microphone muting when there's no voice input. This improves efficiency because a person is usually talking less than half the time in a typical two-way conversation. This can conserve battery life and free up the channel. By default, DTX is disabled.

Setting the bit rate controls the network usage when transmitting on VoIP connections. The higher the bit rate, the better the audio quality, but more network resources are used. A lower bit rate will conserve network resources. By default, the bit rate is 32,000 bits per second.

Once these options have been configured, they apply only to new connections. Existing connections must be closed and reconnected for the new settings to be applied.

To configure these options in a Native application, follow these steps:

1. Create an options handle with ovr\_VoipOptions\_Create.


2. Configure the desired options using the handle with ovr\_VoipOptions\_SetCreateNewConnectionUseDtx and ovr\_VoipOptions\_SetBitrateForNewConnections.


3. Enable the newly configured options with ovr\_Voip\_SetNewConnectionOptions.


4. Destroy the handle with ovr\_VoipOptions\_Destroy.




These functions are described below. Additional details about all functions can be found in the [Platform SDK Reference Content](/documentation/platform/latest/concepts/book-reference/).

An example flow of calls in a Native application would look like this:

```
ovrVoipOptionsHandle options = ovr_VoipOptions_Create();
ovr_VoipOptions_SetCreateNewConnectionUseDtx(options, ovrVoipDtxState_Enabled);
ovr_VoipOptions_SetBitrateForNewConnections(options, ovrVoipBitrate_B64000); 
ovr_Voip_SetNewConnectionOptions(options);
ovr_VoipOptions_Destroy(options);
                 
```

* **Create a handle to set VoIP options:**

Native - ovr\_VoipOptions\_Create()

Unity - var voipOptions = new VoipOptions()

Creates a handle used to set options.


* **Set DTX usage:**

Native - ovr\_VoipOptions\_SetCreateNewConnectionUseDtx()

Unity - voipOptions.SetCreateNewConnectionUseDtx()

Used to enable or disable DTX. Passing the options handle and a value of ovrVoipDtxState\_Enabled enables DTX on all new VoIP connections. It does not apply to existing connections, which must be closed and then reconnected for DTX to be enabled. Passing the options handle and a value of ovrVoipDtxState\_Disabled similarly disables DTX on all new connections.

In Unity, this is set to ovrVoipDtxState.Enabled or ovrVoipDtxState.Disabled.

By default, apps will have DTX disabled.


* **Set the bit rate for new connections:**

Native - ovr\_VoipOptions\_SetBitrateForNewConnections()

Unity - voipOptions.SetBitrateForNewConnections()

Used to set the bit rate on all new VoIP connections. The higher the bit rate, the better the audio quality, at the expense of network usage. It does not apply to existing connections, which must be closed and then reconnected for the new bit rate to take effect.

To change the bit rate, pass the options handle and one of the following values:


	+ ovrVoipBitrate\_B16000
	
	
	+ ovrVoipBitrate\_B24000
	
	
	+ ovrVoipBitrate\_B32000  (default)
	
	
	+ ovrVoipBitrate\_B64000
	
	
	+ ovrVoipBitrate\_B96000
	
	
	+ ovrVoipBitrate\_B128000
	
	
	In Unity, these values are in the format of VoipBitrate.B32000.


* **Enable the newly configured options:**

Native - ovr\_Voip\_SetNewConnectionOptions()

Unity - Platform.Voip.SetNewConnectionOptions()

Enables the options set on all new connections.


* **Destroy the VoIP options handle:**

Native - ovr\_VoipOptions\_Destroy()

Unity - Not necessary

Destroys the options handle. This is not necessary in Unity.




In addition, there are several functions related to these options. 

* **Check if a connection is using DTX:**

Native - ovr\_Voip\_GetIsConnectionUsingDtx()

Unity - Platform.Voip.GetIsConnectionUsingDtx()

Checks if a connection is using DTX. If a connection exists and both sides have DTX enabled, this returns ovrVoipDtxState\_Enabled (Unity: ovrVoipDtxState.Enabled). If a connection exists and only one or neither side has it enabled, this returns ovrVoipDtxState\_Disabled (Unity: ovrVoipDtxState.Disabled). If thereâ€™s no existing connection, this returns ovrVoipDtxState\_Unknown (Unity: ovrVoipDtxState.Unknown).


* **Check the bit rate of the remote user:**

Native - ovr\_Voip\_GetRemoteBitrate()

Unity - Platform.Voip.GetRemoteBitrate()


* **Check the bit rate of the local user:**

Native - ovr\_Voip\_GetLocalBitrate()

Unity - Platform.Voip.GetLocalBitrate()

These functions return an ovrVoipBitrate value specifying the VoIP bit rate of the remote and local users respectively. The bit rates do not have to be the same. For example, if the remote bit rate is very high and the local bit rate is very low, the local user will hear high quality audio but send low quality audio. If there is no existing connection, this returns ovrVoipBitrate\_Unknown (Unity: ovrVoipBitrate.Unknown).




## Implementation Overview - Unity

This section will walk you through the basic process of implementing VoIP in your Unity app. Before integrating VoIP, please review the [Parties](/documentation/platform/latest/concepts/dg-cc-parties/) page for information about potential conflicts with users who launch your app while participating in a party. Neglecting to do so will result in a poor user experience. 

A complete example of a Unity app The general process of implementing VoIP is:

1. Send the connection request. The user initiating the connection request calls Voip.Start with the user id's of the other user. Information about how to retrieve a user id's can be found or the [Users, Friends, and Relationships](/documentation/platform/latest/concepts/dg-presence/ "Users, friends, and relationships manages information about each user's unique persona, their relationship with their friends, and their recent encounters in VR.").
2. Establish a callback as a notification handler to accept incoming connection requests by calling Voip.Accept from the user receiving the request. For example, to accept all incoming connections, you could use the following:Voip.SetVoipConnectRequestCallback((Message&lt;NetworkingPeer&gt; msg) =&gt; { Voip.Accept(msg.Data.ID); });
3. Listen for the state change. Both users will be listening for the callback that the connection has been established. Once this is received the users can begin exchanging data. An example of a state change listener is:Voip.SetVoipStateChangeCallback((Message&lt;NetworkingPeer&gt; msg) =&gt; { Debug.LogFormat("peer {0} is in state {1}", msg.Data.ID, msg.Data.State); });
4. Accept the connection request by calling Voip.Accept to open the connection.
5. Add the playback component. The audio playback component handles buffering and playback of voice data from a remote peer. You should add this component to a game object that represents a connected user, such as their avatar. For each connected user, youâ€™ll need to set the senderID field of each VoipAudioSourceHiLevel object you create. This lets the system know which user's voice data corresponds to each playback component. For example:var audioSource = gameObject.AddComponent &lt;VoipAudioSourceHiLevel&gt;(); audioSource.senderID = remotePeer.ID;
6. You can access the Unity AudioSource object from the VoipAudioSourceHiLevel object to modify playback options. For instance to spatialize the audio playback:Var voipAudio = RemoteAvatar.GetComponent&lt;VoipAudioSourceHiLevel&gt;(); voipAudio.audioSource.spatialize = true;
7. To end a VoIP connection call: Oculus.Platform.Voip.Stop(userID); Voip.Stop(remotePeer.ID);
8. (Optional) At any time either user may mute their microphone by calling Platform.Voip.SetMicrophoneMuted. Calling the same function will unmute the microphone. Call Platform.Voip.GetSystemVoipMicrophoneMuted to check the mute state of the microphone. 


## Implementation Overview - Native

This section will walk you through the basic process of implementing VoIP in your Native app. Before integrating VoIP, please review the [Parties](/documentation/platform/latest/concepts/dg-cc-parties/) page for information about potential conflicts with users who launch your app while participating in a party. Neglecting to do so will result in a poor user experience. 

The general process of implementing VoIP is:

1. Send the connection request. The user initiating the connection request calls ovr\_Voip\_Start with the Id of the user they would like to connect with. Information about retrieving user id's can be found or the [Users, Friends, and Relationships](/documentation/platform/latest/concepts/dg-presence/ "Users, friends, and relationships manages information about each user's unique persona, their relationship with their friends, and their recent encounters in VR.").
2. Accept the connection request. The user on the receiving end of the will be listening for notifications on their message queue. Information about how the Platform SDK uses the message queue can be found on the [Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/ "The Platform SDK uses a message queue to interact with Native apps. This page describes the concept of the queue and how to retrieve messages and information.") page. After handling the request, the receiving user accepts by calling ovr\_Net\_Accept with the peerID of the request.
3. Listen for the state change. Both users will be listening for the notification that the connection has been established by listening for ovrMessage\_Notification\_Voip\_StateChange. Once this is received the users can begin exchanging data.
4. Transmit PCM data. The connected microphone will begin capturing the voice data and the SDK will convert to PCM data and transmit to the user the connection was established with.
5.  Determine the size of the buffer. Call ovr\_Voip\_GetOutputBufferMaxSize to determine the max output size, or the maximum number of elements that can be retrieved.
6. Retrieve PCM data for processing and playback. There are a number of methods you can use to retrieve the PCM data depending on your application's use-case. Before you retrieve any data, call ovr\_Voip\_GetPCMSize to determine the size of the data in the buffer. Then call one of the following methods to retrieve the data. One of these methods needs to be called for each connection, PCM data will only be returned for a single user connection. 
	1. ovr\_Voip\_GetPCM - Retrieves the PCM data in 16 bit fixed point 48khz mono format. ovr\_Voip\_GetPCMWithTimestamp retrieves the same data with an additional timestamp that can be used for synchronization. 
	2. ovr\_Voip\_GetPCMFloat - Retrieves the PCM data in 32 bit floating point 48khz mono. ovr\_Voip\_GetPCMWithTimestampFloat retrieves the same data with an additional timestamp that can be used for synchronization. Using floating point is not recommended unless necessary. 
	
7. (Optional) After retrieving the PCM data, you may wish to spatialize the audio playback. Information about spatializing audio can be found in the [Audio SDK](https://developer.oculus.com/documentation/audiosdk/latest/) documentation.
8. (Optional) At any time either user may mute their microphone by calling ovr\_Voip\_SetMicrophoneMuted. Calling the same function will unmute the microphone. Call ovr\_Voip\_GetSystemVoipMicrophoneMuted to check the mute state of the microphone. 
9. End the connection. Terminate the connection between users at any time, call ovr\_Voip\_Stop to close.


**Notifications and the Message Queue**

As mentioned above, the VoIP service uses notifications to update your app on the status of the connection and service. Review the [Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/) page for more information about the message queue and notifications.

For example, a native application may listen for state changes using:

```
case ovrMessage_Notification_Voip_StateChange: {
    ovrNetworkingPeerHandle netPeer = ovr_Message_GetNetworkingPeer(message);
    ovrPeerConnectionState netState = ovr_NetworkingPeer_GetState(netPeer);
    printf(
        "User: %llu, voip state %s\n", 
        ovr_NetworkingPeer_GetID(netPeer),
        ovrPeerConnectionState_ToString(netState)
    );
}  
Break;
```

## Example Implementation - Unity

The VrVoiceChat Unity app provided in the [Platform SDK](/downloads/) download demonstrates use of the VoIP service. Please see the [Sample Apps](/documentation/platform/latest/concepts/book-sampleapp/) page for more information about the apps that are available.

```
using UnityEngine;
using System.Collections;

using Oculus.Platform;
using Oculus.Platform.Models;

// Helper class to manage the Voice-over-IP connection to the
// remote user
public class VoipManager
{
    // the ID of the remote user I expect to talk to
    private ulong m_remoteID;

    // the last reported state of the VOIP connection
    private PeerConnectionState m_state = PeerConnectionState.Unknown;

    // the GameObject where the remote VOIP will project from
    private readonly GameObject m_remoteHead;

    public VoipManager(GameObject remoteHead)
    {
        m_remoteHead = remoteHead;

        Voip.SetVoipConnectRequestCallback(VoipConnectRequestCallback);
        Voip.SetVoipStateChangeCallback(VoipStateChangedCallback);
    }

    public void ConnectTo(ulong userID)
    {
        m_remoteID = userID;
        var audioSource = m_remoteHead.AddComponent&lt;VoipAudioSourceHiLevel&gt;();
        audioSource.senderID = userID;

        // ID comparison is used to decide who initiates and who gets the Callback
        if (PlatformManager.MyID &lt; m_remoteID)
        {
            Voip.Start(userID);
        }
    }


    public void Disconnect()
    {
        if (m_remoteID != 0)
        {
            Voip.Stop(m_remoteID);
            Object.Destroy(m_remoteHead.GetComponent&lt;VoipAudioSourceHiLevel&gt;(), 0);
            m_remoteID = 0;
            m_state = PeerConnectionState.Unknown;
        }
    }

    public bool Connected
    {
        get
        {
            return m_state == PeerConnectionState.Connected;
        }
    }

    void VoipConnectRequestCallback(Message&lt;NetworkingPeer&gt; msg)
    {
        Debug.LogFormat("Voip request from {0}, authorized is {1}", msg.Data.ID, m_remoteID);

        if (msg.Data.ID == m_remoteID)
        {
            Voip.Accept(msg.Data.ID);
        }
    }

    void VoipStateChangedCallback(Message&lt;NetworkingPeer&gt; msg)
    {
        Debug.LogFormat("Voip state to {0} changed to {1}", msg.Data.ID, msg.Data.State);

        if (msg.Data.ID == m_remoteID)
        {
            m_state = msg.Data.State;

            if (m_state == PeerConnectionState.Timeout &amp;&amp;
                // ID comparison is used to decide who initiates and who gets the Callback
                PlatformManager.MyID &lt; m_remoteID)
            {
                // keep trying until hangup!
                Voip.Start(m_remoteID);
            }
        }

        PlatformManager.SetBackgroundColorForState();
    }
}
```

## Implementation Overview - Unreal

To integrate VoIP in your Unreal app, call the functions below once you've established the online session. You can call these functions from anywhere in your code that you'd like. Please see Epic's [Online::GetVoiceInterface](https://docs.unrealengine.com/latest/INT/API/Plugins/OnlineSubsystem/Online__GetVoiceInterface/index.html) page for more information.

First, to enable VoIP in DefaultEngine.ini:

```
[OnlineSubsystem]
                DefaultPlatformService=Oculus
                bHasVoiceEnabled=true
                
                [Voice]
                bEnabled=true
```

In the session, you can retrieve an array of the players in the session and their corresponding `FUniqueNetIdOculus`.

To connect to someone else:

```
Online::GetVoiceInterface()-&gt;RegisterRemoteTalker(&lt;FUniqueNetIdOculus&gt;);
```

To disconnect from someone:

```
Online::GetVoiceInterface()-&gt;UnregisterRemoteTalker(&lt;FUniqueNetIdOculus&gt;);
```

To see if a remote user is talking:

```
Online::GetVoiceInterface()-&gt;IsRemotePlayerTalking(&lt;FUniqueNetIdOculus&gt;);
```

To unmute yourself:

```
Online::GetVoiceInterface()-&gt;StartNetworkedVoice(0);
```

To mute yourself:

```
Online::GetVoiceInterface()-&gt;StopNetworkedVoice(0);
```
