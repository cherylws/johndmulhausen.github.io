---
title: Native C/C++ (Rift) Getting Started
---

Get started using Oculus Avatars in your own native Rift code by experimenting with our sample Visual Studio 2013 C++ solution.

## Download the Oculus Avatars SDK

The SDK is packaged in a .zip archive file on our developer website.

1. Download the Oculus Avatars SDK from &lt;https://developer.oculus.com/downloads/package/oculus-avatar-sdk/&gt;.
2. Extract the contents of the .zip archive files to your local drive.


## OpenGL is Required

The current version of the Avatar SDK only contains OpenGL shaders.

## Running the Mirror Sample on Microsoft Visual Studio 2013

Our Mirror sample serves as a good foundation for implementing avatars in your own code. Let's take a tour of its features and its code.

To set up the Microsoft Visual Studio 2013 solution for our Mirror sample:

1. Download and install cmake from &lt;https://cmake.org/download&gt;.
2. In Windows Explorer, locate the OVRAvatarSDK\Samples folder and double-click generate\_projects.cmd.
3. Wait for the script to finish creating the VS2013 folder and solution.
4. Open and build the solution: Samples\VS2013\Mirror.sln.
5. Press F5 to start debugging. 


## Key Bindings

The Mirror sample illustrates several features of the Avatar SDK by letting you toggle them:

| Press... |                                       to...                                       |
|----------|------------------------------------------------------------------------------------|
|    1    |                             show/hide the avatar body.                             |
|    2    |                                show/hide the hands.                                |
|    3    |                              show/hide the base cone.                              |
|    4    |                         show/hide the voice visualization.                         |
|    c    |                          show/hide the Touch controllers.                          |
|    f    |                       freeze/unfreeze the current hand pose.                       |
|    s    |                         set the hand pose to 'grip sphere'                         |
|    u    |                          set the hand pose to 'grip cube'                          |
|    j    |                             show/hide the joint lines.                             |
|    r    | start avatar packet recording. Press 'r' again to play recorded packets in a loop. |

## Exploring the Sample Code

Open `Mirror.cpp` file and follow along from `main`. Our tour explores only the portions of code specific to Oculus avatars.

## Rendering Avatars



We compile the Avatar vertex and fragment shaders for our regular shader and our physically based shader (PBS) using a helper function `_compileProgramFromFiles`.

```
_skinnedMeshProgram = _compileProgramFromFiles("AvatarVertexShader.glsl", "AvatarFragmentShader.glsl", sizeof(errorBuffer), errorBuffer);
...
_skinnedMeshPBSProgram = _compileProgramFromFiles("AvatarVertexShader.glsl", "AvatarFragmentShaderPBS.glsl", sizeof(errorBuffer), errorBuffer);
```

### Retrieving Avatar Data From a User Profile

The appearance of every person's avatar is stored in his or her Oculus user profile as an Avatar Specification. The Avatar Specification identifies the meshes and textures that make up a person's avatar. Before we retrieve this specification data, we have to initialize both the Platform SDK and the Avatar SDK using our app ID. To get your own app ID, see the [Platform SDK Getting Started Guide](/documentation/platform/latest/concepts/book-pgsg/).

```
#define MIRROR_SAMPLE_APP_ID "958062084316416"
...
ovrPlatformInitializeWindows(MIRROR_SAMPLE_APP_ID);
...
ovrAvatar_Initialize(MIRROR_SAMPLE_APP_ID);
```

Avatar Specifications are indexed by Oculus user ID. An app has easy access to the Oculus user ID of the currently logged in user.

```
ovrID userID = ovr_GetLoggedInUserID();
ovrAvatar_RequestAvatarSpecification(userID);
```

The function `ovrAvatar_RequestAvatarSpecification()` is asynchronous. We use a message queue to determine when the function has finished obtaining our data (`ovrAvatarMessageType_AvatarSpecification`).

