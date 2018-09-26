---
title: Oculus Guardian System
---

The Oculus Guardian System is designed to display in-application wall and floor markers when users get near boundaries they defined. When the user gets too close to the edge of a boundary, translucent boundary markers are displayed in a layer that is superimposed over the game or experience. 

The following image shows the Guardian System activated. In this example, the user's hands (which are holding Touch controllers) protrude through the guardian.

![](/images/documentationpcsdklatestconceptsdg-guardian-system-0.jpg)

## Setting Up the Guardian System on Your Rift

After the user sets up the boundaries, they will show up in a layer over any application whenever the user gets too close.

To set up the boundaries:

1. Open the Oculus app.
2. Select Settings -&gt; Devices -&gt; Run Full Setup.
3. Select Rift and Touch.
4. Follow the on-screen instructions to confirm sensor tracking.
5. Continue until the Mark Your Boundaries page appears.
6. Follow the on-screen instructions, using the INDEX trigger button to draw the outer bounds of your play area. Currently, there is no minimum width and depth. 

When you are finished, click Next. Your boundaries are saved.


7. If you need to disable the Guardian System, toggle Guardian System Enabled/Disabled on the Universal Menu.


## Game Configuration

During initialization, your application can make an API request to get the outer boundary and play area. The outer boundary is the space that the user defined during configuration. The play area is a rectangular space within the outer boundary. With this information, your application can set up a virtual world with "barriers" that align with the real world. For example, you can adjust the size of a cockpit based on the user-defined play area.

The following functions return information about the outer boundary and play area:

|         Function         |                                                                                                             Description                                                                                                             |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ovr_GetBoundaryDimensions |                                                                          Returns the width, height, and depth of the play area or outer boundary in meters.                                                                          |
|  ovr_GetBoundaryGeometry  | Returns the points that define the play area or outer boundary. For the play area, it returns the four points that define the rectangular area. For the outer boundary, it returns all of the points that define the outer boundary. |

During runtime, your application can request whether the boundaries are visible using ovr_GetBoundaryVisible. When visible, you can choose how the application will respond. For example, you might choose to pause the application, slow the application, or simply display a message.

The boundary status information is returned in a struct which contains the following:

|       Member       |    Type    |                         Description                         |
|--------------------|-------------|--------------------------------------------------------------|
|    IsTriggering    |   ovrBool   |    Returns whether the boundaries are currently visible.    |
|  ClosestDistance  |    float    | Distance to the closest play area or outer boundary surface. |
|    ClosestPoint    | ovrVector3f |            Closest point on the boundary surface.            |
| ClosestPointNormal | ovrVector3f |     Unit surface normal of the closes boundary surface.     |

Additionally, you can set the bounds to be visible to orient the user or explain how you will use the space by setting ovr_RequestBoundaryVisible() to ovrTrue. When you are finished, simply pass ovrFalse. 

The default boundary color is cyan. To change the color, use  ovr_SetBoundaryLookAndFeel(). 

## Code Sample

To help you get started, we provide a code sample at Samples/GuardianSystemDemo that shows usage of the following APIs: 

* ovr\_TestBoundary
* ovr\_TestBoundaryPoint
* ovr\_SetBoundaryLookAndFeel
* ovr\_RequestBoundaryVisible
* ovr\_ResetBoundaryLookAndFee


Boxes collide with the boundary data using the test API, the boundary visibility and color changes every second, and the simulation slows (and then stops) when the HMD or Touch controllers get too close to the boundary.
