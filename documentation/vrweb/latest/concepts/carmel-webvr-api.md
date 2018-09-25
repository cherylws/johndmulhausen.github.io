---
title: Introduction to the WebVR API
---
Oculus Browser supports the W3C WebVR specification which allows developers to present VR experiences on the web using WebGL.

## Initial Setup

First, you should set up your WebGL canvas and any WebGL scene rendering state. The WebGL canvas will be used as the VRLayer source when presenting.

var layerSource; function initWebGLProgram() { layerSource = document.getElementById("webgl-canvas"); // Compile shaders... // Load textures... // Create geometry... // Save attributes and uniform locations }Use window.navigator.getVRDisplays to get the list of available VRDisplay objects. You should verify the getVRDisplays method exists on window.navigator and fall back to a non-VR experience for browsers that do not support WebVR.

if (navigator.getVRDisplays) { navigator.getVRDisplays().then(function (displays) { if (displays.length > 0) { // We reuse this every frame to avoid generating garbage frameData = new VRFrameData(); vrDisplay = displays[0]; // We must adjust the canvas (our VRLayer source) to match the VRDisplay var leftEye = vrDisplay.getEyeParameters("left"); var rightEye = vrDisplay.getEyeParameters("right"); // update canvas width and height based on the eye parameters. // For simplicity we will render each eye at the same resolution layerSource.width = Math.max(leftEye.renderWidth, rightEye.renderWidth) * 2; layerSource.height = Math.max(leftEye.renderHeight, rightEye.renderHeight); // Code for showing an 'Enter VR' button should go here } } else { // There are no VR displays connected. } ).catch(function (err) { // VR Displays are not accessible in this context. // Perhaps you are in an iframe without the allowvr attribute specified. }); } else { // WebVR is not supported in this browser. } Calling navigator.getVRDisplays yields a promise which will either be resolved with a list of available VRDisplays or rejected if access to the VRDisplay list is prohibited. The resolved list of available VRDisplay objects may be empty in the case that there are no VR devices connected. In Oculus Browser there should always be one VRDevice available. 

The VRDisplay can be used to query the eye parameters which will let you know how to size the WebGL canvas. You can also construct a reusable VRFrameData at this time which will be used in the render loop to query the device orientation. 

function enterVRButtonClicked() { vrDisplay.requestPresent([{ source: layerSource }]).then(function () { vrDisplay.requestAnimationFrame(onAnimationFrame); }).catch(function (err) { // Failed to requestPresent }); }; You must call VRDisplay.requestPresent on VRDisplay to begin VR presentation. **Note that this can only be called in response to user input (such as tapping or clicking an “Enter VR” button)**. Use your WebGL canvas as the layer source provided to VRDisplay.requestPresent. 

Finally, you can begin to request animation frames using VRDisplay.requestAnimationFrame. 

## The Render Loop

Now that you have started VR presentation and are receiving animation frames, you need to render your scene taking the VRDisplay frame data into account and continue to request animation frames. 

Call VRDisplay.getFrameData to get the view and projection matrices for the left and right eyes based on the device’s current orientation. These matrices are used to render the scene for each eye in a way that tracks the device motion. 

function onAnimationFrame(timestamp) { // Continue to request frames to keep the render loop going vrDisplay.requestAnimationFrame(onAnimationFrame); // Clear the layer source - we do this outside of render to avoid clearing twice gl.clear(gl.COLOR\_BUFFER\_BIT | gl.DEPTH\_BUFFER\_BIT); // Update the scene once per frame update(timestamp); // Get the current pose data vrDisplay.getFrameData(frameData); // Render the left eye gl.viewport(0, 0, layerSource.width * 0.5, layerSource.height); render(frameData.leftProjectionMatrix, frameData.leftViewMatrix); // Render the right eye gl.viewport(layerSource.width * 0.5, 0, layerSource.width * 0.5, layerSource.height); render(frameData.rightProjectionMatrix, frameData.rightViewMatrix); // Submit the newly rendered layer to be presented by the VRDisplay vrDisplay.submitFrame(); } function update(timestamp) { // Update your scene state } // For VR, it's important that your render method is parameterized by the camera // (projection and view matrices) so that it can be used to render from each // eye's perspective function render(projectionMat, viewMat) { // Render your scene using the given matrices }When rendering for each eye is complete, call VRDisplay.submitFrame to commit the new frame. When another frame is available, your animation callback will run again. 

See [webvr.info](https://webvr.info/samples/) for more example on using WebVR.

