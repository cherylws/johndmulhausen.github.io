---
title: Oculus Go Accessories Guidelines
---
This document provides design guidelines for physical and electrical interfaces on Oculus hardware products, allowing for development of compatible accessories.

When developing Oculus Go accessories, consider the following general guidelines:

* Keep in mind that comfort is paramount, as accessories will be used during immersive VR experiences which can add a dimension to traditional user experience.
* Keep in mind that the fit of accessories, including straps, not only impacts physical comfort in the headset, but can also impact how users experience content in VR.
* Weight is extremely important for comfort, and weight added farther from the user’s head is especially noticeable. 
3D files and high-resolution diagrams are available for download at [https://developer.oculus.com/downloads](/downloads).

## Guidelines for All Accessories

**Magnetic Interference**

It is recommended to avoid magnets and metal components in accessories.

**Radio Frequency Performance**

Materials and Coatings - Accessories should avoid the use of metal and conductive materials.

Antenna Keep-Out - Antenna keep out regions can be found on product drawings and surface files. Materials or coatings that absorb radio frequency can degrade wireless performance.

## Cases

**Access to Inputs and Interconnects**

Access to Controls - The accessory must permit the use to access and operate the devices mechanical controls such as, but not limited to:* Volume buttons
* Power button
**Access to Audio Jack and USB Connector**

1. The accessory must provide ready access to the audio jack. The audio jack opening must be at least 11.0 mm diameter.
2. The accessory must also provide unobstructed access to the usb connector. Recommended opening is 11.0 mm x 9.0 mm
3. The audio jack and usb connector openings must be designed with enough margin to compensate for shifting or dimensional changes of the accessory.
**Faceplate**

Accessories should not cover the faceplate or impact thermal performance

**Acoustics**

The accessory must not impair or degrade the acoustic performance

**Coupling**

Cases must not facilitate the conduction of sound from any speaker to any microphone

**Microphone openings**

Oculus Go has two microphones and both openings to the microphone cannot be blocked by the accessories. Refer to product drawing and surface files for actual locations.

**Speaker openings**

Oculus Go has two slotted speaker openings (one on the left strap arm and one on the right strap arm) where the sound from the integrate speakers will travel to the user's ears. Both openings cannot be blocked by the accessories. Refer to product drawing and surface files for actual location.

## Audio

Oculus Go allows for audio accessories that connect to the headset over a standard 3.5mm TRS jack.

**Mechanical Specifications**

Audio accessories must not detract from the visual user experience provided by the headset.

**Electrical Specifications**

Oculus Go is capable of driving a worst case 16Ω load at this headphone jack. The headphone jack uses a standard TRS pinout, with Left on Tip, Right on Ring, and Ground on Sleeve. No microphone capabilities will be enabled at the headphone jack. While the headphone jack is in use the standard Mic1 and Mic2 on Oculus Go will be enabled.

## Strap

Straps attach in one location on the top and 2 locations on each arm. Maximum strap width is 30.0 mm.

**Facial interface retention rings**

3D geometry is provided for existing retention rings

## Controller

Controller is not to be covered with metal or conductive material

**Buttons**

The accessory must permit the use to access and operate the devices mechanical controls such as, but not limited to:* Trigger
* Touchpad
* Home button
* Back button
## Power

Input power should be designed around a 5V/2A charger supporting the Dedicated Charging Port (DCP) or Charging Downstream Port (CDP) standards in the USB Battery Charging Specification Version 1.2. When using USB OTG, the headset can supply 5V/500mA, but USB device enumeration is currently not supported.

## Bluetooth

**HID Gamepads**

Oculus Go is compatible with Bluetooth HID Gamepads. The recommended input set for a gamepad is:* Face buttons
	+ Key 158 - BACK
	+ Key 172 - HOME
	+ Key 304 - BUTTON\_A
	+ Key 305 - BUTTON\_B
	+ Key 307 - BUTTON\_X
	+ Key 308 - BUTTON\_Y
	+ Key 316 - BUTTON\_MODE
	
* Directional pad
	+ Axis 0x10 - HAT\_X
	+ Axis 0x11 - HAT\_Y
	
* Shoulder buttons
	+ Key 310 - BUTTON\_L1
	+ Key 311 - BUTTON\_R1
	+ Axis 0x06 - THROTTLE or Key 313 - BUTTON\_R2
	+ Axis 0x0a - BRAKE or Key 312 - BUTTON\_L2
	
* Thumb sticks
	+ Key 317 - BUTTON\_THUMBL
	+ Axis 0x00 - X
	+ Axis 0x01 - Y
	+ Key 318 - BUTTON\_THUMBR
	+ Axis 0x02 - Z
	+ Axis 0x05 – RZ
	
