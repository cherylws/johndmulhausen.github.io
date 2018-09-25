---
title: App Deeplinking
---
App Deeplinking allows you to launch users directly into an app event or gameplay mode.

For example, you may have two separate applications, one single player and one multiplayer, and want to allow to join a multiplayer session from the single player app. This requires an integration in both apps. The app the request originates from, and the target app.

## Integrate App Deeplinking

**In the Originating App**

The originating app will call the following API to launch another application.

* **Launch other app:**

Native - ovr\_Application\_LaunchOtherApp()

Unity - Platform.Application.LaunchOtherApp()

Launches another application, defined by that applications app\_id with an optional deeplink message that can be used to tell the target application how or in what mode to launch.


For example, a request from a native application may resemble:

ovrApplicationOptionsHandle options = ovr\_ApplicationOptions\_Create(); ovr\_ApplicationOptions\_SetDeeplinkMessage(options, "abc"); ovr\_Application\_LaunchOtherApp(<app\_id>, options);And in Unity:

var options = new ApplicationOptions(); options.SetDeeplinkMessage("abc"); Platform.Application.LaunchOtherApp(<app\_id>, options);Once you've made the request, check to see if the target application was launched successfully. The request will only succeed if the user is both entitled to (owns) and has installed the target app. If the user does not own the app, or has not downloaded the app, they will be directed to the product information page in Oculus Horizon where they can purchase and download the app. 

Rift only - After receiving the notification that the target app was launched successfully, you must quit the originating app yourself before the target app can continue. 

**In the Target App**

Apps launched by ovr\_Application\_LaunchOtherApp() will launch as normal, but will receive a notification of type ovrMessage\_Notification\_ApplicationLifecycle\_LaunchIntentChanged on the message queue.

On startup check for this notification and call ovr\_ApplicationLifecycle\_GetLaunchDetails() to retrieve information about how the app was launched. All notifications generated by this API will have a launch type of DEEPLINK. This information allows you to direct the user to the proper app location. 

Note: The notification described on this page will not be sent to users using version 3.30 (or earlier) of Oculus Home and Horizon and who's app had previously been running in the background when the ovr\_Application\_LaunchOtherApp API was called. **Unreal Development**

If you're using Unreal, please use the native C API using the information found in [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/ "The Unreal getting started guide will walk you through the basics of setting up your development environment and checking the user's entitlement.").
