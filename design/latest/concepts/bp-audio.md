---
title: Audio
---

Audio plays a critical role in VR immersion. These best practices outline good VR audio design.

**Spatialize** audio for any sound that has an obvious in-app source. The audio should appear to come from same direction as the source. The source should also move to follow the user’s head movements when they wear headphones, but not if they use external speakers. Allow users to choose their output device in game settings, and make sure in-game sounds appear to emanate from the correct location by accounting for head position relative to the output device. Additionally, for positionally tracked apps, sound should get louder as the user leans towards their source, even if the avatar is otherwise stationary.

Not all sound needs to be spatialized. Ambient room noise, background music, and other sounds that have no obvious spatial source can be played without spatialization.

Audio plays an important role in the overall believability of the scene. We recommend every app include a spatialized audio SDK (whether you use the [Oculus Audio SDK](/documentation/audiosdk/latest/concepts/book-audio-intro/) or another method).
