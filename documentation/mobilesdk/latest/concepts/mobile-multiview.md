---
title: Multi-View
---
## Overview

With stock OpenGL, the method of stereo rendering is achieved by rendering to the two eye buffers sequentially. This typically doubles the application and driver overhead, despite the fact that the command streams and render states are almost identical.

The GL\_OVR\_multiview extension addresses the inefficiency of sequential multi-view rendering by adding a means to render to multiple elements of a 2D texture array simultaneously. Using the multi-view extension, draw calls are instanced into each corresponding element of the texture array. The vertex program uses a new ViewID variable to compute per-view values, typically the vertex position and view-dependent variables like reflection.

The formulation of the extension is high level in order to allow implementation freedom. On existing hardware, applications and drivers can realize the benefits of a single scene traversal, even if all GPU work is fully duplicated per-view. But future support could enable simultaneous rendering via multi-GPU, tile-based architectures could sort geometry into tiles for multiple views in a single pass, and the implementation could even choose to interleave at the fragment level for better texture cache utilization and more coherent fragment shader branching.

The most obvious use case in this model is to support two simultaneous views: one view for each eye. However, multi-view can also be used for foveated rendering, where two views are rendered per eye, one with a wide field of view and the other with a narrow one. The nature of wide field of view planar projection is that the sample density can become unacceptably low in the view direction. By rendering two inset eye views per eye, the required sample density is achieved in the center of projection without wasting samples, memory, and time by oversampling in the periphery.

## Basic Usage

The GL\_OVR\_multiview extension is not a turn-key solution that can simply be enabled to support multi-view rendering in an application. An application must explicitly support GL\_OVR\_multiview to get the benefits. 

The GL\_OVR\_multiview extension is used by the application to render the scene, and the VrApi is unaware of its use. The VrApi supports sampling from the layers of a texture array, but is otherwise completely unaware of how the application produced the texture data, whether multi-view rendering was used or not. However, because of various driver problems, an application is expected to query the VrApi to find out whether or not multi-view is properly supported on a particular combination of device and OS. For example:

 vrapi\_GetSystemPropertyInt( &Java, VRAPI\_SYS\_PROP\_MULTIVIEW\_AVAILABLE ) == VRAPI\_TRUE;## Restructuring VrAppFramework Rendering For Multi-view

The following section describes how to convert your application to be Multi-View compliant based on the VrAppFramework Multi-View setup. 

In order to set up your rendering path to be multi-view compliant, your app should specify a list of surfaces and render state back to App Frame(). Immediate GL calls inside the app main render pass are not compatible with multi-view rendering and not allowed.

The first section below describes how to transition your app from rendering with DrawEyeview and instead return a list of surfaces back to the application framework.

The section below describes multi-view rendering considerations and how to enable it in your app.

## Return Surfaces From Frame

Set up the Frame Result:

Apps should set up the ovrFrameResult which is returned by Frame with the following steps:

1. Set up the ovrFrameParms - storage for which should be maintained by the application.
2. Set up the FrameMatrices - this includes the CenterEye and View and Projection matrices for each eye.
3. Generate a list of render surfaces and append to the frame result Surfaces list. 
	1. Note: The surface draw order will be the order of the list, from lowest index (0) to highest index.
	2. Note: Do not free any resources which surfaces in list rely on while Frame render is in flight.
	
4. Optionally, specify whether to clear the color or depth buffer with clear color.
## OvrSceneView Example

An example using the OvrSceneView library scene matrices and surface generation follows:

