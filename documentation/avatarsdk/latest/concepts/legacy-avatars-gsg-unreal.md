---
title: Unreal (Rift) Getting Started
---

The Oculus Avatar SDK for Unreal Beta download file contains an Unreal Engine (UE) C++ sample project illustrating and implementing all the features available to Oculus Avatars in UE.

The example project demonstrates:

* using avatar classes to create and destroy UE avatar objects.
* changing hand poses to custom hand poses and rendering Touch controllers.
* recording local avatar movement packets and replaying the packets back on remote avatars (including voice visualizations).


## Requirements

* Unreal Editor 4.15 (Avatar SDK Unreal beta is currently only supported in version 4.15)
* Microsoft Visual Studio 2015 with C++
* Oculus Avatar SDK for Unreal Beta from &lt;https://developer.oculus.com/downloads/package/oculus-avatar-sdk-unreal-beta/&gt;


## Architecture of a UE Avatar Project

Oculus Avatars for UE are implemented as a plugin. Avatars are embodied within `UOvrAvatar` ActorComponents that you can attach to the UE actors you desire. This lets you keep your game-side code separate from our avatar implementation.

* Config/DefaultInput.ini - contains the avatar input settings for Touch controllers.
* Config/DefaultEngine.ini - contains your app ID and adds Oculus Platform as a subsystem.
* Content/Avatars/ - contains the material assets used by the avatars.
* Plugins/ - contains Oculus Avatars implemented as an Unreal plugin.
* Source/LocalAvatar.cpp and RemoteAvatar.cpp - contain the "game-side" classes that demonstrate how to attach avatar components to actor classes.
* AvatarSamples.uproject - enables the OvrAvatar plugin.


## Launching the Avatar Samples Unreal Project

1. Extract the contents of the Oculus Avatar SDK for Unreal Beta .zip file.
2. Launch **AvatarSamples.uproject**.
3. Click **Play &gt; VR Preview**
4. Wear your Rift.


You should see the hands of your avatar. This first person view where you only see your hands is referred to as the local avatar.



![](/images/documentationavatarsdklatestconceptslegacy-avatars-gsg-unreal-0.jpg)



The code that spawns your first-person avatar is in `LocalAvatar.cpp`: 

```
ALocalAvatar::ALocalAvatar()
{
	RootComponent = CreateDefaultSubobject&lt;USceneComponent&gt;(TEXT("LocalAvatarRoot"));

	PrimaryActorTick.bCanEverTick = true;
	AutoPossessPlayer = EAutoReceiveInput::Player0;

	BaseEyeHeight = 170.f;

	AvatarComponent = CreateDefaultSubobject&lt;UOvrAvatar&gt;(TEXT("LocalAvatar"));
	AvatarComponent-&gt;SetVisibilityType(ovrAvatarVisibilityFlag_FirstPerson);
	AvatarComponent-&gt;SetPlayerHeightOffset(BaseEyeHeight / 100.f);
}
```

## Spawning and Destroying Remote Avatars

Squeeze the right Touch trigger to spawn avatars in a circle around you. Squeeze the left Touch trigger to destroy them. These third-person avatars with hands, heads, and base cones represent other people and are called remote avatars.

The remote avatars in this sample mimic your movements because we hooked them up to our avatar packet recording and playback system. This system records both your movements and your microphone amplitude, letting us transmit them to remote avatars and animate them accordingly. Speak or sing to see the voice animations on the remote avatars.



![](/images/documentationavatarsdklatestconceptslegacy-avatars-gsg-unreal-1.jpg)



The packet recording is handled by `ALocalAvatar::UpdatePacketRecording(float DeltaTime)` in LocalAvatar.cpp.

Packet playback on remote avatars is handled by `ARemoteAvatar::Tick` in RemoteAvatar.cpp. You might notice a small delay in the response between your local avatar movements and the corresponding movement in the remote avatars. This is an artificial delay we added to the sample to simulate network latency.

To toggle packet recording and playback:

* Press A on your right Touch.


## Creating Custom Hand Poses

Press the thumbsticks to cycle through the following hand poses:

* a built-in pose for gripping a sphere:

AvatarComponent-&gt;SetRightHandPose(ovrAvatarHandGesture\_GripSphere);
* a built-in pose for gripping a cube:

AvatarComponent-&gt;SetRightHandPose(ovrAvatarHandGesture\_GripCube);
* a custom hand gesture built from an array of joint transforms, gAvatarRightHandTrans:

AvatarComponent-&gt;SetCustomGesture(ovrHand\_Right, gAvatarRightHandTrans, HAND\_JOINTS);
* a built-in pose depicting Touch controllers:

AvatarComponent-&gt;SetRightHandPose(ovrAvatarHandGesture\_Default); AvatarComponent-&gt;SetControllerVisibility(ovrHand\_Right, true);


The code snippets above from `LocalAvatar.cpp` set the poses for the right hand. For the left hand, substitute the appropriate left hand functions and constants.

## Detaching and Moving Hands Independent of Tracking

Press Y on the left Touch or press B on the right Touch to detach the avatar hands from Touch tracking. You can then use the thumbsticks to drive the avatar hand movements.

