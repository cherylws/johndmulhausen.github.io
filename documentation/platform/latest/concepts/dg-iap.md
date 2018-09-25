---
title: Commerce (IAP)
---
In-app purchases (IAP) allow users to purchase items without leaving your app.

There are two types of items that you can offer in your game, consumable and durable.

* Durable - Durable items are single-use items that persist with the user. Meaning, once the item has been purchased, it cannot be purchased again. For example, you may offer the initial game download for free with only a demo level, then offer additional levels as in-app purchases.
* Consumable - Consumable items can be purchased multiple times. For example, consumable IAP may be 'character lives' or 'coins' that are used during the course of gameplay. Consumable purchases must be ingested by your app before they can be made available for purchased again.
Note: All IAP operations require the user to be connected to the internet.## Defining Items for Purchase

Before you begin integrating the IAP methods in your experience, you’ll need to define the items that you will be offering for purchase. The in-app purchase list can be updated or modified at any time.

At the moment there is no support for selling a single item with multiple currencies. A separate SKU will need to be created for each item and currency combination.

To define your IAP create a tab-separated (.tsv) file in the following format.

SKUNAMEDescriptionCurrencyAmountItem Typeunlock\_level\_2Level 2 Unlock

Purchase this item to unlock the 2nd level in the game.

USD9.99durable100\_coins100 Coins

100 coins to spend as in-game currency.

USD2.99consumableThe values for the items in the table above are:

