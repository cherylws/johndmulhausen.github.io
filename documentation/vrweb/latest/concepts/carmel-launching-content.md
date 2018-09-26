---
title: Launching Your Content
---



From an Android 2D browser such as Chrome you can tap a link with the `ovrweb` protocol to launch Carmel Developer Preview to the URL that follows the protocol. The example below shows how to create HTML links and perform JavaScript navigation using the `ovrweb` protocol. 

```
&lt;!-- Launch Carmel Developer Preview using standard links, replace http://ocul.us/experience with your URL --&gt;
&lt;a href="ovrweb:http://ocul.us/experience"&gt;
  Navigate to an HTTP experience
&lt;/a&gt;
&lt;a href="ovrweb:https://ocul.us/experience"&gt;
  Navigate to an HTTPS experience
&lt;/a&gt;

&lt;script&gt;
// You can also navigate programmatically from script
function onClick() {
  // Replace http://ocul.us/experience with your URL
  window.location.href = "ovrweb:http://ocul.us/experience";
}
&lt;/script&gt;
```

From within a VR experience, you can navigate to other VR experiences using standard web navigation methods. The `ovrweb` protocol can also be used from within Carmel Developer Preview to navigate, but is not required. Navigating to 2D websites is not currently supported in Carmel Developer Preview. 
