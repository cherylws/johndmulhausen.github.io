---
title: Adding C++ Avatar Support
---

This guide outlines Avatar SDK support with a C/C++ game engine or application. The source code samples used in this guide are taken from the Mirror demo, available in `OVRAvatarSDK\Samples\Mirror`.

To add Avatar support to your Visual C++ project:

1. Add Oculus Platform Support to your Project. (&lt;https://developer.oculus.com/documentation/platform/latest/concepts/pgsg-native-gsg/&gt;)
2. Open the project's **Properties &gt; Configuration Properties &gt; VC++ Directories ** page.
3. In **Include Directories**, add the location of the Avatar SDK includes folder (*InstallFolder*\include).
4. In **Library Directories**, add the location of the Avatar SDK library folder (*InstallFolder*\Windows).
5. Add the Avatar library file as linker input: 
	1. Expand **Linker &gt; Input.**
	2. In **Additional Dependencies**, add *InstallFolder*\Windows\libovravatar.lib.
	
6. Add #include &lt;OVR\_Avatar.h&gt; and #include &lt;OVR\_Platform.h&gt;.
7. Initialize the Platform module using your app ID through ovr\_PlatformInitializeWindows(appID)
8. Initialize the Oculus SDK through ovr\_Initialize.
9. Compile the Oculus Avatar OpenGL fragment and vertex reference shader into a shader program.
10. Initialize the Avatar module through ovrAvatar\_Initialize(appID).


## Avatar Message Queue

The functions `ovrAvatar_RequestAvatarSpecification()` and `ovrAvatarAsset_BeginLoading()` are asynchronous. The avatar message queue contains the results of these operations. 

You can retrieve the most recent message with `ovrAvatarMessage_Pop()`. After you finish processing a message on the queue, be sure to call `ovrAvatarMessage_Free()` to free up the memory used by the pop.

## Rendering Avatar Components

Avatars are composed of avatar components (body, base, hands, controller) which are themselves composed of render parts. Each Oculus user has an Avatar Specification that indicates the mesh and texture assets that need to be loaded to recreate the avatar.

Our `Mirror.cpp` example code contains good examples of the entire process and includes helper functions, prefixed with `_`, that we have written to make it easier to render complete avatars. 

The complete process goes something like this:

1. Retrieve the avatar specification for the Oculus user. ovrAvatar\_RequestAvatarSpecification(userID);
2. Set the Avatar capabilities. ovrAvatar\_Create(message-&gt;avatarSpec, ovrAvatarCapability\_All);
3. Iterate through the avatar specification to load the static avatar assets (mesh and textures) into the avatar. ovrAvatar\_GetReferencedAsset(\_avatar);
4. Apply the vertex transforms to determine the position of the avatar component.
5. Apply the material states to determine the appearance of the avatar component.
6. For each render part of an avatar component: 
	1. Get the OpenGL mesh data and tell the renderer to use the Avatar shader program you compiled earlier.
	2. Calculate the inputs on the vertex uniforms.
	3. Set the view position, the world matrix, the view matrix, and the array of mesh poses.
	4. Transform everything in the joint hierarchy.
	5. Set the material state.
	6. Draw the mesh, depth first so that it self-occludes.
	7. Render to the color buffer.
	
7. When there are no more components to render, the avatar render is complete.


### Rendering Controllers

You can render Touch and Gear VR Controllers with the user's Avatar.

**Rift Applications**

To render avatar hands without controllers:

```
ovrAvatar_SetLeftControllerVisibility(_avatar, 0);
ovrAvatar_SetRightControllerVisibility(_avatar, 0);
```

 To render avatar hands with controllers:

```
ovrAvatar_SetLeftControllerVisibility(_avatar, 1);
ovrAvatar_SetRightControllerVisibility(_avatar, 1);
```

**Gear VR Applications**

When using the VrAppFramework there is a bone count limitation which makes us unable to render hands, so you can only render the controller model.

After you've created the avatar, turn off the hands:

```
ovrAvatar_SetLeftHandVisibility( sAvatar, false );
ovrAvatar_SetRightHandVisibility( sAvatar, false );
```

Then, turn on the controller visibility:

```
ovrAvatar_SetRightControllerVisibility( sAvatar, true );
ovrAvatar_SetLeftControllerVisibility( sAvatar, true );
```

In your file that manages the Avatar:

```
void AvatarManager::UpdateTrackedControllerInputState( 
        const ovrPosef&amp; headPose,
        const ovrInputStateTrackedRemote&amp; remoteInputState, 
        const ovrTracking&amp; trackingState,
        const ovrInputTrackedRemoteCapabilities&amp; capabilities,
        const bool isActive )
```

Finally, see the [VrApi Input API](/documentation/mobilesdk/latest/concepts/mobile-vrapi-input-api/) for information about detecting and sampling the controller properly.

### Setting a Custom Touch Grip Pose

You can pass your own custom transforms to the hand pose functions or use our cube and sphere preset hand poses. Here is an example of a custom pose made from freezing the hands in their current pose:

```
const ovrAvatarHandComponent* handComp =
    ovrAvatarPose_GetLeftHandComponent(_avatar);
const ovrAvatarComponent* comp = handComp-&gt;renderComponent;
const ovrAvatarRenderPart* renderPart = comp-&gt;renderParts[0];
const ovrAvatarRenderPart_SkinnedMeshRender* meshRender =
    ovrAvatarRenderPart_GetSkinnedMeshRender(renderPart);
ovrAvatar_SetLeftHandCustomGesture(_avatar,
    meshRender-&gt;skinnedPose.jointCount,
    meshRender-&gt;skinnedPose.jointTransform);
handComp =
    ovrAvatarPose_GetRightHandComponent(_avatar);
comp = handComp-&gt;renderComponent;
renderPart = comp-&gt;renderParts[0];
meshRender = ovrAvatarRenderPart_GetSkinnedMeshRender(renderPart);
ovrAvatar_SetRightHandCustomGesture(_avatar,
    meshRender-&gt;skinnedPose.jointCount,
    meshRender-&gt;skinnedPose.jointTransform);
```

To pose the hands as if to grip cubes:

```
ovrAvatar_SetLeftHandGesture(_avatar, ovrAvatarHandGesture_GripCube);
ovrAvatar_SetRightHandGesture(_avatar, ovrAvatarHandGesture_GripCube);
```

To pose the hands as if to grip spheres:

```
ovrAvatar_SetLeftHandGesture(_avatar, ovrAvatarHandGesture_GripSphere);
ovrAvatar_SetRightHandGesture(_avatar, ovrAvatarHandGesture_GripSphere);
```

 To unfreeze the hand poses:

```
ovrAvatar_SetLeftHandGesture(_avatar, ovrAvatarHandGesture_Default);
ovrAvatar_SetRightHandGesture(_avatar, ovrAvatarHandGesture_Default);
```

## Voice Visualization



Voice visualization is an avatar component. It is created as a projection on top of an existing mesh.

Create the microphone:

```
ovrMicrophoneHandle mic = ovr_Microphone_Create();
        if (mic)
        {
        ovr_Microphone_Start(mic);
        }
```

Pass an array of voice samples to `ovrAvatarPose_UpdateVoiceVisualization()`.

```
float micSamples[48000];
      size_t sampleCount = ovr_Microphone_ReadData(mic, micSamples, sizeof(micSamples) / sizeof(micSamples[0]));
      if (sampleCount &gt; 0)
      {
      ovrAvatarPose_UpdateVoiceVisualization(_avatar, (uint32_t)sampleCount, micSamples);
      }
```

The render parts of the voice visualization component are a ProjectorRender type.

## Pose Recording and Playback



The Avatar SDK contains a complete avatar pose recording and playback system. You can save pose data to packets at regular intervals and then transmit these packets to a remote computer to drive the avatar poses there.

### Pose Recording

Call `ovrAvatarPacket_BeginRecording() ` to begin recording 

```
ovrAvatarPacket_BeginRecording(_avatar);
```

 After you record as many frames worth of pose changes you want, stop the recording with `ovrAvatarPacket_EndRecording()` and then write your packet out with `ovrAvatarPacket_Write()`.

```
ovrAvatarPacket* recordedPacket = ovrAvatarPacket_EndRecording(_avatar);
// Write the packet to a byte buffer to exercise the packet writing code
uint32_t packetSize = ovrAvatarPacket_GetSize(recordedPacket);
uint8_t* packetBuffer = (uint8_t*)malloc(packetSize);
ovrAvatarPacket_Write(recordedPacket, packetSize, packetBuffer);
ovrAvatarPacket_Free(recordedPacket);
```

Transmit your data to your destination using your own network code.

### Pose Playback

To read your pose data back into packets:

```
// Read the buffer back into a packet
playbackPacket = ovrAvatarPacket_Read(packetSize, packetBuffer);
free(packetBuffer);
```

To play the packets back:

```
float packetDuration = ovrAvatarPacket_GetDurationSeconds(packet);
*packetPlaybackTime += deltaSeconds;
if (*packetPlaybackTime &gt; packetDuration)
{
    ovrAvatarPose_Finalize(avatar, 0.0f);
    *packetPlaybackTime = 0;
}
ovrAvatar_UpdatePoseFromPacket(avatar, packet, *packetPlaybackTime);
```

The playback routine uses the timestamp `deltaSeconds` to interpolate a tween pose in case the frames on the remote computer are offset by a different amount.