```
// Pump avatar messages
        while (ovrAvatarMessage* message = ovrAvatarMessage_Pop())
        {
            switch (ovrAvatarMessage_GetType(message))
            {
                case ovrAvatarMessageType_AvatarSpecification:
                    _handleAvatarSpecification(ovrAvatarMessage_GetAvatarSpecification(message));
                    break;
                case ovrAvatarMessageType_AssetLoaded:
                    _handleAssetLoaded(ovrAvatarMessage_GetAssetLoaded(message));
                    break;
            }
            ovrAvatarMessage_Free(message);
        }
```

With the Avatar Specification in hand, we then use our helper function `_handleAvatarSpecification` to:

* Create an avatar instance (ovrAvatar\_Create).
* Load all the relevant avatar assets into that instance.


Loading avatar assets is also asynchronous and we again rely on popping our message queue to determine when an asset for an avatar has finished loading (`ovrAvatarMessageType_AssetLoaded`).

```
static void _handleAvatarSpecification(const ovrAvatarMessage_AvatarSpecification* message)
{
    // Create the avatar instance
    _avatar = ovrAvatar_Create(message-&gt;avatarSpec, ovrAvatarCapability_All);

    // Trigger load operations for all of the assets referenced by the avatar
    uint32_t refCount = ovrAvatar_GetReferencedAssetCount(_avatar);
    for (uint32_t i = 0; i &lt; refCount; ++i)
    {
        ovrAvatarAssetID id = ovrAvatar_GetReferencedAsset(_avatar, i);
        ovrAvatarAsset_BeginLoading(id);
        ++_loadingAssets;
    }
    printf("Loading %d assets...\r\n", _loadingAssets);
}

static void _handleAssetLoaded(const ovrAvatarMessage_AssetLoaded* message)
{
    // Determine the type of the asset that got loaded
    ovrAvatarAssetType assetType = ovrAvatarAsset_GetType(message-&gt;asset);
    void* data = nullptr;

    // Call the appropriate loader function
    switch (assetType)
    {
    case ovrAvatarAssetType_Mesh:
        data = _loadMesh(ovrAvatarAsset_GetMeshData(message-&gt;asset));
        break;
    case ovrAvatarAssetType_Texture:
        data = _loadTexture(ovrAvatarAsset_GetTextureData(message-&gt;asset));
        break;
    }

    // Store the data that we loaded for the asset in the asset map
    _assetMap[message-&gt;assetID] = data;
    --_loadingAssets;
    printf("Loading %d assets...\r\n", _loadingAssets);
}
```

### Rendering the Avatar

Our sample code is called Mirror and it calls the avatar rendering helper function `_renderAvatar()` twice. The first call renders a first-person avatar. A first person avatar can depict the player's hands and world position. 

```
// If we have the avatar and have finished loading assets, render it
if (_avatar &amp;&amp; !_loadingAssets)
{
    _renderAvatar(_avatar, ovrAvatarVisibilityFlag_FirstPerson, view, proj, eyeWorld, renderJoints);
```

The second call renders a third-person avatar, transformed so that it faces you as if looking in a mirror. A third-person avatar can depict hands, body, and base cone.

```
glm::vec4 reflectionPlane = glm::vec4(0.0, 0.0, -1.0, 0.0);
    glm::mat4 reflection = _computeReflectionMatrix(reflectionPlane);

    glFrontFace(GL_CW);
    _renderAvatar(_avatar, ovrAvatarVisibilityFlag_ThirdPerson, view * reflection, proj, glm::vec3(reflection * glm::vec4(eyeWorld, 1.0f)), renderJoints);
    glFrontFace(GL_CCW);
}
```

### Hiding and Displaying Avatar Capabilities

 When we first created our avatar instance, we created it with all capabilities active:

```
_avatar = ovrAvatar_Create(message-&gt;avatarSpec, ovrAvatarCapability_All);
```

You can enable different capabilities by calling `ovrAvatar_SetActiveCapabilities()`. In our sample, we toggle different capabilities in real-time using the bit masks defined in `ovrAvatarCapabilities`:

