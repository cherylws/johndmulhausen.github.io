---
title: Multiview WebGL rendering
---

To render VR content, developers need to draw the same 3D scene twice — for the left eye, and for the right eye.

There is usually only a very slight difference between the two rendered views, but that is what enables the stereoscopic effect that makes VR work.

With stock WebGL the only option available to a developer is to render to the two eye buffers sequentially — essentially incurring double the application and driver overhead — despite the GPU command streams and render states typically being almost identical. 

The OpenGL/WebGL [multiview extension](https://www.khronos.org/registry/webgl/extensions/WEBGL_multiview/) addresses this inefficiency by enabling simultaneous rendering to multiple elements of a 2D texture array.

**Note: **Only CPU-bound experiences will benefit from multi-view. Typically a CPU usage reduction of 25% - 50% is possible.

## Design

With the multiview extension draw calls are instanced into each corresponding element of the texture array. The vertex program uses a new `ViewID` variable to compute per-view values — typically the vertex position and view-dependent variables like reflection.

The formulation of the multiview extension is purposely high-level to allow implementation freedom. On existing hardware, applications and drivers can realize the benefits of a single scene traversal, even if all GPU work is fully duplicated per view.

In WebGL, multiview is exposed via the [WEBGL_multiview extension](https://www.khronos.org/registry/webgl/extensions/WEBGL_multiview/).

Oculus Browser currently supports the ‘opaque multiview framebuffer’ approach, where JavaScript code does not need to allocate and manage texture arrays and instead deals with pre-allocated multiview framebuffers with all attachments pre-set ‘under-the-hood’. 

## Using multiview in WebGL

In WebGL you can use the [WEBGL_multiview](https://www.khronos.org/registry/webgl/extensions/WEBGL_multiview/) extension to use multiview GL.

Oculus Browser currently implements only part of the WEBGL_multiview specification - *opaque multi-view framebuffer*. 

 This means WebVR will provide a framebuffer that should be bound to a context and all the attachment mechanics is hidden from the JavaScript code. 

 WebGL 2.0 allows developers to explicitly create a multiview framebuffer and attach user’s texture 2D arrays as render targets. Your JavaScript code will be responsible for allocating texture 2D arrays, and creating the multiview framebuffer with proper attachments. This approach is currently not supported in the Oculus Browser. 

 At the moment only WebVR apps can benefit from the multiview extension, as only WebVR extensions may create the multi-view-enabled framebuffer. 

 A WebGL / WebVR app can easily be modified to benefit from the extension. First of all, the WEBGL_multiview extension should be requested: 

```
var ext = gl.getExtension('WEBGL_multiview');
if (ext) // Multi-view extension is supported

```

At the moment, only ES 3.00 shaders support multiview.

 The following changes might be necessary for vertex shaders in a multiview-enabled experience:



* #version 300 es should be added at the top of the shader code;
* GL\_OVR\_multiview extension should be requested on the second line: #extension GL\_OVR\_multiview : require
* layout(num\_views=2) in; must be provided on the following line;
* in order to convert a WebGL 1.0 shader to ES 3.00, all attribute entries must be changed from in / varying to out:
+ in vec3 position;
+ in vec2 texCoord;
+ out vec2 vTexCoord;
* Both left and right projection / model matrices must be provided as uniforms:
+ uniform mat4 leftProjectionMat;
+ uniform mat4 leftModelViewMat;
+ uniform mat4 rightProjectionMat;
+ uniform mat4 rightModelViewMat;
* A built-in view identifier - gl\_ViewID\_OVR - should be used to determine which matrix set - left or right to use:
+  mat4 m = gl\_ViewID\_OVR == 0u ? (leftProjectionMat * leftModelViewMat) : (rightProjectionMat * rightModelViewMat);
+ The gl\_ViewID\_OVR is of unsigned int type.




 An example WebGL 1.0 vertex shader...

```
uniform mat4 projectionMat;
uniform mat4 modelViewMat;
attribute vec3 position;
attribute vec2 texCoord;
varying vec2 vTexCoord;

void main() {
  vTexCoord = texCoord;
  gl_Position = projectionMat * modelViewMat * vec4( position, 1.0 );
}

```

...and the equivalent multiview ES 3.00 shader:

```
#version 300 es
#extension GL_OVR_multiview : require
layout(num_views=2) in;
uniform mat4 leftProjectionMat;
uniform mat4 leftModelViewMat;
uniform mat4 rightProjectionMat;
uniform mat4 rightModelViewMat;
in vec3 position;
in vec2 texCoord;
out vec2 vTexCoord;

void main() {
  vTexCoord = texCoord;
  mat4 m = gl_ViewID_OVR == 0u ? (leftProjectionMat * leftModelViewMat) :
                                 (rightProjectionMat * rightModelViewMat);
  gl_Position = m * vec4( position, 1.0 );
}
  
```

 The fragment (pixel) shader should be modified to comply with ES 3.00 spec as well, even though the shader's logic remains untouched. (Both vertex and fragment shaders must be written using the same specification, otherwise shaders won't link.) 

 The main difference is absence of `gl_FragColor` and necessity to use `in` and `out` modifiers. Use explicit `out` declaration instead of `gl_FragColor`. 

 An example WebGL 1.0 fragment shader... 

```
precision mediump float;
uniform sampler2D diffuse;
varying vec2 vTexCoord;

void main() {
  vec4 color = texture2D(diffuse, vTexCoord);
  gl_FragColor = color;
}

```

 ...and the equivalent multiview ES 3.00 shader: 

```
#version 300 es
precision mediump float;
uniform sampler2D diffuse;
in vec2 vTexCoord;
out vec4 color;

void main() {
  color = texture(diffuse, vTexCoord);
}

```

 The conversion to ESSL 3.0 won't be necessary in a future version of Oculus Browser. 

**Hint:** After the conversion, please see console output in the browser developer tools: there will be a detailed error message if the converted shaders have issues. 

## WebGL 2.0 or WebGL 1.0?

 The vast majority of the current WebVR experiences are written using WebGL 1.0. However, WebGL 2.0 has obvious benefits over WebGL 1.0, including better performance. Most WebGL 1.0 code can run as WebGL 2.0 without major modifications.

Please see the following summaries of WebGL 2 benefits:

* [WebGL 2.0 from WebGL 1.0](https://webgl2fundamentals.org/webgl/lessons/webgl1-to-webgl2.html)
* [WebGL 2.0: What's new](https://webgl2fundamentals.org/webgl/lessons/webgl2-whats-new.html)


We strongly encourage switching to WebGL 2.0 as soon as possible, even if you do not plan on using the multiview extension. New WebGL 2.0 features like uniform buffers can save a lot of CPU usage.

## WebVR extension

WebVR 1.1 has also been extended to provide *opaque multiview framebuffer* support, with corresponding views / viewports. The upcoming WebXR standard already has multiview support. 

Multiview adds the following functionality in WebVR 1.1:

VRDisplay.getViews() returns a list of Views (see 'VRViewList' below).

```
VRViewList? getViews();

```

**Note: **`VRDisplay.getViews` will be undefined if the WebGL / WebVR extension is not available or enabled. 

In the case of multiview rendering, getViews will return VRViewList with a single View; otherwise, two Views will be returned.

 VRViewList - a list of VRViews: 

```
interface VRViewList {
    readonly attribute unsigned long length;
    getter VRView? item (unsigned long index);
};
```

VRView - represents a single eye view. For non-multi-view case there will be two VRView instances (for left and right eye); otherwise, a single VRView will be provided. 

```
interface VRView {
  readonly attribute WebGLFramebuffer framebuffer;
                
  VRViewport? getViewport();
  VRAttributes getAttributes();
};
```

VRViewport, represents a viewport for the particular VRView:

```
dictionary VRViewport {
  readonly attribute long x; // in pixels
  readonly attribute long y;
  readonly attribute long width;
  readonly attribute long height;
};

```

VRAttributes - a dictionary with attributes, used to request / check multi-view mode:

```
dictionary VRAttributes {
  boolean depth;                 // is depth buffer required?
  boolean multiview = false;     // is multi-view required?
  boolean antialias;             // is anti-aliasing required?

  unsigned long framebufferWidth;  // optional width of framebuffer, in pixels
  unsigned long framebufferHeight; // optional width of framebuffer, in pixels
 }

```

`attributes` could be used to request multi-view at `requestPresent` stage. VRAttribute fields:

* multiview - if set to true, then multiview framebuffer is provided as VRView.framebuffer;
* depth - indicates that depth buffer is required in multiview framebuffer; if not set then default setting will be used (the one that was used for requesting WebGL context);
* antialias - indicates that anti-aliasing is required; if not set then default setting will be used (the one that was used for requesting WebGL context);
* framebufferWidth / framebufferHeight - if specified, then specify the dimensions of the multiview framebuffer. Note, the dimensions should be specified for a single eye buffer; the second eye buffer will have the same dimension. For example, instead of specifying 2048 x 1024, you should use 1024 x 1024.


An example of requesting multi-view:

```
  var attributes = {
    depth: true,
    multiview: true,
  };
  vrDisplay.requestPresent([{ source: webglCanvas, attributes: attributes}]).then(function () {
  }, function () {
    // report error "requestPresent failed."
  });

```

The updated IDL for VRLayer looks as follows:

```
dictionary VRLayer {
  HTMLCanvasElement source;
  sequence&lt;float&gt; leftBounds;
  sequence&lt;float&gt; rightBounds;
  VRAttributes attributes;
};

```

VRView.getAttribute() can be used to check if the multi-view was actually enabled. For example, in the `vrdisplaypresentchange` handler:

```
  if (vrDisplay.isPresenting) {
    var views = vrDisplay.getViews ? vrDisplay.getViews() : [];
    if (views.length &gt; 0) {
      var view = views[0];
      is_multiview = view.getAttributes().multiview;
      console.log("onVRPresentChange, presenting, multiview = " + is_multiview);
    }
  }

```

The rendering loop should be changed to perform a single rendering pass instead of two. The multiview framebuffer should also be bound to the GL context. Here is an example:

```
if (vrDisplay.isPresenting) {
  var views = vrDisplay.getViews ? vrDisplay.getViews() : [];
  //console.log("views: " + vrDisplay.getViews);
  if (views.length &gt; 0) {
    var view = views[0];
    gl.enable(gl.SCISSOR_TEST);
    for (var i = 0; i &lt; views.length; ++i) {
      var view = views[i];
      var multiview = view.getAttributes().multiview;
      var viewport = view.getViewport();
      gl.bindFramebuffer(gl.FRAMEBUFFER, view.framebuffer);
      gl.viewport(viewport.x, viewport.y, viewport.width, viewport.height);
      gl.scissor(viewport.x, viewport.y, viewport.width, viewport.height);
      gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
      if (multiview) {
        var projections = [frameData.leftProjectionMatrix, frameData.rightProjectionMatrix];
        var viewMats = [frameData.leftViewMatrix, frameData.rightViewMatrix];
        cubeSea.render(projections, viewMats, stats, /*multiview*/ true);
        break; 
      }
      else {
        // Direct render to VR framebuffer, non-multiview case
        var viewMat = i == 0 ? frameData.leftViewMatrix : frameData.rightViewMatrix;
        cubeSea.render(i == 0 ? frameData.leftProjectionMatrix : frameData.rightProjectionMatrix, viewMat, stats);
      }
    }
    gl.disable(gl.SCISSOR_TEST);
  }
  else {
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
    // Note that the viewports use the eyeWidth/height rather than the
    // canvas width and height.
    gl.viewport(0, 0, webglCanvas.width * 0.5, webglCanvas.height);
    cubeSea.render(frameData.leftProjectionMatrix, frameData.leftViewMatrix, stats);
    gl.viewport(webglCanvas.width * 0.5, 0, webglCanvas.width * 0.5, webglCanvas.height);
    cubeSea.render(frameData.rightProjectionMatrix, frameData.rightViewMatrix, stats);
  }
}
```

Note:

* Even if VRDisplay.getViews is presented, it may return two views. This means that multiview is not enabled, however, feel free to use view.framebuffer and view.getViewport(): those will be correctly set for each view;
* This sample shows usage of scissor rect to clear only a certain eye buffer (in non-multi-view case); it is not mandatory, global clear still could be used (and, in fact, is more efficient);
* See the full working samples with source code in code samples section below.


In the case if dynamic resolution is necessary (or, when you don't want to use the full resolution of the rendering buffer for performance or other reasons), then the same approach as before can be used by setting VRLayer.leftBounds / rightBounds. The only requirement is to either specify only one of them (either leftBounds or rightBounds, or, if both of them are specified then they should be set to identical values). The bounds are specified in UV coordinates in the range [0.0...1.0]. See Dynamic Resolution sample in code samples section.

## Multi-view / WebVR code examples

[Cubes (WebGL 1.0)](https://github.com/Artyom17/webvr.info/tree/gh-pages/mv/vr-presentation-webgl1.html)

[Cubes (WebGL 2.0)](https://github.com/Artyom17/webvr.info/tree/gh-pages/mv/vr-presentation.html)

[Dynamic resolution (WebGL 1.0)](https://github.com/Artyom17/webvr.info/tree/gh-pages/mv/dynamic-resolution.html)

[Instancing Cubes (WebGL 2.0)](https://github.com/Artyom17/webvr.info/tree/gh-pages/mv/WebGL2-instancing-cubes.html)

For the first 3 samples, white cubes in WebVR mode indicate that multiview is used; pink cubes indicate that multi-view isn't working - either it is not enabled (see chrome://flags) or your hardware doesn't support it (see console output in DevTools).-
