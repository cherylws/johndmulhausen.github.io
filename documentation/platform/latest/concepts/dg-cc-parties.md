---
title: Parties
---

Parties allow users to voice chat with friends in Oculus Home. 

For example, a group of friends can start a party in Home and chat about the game that they want to play together. Then, when they launch the app their chat session continues even while in that app. You may wish to disable party chat if your multiplayer app also has a voice chat feature.

Users can create Parties, start a voice chat using [Voice Chat (VoIP)](/documentation/platform/latest/concepts/dg-cc-voip/), invite friends to join them in [Rooms](/documentation/platform/latest/concepts/dg-rooms/), and even invite their Party to join an app using [Coordinated App Launch (CAL)](/documentation/platform/latest/concepts/dg-cc-cordapplaunch/) (only on Gear VR). Party voice chat persists across apps in VR and users can continue to interact while navigating between apps.

**Parties Integration**

No integration is required to support parties; however, there are some things you should consider if you are planning to use the microphone for commands or chat in your app.

We’ll discuss a number of VoIP services on this page, in short:

* Platform VoIP (aka VoIP) is the VoIP service provided by the Platform SDK that you can integrate and use in your app. Additional information can be found on [Voice Chat (VoIP)](/documentation/platform/latest/concepts/dg-cc-voip/ "Use the Platform VoIP service to add voice chat to your app.").
* System VoIP (aka Parties VoIP) is the VoIP service used in Oculus Home and Parties. This service does not require an integration and is available to any user.
* Application VoIP is any non-Oculus VoIP service that you use in your app. 


This page reviews how your app can use the microphone for chat or commands in collaboration with Parties.

## Rift

If you’re planning to have some form of VoIP in your application, you’ll need a way to handle the two chat streams. For example, if User A and B are in a party and User A launches an application that User C is playing and invites User C to a multiplayer game; User A will then be able to talk to B (on Party VoIP) and C (on Application or Platform VoIP), but B and C will not be able to hear each other. You’ll want to suppress one of the chat streams to avoid this conflict.

Oculus provides the System VoIP API that you can use to detect if the user is in a party and using (System VoIP), and allows you to disable a VoIP stream.

To use the SystemVoIP API first check the status of the SystemVoIP. There are two ways to check the state of SystemVoIP (active means the user is using Party VoIP). One way is to check every frame, the other is to listen for a notification.

1. Check Every Frame - To check whether SystemVoIP is active at any time (these are synchronous functions, not requests):* Native: ovr\\_Voip\\_GetSystemVoipStatus() == ovrSystemVoipStatus\\_Active * Unity: Voip.GetSystemVoipStatus() == SystemVoipStatus.Active 


2. Listen for a Notification - To get a notification for changes in the VoIP state you can make the following request:* In Native apps, listen or the notification for ovrMessage\\_Notification\\_Voip\\_SystemVoipState, and then use ovr\\_Message\\_GetSystemVoipState() and ovr\\_SystemVoipState\\_GetStatus() to get the status. * In Unity listen for MessageType.Notification\\_Voip\\_SystemVoipState which has a Message&lt;SystemVoipState&gt; from which you can access the Status field, or call SetSystemVoipStateNotificationCallback with a Message&lt;SystemVoipState&gt; callback. 




It's possible for the state to change quickly. The values you extract from notification messages will be the state at the time the notification was added to the message queue, which may be different from the state then the message is processed. You may wish to listen for the notification, and then ignore its values and check the current state using the synchronous functions.

Next, you can suppress the VoIP stream that you don’t want the user to hear or allow the user to hear the stream that they choose.

If the SystemVoIP is active you can:

* Use In-App VoIP - i.e. you want the user to be in your in-app chat instead of their party chat. Suppress SystemVoIP by calling ovr\_Voip\_SetSystemVoipSuppressed(bool suppressed), then use either Platform VoIP or your own VoIP service to run the app VoIP.
* Use SystemVoIP (Party VoIP) - i.e. you want to allow the user to continue using their party chat instead of the app VoIP. Suppress your in-app VoIP (don't send the user's mic input to other users and don't play other user's audio to the user). If youâ€™re using PlatformVoIP, information about suppressing that VoIP stream can be found on the [Voice Chat (VoIP)](/documentation/platform/latest/concepts/dg-cc-voip/ "Use the Platform VoIP service to add voice chat to your app.") page.


SystemVoIP will be unsuppressed if the app that has it suppressed quits. You may also wish to unsupress a user’s party VoIP when they leave the multiplayer portion of your app, e.g. your home menu, so that they may resume chatting with their party.

You may also allow your users to toggle between SystemVoIP and your in-app VoIP. This allows users to choose if they want to keep talking to their party (in which case you would need to suppress your in-app VoIP), or if they want to use your in-app VoIP (in which case you would need to suppress the SystemVoIP).

**Unreal Development**

If you're using Unreal, please use the native C API using the information found in [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/).

## Mobile

There are two integrations that you may need to add to your mobile app. If you’re planning to have voice chat in your app you’ll need to add the integrations listed in both the **Handle Multiple VoIP Streams** and **Manage the Shared Microphone** sections below. If you’re only using the microphone for voice commands, you can skip the **Handle Multiple VoIP Streams** section, you only need the steps in **Manage the Shared Microphone**.

**Handle Multiple VoIP Streams**

If you’re planning to have some form of VoIP in your application, you’ll need a way to handle the two chat streams. For example, if User A and B are in a party and User A launches an application that User C is playing and invites User C to a multiplayer game; User A will then be able to talk to B (on Party VoIP) and C (on Application or Platform VoIP), but B and C will not be able to hear each other. You’ll want to suppress one of the chat streams to avoid this conflict.

