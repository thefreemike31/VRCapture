# Microphone, game audio and editing

## Pick the right devices

Connect your headset before selecting audio. Click **Refresh devices** if a device is missing. With Virtual Desktop, enable microphone passthrough and select **Microphone (Virtual Desktop Audio)**. With Steam Link or Link, select the microphone supplied by that connection, or your usual narration microphone.

**Automatic game output** resolves the game's audio output when a take starts, falling back to the Windows default when necessary. It does not follow a device switch halfway through a take. It captures everything playing through that output, including other applications. To change the route, finish the take, select a device, then arm again.

## Balance voice and gameplay

The microphone and game sliders independently scale the recorded audio. Start at mic 100% and game 65%, speak at your usual volume, and listen to a short recorded take. Lower the game further if it masks narration. Meters work while armed and recording.

Increasing a quiet microphone also raises its noise. Lowering the recorder slider cannot repair distortion already present at the microphone input. If input is distorted, adjust the headset/input level first. A 120% microphone setting is only a modest boost; it cannot overcome an overwhelmingly loud game mix.

## Separate tracks for DaVinci Resolve

Choose **Editing: Mix + Microphone + Game** before arming. The MP4 contains:

| Audio stream | Contents |
| --- | --- |
| 1 — Mix | Microphone and game together, for normal playback |
| 2 — Microphone | Narration alone, with the microphone slider applied |
| 3 — Game | Game output alone, with the game slider applied |

Import the MP4 into Resolve. Depending on its import settings, you may need **Clip Attributes > Audio** to expose the embedded streams as separate tracks. **Mute the Mix track when using Microphone and Game**, or the audio will be doubled. These are separate streams inside one MP4, not three finished audio files next to it.

For one combined playback track, choose **Mixed (game + microphone)** instead. Track mode is selected before arming; the volume sliders can be adjusted during recording.
