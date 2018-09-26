---
title: "Oculus Go: Switching Display Refresh Rate"
---

With Oculus Go, you can switch the frame rate between 60 Hz and 72 Hz. 

## Overview

All mobile devices must deal with heat and battery issues. Mobile chipsets are very efficient, but they still generate a significant amount of heat and draw a lot of battery power during computationally intense tasks. On a phone or tablet, it is normal for an overtaxed mobile CPU to simply slow down in order to avoid overheating. On a VR device, that approach generally leads to a loss of application frame rate, which reduces the quality of the experience and can immediately make users uncomfortable. One solution is to dynamically downgrade the display frequency from 72 Hz to 60 Hz during heavy rendering.

Three Blueprints are provided to help you mange the display frequency:

**Get Available Display Frequencies**

This Blueprint retrieves an array of floats that represent the available display frequencies. 

![](/images/documentationunreallatestconceptsunreal-switching-display-refresh-rate-go-0.png)

For Oculus Go, the return values may be:

* Index 0 = 60 Hz
* Index 1 = 72 Hz


For Gear VR, the only return value is:

* Index 0 = 60 Hz


 For Oculus Rift, the only value is:

* Index 0 = 90 Hz


**Get Current Display Frequency**

This Blueprint retrieves a float that represents the current display frequency.

![](/images/documentationunreallatestconceptsunreal-switching-display-refresh-rate-go-1.png)

**Set Display Frequency**

This Blueprint Accepts a float and sets the current display frequency to that value. That float value must equal a valid display frequency for the headset.

![](/images/documentationunreallatestconceptsunreal-switching-display-refresh-rate-go-2.png)

**Best Practice for Setting Display Frequency**

It is generally a good practice to set the display frequency based on what Get Available Display Frequencies returns. The following Blueprints sample sets the frame rate to 72 Hz for the Oculus Go:

![](/images/documentationunreallatestconceptsunreal-switching-display-refresh-rate-go-3.png)

Here is another sample, where the frame rate is set to 72 Hz while the controller button is pushed down, and 60 Hz otherwise. (In a production application, the array length should be checked before accessing element 1 in the array.)

![](/images/documentationunreallatestconceptsunreal-switching-display-refresh-rate-go-4.png)
