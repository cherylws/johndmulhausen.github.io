---
title: Browser Navigation in VR
---

This navigation sample demonstrates how to utilize browser history APIs and the back button to make deep-linkable experiences.

This sample pushes navigation state when the user taps the trackpad (or clicks) and when the user hits the back button, this state is popped.

![](/images/documentationvrweblatestconceptscarmel-navigation-0.png)

## About Deep Linking

A single webpage can represent multiple logical locations (or states). For example, your application may allow a user to traverse a multi-level menu. When the user hits the back button, you want your application to return to the parent menu without a page navigation. This is made possible with the history APIs.

By representing navigation state in the URL, you enable deep linking. For example, you could send a link to a friend that opens Oculus Browser directly into a sub-menu. 

## State and the Browser history API 

Applications typically have three states:

* Transient 
	+ If you refresh the browser, the state is lost (or reset).
	+ Transient state is not persisted to the URL.
	
* Persistent 
	+ If you change this state, history.replaceState is used to preserve the change. 
	+ An example of this is the current gaze angle. You would not want to cause additional breadcrumbs to be pushed every time the gaze angle changes, however you may want to persist this so that deep links can link directly into a particular gaze. 
	
* Navigation 
	+ If you change this state, history.pushState is used to preserve the change. 
	+ If you hit the back button, the previous navigation state is restored. 
	+ An example of this is the application location (such as sub menu). When the current sub menu changes you want to persist this in the URL as well as push a breadcrumb on the history. 
	


## Hardware back button

The hardware back button will cause the `window.popstate` event to be raised if state had been previously pushed with `history.pushState`.

## Sample code

When your application first starts, you need to load persisted state from the URL. 

```
// Helper method to convert query parameters to json
function getJsonFromUrl() {
    var query = location.search.substr(1);
    var result = {};
    query.split("&amp;").forEach(function(part) {
    var item = part.split("=");
    result[item[0]] = decodeURIComponent(item[1]);
    });
    return result;
}

// Update our state from the current location
function loadFromUrl() {
    var urlArgs = getJsonFromUrl();
    changeState(Number(urlArgs.depth) || 1, true);
}
```

When you want to change persisted state, you must update the URL, and call the appropriate history API.

```
// When we change the state, we need to update the location and re-render the canvas (to visualize the change)
function changeState(newState, replace) {
    depth = newState;
    var path = window.location.pathname + "?";
    // Encode the state as query parameters in the URL.  This makes it so we can copy/paste the URL and end up in the same state.
    path += "depth=" + encodeURIComponent(depth);
    if (replace) {
    // Sometimes you want to replace the state, which doesn't push anything onto the backstack.  For example you might encode the camera yaw
    // as state that doesn't change the backstack.
    window.history.replaceState({}, "Navigation", path);
    } else {
    // Some state changes are considered by the user to be a new breadcrumb in the history.  For example if you are navigating through a menu,
    // you would represent each 'depth' of the menu as a breadcrumb by calling pushState.  This doesn't actually navigate the browser.
    window.history.pushState({}, "Navigation", path);
    }
    renderCanvas(depth, path);
};
```

When the user presses the back button, the `onpopstate` event will be raised. We respond to this by re-loading the state from the URL.

```
// When the browser pops the state, we need to load the state from the Url again.
// The Gear VR back button will cause this event to be raised.
window.onpopstate = loadFromUrl;
```

## Conclusion

Persisting important states to the URL and working with the history APIs is easy to do and improves the experience of your WebVR application running in Oculus Browser. 

The full sample can be found [here](https://s3.amazonaws.com/static.oculus.com/carmel/WebVRSamples/Navigation/index.html).
