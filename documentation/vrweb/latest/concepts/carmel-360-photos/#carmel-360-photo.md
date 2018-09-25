---
title: Displaying 360 Photos
---
360 Photos and other forms of panoramas are a great way to add a sense of presence to a VR environment with relatively low performance overhead. This topic discusses the various tradeoffs in the different ways a WebVR application can render a panorama using WebGL.

## Getting Started

This sample makes use of a few libraries to reduce boilerplate code and keep focused on what’s unique.

WebVRCommon.js provides general purpose wrappers around WebGL for initializing the VRDisplay, loading textures, and rendering geometry. For more information on this, see [Introduction to the WebVR API](/documentation/vrweb/latest/concepts/carmel-webvr-api/ "Oculus Browser supports the W3C WebVR specification which allows developers to present VR experiences on the web using WebGL. There are a few simple steps to get your application bootstrapped into VR presentation mode which will be covered in this sample."). 

GamepadState.js provides a simplified wrapper around navigator.getGamepads to expose Gear VR trackpad events. For more information on this, see [Using the Gear VR Controller](/documentation/vrweb/latest/concepts/carmel-gearvr-controller/). 

To run the sample in your browser, click [here](https://s3.amazonaws.com/static.oculus.com/carmel/WebVRSamples/Pano/index.html).

## Types of Panoramas

 There are two common methods of encoding a 360 panorama into an image.

* Equirectangle – A single image encodes the color coming from every angle by interpreting the image axis as polar coordinates (yaw/pitch). Equirectangle images should always be 5120x2560 or lower.

![](/images/documentation-vrweb-latest-concepts-carmel-360-photos-carmel-360-photos-0.png)  

	+ Pros 
		- Simple to load/display by texture mapping on a sphere.
		- Easy to capture from a 360 camera.
		
	+ Cons 
		- Un-even distribution of texels due to the poles of the sphere mapping onto entire rows of the texture.
		- Harder to incrementally load.
		- Requires additional geometry for sphere
		
	
* Cubemap - Six images form a cube around the viewer, and a fragment shader is used to sample the cubemap at any angle. Cubemap images should always be 1536x1536 per face or lower.

![](/images/documentation-vrweb-latest-concepts-carmel-360-photos-carmel-360-photos-1.png)  

	+ Pros 
		- Less distortion due to more evenly distributed texels. 
		- Flexible geometry, including a sphere, cube, and so on. 
		- Easier to incrementally load
		
	+ Cons 
		- More complex setup.
		- Requires more texture space for the same quality around the equator.
		
	
**360 Image Formats**

Generally, unless you're concerned with network transfer time, use .ktx files with ASTC compression. They will load more quickly (from flash, not over the internet) and render more efficiently. 8 bpp will appear lossless, but going to 4 bpp or less is .jpg level quality.

## Stereo Rendering

Stereo panoramas are a great way to give depth to your scene without blowing your frame budget on thousands of polygons. You might be thinking that a stereo panorama is just two mono panoramas, where the 360 camera is offset by some amount (the interpupillary distance). Unfortunately, that would only work at one gaze angle, as the diagram below illustrates.

![](/images/documentation-vrweb-latest-concepts-carmel-360-photos-carmel-360-photos-2.png)  
As you can see, if you space the 360 cameras apart (along the x axis), then as the gaze rotates the two panoramas are no longer spaced correctly. The correct way to capture stereo panoramas is beyond the scope of this sample, but it requires specialized hardware and software. The easiest way to create a stereo panorama is to render one in a 3d modeling package. 

Given two panorama images (or cubemaps) you can use one when rendering the left eye and the other when rendering the right eye. Alternately, if you are using equirectangle panoramas, you can pack both the left and right into the same image. It is common to put the left eye on top of the right eye, for example. 

When should you use stereo panoramas? Often if you have a stereo panorama, the experience will be better in VR as opposed to mono, but this isn’t always the case. If your experience has UI elements, you must be careful with stereo panoramas to avoid a discrepancy between the depth in the panorama and the UI. Generally speaking, panoramas do not write anything to the Z buffer, so it is possible to confuse the user by rendering UI at a depth deeper than the surrounding panorama. Another issue with stereo panoramas is that the effect breaks down at the poles because we are only approximating a light field with two panoramas. Similar to the diagram above, if you roll your head or look up or down too much, the IPD may not be correct. 

## A Look at the Code

### Setup

Before we dig into the details, let's take a high level look at how the sample is setup.

var webVRCommon = new WebVRCommon({ layerSourceId: 'webgl-canvas', messageElementId: 'messages', }); var panos = []; var currentPano = 0; // These factory methods create different types of Panos. var createPano = [ function () { return new Pano(webVRCommon, { src: "../assets/monoPano.jpg", stereoMode: Pano.MONO }); }, ... ];We initialize a WebVRCommon instance and use this to create several Pano objects in an array of factory methods. These abstract away the details of WebGL/WebVR and Pano render, but we would encourage you to dig into their details as well.

The factory methods are used to delay-create the Pano’s as the currentPano index changes.

### Input Handling

We want the user to be able to swipe left/right or press left/right keys to cycle between different types of panoramas. For this we will make use of a GamepadState instance.

// If you swipe left/right on the controller, or press left/right on the keyboard, // we cycle between panos. var oninput = function (direction) { switch (direction) { case 'left': currentPano = (currentPano - 1 + createPano.length) % createPano.length; break; case 'right': currentPano = (currentPano + 1) % createPano.length; break; } }; // Helper for detecting swipes on the controller touch pad. gamepad = new GamepadState(); gamepad.ongearvrinput = oninput; // When run in the browser, the keyboard emulates controller touch pad swipes window.onkeydown = function (e) { switch (e.keyCode) { case 37: oninput('left'); break; case 39: oninput('right'); break; } }; // Every frame we need to detect input events. webVRCommon.update = function (time) { gamepad.update(time); }; As you can see we have some central logic handling code in oninput, and both the GamepadState and the window.onkeydown event call into it. 

### Rendering

Rendering the pano requires setting up a context object and passing it to the current Pano instance.

webVRCommon.render = function (projectionMat, viewMat, eye) { // delay create the pano if (!panos[currentPano]) { panos[currentPano] = createPano[currentPano](); } var context = { projectionMat: projectionMat, viewMat: viewMat, eye: eye }; // render the current pano panos[currentPano].render(context); };The Pano instance looks at the eye to determine what which panorama texture to use for rendering (in stereo mode). It then renders a sphere geometry around the user, and texture maps this with the panorama.

It's important that the sphere either has a very large radius or that you zero out any translation in the view matrix. If you don't do this, then the translation due to the camera's IPD will be compounded by the translation that is baked into the textures of a stereo panorama. By making the sphere large the view’s translation is insignificant enough to eliminate this issue.

Instead of going into the details of all of the Pano rendering code, let’s instead take a serialized view of just the WebGL calls involved.

depthMask(false) disable(DEPTH\_TEST) useProgram([monoEquirectProgram]) bindBuffer(ARRAY\_BUFFER, [sphereVertexBuffer]) enableVertexAttribArray(0) vertexAttribPointer(0, 3, FLOAT, false, 20, 0) enableVertexAttribArray(1) vertexAttribPointer(1, 2, FLOAT, false, 20, 12) bindBuffer(ELEMENT\_ARRAY\_BUFFER, [sphereIndexBuffer]) activeTexture(TEXTURE0) bindTexture(TEXTURE\_2D, [monoPano]) texParameteri(TEXTURE\_2D, TEXTURE\_WRAP\_S, REPEAT) texParameteri(TEXTURE\_2D, TEXTURE\_WRAP\_T, REPEAT) texParameteri(TEXTURE\_2D, TEXTURE\_MIN\_FILTER, LINEAR) texParameteri(TEXTURE\_2D, TEXTURE\_MAG\_FILTER, LINEAR) uniform1i("texture", 0) uniformMatrix4fv("projectionMat", false, [1.2,0,0,0,0,1,0,0,0,0,-1.0,-1,0,0,-0.02,0]) uniformMatrix4fv("viewMat", false, [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1]) uniformMatrix4fv("modelMat", false, [-5000,0,0,0,0,-5000,0,0,0,0,5000,0,0,0,0,1]) uniform1f("opacity", 1) uniform2fv("texOffset", [0,0]) uniform2fv("texScale", [1,1]) drawElements(TRIANGLES, 3420, UNSIGNED\_SHORT, 0)As you can see, we’re simply drawing a texture mapped sphere. All of the magic is in the shaders.

### Shaders

From a rendering perspective, the main difference between equirect and cubemap based panoramas is the shader you use to render them. First let’s look at the equirect shader: 

vs = "uniform mat4 projectionMat;\n" + "uniform mat4 viewMat;\n" + "uniform mat4 modelMat;\n" + "uniform vec2 texOffset;\n" + "uniform vec2 texScale;\n" + "attribute vec3 position;\n" + "attribute vec2 texCoord;\n" + "varying vec2 vTexCoord;\n" + "void main() {\n" + " vTexCoord = texCoord * texScale + texOffset;\n" + " gl\_Position = projectionMat * viewMat * modelMat * vec4(position.xyz, 1.0);\n" + "}\n"; fs = "precision mediump float;\n" + "uniform sampler2D texture;\n" + "uniform float opacity;\n" + "varying vec2 vTexCoord;\n" + "void main() {\n" + " vec4 texture = texture2D(texture, vTexCoord);\n" + " gl\_FragColor = vec4(texture.rgb, texture.a * opacity);\n" + "}\n";The vertex shader is simply transforming the position by the model/view/projection matrices (note that it’s often better to concatenate these prior to the shader). It is transforming the texture coordinates by texScale and texOffset so that we can support top/bottom and left/right stereo modes.

The fragment shader is a simple texture lookup with support for an opacity uniform (can be used to cross-fade panoramas).

Now let’s examine the shaders used to render cubemapped panoramas.

vs = "uniform mat4 projectionMat;\n" + "uniform mat4 viewMat;\n" + "uniform mat4 modelMat;\n" + "attribute vec3 position;\n" + "varying vec3 vTexCoord;\n" + "void main() {\n" + " vTexCoord = normalize(position) * vec3(-1.0, -1.0, 1.0);\n" + " gl\_Position = projectionMat * viewMat * modelMat * vec4(position.xyz, 1.0);\n" + "}\n"; fs = "precision mediump float;\n" + "uniform samplerCube texture;\n" + "uniform float opacity;\n" + "varying vec3 vTexCoord;\n" + "void main() {\n" + " vec4 texture = textureCube(texture, vTexCoord);\n" + " gl\_FragColor = vec4(texture.rgb, texture.a * opacity);\n" + "}\n";You can see that it is similar to the previous shaders. The main difference is that the texture coordinates are derived from the position, and the texture sample comes from textureCube.

### Conclusion

This sample has demonstrated how to use WebGL and WebVR to render 360 photos and other panoramas. Many experiences for the Gear VR and Oculus Go make use of a panorama to immerse the user in a rich environment. 

Rendering a pano is straightforward, but the way in which you capture and encode a panorama determines how you render it. Whether you’re using equirectangle or cubemap, stereo or mono, the process is similar and can be generalized into something like we saw with Pano.js.