Oculus provides the System VoIP API that you can use to detect if the user is in a party and using (System VoIP), and allows you to disable a VoIP stream.

To use the SystemVoIP API first check the status of the SystemVoIP. There are two ways to check the state of SystemVoIP (active means the user is using Party VoIP). One way is to check every frame, the other is to listen for a notification.

1. Check Every Frame - To check whether SystemVoIP is active at any time (these are synchronous functions, not requests):* Native: ovr\\_Voip\\_GetSystemVoipStatus() == ovrSystemVoipStatus\\_Active * Unity: Voip.GetSystemVoipStatus() == SystemVoipStatus.Active 


2. Listen for a Notification - To get a notification for changes in the VoIP state you can make the following request:* In Native apps, listen or the notification for ovrMessage\\_Notification\\_Voip\\_SystemVoipState, and then use ovr\\_Message\\_GetSystemVoipState() and ovr\\_SystemVoipState\\_GetStatus() to get the status. * In Unity listen for MessageType.Notification\\_Voip\\_SystemVoipState which has a Message&lt;SystemVoipState&gt; from which you can access the Status field, or call SetSystemVoipStateNotificationCallback with a Message&lt;SystemVoipState&gt; callback. 




It's possible for the state to change quickly. The values you extract from notification messages will be the state at the time the notification was added to the message queue, which may be different from the state then the message is processed. You may wish to listen for the notification, and then ignore its values and check the current state using the synchronous functions.

Next, you can suppress the VoIP stream that you don’t want the user to hear or allow the user to hear the stream that they choose.

If the SystemVoIP is active you can:

* Use In-App VoIP - i.e. you want the user to be in your in-app chat instead of their party chat. Suppress SystemVoIP by calling ovr\_Voip\_SetSystemVoipSuppressed(bool suppressed), then use either Platform VoIP or your own VoIP service to run the app VoIP.
* Use SystemVoIP (Party VoIP) - i.e. you want to allow the user to continue using their party chat instead of the app VoIP. Suppress your in-app VoIP (don't send the user's mic input to other users and don't play other user's audio to the user). If youâ€™re using PlatformVoIP, information about suppressing that VoIP stream can be found on the [Voice Chat (VoIP)](/documentation/platform/latest/concepts/dg-cc-voip/ "Use the Platform VoIP service to add voice chat to your app.") page.


SystemVoIP will be unsuppressed if the app that has it suppressed quits. You may also wish to unsupress a user’s party VoIP when they leave the multiplayer portion of your app, e.g. your home menu, so that they may resume chatting with their party.

You may also allow your users to toggle between SystemVoIP and your in-app VoIP. This allows users to choose if they want to keep talking to their party (in which case you would need to suppress your in-app VoIP), or if they want to use your in-app VoIP (in which case you would need to suppress the SystemVoIP).

**Unreal Development**

If you're using Unreal, please use the native C API using the information found in [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/).

## Manage the Shared Microphone

Android only allows one device to access the microphone at a time. So, Oculus has developed an application layer that allows multiple applications to access the microphone at the same time.

The following functions can be used to access microphone data on an Android device. These functions allow the microphone to be accessed by multiple services. These functions should be used if you plan to use your own VoIP service or if you plan to use the microphone for voice commands in your application. Detail about each function can be found in the Platform SDK [Reference Content](/documentation/platform/latest/concepts/book-reference/).

* **Create a microphone object:**

Native - ovr\_Microphone\_Create()

Unity - Platform.Microphone.Create()

Create an ovrMicrophone object and receives a handle to it. The caller owns this memory and is responsible for freeing it. Use ovr\_Microphone\_Destroy to free the object.


* **Destroy a microphone object:**

Native - ovr\_Microphone\_Destroy()

Unity - Platform.Microphone.Destroy()

Stops and frees a previously created microphone object.


* **Retrieve microphone PCM data:**

Native - ovr\_Microphone\_GetPCM()

Unity - Platform.Microphone.GetPCM()

Retrieves all available samples of microphone data and copies it into the outputBuffer. The microphone will generate data at roughly the rate of 480 samples per 10ms. The data format is 16 bit fixed point 48khz mono. This function can be safely called from any thread.


* **Retrieve microphone PCM data (float):**

Native - ovr\_Microphone\_GetPCMFloat()

Unity - Platform.Microphone.GetPCMFloat()

Retrieves all available samples of microphone data and copies it into the outputBuffer. The microphone will generate data at roughly the rate of 480 samples per 10ms. The data format is 32 bit floating point 48khz mono. This function can be safely called from any thread.


* **Start microphone capture:**

Native - ovr\_Microphone\_Start()

Unity - Platform.Microphone.Start()

Start gathering microphone data. After this is called PCM data can be extracted. This function can be safely called from any thread.


* **Stop microphone capture:**

Native - ovr\_Microphone\_Stop()

Unity - Platform.Microphone.Stop()

Stop gathering microphone data. This function can be safely called from any thread.




**Integration**

In general, creating a microphone object may resemble the following:

* Create the microphone object by calling ovr\_Microphone\_Create().
* Start capturing microphone data in your app, when appropriate, by calling ovr\_Microphone\_Start(). 
* When youâ€™re ready to read the microphone data, call either ovr\_Microphone\_GetPCMFloat() or ovr\_Microphone\_GetPCM() to retrieve the PCM data off the buffer and use as needed in your application. 
* When finished, you can either stop collecting PCM data by calling ovr\_Microphone\_Stop() if you intend to start again at some point, or ovr\_Microphone\_Destroy() to destroy the microphone object. 

