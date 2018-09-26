---
title: Native Development Getting Started
---

The native getting started guide will walk you through the basics of setting up your development environment, initializing the SDK, and checking the user's entitlement. 

The [Sample Apps](/documentation/platform/latest/concepts/book-sampleapp/) are available as reference when implementing the steps on this page.

You'll need your App Id to call the initialization APIs on this page. Your App Id can be retrieved from the [API](https://dashboard.oculus.com/app/api/) page on the Oculus Dashboard.

## Create an App

Before you can integrate the Platform SDK, you'll need to create an app if you have not done so already. To create an app see the information on the [Creating and Managing Apps](/documentation/publish/latest/concepts/publish-create-app/) page.

## Configure Your Development Environment

The steps to configure your environment will be different depending on the type of app you're building. Follow the steps for the app you're building.

**Configure Your Development Environment for Rift**

Configuring Visual Studio for your Rift project is the first step in integrating the Oculus Platform SDK for your Rift app. The SDK download provides a loader that enables DLL signature verification and graceful detection of the Oculus Runtime. To use the loader:

1. In your Visual C++ project, open **Properties**, expand the **Linker** tab, and select **Input**. Then, add the loader library (LibOVRPlatform32\_1.lib or LibOVRPlatform64\_1.lib) to **Additional Dependencies**.
2. Add the cpp loader file (*InstallFolder*/Windows/OVR\_PlatformLoader.cpp) to your project.


**Configure Your Development Environment for Gear VR**

Configuring Android Studio for your Gear VR project is the first step in integrating the Oculus Platform SDK for your Gear VR app. There are two SDKs that you need to apply in the SDK Manager, **Tools / Android / SDK Manager**.

1. The Oculus Platform SDK provides a loader that enables .so signature verification and graceful detection of the Oculus Runtime. To use the loader, add the SDK location to the manager (*InstallFolder*/Android/libs/armeabi-v7a/libovrplatformloader.so). 
2. Then, add the Android NDK (found in the **SDK Tools** tab of the **SDK Manager**). The NDK is a set of tools that allows you to use C++ code on Android devices. The NDK also manages device activities and allows your app access to device sensors and inputs. 


## Configuring Your App for Local Development

The configuration steps in this section will allow developers to run local builds of the application during the development process. This process is required, otherwise local versions of the app will not pass the entitlement check that you'll integrate below.

