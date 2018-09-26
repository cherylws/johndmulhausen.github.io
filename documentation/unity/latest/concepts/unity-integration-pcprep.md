---
title: "Preparing for Development: Rift"
---



We recommend Rift developers begin by reviewing the [PC Developer Guide](/documentation/pcsdk/latest/concepts/book-dg/). Mobile developers should review [Mobile Development Basics](/documentation/mobilesdk/latest/concepts/book-mobile-basics/).

## Recommended Configuration

* On Windows, enable Direct3D 11 - it exposes the most advanced VR rendering capabilities. Direct3D 9 and Windows OpenGL are not supported. D3D 12 is currently available as an experimental feature. 
* Use the Linear Color Space. Linear lighting is not only more correct for shading, it also causes Unity to perform sRGB read/write to the eye textures. This helps reduce aliasing during VR distortion rendering, where the eye textures are interpolated with slightly greater dynamic range.
* Never clone displays. When the Rift is cloned with another display, the application may not vsync properly. This leads to visible tearing or judder (stuttering or vibrating motion).

