---
title: Unreal Samples
---

Oculus provides samples which illustrate basic VR concepts in Unreal such as Touch, haptics, and the Boundary Component API for interacting with the Guardian System. 

Samples are available from the [Oculus Unreal GitHub repository](https://github.com/Oculus-VR/UnrealEngine). To access this repository, **you must** be subscribed to the private EpicGames/UnrealEngine repository (see [https://www.unrealengine.com/ue4-on-github](https://www.unrealengine.com/ue4-on-github) for details). An Unreal license is not required.

All samples require a compatible version of the Unreal Engine which supports the illustrated features. To explore samples, we generally recommend using Unreal versions that we ship from our GitHub repository, which always include the latest features. For a review of which Unreal versions support which features, see [Unreal Game Engine](/documentation/unreal/latest/concepts/unreal-engine/).

## Boundary Sample

BoundarySample is a Blueprint sample that illustrates the use of the [Boundary Component API](/documentation/unreal/latest/concepts/unreal-boundary/) for interacting with our Guardian System. The Guardian System is only available on the Oculus Rift. This API allows developers to query the Guardian System trigger state, return the closest boundary point to a queried device or point, and more.

In this sample, the Guardian System Boundary Area is visualized on the ground in orange-yellow, and the Play Area is visualized on the ground in purple.

Two spheres track the Touch controllers. When they approach the Boundary Area, they project a colored arrow toward the nearest sample point in the Guardian Area.

![](/images/documentationunreallatestconceptsunreal-samples-0.png)

NewGameMode and VRCharacter are used to initialize the scene and make the scene display at the appropriate height, and so forth.

Controls and Behavior

These behaviors are controlled by the BoundarySampleMap, which you can use as a reference for implementing related functionality.

|              Test              |                                                Control or Behavior                                                |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------|
|  RequestOuterBoundaryVisible()  |   Press 'V' on keyboard/right Touch button A to request boundary on. Press 'X'/right Touch button B to cancel.   |
|     SetOuterBoundaryColor()     | Press 'G' on keyboard/left Touch button X to set boundary to green. Press 'P'/left Touch button Y to make purple. |
|   IsOuterBoundaryDisplayed()   |                                          If so, cylinder is not visible.                                          |
|   IsOuterBoundaryTriggered()   |          If so, cone is not visible (cone should remain if boundaries are requested on by application).          |
| GetTriggeredOuterBoundaryInfo() |                                                Visualize normals.                                                |
|   GetTriggeredPlayAreaInfo()   |                                                Visualize normals.                                                |
| OnOuterBoundaryTriggered Event |                                                Cube made visible.                                                |
|  OnOuterBoundaryReturned Event  |                                               Cube made invisible.                                               |

## Layer Sample

LayerSample is a Blueprint sample that illustrates the use of [VR Compositor Layers](/documentation/unreal/latest/concepts/unreal-overlay/) to display a [UMG UI](https://docs.unrealengine.com/latest/INT/Engine/UMG/UserGuide/).

This sample includes two spheres that track with the Touch controllers and two UMG widgets rendered as VR Compositor layers. One is rendered as a quad layer and the other as a cylinder layer.

Actor_Blueprint illustrates rendering a UMG widget into a stereo layer. The widget is first rendered into a Material, then the SlateUI texture is pulled from the Material into the stereo layer. This is the UMG widget that is rendered to the quad and cylindrical layers in the sample.

Open MenuBlueprint to open the UMG widget in the [UMG Editor](https://docs.unrealengine.com/latest/INT/Engine/UMG/UserGuide/WidgetBlueprints/index.html). 

NewGameMode and VRCharacter are used to initialize the scene and make the scene display at the appropriate height, and so forth.

## Input Samples

The Oculus GitHub repo includes two samples illustrating input in Oculus/Samples. The Gear VR Controller illustrates tracking and input for the Oculus Go Controller and Gear VR Controller - open the Level Blueprint to see a typical implementation.

The Touch sample illustrates tracking, thumbstick control, and [haptics](/documentation/unreal/latest/concepts/unreal-haptics/) control using PlayHapticEffect() and PlayHapticSoundWave(). Two spheres track with the Touch controllers. The right controller thumbstick may be used to control the position of the light gray box. Touch capacitance sensors detect whether the right thumb is in a touch or near-touch position, which controls the height of the box. Press and hold the left Touch grip button to play a haptics clip. Press and hold the left Touch X button to create a haptics effect by setting the haptics value directly.

![](/images/documentationunreallatestconceptsunreal-samples-1.png)

You will find the Haptics control Blueprint and the Thumbstick control Blueprint in the Touch sample Level Blueprint. NewGameMode and VRCharacter are used to initialize the scene and make the scene display at the appropriate height, and so forth.

## Mixed Reality Capture Sample

A trivial sample map with mixed reality capture enabled is available in our GitHub repository (access instructions [here](/documentation/unreal/latest/concepts/unreal-engine/)) in Samples/Oculus/MixedRealitySample. Select the OculusMR_CastingCameraActor1 instance to see how it is configured for the Level.

For more information, see [Oculus Rift: Mixed Reality Capture](/documentation/unreal/latest/concepts/unreal-mrc/).

![](/images/documentationunreallatestconceptsunreal-samples-2.png)

## Sample Scene

A trivial sample map with mixed reality capture enabled is available in our GitHub repository (access instructions [here](/documentation/unreal/latest/concepts/unreal-engine/)) in Samples/Oculus/MixedRealitySample.

## Legacy Touch Sample

This is sample is available with legacy versions using Oculus integration 1.14 or earlier - for more information, see [Unreal Game Engine](/documentation/unreal/latest/concepts/unreal-engine/).

TouchSample illustrates basic use of Oculus Touch including controller tracking and thumbstick control. It also illustrates [haptics](/documentation/unreal/latest/concepts/unreal-haptics/) control using PlayHapticEffect() and PlayHapticSoundWave(). Two spheres track with the Touch controllers. The right controller thumbstick may be used to control the position of the light gray box. Touch capacitance sensors detect whether the right thumb is in a touch or near-touch position, which controls the height of the box. Press and hold the left Touch grip button to play a haptics clip. Press and hold the left Touch X button to create a haptics effect by setting the haptics value directly.

You will find the Haptics control Blueprint and the Thumbstick control Blueprint in the sample Level Blueprint. NewGameMode and VRCharacter are used to initialize the scene and make the scene display at the appropriate height, and so forth.
