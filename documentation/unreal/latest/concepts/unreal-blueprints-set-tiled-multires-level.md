---
title: Set Tiled Multires Level
---
Sets the multi-resolution level for fixed foveated rendering.

## Overview

This blueprint sets the multi-resolution level for fixed foveated rendering. For more information about fixed foveated rendering, see [Oculus Go: Fixed Foveated Rendering](/documentation/unreal/latest/concepts/unreal-ffr/ "Oculus Go supports Fixed Foveated Rendering (FFR) which enables the edges of the eye buffers to be rendered at a lower resolution than the center portion of the eye buffers."). ## Blueprint

![](/images/documentation-unreal-latest-concepts-unreal-blueprints-set-tiled-multires-level-0.png)  
## Arguments

* Level: The desired multi-resolution level for fixed foveated rendering. This is an index into the ETiledMultiResLevel enum, which can be one of the following values: 
	+ ETiledMultiResLevel\_Off (index = 0): No reduction of resolution. (Default) 
	+ ETiledMultiResLevel\_LMSLow (index = 1): The lowest level of resolution reduction. 
	+ ETiledMultiResLevel\_LMSMedium (index = 2): The medium level of resolution reduction. 
	+ ETiledMultiResLevel\_LMSHigh (index = 3): The highest level of resolution reduction. 
	 For more information, see [Oculus Go: Fixed Foveated Rendering](/documentation/unreal/latest/concepts/unreal-ffr/ "Oculus Go supports Fixed Foveated Rendering (FFR) which enables the edges of the eye buffers to be rendered at a lower resolution than the center portion of the eye buffers.").
## Output

* No output.
