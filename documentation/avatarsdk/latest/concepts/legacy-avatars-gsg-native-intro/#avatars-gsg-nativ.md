---
title: Native C/C++ (Rift) Getting Started
---
Get started using Oculus Avatars in your own native Rift code by experimenting with our sample Visual Studio 2013 C++ solution.

## Download the Oculus Avatars SDK

The SDK is packaged in a .zip archive file on our developer website.

1. Download the Oculus Avatars SDK from [https://developer.oculus.com/downloads/package/oculus-avatar-sdk/](/downloads/package/oculus-avatar-sdk/).
2. Extract the contents of the .zip archive files to your local drive.
## OpenGL is Required

The current version of the Avatar SDK only contains OpenGL shaders.

## Running the Mirror Windows Sample on Microsoft Visual Studio 2013

Our Mirror Windows sample serves as a good foundation for implementing avatars in your own code. Let's take a tour of its features and its code.

To set up the Microsoft Visual Studio 2013 solution for our Mirror sample:

1. Download and install cmake from <https://cmake.org/download>.
2. In Windows Explorer, locate the OVRAvatarSDK\Samples\MirrorWindows folder and double-click generate\_projects.cmd.
3. Wait for the script to finish creating the VS2013 folder and solution.
4. Open and build the solution: Samples\MirrorWindows\VS2013\MirrorWindows.sln.
5. Press F5 to start debugging. 
## Key Bindings

The Mirror sample illustrates several features of the Avatar SDK by letting you toggle them:

Press...to...1show/hide the avatar body.2show/hide the hands.3show/hide the base cone.4show/hide the voice visualization.cshow/hide the Touch controllers.ffreeze/unfreeze the current hand pose.sset the hand pose to 'grip sphere'uset the hand pose to 'grip cube'jshow/hide the joint lines.rstart avatar packet recording. Press 'r' again to play recorded packets in a loop.## Exploring the Sample Code

Open Mirror.cpp file and follow along from main. Our tour explores only the portions of code specific to Oculus avatars.

## Rendering Avatars

We compile the Avatar vertex and fragment shaders for our regular shader and our physically based shader (PBS) using a helper function \_compileProgramFromFiles.

\_skinnedMeshProgram = \_compileProgramFromFiles("AvatarVertexShader.glsl", "AvatarFragmentShader.glsl", sizeof(errorBuffer), errorBuffer); ... \_skinnedMeshPBSProgram = \_compileProgramFromFiles("AvatarVertexShader.glsl", "AvatarFragmentShaderPBS.glsl", sizeof(errorBuffer), errorBuffer);### Retrieving Avatar Data From a User Profile

The appearance of every person's avatar is stored in his or her Oculus user profile as an Avatar Specification. The Avatar Specification identifies the meshes and textures that make up a person's avatar. Before we retrieve this specification data, we have to initialize both the Platform SDK and the Avatar SDK using our app ID. To get your own app ID, see the [Platform SDK Getting Started Guide](/documentation/platform/latest/concepts/book-pgsg/).

#define MIRROR\_SAMPLE\_APP\_ID "958062084316416" ... ovrPlatformInitializeWindows(MIRROR\_SAMPLE\_APP\_ID); ... ovrAvatar\_Initialize(MIRROR\_SAMPLE\_APP\_ID);Avatar Specifications are indexed by Oculus user ID. An app has easy access to the Oculus user ID of the currently logged in user.

Tip: If you wanted to create a social experience, you would write code to share user IDs between instances of your app so that you could load and render the appearance of other avatars too.ovrID userID = ovr\_GetLoggedInUserID(); ovrAvatar\_RequestAvatarSpecification(userID);The function ovrAvatar\_RequestAvatarSpecification() is asynchronous. We use a message queue to determine when the function has finished obtaining our data (ovrAvatarMessageType\_AvatarSpecification).

// Pump avatar messages while (ovrAvatarMessage* message = ovrAvatarMessage\_Pop()) { switch (ovrAvatarMessage\_GetType(message)) { case ovrAvatarMessageType\_AvatarSpecification: \_handleAvatarSpecification(ovrAvatarMessage\_GetAvatarSpecification(message)); break; case ovrAvatarMessageType\_AssetLoaded: \_handleAssetLoaded(ovrAvatarMessage\_GetAssetLoaded(message)); break; } ovrAvatarMessage\_Free(message); }With the Avatar Specification in hand, we then use our helper function \_handleAvatarSpecification to:

* Create an avatar instance (ovrAvatar\_Create).
* Load all the relevant avatar assets into that instance.
Loading avatar assets is also asynchronous and we again rely on popping our message queue to determine when an asset for an avatar has finished loading (ovrAvatarMessageType\_AssetLoaded).

static void \_handleAvatarSpecification(const ovrAvatarMessage\_AvatarSpecification* message) { // Create the avatar instance \_avatar = ovrAvatar\_Create(message->avatarSpec, ovrAvatarCapability\_All); // Trigger load operations for all of the assets referenced by the avatar uint32\_t refCount = ovrAvatar\_GetReferencedAssetCount(\_avatar); for (uint32\_t i = 0; i < refCount; ++i) { ovrAvatarAssetID id = ovrAvatar\_GetReferencedAsset(\_avatar, i); ovrAvatarAsset\_BeginLoading(id); ++\_loadingAssets; } printf("Loading %d assets...\r\n", \_loadingAssets); } static void \_handleAssetLoaded(const ovrAvatarMessage\_AssetLoaded* message) { // Determine the type of the asset that got loaded ovrAvatarAssetType assetType = ovrAvatarAsset\_GetType(message->asset); void* data = nullptr; // Call the appropriate loader function switch (assetType) { case ovrAvatarAssetType\_Mesh: data = \_loadMesh(ovrAvatarAsset\_GetMeshData(message->asset)); break; case ovrAvatarAssetType\_Texture: data = \_loadTexture(ovrAvatarAsset\_GetTextureData(message->asset)); break; } // Store the data that we loaded for the asset in the asset map \_assetMap[message->assetID] = data; --\_loadingAssets; printf("Loading %d assets...\r\n", \_loadingAssets); }### Rendering the Avatar

Our sample code is called Mirror and it calls the avatar rendering helper function \_renderAvatar() twice. The first call renders a first-person avatar. A first person avatar can depict the player's hands and world position. 

// If we have the avatar and have finished loading assets, render it if (\_avatar && !\_loadingAssets) { \_renderAvatar(\_avatar, ovrAvatarVisibilityFlag\_FirstPerson, view, proj, eyeWorld, renderJoints);The second call renders a third-person avatar, transformed so that it faces you as if looking in a mirror. A third-person avatar can depict hands, body, and base cone.

glm::vec4 reflectionPlane = glm::vec4(0.0, 0.0, -1.0, 0.0); glm::mat4 reflection = \_computeReflectionMatrix(reflectionPlane); glFrontFace(GL\_CW); \_renderAvatar(\_avatar, ovrAvatarVisibilityFlag\_ThirdPerson, view * reflection, proj, glm::vec3(reflection * glm::vec4(eyeWorld, 1.0f)), renderJoints); glFrontFace(GL\_CCW); }### Hiding and Displaying Avatar Capabilities

 When we first created our avatar instance, we created it with all capabilities active:

\_avatar = ovrAvatar\_Create(message->avatarSpec, ovrAvatarCapability\_All);You can enable different capabilities by calling ovrAvatar\_SetActiveCapabilities(). In our sample, we toggle different capabilities in real-time using the bit masks defined in ovrAvatarCapabilities:

case '1': capabilities ^= ovrAvatarCapability\_Body; ovrAvatar\_SetActiveCapabilities(\_avatar, static\_cast<ovrAvatarCapabilities>(capabilities)); break; case '2': capabilities ^= ovrAvatarCapability\_Hands; ovrAvatar\_SetActiveCapabilities(\_avatar, static\_cast<ovrAvatarCapabilities>(capabilities)); break; case '3': capabilities ^= ovrAvatarCapability\_Base; ovrAvatar\_SetActiveCapabilities(\_avatar, static\_cast<ovrAvatarCapabilities>(capabilities)); break; case '4': capabilities ^= ovrAvatarCapability\_Voice; ovrAvatar\_SetActiveCapabilities(\_avatar, static\_cast<ovrAvatarCapabilities>(capabilities)); break;## Translating Touch Controllers To Avatar Movements

Our sample code translates Touch controller input into Avatar movements in two parts:

1. Processing the Touch inputs
2. Updating the Avatar
### Processing the Touch Controller Inputs

We translate the position and orientation of the head-mounted display and the left and right Touch controllers to avatar body and hand positions using our helper function \_ovrAvatarTransformFromGlm().

We call our helper function \_ovrAvatarHandInputStateFromOvr() to translate the various Touch button, trigger, and touch states.

// Convert the OVR inputs into Avatar SDK inputs ovrInputState touchState; ovr\_GetInputState(ovr, ovrControllerType\_Active, &touchState); ovrTrackingState trackingState = ovr\_GetTrackingState(ovr, 0.0, false); glm::vec3 hmdP = \_glmFromOvrVector(trackingState.HeadPose.ThePose.Position); glm::quat hmdQ = \_glmFromOvrQuat(trackingState.HeadPose.ThePose.Orientation); glm::vec3 leftP = \_glmFromOvrVector(trackingState.HandPoses[ovrHand\_Left].ThePose.Position); glm::quat leftQ = \_glmFromOvrQuat(trackingState.HandPoses[ovrHand\_Left].ThePose.Orientation); glm::vec3 rightP = \_glmFromOvrVector(trackingState.HandPoses[ovrHand\_Right].ThePose.Position); glm::quat rightQ = \_glmFromOvrQuat(trackingState.HandPoses[ovrHand\_Right].ThePose.Orientation); ovrAvatarTransform hmd; \_ovrAvatarTransformFromGlm(hmdP, hmdQ, glm::vec3(1.0f), &hmd); ovrAvatarTransform left; \_ovrAvatarTransformFromGlm(leftP, leftQ, glm::vec3(1.0f), &left); ovrAvatarTransform right; \_ovrAvatarTransformFromGlm(rightP, rightQ, glm::vec3(1.0f), &right); ovrAvatarHandInputState inputStateLeft; \_ovrAvatarHandInputStateFromOvr(left, touchState, ovrHand\_Left, &inputStateLeft); ovrAvatarHandInputState inputStateRight; \_ovrAvatarHandInputStateFromOvr(right, touchState, ovrHand\_Right, &inputStateRight);### Updating the Avatar

Everything that can be changed has a related update function in the SDK. Our helper function \_updateAvatar() calls the individual pose update functions:

ovrAvatarPose\_UpdateBody(avatar, hmd); ovrAvatarPose\_UpdateHands(avatar, left, right);It also closes the update by finalizing the updates to the avatar's pose with a timestamp deltaSeconds. This timestamp is used for avatar playback and recording as discussed in [Pose Recording and Playback](/documentation/avatarsdk/latest/concepts/avatars-sdk-native-intro/#avatars-sdk-native-recording).

ovrAvatarPose\_Finalize(avatar, deltaSeconds);