ovrFrameResult OvrApp::Frame( const ovrFrameInput & vrFrame ) { ... // fill in the frameresult info for the frame. ovrFrameResult res; // Let scene construct the view and projection matrices needed for the frame. Scene.GetFrameMatrices( vrFrame.FovX, vrFrame.FovY, res.FrameMatrices ); // Let scene generate the surface list for the frame. Scene.GenerateFrameSurfaceList( res.FrameMatrices, res.Surfaces ); // Initialize the FrameParms. FrameParms = vrapi\_DefaultFrameParms( app->GetJava(), VRAPI\_FRAME\_INIT\_DEFAULT, vrapi\_GetTimeInSeconds(), NULL ); for ( int eye = 0; eye < VRAPI\_FRAME\_LAYER\_EYE\_MAX; eye++ ) { FrameParms.Layers[0].Textures[eye].ColorTextureSwapChain = vrFrame.ColorTextureSwapChain[eye]; FrameParms.Layers[0].Textures[eye].DepthTextureSwapChain = vrFrame.DepthTextureSwapChain[eye]; FrameParms.Layers[0].Textures[eye].TextureSwapChainIndex = vrFrame.TextureSwapChainIndex; FrameParms.Layers[0].Textures[eye].TexCoordsFromTanAngles = vrFrame.TexCoordsFromTanAngles; FrameParms.Layers[0].Textures[eye].HeadPose = vrFrame.Tracking.HeadPose; } FrameParms.ExternalVelocity = Scene.GetExternalVelocity(); FrameParms.Layers[0].Flags = VRAPI\_FRAME\_LAYER\_FLAG\_CHROMATIC\_ABERRATION\_CORRECTION; res.FrameParms = (ovrFrameParmsExtBase *) & FrameParms; return res; }Custom Rendering Example

First, you need to make sure any immediate GL render calls are represented by an ovrSurfaceDef.

In the DrawEyeView path, custom surface rendering was typically done by issuing immediate GL calls. 

 glActiveTexture( GL\_TEXTURE0 ); glBindTexture( GL\_TEXTURE\_2D, BackgroundTexId ); glDisable( GL\_DEPTH\_TEST ); glDisable( GL\_CULL\_FACE ); GlProgram & prog = BgTexProgram; glUseProgram( prog.Program ); glUniform4f( prog.uColor, 1.0f, 1.0f, 1.0f, 1.0f ); glBindVertexArray( globeGeometry.vertexArrayObject ); glDrawElements( globeGeometry.primitiveType, globeGeometry.indexCount, globeGeometry.IndicesType, NULL ); glUseProgram( 0 ); glActiveTexture( GL\_TEXTURE0 ); glBindTexture( GL\_TEXTURE\_2D, 0 );Instead, with the multi-view compliant path, an ovrSurfaceDef and GlProgram would be defined at initialization time as follows.

static ovrProgramParm BgTexProgParms[] = { { "Texm", ovrProgramParmType::FLOAT\_MATRIX4 }, { "UniformColor", ovrProgramParmType::FLOAT\_VECTOR4 }, { "Texture0", ovrProgramParmType::TEXTURE\_SAMPLED }, }; BgTexProgram= GlProgram::Build( BgTexVertexShaderSrc, BgTexFragmentShaderSrc, BgTexProgParms, sizeof( BgTexProgParms) / sizeof( ovrProgramParm ) ); GlobeSurfaceDef.surfaceName = "Globe"; GlobeSurfaceDef.geo = BuildGlobe(); GlobeSurfaceDef.graphicsCommand.Program = BgTexProgram; GlobeSurfaceDef.graphicsCommand.GpuState.depthEnable = false; GlobeSurfaceDef.graphicsCommand.GpuState.cullEnable = false; GlobeSurfaceDef.graphicsCommand.UniformData[0].Data = &BackGroundTexture; GlobeSurfaceDef.graphicsCommand.UniformData[1].Data = &GlobeProgramColor; At Frame time, the uniform values can be updated, changes to the gpustate can be made, and the surface(s) added to the render surface list.

Note: This manner of uniform parm setting requires the application to maintain storage for the uniform data. Future SDKs will provide helper functions for setting up uniform parms and materials.An example of setting up FrameResult using custom rendering follows:

ovrFrameResult OvrApp::Frame( const ovrFrameInput & vrFrame ) { ... // fill in the frameresult info for the frame. ovrFrameResult res; // calculate the scene matrices for the frame. res.FrameMatrices.CenterView = vrapi\_GetCenterEyeViewMatrix( &app->GetHeadModelParms(), &vrFrame.Tracking, NULL ); for ( int eye = 0; eye < VRAPI\_FRAME\_LAYER\_EYE\_MAX; eye++ ) { res.FrameMatrices.EyeView[eye] = vrapi\_GetEyeViewMatrix( &app->GetHeadModelParms(), &CenterEyeViewMatrix, eye ); res.FrameMatrices.EyeProjection[eye] = ovrMatrix4f\_CreateProjectionFov( vrFrame.FovX, vrFrame.FovY, 0.0f, 0.0f, 1.0f, 0.0f ); } // Update uniform variables and add needed surfaces to the surface list. BackGroundTexture = GlTexture( BackgroundTexId, 0, 0 ); GlobeProgramColor = Vector4f( 1.0f, 1.0f, 1.0f, 1.0f ); res.Surfaces.PushBack( ovrDrawSurface( &GlobeSurfaceDef ) ); // Initialize the FrameParms. FrameParms = vrapi\_DefaultFrameParms( app->GetJava(), VRAPI\_FRAME\_INIT\_DEFAULT, vrapi\_GetTimeInSeconds(), NULL ); for ( int eye = 0; eye < VRAPI\_FRAME\_LAYER\_EYE\_MAX; eye++ ) { FrameParms.Layers[0].Textures[eye].ColorTextureSwapChain = vrFrame.ColorTextureSwapChain[eye]; FrameParms.Layers[0].Textures[eye].DepthTextureSwapChain = vrFrame.DepthTextureSwapChain[eye]; FrameParms.Layers[0].Textures[eye].TextureSwapChainIndex = vrFrame.TextureSwapChainIndex; FrameParms.Layers[0].Textures[eye].TexCoordsFromTanAngles = vrFrame.TexCoordsFromTanAngles; FrameParms.Layers[0].Textures[eye].HeadPose = vrFrame.Tracking.HeadPose; } FrameParms.ExternalVelocity = Scene.GetExternalVelocity(); FrameParms.Layers[0].Flags = VRAPI\_FRAME\_LAYER\_FLAG\_CHROMATIC\_ABERRATION\_CORRECTION; res.FrameParms = (ovrFrameParmsExtBase *) & FrameParms; return res; }## Specify the Render Mode:

In your app Configure(), specify the appropriate render mode. To configure the app to render using the surfaces returned by Frame, set the following:

settings.RenderMode = RENDERMODE\_STEREO;Multi-view Render Path

Before enabling the multi-view rendering path, you will want to make sure your render data is multi-view compatible. This involves:

Position Calculation

App render programs should no longer specify Mvpm directly and should instead calculate gl\_Position using the system provided TransformVertex() function which accounts for the correct view and projection matrix for the current viewID.

Per-Eye View Calculations

Apps will need to take into consideration per-eye-view calculations: Examples follow:

Per-Eye Texture Matrices:

In the DrawEyeView path, the texture matrix for the specific eye was bound at the start of each eye render pass. For multi-view, an array of texture matrices indexed by VIEW\_ID should be used.

Note: Due to a driver issue with the Adreno 420 and version 300 programs, uniform array of matrices should be contained inside a uniform buffer object.Stereo Images:

In the DrawEyeView path, the image specific to the eye was bound at the start of each eye render pass. For multi-view, while an array of texture index by VIEW\_ID would be preferable, Not all supported platforms support using texture arrays. Instead, specify both textures in the fragment shader and the selection determined by the VIEW\_ID.

External Image Usage

Applications which make use of image\_external, i.e. video rendering applications, must take care when constructing image\_external shader programs.

Not all drivers support image\_external as version 300. The good news is that drivers which fully support multi-view will support image\_external in the version 300 path, which means image\_external programs will work correctly when the multi-view path is enabled. However, for drivers which do not fully support multi-view, these shaders will be compiled as version 100.

These shaders must continue to work in both paths, i.e., version 300 only constructs should not be used and the additional extension specification requirements, listed above, should be made.

For some cases, the cleanest solution may be to only use image\_external during Frame to copy the contents of the external image to a regular texture2d which is then used in the main app render pass (which could eat into the multi-view performance savings)

Enable Multi-view Rendering

Finally, to enable the multi-view rendering path, set the render mode in your app Configure() to the following:

settings.RenderMode = RENDERMODE\_MULTIVIEW;