The following code in `LocalAvatar.cpp` detaches the hands:

```
AvatarHands[ovrHand_Right] = AvatarComponent-&gt;DetachHand(ovrHand_Right);
```

`ALocalAvatar::DriveHand` drives the hand movement after detaching.

## Adding Avatars to An Existing Project

Copy the `Plugins` folder to the root folder of your project. It contains our OvrAvatar plugin.

Update your project's `Config/DefaultInput.ini `file with content from the sample project's `Config/DefaultInput.ini` file.

Update the Modules and Plugins sections of your `.uproject `file with additional items. Remember to add a comma (,) to the last item in any existing Modules or Plugins sections before pasting the additional lines:

```
    "Modules": [
        {
            "AdditionalDependencies": [
                "Engine",
                "OnlineSubsystem",
                "OnlineSubsystemUtils"
            ]
        }
    ],
    "Plugins": [
        {
          "Name": "OnlineSubsystemOculus",
          "Enabled": true
        },
        {
            "Name": "OvrAvatar",
            "Enabled": true
        }
    ]
```

Update your project's `Config/DefaultEngine.ini` file with the following:

```
[OnlineSubsystem]
DefaultPlatformService=Oculus
        
[OnlineSubsystemOculus]
bEnabled=true
OculusAppId=YOUR_APP_ID
```

 Get **YOUR_APP_ID** from the Oculus Developer Dashboard: [https://dashboard.oculus.com](https://dashboard.oculus.com/)

In your code, the local user actor must implement the `SetupPlayerInputComponent` function, as the component needs controller input sent to it to animate the hands properly. A set of macros define these repetitive functions. Two things to consider are that:

*  the macros depend on the component member variable being named AvatarComponent
* it stubs out member functions for the Actor class.


You also need to replace the `ALocalAvatar::` entries with the name of your own Actor class.

```
// LocalAvatar.cpp
void ALocalAvatar::SetupPlayerInputComponent(UInputComponent* Input)
{
    Super::SetupPlayerInputComponent(Input);

#define INPUT_ENTRY(entry, hand, flag) \
    Input-&gt;BindAction(#entry, IE_Pressed, this, &amp;ALocalAvatar::##entry##_Pressed); \
    Input-&gt;BindAction(#entry, IE_Released, this, &amp;ALocalAvatar::##entry##_Released); 
    INPUT_COMMAND_TUPLE
#undef INPUT_ENTRY

#define AXIS_ENTRY(entry, hand, flag) \
    Input-&gt;BindAxis(#entry, this, &amp;ALocalAvatar::##entry##_Value);
        AXIS_INPUT_TUPLE
#undef AXIS_ENTRY

#define CUSTOM_ENTRY(entry, hand, field, invert) \
        Input-&gt;BindAxis(#entry, this, &amp;ALocalAvatar::##entry##_Value);
        CUSTOM_AXIS_TUPLE
#undef CUSTOM_ENTRY
}

#define CUSTOM_ENTRY(entry, hand, field, invert) \
        void ALocalAvatar::##entry##_Value(float value)  {  AvatarComponent-&gt;##entry##_Value(value); }
CUSTOM_AXIS_TUPLE
#undef CUSTOM_ENTRY


#define INPUT_ENTRY(entry, hand, flag) \
    void ALocalAvatar::##entry##_Pressed()  { AvatarComponent-&gt;##entry##_Pressed();}\
    void ALocalAvatar::##entry##_Released() {  AvatarComponent-&gt;##entry##_Released(); }
INPUT_COMMAND_TUPLE
#undef INPUT_ENTRY

#define AXIS_ENTRY(entry, hand, flag) \
    void ALocalAvatar::##entry##_Value( float value) { AvatarComponent-&gt;##entry##_Value(value); }
AXIS_INPUT_TUPLE
#undef AXIS_ENTRY
```

Note in `LocalAvatar.h` where these functions are declared:

```
private:

#define INPUT_ENTRY(entry, hand, flag) \
    void entry##_Pressed();\
    void entry##_Released();
    INPUT_COMMAND_TUPLE
#undef INPUT_ENTRY

#define AXIS_ENTRY(entry, hand, flag) \
    void entry##_Value( float value);
        AXIS_INPUT_TUPLE
#undef AXIS_ENTRY

#define CUSTOM_ENTRY(entry, hand, field, invert) \
    void entry##_Value( float value);
        CUSTOM_AXIS_TUPLE
#undef CUSTOM_ENTRY
```

Place your request to fetch the avatar wherever you have set up online login functionality. For example:

```
void ALocalAvatar::OnLoginComplete(int32 LocalUserNum, bool bWasSuccessful, const FUniqueNetId&amp; UserId, const FString&amp; Error)
{
    IOnlineIdentityPtr OculusIdentityInterface = Online::GetIdentityInterface();
    OculusIdentityInterface-&gt;ClearOnLoginCompleteDelegate_Handle(0, OnLoginCompleteDelegateHandle);

    if (AvatarComponent)
    {
        AvatarComponent-&gt;RequestAvatar(10149999027226798);
    }
}
```
