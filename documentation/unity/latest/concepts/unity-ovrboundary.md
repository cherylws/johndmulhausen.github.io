---
title: OVRBoundary Guardian System API
---

OVRBoundary exposes an API for interacting with the Rift Guardian System for Touch.

The Oculus Guardian System is an in-VR visualization of Play Area bounds for Touch users. The boundary visualization is handled automatically by Oculus software, but developers may interact with the Guardian System in various ways using the OVRBoundary API. Possible use cases include pausing the game if the user leaves the Play Area, or placing geometry in the world based on boundary points to create a “natural” integrated barrier with in-scene objects.

For a sample illustrating how to use OVRBoundary, see the Guardian Boundary Sample in the [Unity Sample Framework](/documentation/unity/latest/concepts/unity-sample-framework/). 

During Touch setup, users define an interaction area by drawing a perimeter called the Outer Boundary in space with the controller. An axis-aligned bounding box called the Play Area is calculated from this perimeter.

![](/images/documentationunitylatestconceptsunity-ovrboundary-0.png)

When tracked devices approach the Outer Boundary, the Oculus runtime automatically provides visual cues to the user demarcating the Outer Boundary. This behavior may not be disabled or superseded by applications, though the Guardian System visualization may be disabled via user configuration in the Oculus app. 

See OVRBoundary in our [Developer Reference](/documentation/game-engines/latest/concepts/book-unity-reference/) for additional details.

## Basic Use

Boundaries are `BoundaryType.OuterBoundary` and `BoundaryType.PlayArea`.

Node types are `Node.HandLeft`, `Node.HandRight`, and `Node.Head`.

Applications may query the location of nodes relative to the Outer Boundary or Play Area by using `OVRBoundary.BoundaryTestResult TestNode()`, which takes the node and boundary type as arguments.

Applications may also query arbitrary points relative to the Play Area or Outer Boundary using `OVRBoundary.BoundaryTestResult TestPoint()`, which takes the point coordinates in the tracking space as a Vector3 and boundary type as arguments.

Results are returned as a struct called `OVRBoundary.BoundaryTestResult`, which includes the following members:

|       Member       |  Type  |                                             Description                                             |
|--------------------|---------|------------------------------------------------------------------------------------------------------|
|    IsTriggering    |  bool  |                Returns true if the node or point triggers the queried boundary type.                |
|  ClosestDistance  |  float  |              Distance between the node or point and the closest point of the test area.              |
|    ClosestPoint    | Vector3 | Describes the location in tracking space of the closest boundary point to the queried node or point. |
| ClosestPointNormal | Vector3 |       Describes the normal of the boundary point that is closest to the queried node or point.       |

Applications may request that boundaries be displayed or hidden using `OVRBoundary.SetVisible()`. Note that the Oculus runtime will override application requests under certain conditions. For example, setting Boundary Area visibility to false will fail if a tracked device is close enough to trigger the boundary’s automatic display, and setting the visibility to true will fail if the user has disabled the visual display of the boundary system.

Applications may query the current state of the boundary system using `OVRBoundary.GetVisible()`.

## Additional Features

You may set the boundary color of the automated Guardian System visualization using `OVRBoundary.SetLookAndFeel()`. Alpha is unaffected. Use `ResetLookAndFeel()` to reset.

`OVRBoundary.GetGeometry()` returns an array of up to 256 points that define the Boundary Area or Play Area in clockwise order at floor level. You may query the dimensions of a Boundary Area or Play Area using `OVRBoundary.GetDimensions()`, which returns a Vector3 containing the width, height, and depth in tracking space units, with height always returning 0.
