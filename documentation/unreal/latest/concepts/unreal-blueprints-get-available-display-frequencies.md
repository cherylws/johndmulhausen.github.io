---
title: Get Available Display Frequencies
---

Returns the display frequencies that are available with the current headset. 

## Overview

The Oculus headsets provide different display frequencies (or frame rates). The Rift is always set to 90 Hz. Gear VR is always set to 60 Hz. However, Oculus Go can be set to either 60 Hz or 72 Hz. This blueprint returns to available display frequencies for the current head set. Thus, if a Rift is attached, this blueprint will simply return 60 Hz. However, if an Oculus Go is attached, this blueprint returns an array, where the first entry in the array (with index 0) is 60 Hz, and the second entry in the array (with index 1) is 72 Hz.

## Blueprint

![](/images/documentationunreallatestconceptsunreal-blueprints-get-available-display-frequencies-0.png)

## Arguments

* No arguments.


## Output

* Return Value: An array containing one or more available display frequencies. For the Oculus Rift and Gear VR, the output array contains a single entry, containing the values 90 Hz and 60 Hz, respectively. For the Oculus Go, the output array contains two entries, containing the values 60 Hz (index 0) and 72 Hz (index 1).


## Sample

In this sample, the Oculus Go frame rate is set to 72 Hz whenever the controller button is pressed down, and 60 Hz whenever the controller button has been released. (In a production application, the array length should be checked before accessing element 1 in the array.)

![](/images/documentationunreallatestconceptsunreal-blueprints-get-available-display-frequencies-1.png)