1. Add the user(s) to your org. See the [Manage Your Organization and Users](https://developer.oculus.com/distribute/latest/concepts/publish-account-management-intro/) for information about managing your organization.
2. If some of your developers are not part of the application's organization, and they need to run your application outside the normal install directory. Add the registry key AllowDevSideloaded as DWORD(1) to the registry folder at HKLM\SOFTWARE\Wow6432Node\Oculus\OculusThis does not bypass having a valid entitlement, it just bypasses the directory check.


Once the steps above are completed the entitlement check will succeed when running a local build of your application.

## Initialize the SDK and Perform the Entitlement Check

The first step to integrating the SDK is implementing the initialization function. There are two initialization functions you can call with your App Id. One is synchronous and runs on the thread you initialize on, the other is asynchronous and allows you to perform other functions, including calls to the Platform SDK, while the SDK is initializing. We recommend using the asynchronous method for better app performance, especially on mobile, and less state management.

1. Synchronous:* Native Rift - ovr\\_PlatformIntializeWindows() * Native Gear VR - ovr\\_PlatformInitializeAndroid() 

The following example shows the synchronous initialization call for a Rift app, with another call to ovr\_Entitlement\_GetIsViewerEntitled(). The second call is the entitlement check that verifies that the user owns your app. Both steps are required to successfully initialize the SDK. The entitlement check must be made within 10 seconds of the user launching the app. 

// Initialization call if (ovr\_PlatformInitializeWindows(appID) != ovrPlatformInitialize\_Success) { // Exit. Initialization failed which means either the oculus service isn’t on the machine or they’ve hacked their DLL } ovr\_Entitlement\_GetIsViewerEntitled();When the SDK has finished initializing, a ovrMessage\_PlatformInitializeWindows message will be sent to the queue. 


2. Asynchronous:* Native Rift - ovr\\_PlatformInitializeWindowsAsynchronous() * Native Gear VR - ovr\\_PlatformInitializeAndroidAsynchronous() 

The example below shows the asynchronous initialization call for a Gear VR game. When using the asynchronous call, the SDK is placed in an intermediate initializing state before full initialization. In this initializing state you're able to run other processes, including making calls to asynchronous Platform SDK methods. Requests made to the Platform SDK in the initializing state will be queued and run after the SDK finishes initializing.

The second call in the example below is the entitlement check that verifies that the user owns your app. Both steps are required to successfully initialize the SDK.

// Initialization call if (ovr\_PlatformInitializeAndroidAsynchronous(appID) != ovrPlatformInitialize\_Success) { // Exit. Initialization failed which means either the oculus service isn’t on the machine or they’ve hacked their DLL } ovr\_Entitlement\_GetIsViewerEntitled(); When the SDK has finished initializing, a ovrMessage\_PlatformInitializeAndroidAsynchronous message will be sent to the queue. 




After initializing the SDK with either initialization method and making the entitlement check, you’ll need to check the response of the entitlement check and handle the result. The following example immediately quits the application if the user is not entitled to your app. You may wish to handle the situation more gracefully by showing the user a message stating that you were unable to verify their credentials, suggest that they check their internet connection, then quit the app. **You may not allow the user to proceed in your app after a failed entitlement check.**

```
// Poll for a response
while ((message = ovr_PopMessage()) != nullptr) 
  {
    switch (ovr_Message_GetType(message)) 
      {
        case ovrMessage_Entitlement_GetIsViewerEntitled:
                
          if (!ovr_Message_IsError(message))
             {
                // User is entitled.  Continue with normal game behaviour
              }
          else
             {
                // User is NOT entitled.  Exit
              }
          break;
      default:
   break;
   }
}
```

Please see the [Requests and Messages](/documentation/platform/latest/concepts/sdkgs-requestsnmessages/) page for information on how native apps interact with the Platform SDK.

**What is the Entitlement Check?**

Verifying that the user is entitled to your app is required to sell an app on the Oculus Store. This check verifies that the copy of your app is legitimate. The entitlement check does not require the user to be connected to the Internet. In the event of a failed check, you should handle the situation in your app. For example, show the user an error message and quit the app. A failed entitlement check won’t result in any action on its own.

Additional user verification is available if you want to verify the identity of the user to your back-end server. [User Verification](/documentation/platform/latest/concepts/dg-ownership/) provides a cryptographic nonce you can pass to verify that the user's identity. This method does not replace the entitlement check. 

Entitlement verification is required to distribute apps through the Oculus Store.

## Initializing in Standalone Mode

Standalone mode allows you to initialize the Platform SDK in test and development environments. Standalone mode is useful for testing [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/) where you can run multiple apps on the same box to test your integration. Initializing in standalone mode limits the SDK from connecting any locally running Oculus Service processes.

To initialize the SDK in standalone mode, call `ovr_Platform_InitializeStandaloneOculus` with the `OculusInitParams` identified below.

```
OVRPL_PUBLIC_FUNCTION(ovrRequest) 
  ovr_Platform_InitializeStandaloneOculus(
  const ovrOculusInitParams *params)
```

Where the `ovrOculusInitParams` are formed:

```
typedef struct
{
 ovrPlatformStructureType sType; 
 const char *email; 
 const char *password; 
 ovrID appId; 
 const char *uriPrefixOverride; 
} ovrOculusInitParams;
```

The Init Param values are: 

* sType - Credential struct type, must be: ovrPlatformStructureType\_OculusInitParams.
* email - Email address associated with Oculus account.
* password - Password for the Oculus account.
* appID - ID of the application (the user must be entitled to this app)
* uriPrefixOverride - optional override for https://graph.oculus.com


## Checking Errors

Sometimes things go wrong and you'll want to know what happened. Checking the error code and message can provide insight to what happened. Some errors have an accompanying message that you can display to your users if the error results from their actions. 

To check for an error:

1. With every request you make to the Oculus Platform, check to see if the message is an error by calling ovr\_Message\_IsError().
2. If the message is an error, then call ovr\_Message\_GetError() to retrieve the error object.
3. The error object contains information you can use to debug the reason for the error:* ovr\\_Error\\_GetHttpCode() returns an http code for the request, such as 400 or 500. * ovr\\_Error\\_GetCode() returns a code representing the class of error. For example, all errors with 100 as the code are invalid parameter errors. Different errors may map to the same code. Review the error message for specifics of what went wrong. For example, an invalid id or missing required param would both return errors with 100 as the code. * ovr\\_Error\\_getMessage() returns a the raw error as a JSON string, which include the fields: + message: the description of the what went wrong and possibly how to debug/fix the issue. + code: It typically matches ovr\\_Error\\_GetCode, except in cases when there is a conflict in client/server code. Use the value from ovr\\_Error\\_GetCode instead. + fbtrace\\_id: Helpful for when you are contacting support. We use this internally to find more information about the failing request. * ovr\\_Error\\_getDisplayableMessage() returns a message that you may optionally display to the user. It has none of the technical information obtained from ovr\\_Error\\_getMessage. An example displayable message could be `You're not yet ranked on this leaderboard.` if you are querying for the leaderboard of the app that the user has not been placed in. The value may be empty in the cases where it is a developer-caused error rather than a user-caused error. 



