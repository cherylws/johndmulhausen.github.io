---
title: Adding C++ Avatar Support
---
This guide outlines Avatar SDK support with a C/C++ game engine or application. The source code samples used in this guide are taken from the Mirror demo, available in OVRAvatarSDK\Samples\Mirror.

To add Avatar support to your Visual C++ project:

1. Add Oculus Platform Support to your Project. ([https://developer.oculus.com/documentation/platform/latest/concepts/pgsg-native-gsg/](/documentation/platform/latest/concepts/pgsg-native-gsg/))
2. Open the project's **Properties > Configuration Properties > VC++ Directories ** page.
3. In **Include Directories**, add the location of the Avatar SDK includes folder (*InstallFolder*\include).
4. In **Library Directories**, add the location of the Avatar SDK library folder (*InstallFolder*\Windows).
5. Add the Avatar library file as linker input: 
	1. Expand **Linker > Input.**
	2. In **Additional Dependencies**, add *InstallFolder*\Windows\libovravatar.lib.
	
6. Add #include <OVR\_Avatar.h> and #include <OVR\_Platform.h>.
7. Initialize the Platform module using your app ID through ovr\_PlatformInitializeWindows(appID)
8. Initialize the Oculus SDK through ovr\_Initialize.
9. Compile the Oculus Avatar OpenGL fragment and vertex reference shader into a shader program.
10. Initialize the Avatar module through ovrAvatar\_Initialize(appID).
## Avatar Message Queue

The functions ovrAvatar\_RequestAvatarSpecification() and ovrAvatarAsset\_BeginLoading() are asynchronous. The avatar message queue contains the results of these operations. 

You can retrieve the most recent message with ovrAvatarMessage\_Pop(). After you finish processing a message on the queue, be sure to call ovrAvatarMessage\_Free() to free up the memory used by the pop.

## Rendering Avatar Components

Avatars are composed of avatar components (body, base, hands, controller) which are themselves composed of render parts. Each Oculus user has an Avatar Specification that indicates the mesh and texture assets that need to be loaded to recreate the avatar.

Our Mirror.cpp example code contains good examples of the entire process and includes helper functions, prefixed with \_, that we have written to make it easier to render complete avatars. 

The complete process goes something like this:

1. Retrieve the avatar specification for the Oculus user. ovrAvatar\_RequestAvatarSpecification(userID);
2. Set the Avatar capabilities. ovrAvatar\_Create(message->avatarSpec, ovrAvatarCapability\_All);
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

ovrAvatar\_SetLeftControllerVisibility(\_avatar, 0); ovrAvatar\_SetRightControllerVisibility(\_avatar, 0); To render avatar hands with controllers:

ovrAvatar\_SetLeftControllerVisibility(\_avatar, 1); ovrAvatar\_SetRightControllerVisibility(\_avatar, 1);**Gear VR Applications**

When using the VrAppFramework there is a bone count limitation which makes us unable to render hands, so you can only render the controller model.

After you've created the avatar, turn off the hands:

ovrAvatar\_SetLeftHandVisibility( sAvatar, false ); ovrAvatar\_SetRightHandVisibility( sAvatar, false );Then, turn on the controller visibility:

ovrAvatar\_SetRightControllerVisibility( sAvatar, true ); ovrAvatar\_SetLeftControllerVisibility( sAvatar, true );In your file that manages the Avatar:

void AvatarManager::UpdateTrackedControllerInputState( const ovrPosef& headPose, const ovrInputStateTrackedRemote& remoteInputState, const ovrTracking& trackingState, const ovrInputTrackedRemoteCapabilities& capabilities, const bool isActive )Finally, see the [VrApi Input API](/documentation/mobilesdk/latest/concepts/mobile-vrapi-input-api/) for information about detecting and sampling the controller properly.

### Setting a Custom Touch Grip Pose

You can pass your own custom transforms to the hand pose functions or use our cube and sphere preset hand poses. Here is an example of a custom pose made from freezing the hands in their current pose:

const ovrAvatarHandComponent* handComp = ovrAvatarPose\_GetLeftHandComponent(\_avatar); const ovrAvatarComponent* comp = handComp->renderComponent; const ovrAvatarRenderPart* renderPart = comp->renderParts[0]; const ovrAvatarRenderPart\_SkinnedMeshRender* meshRender = ovrAvatarRenderPart\_GetSkinnedMeshRender(renderPart); ovrAvatar\_SetLeftHandCustomGesture(\_avatar, meshRender->skinnedPose.jointCount, meshRender->skinnedPose.jointTransform); handComp = ovrAvatarPose\_GetRightHandComponent(\_avatar); comp = handComp->renderComponent; renderPart = comp->renderParts[0]; meshRender = ovrAvatarRenderPart\_GetSkinnedMeshRender(renderPart); ovrAvatar\_SetRightHandCustomGesture(\_avatar, meshRender->skinnedPose.jointCount, meshRender->skinnedPose.jointTransform);To pose the hands as if to grip cubes:

ovrAvatar\_SetLeftHandGesture(\_avatar, ovrAvatarHandGesture\_GripCube); ovrAvatar\_SetRightHandGesture(\_avatar, ovrAvatarHandGesture\_GripCube);To pose the hands as if to grip spheres:

ovrAvatar\_SetLeftHandGesture(\_avatar, ovrAvatarHandGesture\_GripSphere); ovrAvatar\_SetRightHandGesture(\_avatar, ovrAvatarHandGesture\_GripSphere); To unfreeze the hand poses:

ovrAvatar\_SetLeftHandGesture(\_avatar, ovrAvatarHandGesture\_Default); ovrAvatar\_SetRightHandGesture(\_avatar, ovrAvatarHandGesture\_Default);## Voice Visualization

Voice visualization is an avatar component. It is created as a projection on top of an existing mesh.

Create the microphone:

ovrMicrophoneHandle mic = ovr\_Microphone\_Create(); if (mic) { ovr\_Microphone\_Start(mic); }Pass an array of voice samples to ovrAvatarPose\_UpdateVoiceVisualization().

float micSamples[48000]; size\_t sampleCount = ovr\_Microphone\_ReadData(mic, micSamples, sizeof(micSamples) / sizeof(micSamples[0])); if (sampleCount > 0) { ovrAvatarPose\_UpdateVoiceVisualization(\_avatar, (uint32\_t)sampleCount, micSamples); }The render parts of the voice visualization component are a ProjectorRender type.

## Pose Recording and Playback

The Avatar SDK contains a complete avatar pose recording and playback system. You can save pose data to packets at regular intervals and then transmit these packets to a remote computer to drive the avatar poses there.

### Pose Recording

Call ovrAvatarPacket\_BeginRecording()  to begin recording 

ovrAvatarPacket\_BeginRecording(\_avatar); After you record as many frames worth of pose changes you want, stop the recording with ovrAvatarPacket\_EndRecording() and then write your packet out with ovrAvatarPacket\_Write().

ovrAvatarPacket* recordedPacket = ovrAvatarPacket\_EndRecording(\_avatar); // Write the packet to a byte buffer to exercise the packet writing code uint32\_t packetSize = ovrAvatarPacket\_GetSize(recordedPacket); uint8\_t* packetBuffer = (uint8\_t*)malloc(packetSize); ovrAvatarPacket\_Write(recordedPacket, packetSize, packetBuffer); ovrAvatarPacket\_Free(recordedPacket);Transmit your data to your destination using your own network code.

### Pose Playback

To read your pose data back into packets:

// Read the buffer back into a packet playbackPacket = ovrAvatarPacket\_Read(packetSize, packetBuffer); free(packetBuffer);To play the packets back:

float packetDuration = ovrAvatarPacket\_GetDurationSeconds(packet); *packetPlaybackTime += deltaSeconds; if (*packetPlaybackTime > packetDuration) { ovrAvatarPose\_Finalize(avatar, 0.0f); *packetPlaybackTime = 0; } ovrAvatar\_UpdatePoseFromPacket(avatar, packet, *packetPlaybackTime);The playback routine uses the timestamp deltaSeconds to interpolate a tween pose in case the frames on the remote computer are offset by a different amount.

