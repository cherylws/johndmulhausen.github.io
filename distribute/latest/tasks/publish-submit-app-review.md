---
title: App Upload and Store Submission
---

The process for distributing your app begins by uploading your build to the Oculus Dashboard.

You may upload an app at any time during the development process, however there are some additional things to keep in mind when uploading for store review.

Plan to submit at least two weeks in advance of your target launch date to allow time for us to review your app and make changes if necessary. During this time we'll verify that your app meets the Virtual Reality Check Guidelines (VRCs) for either [Rift](/distribute/latest/concepts/publish-rift-app-submission/) or [Mobile](/distribute/latest/concepts/publish-mobile-req/). We'll review the content for production value, polish, and general utility or appeal. Once the review is complete, we will contact you with details about your placement within the Oculus Store, verify that your assets and copy meet our [design guidelines](https://scontent-sjc3-1.xx.fbcdn.net/v/t39.2365-6/10000000_2007708799495262_8508290021072044032_n.pdf?_nc_cat=111&amp;oh=5a41a1fd066453853ad1ee4880be6e93&amp;oe=5C5CF91A) and coordinate your release. 

For an overview of the app review process, see [Lifecycle of an Oculus VR App](/distribute/latest/concepts/publish-app-review/).

**Upload an App**

1. Verify that your build meets the content and technical design requirements set in [Designing for Distribution](/distribute/latest/concepts/publish-prep-app/ "All apps on the Oculus Store must meet our criteria for content and technical requirements.") if you're submitting to the Store channel. 
2. In the Developer Dashboard, copy or upload your app. Please see the [Uploading Gear VR Apps](https://developer.oculus.com/distribute/latest/concepts/publish-uploading-mobile/) or [Uploading Rift Apps](https://developer.oculus.com/distribute/latest/concepts/publish-uploading-rift/) for information about how to upload the apps to the Dashboard. Read more about the options for uploading on the [Release Channels](https://developer.oculus.com/distribute/latest/concepts/publish-release-channels/) page.
3. Click the **Submission Info** tab.
4. Click **Edit**.
5. Fill out all the fields in the **App Specifications** page and then click **Save and Continue**.
6. Fill out all the fields in the **About This App **page and then click **Save and Continue**.
7. If this is a Gear VR app, enter a GRAC rating on the **Content Rating** page. 
8. Request an IARC certificate from the **Content Rating** page and then click **Save and Continue**.
9. Fill out all the fields in the **Translations** page - this is information appears in your app's product description page. If you have localized descriptions and app titles for different languages: 
	1. Click **Manage Languages**.
	2. Add the language and then click **Update**.
	3. Fill the new fields with your localized content.
	
10. Click **Save and Continue**.
11. Add the art assets required on the **Assets** page and then click **Save and Continue**.
12. Specify an MSRP on the Pricing &amp; Distribution page and then click **Save and Continue**. Please note that once your app has been approved, you will not be able to make any changes to the app MSRP. You may choose to run a temporary sale, please contact submissions@oculus.com for information about running a sale. 
13. If there are any issues with your submission information, review and correct the errors on the **Submit Your App** page.
14. Click **Submit Your App**. 


If you submit your app for review to the Store Team, you should receive email confirmation. If you do not receive email confirmation, your app may not have been successfully submitted.

**Submit your App to the Store**

To submit your app to the Store for public release, follow the steps above for the Store Release Channel.

Once submitted, you'll be able to track the review progress:

* Submitted - your app has been received by Oculus, if you need to make changes you have one hour before it changes to “Under Review”.
* Under Review - we are checking if your app meets our requirements to be published on the Oculus Store. While under review you won't be able to make updates to the build, copy, assets, etc. If you need to make changes, email us at submissions@oculus.com.
* Changes Requested - we will move it to this status if edits are required to the app. You'll receive an email with specifics on what you need to change.


**Review Process**

The review process consists of three parts: Technical Review, Content Review, and Publishing Review.

The **technical review** verifies the app conforms to our Virtual Reality Check (VRC) guidelines [PC](/distribute/latest/concepts/publish-rift-app-submission/) and [Mobile](/distribute/latest/concepts/publish-mobile-req/), which includes things like meeting performance targets and Oculus-specific integrations like entitlement checks and reserved interactions. The results of these tests will be shown in the developer dashboard and also be sent to you via email. The [VRC Validator](/documentation/pcsdk/latest/concepts/dg-vrcvalidator/) is available to check your build before submitting for review.

During the **content review** phase, we evaluate apps based on their production value, polish, utility, and entertainment value.

The third phase is **publishing review**, where we will discuss details for your app release such as launch date, price, and assets. Oculus may make recommendations to any of these areas to maximize the impact of your launch.

You will receive an email as we complete each part of the process. When we request updates or changes, we will move your submission into “Changes Requested” status with an explanation of what you need to do. In order to proceed, resolve the issue and then resubmit the application to us. If you have any questions, send us a message on the forums or email submissions@oculus.com and we'll clarify your next steps. You can also email us if your submission is locked in “under review” status and you'd like us to put it into “changes requested” so that you can make updates.

**Post Review**

After the review has been completed, we'll update your status to one of the following:

* Approved: Your app is ready to publish. Oculus will coordinate with you what the date and time of your release will be. If you need to make updates to the build please wait until your app has gone live.
* Published: your app is published and live on the Oculus Store.
* Approved for keys: your app is approved to take advantage of the Oculus platform, but we will not provide discovery and marketing within the Oculus Store. Common reasons why apps are approved for keys are when the content is too advertorial, there's no compelling consumer use case, or the app is so low quality that it doesn't really work.
* Rejected: Rejections are rare and used only when apps break policies regarding security, adult content, and other serious violations.


Once the review is complete and your app is released, updates to the app binary do not require any additional review. The moment you upload a new version of your app binary to the Developer Dashboard's STORE channel, the app will be pushed out to all existing users of your app, immediately and without review. Please review the [Updating Published Apps](/distribute/latest/concepts/publish-content-updating/) for more information about updating apps that have already been published.

However, updates to the app metadata (banner images, descriptions, trailers, etc.) will require a review. This review will take 1-2 business days after submission. 
