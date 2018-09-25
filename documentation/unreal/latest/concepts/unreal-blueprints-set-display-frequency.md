---
title: Set Display Frequency
---
Sets the display frequency (frame rate) for Oculus Go to either 60 Hz or 72 Hz.

## Overview

The Oculus headsets support different display frequencies (frame rates). The Oculus Rift is always set to 90 Hz. Gear VR is always set to 60 Hz. However, Oculus Go can be set to either 60 Hz or 72 Hz. This blueprint sets the display frequency, in frames per second, for the Oculus Go to a floating point value that is either 60.0 or 72.0.

Also see [Get Available Display Frequencies](/documentation/unreal/latest/concepts/unreal-blueprints-get-available-display-frequencies/ "Returns the display frequencies that are available with the current headset.").

## Blueprint

![](/images/documentation-unreal-latest-concepts-unreal-blueprints-set-display-frequency-0.png)  
## Arguments

* Requested Frequency: A floating point value that indicates the desired display frequency, in frames per second. Allowable values for Oculus Go are: 60.0 and 72.0.
## Output

* No output.
## Sample

In this sample, the Oculus Go frame rate is set to 72 Hz whenever the controller button is pressed down, and 60 Hz whenever the controller button has been released. (In a production application, the array length should be checked before accessing element 1 in the array that is output by [Get Available Display Frequencies](/documentation/unreal/latest/concepts/unreal-blueprints-get-available-display-frequencies/ "Returns the display frequencies that are available with the current headset.").)![](/images/documentation-unreal-latest-concepts-unreal-blueprints-set-display-frequency-1.png)  
