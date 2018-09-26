---
title: Get Tiled Multires Level
---

 Returns the current multi-resolution level, which applies to fixed foveated rendering.

## Overview

## Blueprint

![](/images/documentationunreallatestconceptsunreal-blueprints-get-tiled-multires-level-0.png)

## Arguments

* No arguments.


## Output

* Return Value: The current multi-resolution level for fixed foveated rendering. This returns an index into the ETiledMultiResLevel enum, which can be one of the following values: 
	+ ETiledMultiResLevel\_Off (index = 0): No reduction of resolution. (Default) 
	+ ETiledMultiResLevel\_LMSLow (index = 1): The lowest level of resolution reduction. 
	+ ETiledMultiResLevel\_LMSMedium (index = 2): The medium level of resolution reduction. 
	+ ETiledMultiResLevel\_LMSHigh (index = 3): The highest level of resolution reduction. 
	 For more information, see [Oculus Go: Fixed Foveated Rendering](/documentation/unreal/latest/concepts/unreal-ffr/ "Oculus Go supports Fixed Foveated Rendering (FFR) which enables the edges of the eye buffers to be rendered at a lower resolution than the center portion of the eye buffers.").

