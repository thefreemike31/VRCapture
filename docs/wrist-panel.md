# Wrist controls in VR

Before arming, open **Settings** and choose **Wrist panel: Left** or **Right**. The default is Off. Choose Near wrist, Offset from wrist, or Farther out to avoid a game's own wrist HUD.

Raise that wrist and look toward the front of the panel. **Always show** relaxes the viewing-angle requirement; the controller must still be tracked and the panel in view. The panel shows recording state, elapsed/saved time, and microphone/game meters.

## Use the controls

This beta uses **head aiming**, not controller pointing or eye tracking. A dot shows where your head is aimed on the panel. Hold the dot on a button for about 1.5 seconds as its progress fills.

- **Arm:** prepare recording before launching or returning to a supported game.
- **Cancel:** cancel an armed take that has not begun.
- **Stop recording:** reveals a separate **Confirm Stop** target; aim at that target and dwell again.

After saving completes, you can re-arm. Pause/resume is not implemented. The recorder still provides audible alarms; a visual notice cannot survive a failed headset/runtime connection.

## Keep it out of the video

**OpenXR source:** leave **Include wrist panel in recording** off. The headset receives the panel after the recorder captures game layers. Turn inclusion on to demonstrate VRCapture. Normal crop/framing can still put a wrist outside the recorded image. This capture path also applies to supported OpenXR games running on SteamVR; compatibility must be tested with your setup.

**SteamVR / OpenVR compositor source:** a visible panel is already part of SteamVR's mirror and appears in the recording. Its settings explain this limitation. Turning the wrist panel off removes it from both headset and recording. Independent exclusion for native OpenVR is not part of this beta.

Some SteamVR controller drivers may lack the grip-pose data used for placement. The recorder reports a wrist error and hides the panel in that case; video capture is separate. Describe your controller/runtime when reporting positioning problems.
