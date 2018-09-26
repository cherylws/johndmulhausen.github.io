---
title: Get Outer Boundary Points
---

Retrieves the outer boundary points in world space coordinates.

## Overview

This is a mixed reality function. It is only available in versions of the Oculus Unreal integration that you obtain directly from Oculus (not from Epic). This Blueprint only works with the Oculus Rift, since it retrieves Oculus Guardian boundary points, which is only meaningful when positional tracking is available.

This Blueprint retrieves an array of variables of type `FVector`, where each entry in the array represents an outer boundary point for the Guardian rectangle. These points are translated behind the scenes so that they represent the boundary within world space (not tracking space). This means the Guardian boundary outer points are provided within the same frame of reference as the other objects in your virtual world.

## Blueprint

![](/images/documentationunreallatestconceptsunreal-blueprints-get-outer-boundary-points-0.png)

## Arguments

* No arguments. 


## Output

* Return Value: An array of variables of type FVector, which contains four points that define the Guardian boundaries, which is a rectangle within the tracking space.

