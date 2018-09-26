---
title: Sharing
---

The Oculus Platform allows users to share their VR experience with their Facebook network. 

Users who wish to share with their Facebook network first need to connect their Oculus account to their Facebook account. You may wish to encourage users to stream, to do so notify them that Sharing is available if they link their Oculus and Facebook accounts. Account linking is available in the **Settings** menu of the Oculus 2D app. 

When implementing any Sharing feature, you'll need to opt-in on the Oculus Platform. To enable Sharing, navigate to [Sharing](https://dashboard.oculus.com/app/sharing) in the Developer Center, check the box to indicate that you have read and accept the terms, and select **Save**.

If you do not want to enable sharing, you'll still need to navigate to the [Sharing](https://dashboard.oculus.com/app/sharing) page and select **Save** with the box unchecked. There is no default setting, you have to choose to enable or disable Sharing in order to publish your app.

There are two sharing options, Livestreaming and Photo Sharing. The sections below describe how to implement these features.

## Livestreaming

All sharing is initiated by the user through the Oculus Platform. However, there are a couple of SDK methods you should call at certain points in your game to accommodate livestreaming. For example, you should pause a livestream if the user is entering a password or credit card information. Then, once the user has finished that activity, you can resume the stream.

The following SDK methods can be called from the client app. To create an achievement, go to the [Achievements](https://dashboard.oculus.com/app/achievements) tab on the Developer Dashboard.

* **Check the livestream status:**

Native - ovr\_Livestreaming\_GetStatus()

Unity - Platform.Livestreaming.GetStatus()

Check the status of the livestream.


* **Pause the livestream: **

Native - ovr\_Livestreaming\_PauseStream()

Unity - Platform.Livestreaming.PauseStream()

Pause the livestream. 


* **Resume the livestream:**

Native - ovr\_Livestreaming\_ResumeStream()

Unity - Platform.Livestreaming.ResumeStream()

Resume the paused livestream. 




If you're using Unreal, please use the native C API using the information found in [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/).

**Testing Livestreaming**

Livestreaming a user's experience may have an impact on the performance of your app. We recommend testing how your app performs when a user is livestreaming and adjusting features and performance as appropriate. 

To test livestreaming in your app:

1. Add the ovr\_Livestreaming\_GetStatus() check to your app to determine when a user has enabled livestreaming. 
2. Upload a build to a testing channel in the Developer Center. Information about release channels and uploading builds can be found in the [Distribute](https://developer.oculus.com/distribute/latest) section of these docs. Any user who has been added to your app's organization will be able to test livestreaming.
3. Launch the app and initiate a livestream. Monitor the performance of your app while the livestream is running to determine if any adjustments are necessary. Please see the [Mobile Rendering Guidelines](https://developer.oculus.com/documentation/mobilesdk/latest/concepts/mobile-rendering/) page for best practices and performance requirements when developing Gear VR apps.
4. If adjustments are required during a livestream, enable them any time a user has initiated a livestream by checking ovr\_Livestreaming\_GetStatus().


## Photo Sharing

Photo Sharing allows users to post screen captures they take in VR to their Facebook network. If a user has not previously associated their Facebook and Oculus accounts, they will be prompted to do so the first time they are shown the sharing modal.

The following SDK method allows users to share photos from inside your app.

* Native - ovr\_Media\_ShareToFacebook&gt;
* Unity - Platform.Media.ShareToFacebook


When calling `ovr_Media_ShareToFacebook`, you’ll provide a path to an image that will be shared with Oculus Home. You’ll also be able to pass a text suggestion that will be populated in the post body of the modal presented to the user. They may edit the text before they post to their Facebook feed.

Photo Sharing supports PNG, GIF, and JPEG image formats.

If you're using Unreal, please use the native C API using the information found in [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/).

**Recording and Accessing Photos**

Photos that users want to share should be saved internally in your app. When a user initiates the request to share the photo, you’ll provide access to Oculus by sending a path to a file saved in the internal storage directory for your application.

* Native Android - If you save the photo to external (to the app) storage, you'll need to provide share permissions to the file. Android provides documentation about [sharing files](https://developer.android.com/training/secure-file-sharing/share-file.html).
* Unity Apps - If you save the photo to external (to the app) storage, you'll need to provide share permissions to the file. This can be done by explicitly providing access or by saving to system folders that the Oculus app has access to.


If you use external storage and the Oculus app does not have permission to access the file, the request will fail.

**Integration**

In general, use the following to launch the photo sharing modal:

```
OVRP_PUBLIC_FUNCTION(ovrRequest) ovr_Media_ShareToFacebook(const char *postTextSuggestion, const char *filePath, ovrMediaContentType contentType);
```

Where `*postTextSuggestion` is a default, pre-populated text for the post body and `*filePath` is the to a file in your app's internal storage directory that should be shared with Oculus Home. `ovrMediaContentType` is the media type of the file identified by the filePath. At this time only `ovrMediaContentType_Photo` is supported.

After calling `ovr_Media_ShareToFacebook`, the user will be shown an Oculus modal displaying their chosen photo. Here, the user can add their own message for the body of the post and select their desired privacy settings. 



![](/images/documentationplatformlatestconceptsdg-sharing-0.png)



The user can then select ‘Share to Facebook’ to complete the action, close the modal, and return to your app. A status of `SHARED` will be returned indicating if the user successfully shared the photo, or `CANCELLED` if the user canceled the action. An error will be returned if something went wrong.
