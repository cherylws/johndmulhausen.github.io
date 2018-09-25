---
title: UI and Input Handling
---
This guide describes resources for handling UI and input for native apps using VrAppFramework.

## Native User Interface

Applications using the application framework have access to the VrGUI interface code. The VrGUI system is contained in VrAppSupport/VrGui/Src. Menus are represented as a generic hierarchy of menu objects. Each object has a local transform relative to its parent and local bounds.

VrGUI may be used to implement menus in a native application, such as the Folder Browser control used in Oculus 360 Photos SDK and Oculus 360 Videos SDK (found in FolderBrowser.cpp).

VrGUI allows for functional improvements by implementing a component model. When a menu object is created, any number of components can be specified. These components derive from a common base class, defined in VRMenuComponent.h, that handles events sent from the parent VRMenu. Components can be written to handle any event listed in VRMenuEvent.h.

Events are propagated to child objects either by broadcasting to all children or by dispatching them along the path from the menuâ€™s root to the currently focused object. When handling an event a component can consume it by returning MSG\_STATUS\_CONSUMED, which will halt further propagation of that event instance. See VRMenuEventHandler.cpp for implementation details.

Examples of reusable components can be found in the native UI code, including DefaultComponent.h, ActionComponents.h and ScrollBarComponent.h.

## Input Handling

Input to the application is intercepted in the Java code in VrActivity.java in the dispatchKeyEvent() method. If the event is NOT of type ACTION\_DOWN or ACTION\_UP, the event is passed to the default dispatchKeyEvent() handler. If this is a volume up or down action, it is handled in Java code. Otherwise the key is passed to the buttonEvent() method, which passes the event to nativeKeyEvent().

nativeKeyEvent() posts the message to an event queue, which is then handled by the AppLocal::Command() method. 

In previous versions of the SDK, AppLocal::Command() called AppLocal::KeyEvent() with the event parameters. However, in 0.6.0 this was changed to buffer the events into the InputEvents array. Up to 16 events can be buffered this way, per frame.

Each time the VrThreadFunction executes a frame loop, these buffered events are passed into VrFrameBuilder::AdvanceVrFrame(), which composes the VrFrame structure for that frame. The InputEvents array is then cleared.

After composition, the current VrFrame is passed to FrameworkInputProcessing(), which iterates over the input event list and passes individual events to the native application via VrAppInterface::OnKeyEvent(). Native applications using the VrAppFramework should overload this method in their implementation of VrAppInterface to receive key events.

The application is responsible for sending events to the GUI or other systems from its overloaded VrAppInterface::OnKeyEvent(), and returning true if the event is consumed at any point. If OnKeyEvent() returns true, VrAppFramework assumes the application consumed the event and will not act upon it.

If the application passes an input event to the VrGUI System, any system menus or menus created by the application have a chance to consume it in their OnEvent\_Impl implementation by returning MSG\_STATUS\_CONSUMED, or pass it to other menus or systems by returning MSG\_STATUS\_ALIVE.