* SKU - The unique string that you use to reference the IAP item in your app. The SKU is case-sensitive, the name you define in the Dashboard must exactly match the SKU you reference in your code. 
* Name - The short descriptive name that the user will see.
* Description - The full description of the item the user will see. Be as descriptive as necessary to avoid any confusion. 
* Currency - Currency is the unit of currency that the item will be charged in. Only USD is supported at this time. The IAP item will be converted to the local user's preferred currency at the time of purchase. 
* Amount - The amount to charge for the IAP item. Available prices are listed below.
* Item Type - The type of item for sale. Options are consumable and durable. Please see the description above for the difference between the two. 
An IAP item template is available for download from the [IAP](https://dashboard.oculus.com/app/iap) section of the Developer Center. Once you’ve created your file, you can upload your IAP items by selecting **Upload TSV** and following the on-screen prompts.

Note: You must enter your payment information before you can download the template or upload a file.**Available IAP Prices**

The following are the supported IAP item price tiers:

$0.01, $0.10, $0.99, $1.49, $1.99, $2.00, $2.37, $2.49, $2.67, $2.75, $2.99, $3.34, $3.99, $4.99, $5.35, $5.99, $6.69, $6.99, $7.49, $7.99, $8.99, $9.69, $9.99, $10.49, $10.99, $11.99, $12.99, $14.99, $16.74, $16.99, $18.74, $19.99, $20.99, $22.49, $22.99, $24.99, $26.99, $27.99, $29.99, $33.49, $34.99, $36.99, $39.99, $44.99, $45.99, $48.99, $49.99, $54.99, $59.99, $69.99, $79.99 $89.99, $99.99, $159.99, $199.99

## Integrating IAP - Unity & Unreal

Once you’ve finished defining the items that you would like to offer as purchases, you can start building them as purchasable items into your app.

The following SDK methods can be called from your client app. Detail about each function can be found in the Platform SDK [Reference Content](/documentation/platform/latest/concepts/book-reference/ "The Platform SDK developer reference contains a complete list of the Platform SDK headers, functions, and data structures.").

* **Retrieve the user's purchased items:**

Native - ovr\_IAP\_GetViewerPurchases()

Unity - Platform.IAP.GetViewerPurchases()

Retrieve a list of IAP purchases that the user has made. This list will include all durable type purchases and any consumable type purchases that have not been consumed. 


* **Retrieve a list of available items and prices by SKU:**

Native - ovr\_IAP\_GetProductsBySKU()

Unity - Platform.IAP.GetProductsBySKU()

Retrieve a list of IAP items that are available to the user to purchase. 


* **Launch the checkout flow for a SKU (Purchase an item):**

Native - ovr\_IAP\_LaunchCheckoutFlow()

Unity - Platform.IAP.LaunchCheckoutFlow()

Launch the checkout flow for a user to complete the purchase of a specified user. 


* **Consume a purchased item:**

Native - ovr\_IAP\_ConsumePurchase()

Unity - Platform.IAP.ConsumePurchase()

Consume (use) a consumable type IAP item indicating that the item was used in-app. 


## Example Implementation

The following Unity example demonstrates the end-to-end flow of retrieving information for an IAP item, displaying that information to the user, consuming any outstanding purchases, and initiating the checkout flow when a user indicates that they would like to make a purchase. The following example is taken from the VRBoardGame sample app. Please see the [Sample Apps](/documentation/platform/latest/concepts/book-sampleapp/) page for more information about the apps that are available.

using UnityEngine; using Oculus.Platform; using Oculus.Platform.Models; using UnityEngine.UI; // This class coordinates In-App-Purchases (IAP) for the application. Follow the // instructions in the Readme for setting up IAP on the Oculus Dashboard. Only // one consumable IAP item is used is the demo: the Power-Ball! public class IAPManager : MonoBehaviour { // the game controller to notify when the user purchase more powerballs [SerializeField] private GameController m\_gameController; // where to record to display the current price for the IAP item [SerializeField] private Text m\_priceText; // purchasable IAP products we've configured on the Oculus Dashboard private const string CONSUMABLE\_1 = "PowerballPack1"; void Start() { FetchProductPrices(); FetchPurchasedProducts(); } // get the current price for the configured IAP item public void FetchProductPrices() { string[] skus = { CONSUMABLE\_1 }; IAP.GetProductsBySKU(skus).OnComplete(GetProductsBySKUCallback); } void GetProductsBySKUCallback(Message<ProductList> msg) { if (msg.IsError) { PlatformManager.TerminateWithError(msg); return; } foreach (Product p in msg.GetProductList()) { Debug.LogFormat("Product: sku:{0} name:{1} price:{2}", p.Sku, p.Name, p.FormattedPrice); if (p.Sku == CONSUMABLE\_1) { m\_priceText.text = p.FormattedPrice; } } } // fetches the Durable purchased IAP items. should return none unless you are expanding the // to sample to include them. public void FetchPurchasedProducts() { IAP.GetViewerPurchases().OnComplete(GetViewerPurchasesCallback); } void GetViewerPurchasesCallback(Message<PurchaseList> msg) { if (msg.IsError) { PlatformManager.TerminateWithError(msg); return; } foreach (Purchase p in msg.GetPurchaseList()) { Debug.LogFormat("Purchased: sku:{0} granttime:{1} id:{2}", p.Sku, p.GrantTime, p.ID); } } public void BuyPowerBallsPressed() { #if UNITY\_EDITOR m\_gameController.AddPowerballs(1); #else IAP.LaunchCheckoutFlow(CONSUMABLE\_1).OnComplete(LaunchCheckoutFlowCallback); #endif } private void LaunchCheckoutFlowCallback(Message<Purchase> msg) { if (msg.IsError) { PlatformManager.TerminateWithError(msg); return; } Purchase p = msg.GetPurchase(); Debug.Log("purchased " + p.Sku); m\_gameController.AddPowerballs(3); } } ## Integrating IAP- Unreal

To use IAP with UE4 apps, please review the information about calling the native C APIs on the [Unreal Development Getting Started](/documentation/platform/latest/concepts/pgsg-unreal-gsg/ "The Unreal getting started guide will walk you through the basics of setting up your development environment and checking the user's entitlement.") page.

## S2S REST Requests

Our S2S REST APIs are available as a secure channel to interact with the Oculus Platform. For example, you may wish to track and consume coins purchased through in-app purchases on your trusted server. This prevents any client-side tampering to grant unpurchased gems. Using the S2S APIs are not required, but may be used if you wish. 

See the [Server-to-Server API Basics](/documentation/platform/latest/concepts/pgsg-s2s-basics/ "Some platform features use server-to-server (S2S) REST API calls to perform actions not appropriate to be sent from client devices. These APIs are provided to ensure a secure interaction between your back-end servers and the Oculus Platform.") page for information about interacting with our APIs.

ParameterRequiredDescriptionTypeExampleskuY

The sku for the item, defined when created on the Developer Center.

string

"50\_gems"**Verify Item Ownership**

Verify that a user owns an item.

Example Request

$ curl -d "access\_token=$USER\_ACCESSTOKEN" -d "sku=$SKU" https://graph.oculus.com/$APPID/verify\_entitlementExample Response

{"success":true}**Consume an IAP Item**

Consume an IAP item that a user has purchased.

Example Request

$ curl -d "access\_token=$USER\_ACCESSTOKEN" -d "sku=$SKU" https://graph.oculus.com/$APPID/consume\_entitlementExample Response

{"success":true}**Retrieve Items Owned**

Retrieve a list of items that the user owns.

Example Request

$ curl -G -d "access\_token=$USER\_ACCESSTOKEN" -d "sku=$SKU" -d 'fields'='item{skus},id' https://graph.oculus.com/$APPID/viewer\_purchasesExample Response

{ "data": [ { "id": "963119010431337", "item": { "sku": "EXAMPLE1" } } ] }## Test IAP

You can test your IAP integration by creating test users for your organization. These test users have permission to purchase IAP items in your app, including Alpha, Beta, and Release Candidate apps, without using real money. These users will work with all applications in your organization and can be deleted at any time.

Create a test user by navigating to your Org's publishing page on the Developer Center and selecting **Test Users** in the Settings menu. On this page, select **+ Add Test User** and enter a password and pin for the user. Click **Submit** to create the user. This user will be assigned a name and an email address similar to the account creator, and a unique Oculus Id. The test user inherits permissions to all apps and channels of the Organization that the user is created in.

Once the test user has been created, log in to that account using the generated email and password you created and add a payment method for the user. Since this user will be testing the IAP checkout flow, add the following credit card numbers to test different IAP flows.

* Always succeeds - 4111 1177 1155 2927
* Fails at sale - 4111 1193 1540 5122 
These cards only work with test users and can only be used within your organization. When using the test credit cards you must use a valid address, an expiration date that has not already passed, and 111 for the Security Code.

Note: Do not use a real credit card with test users, it will be charged as a regular transaction. Please use the test credit card numbers provided.Once the test user has been created and payment methods have been added, login to the Oculus Store as the test user and download the app that you would like to test. This entitles the user to the app and allows them to complete the IAP purchase process. Information about downloading test and development builds can be found in the [Testing and Releasing Builds](/distribute/latest/concepts/publish-release-channels/) section.