```
case '1':
    capabilities ^= ovrAvatarCapability_Body;
    ovrAvatar_SetActiveCapabilities(_avatar, static_cast&lt;ovrAvatarCapabilities&gt;(capabilities));
    break;
case '2':
    capabilities ^= ovrAvatarCapability_Hands;
    ovrAvatar_SetActiveCapabilities(_avatar, static_cast&lt;ovrAvatarCapabilities&gt;(capabilities));
    break;
case '3':
    capabilities ^= ovrAvatarCapability_Base;
    ovrAvatar_SetActiveCapabilities(_avatar, static_cast&lt;ovrAvatarCapabilities&gt;(capabilities));
    break;
case '4':
    capabilities ^= ovrAvatarCapability_Voice;
    ovrAvatar_SetActiveCapabilities(_avatar, static_cast&lt;ovrAvatarCapabilities&gt;(capabilities));
    break;
```

## Translating Touch Controllers To Avatar Movements



Our sample code translates Touch controller input into Avatar movements in two parts:

1. Processing the Touch inputs
2. Updating the Avatar


### Processing the Touch Controller Inputs

We translate the position and orientation of the head-mounted display and the left and right Touch controllers to avatar body and hand positions using our helper function `_ovrAvatarTransformFromGlm()`.

We call our helper function `_ovrAvatarHandInputStateFromOvr()` to translate the various Touch button, trigger, and touch states.

```
// Convert the OVR inputs into Avatar SDK inputs
ovrInputState touchState;
ovr_GetInputState(ovr, ovrControllerType_Active, &amp;touchState);
ovrTrackingState trackingState = ovr_GetTrackingState(ovr, 0.0, false);
                
glm::vec3 hmdP = _glmFromOvrVector(trackingState.HeadPose.ThePose.Position);
glm::quat hmdQ = _glmFromOvrQuat(trackingState.HeadPose.ThePose.Orientation);
glm::vec3 leftP = _glmFromOvrVector(trackingState.HandPoses[ovrHand_Left].ThePose.Position);
glm::quat leftQ = _glmFromOvrQuat(trackingState.HandPoses[ovrHand_Left].ThePose.Orientation);
glm::vec3 rightP = _glmFromOvrVector(trackingState.HandPoses[ovrHand_Right].ThePose.Position);
glm::quat rightQ = _glmFromOvrQuat(trackingState.HandPoses[ovrHand_Right].ThePose.Orientation);

ovrAvatarTransform hmd;
_ovrAvatarTransformFromGlm(hmdP, hmdQ, glm::vec3(1.0f), &amp;hmd);

ovrAvatarTransform left;
_ovrAvatarTransformFromGlm(leftP, leftQ, glm::vec3(1.0f), &amp;left);

ovrAvatarTransform right;
_ovrAvatarTransformFromGlm(rightP, rightQ, glm::vec3(1.0f), &amp;right);

ovrAvatarHandInputState inputStateLeft;
_ovrAvatarHandInputStateFromOvr(left, touchState, ovrHand_Left, &amp;inputStateLeft);

ovrAvatarHandInputState inputStateRight;
_ovrAvatarHandInputStateFromOvr(right, touchState, ovrHand_Right, &amp;inputStateRight);
```

### Updating the Avatar

Everything that can be changed has a related update function in the SDK. Our helper function `_updateAvatar()` calls the individual pose update functions:

```
ovrAvatarPose_UpdateBody(avatar, hmd);
ovrAvatarPose_UpdateHands(avatar, left, right);
```

It also closes the update by finalizing the updates to the avatar's pose with a timestamp `deltaSeconds`. This timestamp is used for avatar playback and recording as discussed in [Pose Recording and Playback](/documentation/avatarsdk/latest/concepts/avatars-sdk-native-intro/#avatars-sdk-native-recording).

```
ovrAvatarPose_Finalize(avatar, deltaSeconds);
```
