---
title: Guardian System Boundary Component 
---

OculusBoundaryComponent exposes an API for interacting with the Oculus Guardian System.

During Touch setup, users define an interaction area by drawing a perimeter called the Outer Boundary in space with the controller. An axis-aligned bounding box called the Play Area is calculated from this perimeter.

When tracked devices approach the Outer Boundary, the Oculus runtime automatically provides visual cues to the user demarcating the Outer Boundary. This behavior may not be disabled or superseded by applications, though the Guardian System visualization may be disabled via user configuration in the Oculus app.

![](/images/documentationunreallatestconceptsunreal-boundary-0.png)

Additional handling may be implemented by applications using the class `UOculusBoundaryComponent`. Possible use cases include pausing the game if the user leaves the Play Area, placing geometry in the world based on boundary points to create a “natural” integrated barrier with in-scene objects, disabling UI when the boundary is being rendered to avoid visual discomfort, and so forth.

All `UOculusBoundaryComponent` public methods are available as Blueprints.

Please see OculusBoundaryComponent.h for additional details.

## Basic Use

Boundary types are `Boundary_Outer` and `Boundary_PlayArea`.

Device types are `HMD`, `LTouch`, `RTouch`, `Touch` (i.e., both controllers), and `All`.

Applications may query the interaction between devices and the Outer Boundary or Play Area by using UOculusBoundaryComponent::GetTriggeredPlayAreaInfo() or UOculusBoundaryComponent::GetTriggeredOuterBoundaryInfo().

Applications may also query arbitrary points relative to the Play Area or Outer Boundary using UOculusBoundaryComponent::CheckIfPointWithinOuterBounds() or UOculusBoundaryComponent::CheckIfPointWithinPlayArea(). This may be useful for determining the location of particular Actors in a scene relative to boundaries so, for example, they are spawned within reach, and so forth.

Results are returned as a struct called FBoundaryTestResult, which includes the following members:

|       Member       |        Type        |                                              Description                                              |
|--------------------|--------------------|--------------------------------------------------------------------------------------------------------|
|    IsTriggering    |        bool        |                Returns true if the device or point triggers the queried boundary type.                |
|     DeviceType     | ETrackedDeviceType |                                    Device type triggering boundary.                                    |
|  ClosestDistance  |       float       |              Distance between the device or point and the closest point of the test area.              |
|    ClosestPoint    |      FVector      | Describes the location in tracking space of the closest boundary point to the queried device or point. |
| ClosestPointNormal |      FVector      |           Describes the normal of the closest boundary point to the queried device or point.           |

All dimensions, points, and vectors are returned in Unreal world coordinate space.

Applications may request that boundaries be displayed or hidden using `RequestOuterBoundaryVisible()`. Note that the Oculus runtime will override application requests under certain conditions. For example, setting Boundary Area visibility to false will fail if a tracked device is close enough to trigger the boundary’s automatic display. Setting the visibility to true will fail if the user has disabled the visual display of the boundary system.

Applications may query the current state of the boundary system using `UOculusBoundaryComponent::IsOuterBoundaryDisplayed()` and `UOculusBoundaryComponent::IsOuterBoundaryTriggered()`.

You may bind delegates using the object `OnOuterBoundaryTriggered`.

## Additional Features

You may set the boundary color of the automated Guardian System visualization (alpha is unaffected) using `UOculusBoundaryComponent::SetOuterBoundaryColor()`. Use `UOculusBoundaryComponent::ResetOuterBoundaryColor()`to reset to default settings.

`UOculusBoundaryComponent::GetOuterBoundaryPoints()` and `UOculusBoundaryComponent::GetPlayAreaPoints()`return an array of up to 256 3D points that define the Boundary Area or Play Area in clockwise order at floor level. You may query the dimensions of a Boundary Area or Play Area using `UOculusBoundaryComponent::GetOuterBoundaryDimensions()` or

`UOculusBoundaryComponent::GetPlayAreaDimensions()`, which return a vector containing the width, height, and depth in tracking space units, with height always returning 0. 

## Boundary Sample

BoundarySample, available from our Unreal GitHub repository, illustrates the use of the Boundary Component API for interacting with our Guardian System. For more information, see [Unreal Samples](/documentation/unreal/latest/concepts/unreal-samples/).
