---
title: Unity Development Getting Started
---
The Unity getting started guide will walk you through the basics of setting up your development environment, initializing the SDK, and checking the user's entitlement. 

The [Sample Apps](/documentation/platform/latest/concepts/book-sampleapp/) are available as reference when implementing the steps on this page.

## Create an App

Before you can integrate the Platform SDK, you'll need to create an app if you have not done so already. To create an app see the information on the [Creating and Managing Apps](/documentation/publish/latest/concepts/publish-create-app/) page.

## Configure Your Development Environment

Configure your development environment by adding Oculus Platform Support to your Unity project. There are two ways to add the Oculus APIs to your Unity development environment. 

1. Navigate to the [Oculus Integration](https://www.assetstore.unity3d.com/en/#!/content/82022) page and select Import.
2. In the Editor, select the **Asset Store** tab, Search for 'Oculus Integration', and select **Import**.
Note: We recommend importing the complete integration package. This enables the core Oculus APIs, the Platform and Avatar APIs, and the [Social Starter](/documentation/avatarsdk/latest/concepts/avatars-sdk-unity-example-social/) sample scene. Read about the Social Starter, a sample scene that demonstrates how the Avatar and Platform APIs compliment each-other to create an engaging social experience.Once you've imported the Oculus Integration package, select the **Oculus Platform** tab at the top of the page and select **Edit Settings**. A panel will open for you to enter either your **Oculus Rift App Id** or **Gear VR App Id**. These are your unique app identifiers and can be retrieved from the [API](https://dashboard.oculus.com/app/api/) page on the Oculus Dashboard.

If you're planning to test your builds locally in standalone mode, also add valid test user credentials to the Use Standalone Platform section. Create test users for your organization in the [Developer Center](https://dashboard.oculus.com/) under the Settings tab. Additional information about using the SDK in Standalone Mode can be found below. 

## Configuring Your App for Local Development

The configuration steps in this section will allow developers to run local builds of the application during the development process. This process is required, otherwise local versions of the app will not pass the entitlement check that you'll integrate below.

1. Add the user(s) to your org. See the [Manage Your Organization and Users](/distribute/latest/concepts/publish-account-management-intro/) for information about managing your organization.
2. If some of your developers are not part of the application's organization, and they need to run your application outside the normal install directory. Add the registry key AllowDevSideloaded as DWORD(1) to the registry folder at HKLM\SOFTWARE\Wow6432Node\Oculus\OculusThis does not bypass having a valid entitlement, it just bypasses the directory check.
Once the steps above are completed the entitlement check will succeed when running a local build of your application.

## Initialize the SDK and Perform the Entitlement Check

The first step to integrating the SDK is implementing the initialization function. There are two initialization functions you can call with your App Id. One is synchronous and runs on the thread you initialize on, the other is asynchronous and allows you to perform other functions, including calls to the Platform SDK, while the SDK is initializing. We recommend using the asynchronous method for better app performance, especially on mobile, and less state management.

1. Synchronous - Platform.Core.Initialize()
2. Asynchronous - Platform.Core.AsyncInitialize()
For example:

Platform.Core.AsyncInitialize(appID)When using the asynchronous call, the SDK is placed in an intermediate initializing state before full initialization. In this initializing state you're able to run other processes, including making calls to asynchronous Platform SDK methods. Requests made to the Platform SDK in the initializing state will be queued and run after the SDK finishes initializing.

Then, after you've made the call to initialize the SDK, verify that the user is entitled to your app. This check must be made within 10 seconds of the user launching the app. 

Platform.Entitlements.IsUserEntitledToApplication().OnComplete(callbackMethod);Note: With older versions of Unity, you may need to call Request.RunCallbacks() to process the callbacks and retrieve the results of the check.After retrieving the response to the check, you'll need to handle the result. The following example immediately quits the application if the user is not entitled to your app. You may wish to handle the situation more gracefully by showing the user a message stating that you were unable to verify their credentials, suggest that they check their internet connection, then quit the app. *You may not allow the user to proceed in your app after a failed entitlement check.*

void callbackMethod (Message msg) { if (msg.IsSuccess) { // Entitlement check passed } else { // Entitlement check failed. Quit app } }**What is the Entitlement Check?**

Verifying that the user is entitled to your app is required to sell an app on the Oculus Store. This check verifies that the copy of your app is legitimate. The entitlement check does not require the user to be connected to the Internet. In the event of a failed check, you should handle the situation in your app. For example, show the user an error message and quit the app. A failed entitlement check wonâ€™t result in any action on its own.

Additional user verification is available if you want to verify the identity of the user to your back-end server. [User Verification](/documentation/platform/latest/concepts/dg-ownership/ "User Verification validates the identity of each user accessing your application.") provides a cryptographic nonce you can pass to verify that the user's identity. This method does not replace the entitlement check. 

Entitlement verification is required to distribute apps through the Oculus Store.

## Entitlement Check Best Practices

In order to properly perform entitlement checking, follow these recommendations:

* Use AsyncInitialize() rather than Initialize() for mobile apps. This is important because AsyncInitialize() does not block the initialization code, which allows your application to load faster. In addition, AsyncInitialize() does not throw an exception on Android if the initialization failed.
* Surround the platform API initialization code with a try/catch block, and treat any exceptions that are caught as if the entitlement check failed.
* Set App Id in OculusPlatformSettings in the Unity Editor, or call AsyncInitialize() with an explicit AppId argument. For Gear VR users: If you need to run Gear VR applications in the Unity Editor, you must provide Oculus login credentials (username/password) in the OculusPlatformSettings. Simply setting App Id isn't sufficient.
## Entitlement Check Sample Code

Here is an sample entitlement check class for a Unity application: 

using UnityEngine; using Oculus.Platform; public class AppEntitlementCheck: MonoBehaviour { void Awake () { try { Core.AsyncInitialize(); Entitlements.IsUserEntitledToApplication().OnComplete(EntitlementCallback); } catch(UnityException e) { Debug.LogError("Platform failed to initialize due to exception."); Debug.LogException(e); // Immediately quit the application. UnityEngine.Application.Quit(); } } void EntitlementCallback (Message msg) { if (msg.IsError) { Debug.LogError("You are NOT entitled to use this app."); UnityEngine.Application.Quit(); } else { Debug.Log("You are entitled to use this app."); } } } ## Use the SDK in Standalone Mode

Standalone mode allows you to initialize the Platform SDK in test and development environments. Standalone mode is useful for testing [Matchmaking](/documentation/platform/latest/concepts/dg-matchmaking-1intro/ "Matchmaking places users together in a shared multiplayer experience. User matching can be done by common skill or other criteria that you define. The Matchmaking service offers two modes, Quickmatch and Browse.") where you can run multiple apps on the same box to test your integration. Initializing in standalone mode limits the SDK from connecting any locally running Oculus Service processes.

Note: Initializing in standalone mode uses a different set of credentials from the other initialization processes. When initializing in standalone mode, use your Oculus developer account email and password.![](/images/documentation-platform-latest-concepts-pgsg-unity-gsg-0.png)  
To initialize the SDK in standalone mode, call Platform.InitializeStandaloneOculus to initialize in standalone mode with the OculusInitParams identified below. 

Where the OculusInitParams are formed:

{ public int sType; public string email; public string password; public UInt64 appId; public string uriPrefixOverride; }The Init Param values are: 

* sType - Credential struct type.
* email - Email address associated with Oculus account.
* password - Password for the Oculus account.
* appID - ID of the application (the user must be entitled to this app)
* uriPrefixOverride - optional override for https://graph.oculus.com
## Checking Errors

Sometimes things go wrong and you'll want to know what happened. Checking the error code and message can provide insight to what happened. Some errors have an accompanying message that you can display to your users if the error results from their actions. 

To check for an error:

1. With every request you make to the Oculus Platform, check to see if the message is an error by calling Platform.Message.IsError().
2. If the message is an error, then call Platform.Message.GetError() to retrieve the error object.
3. The error object contains information you can use to debug the reason for the error:
	* Error.GetHttpCode() returns an http code for the request, such as 400 or 500.
	* Error.GetCode() returns a code representing the class of error. For example, all errors with 100 as the code are invalid parameter errors. Different errors may map to the same code. Review the error message for specifics of what went wrong. For example, an invalid id or mission required param would both return errors with 100 as the code.
	* Error.getMessage() returns a the raw error as a JSON string, which include the fields:
		+ message: the description of the what went wrong and possibly how to debug/fix the issue.
		+ code: It typically matches Error.GetCode, except in cases when there is a conflict in client/server code. Use the value from Error.GetCode instead.
		+ fbtrace\_id: Helpful for when you are contacting support. We use this internally to find more information about the failing request.
		
	* Error.getDisplayableMessage() returns a message that you may optionally display to the user. It has none of the technical information obtained from Error.getMessage. An example displayable message could be `You're not yet ranked on this leaderboard.` if you are querying for the leaderboard of the app that the user has not been placed in. The value may be empty in the cases where it is a developer-caused error rather than a user-caused error.
	
