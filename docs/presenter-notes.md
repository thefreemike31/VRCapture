# Presenter notes in VR

Keep talking points on a separate wrist sheet while you record. Configure them on the desktop before launching your game.

1. Open **Settings > Presenter notes...**, enter your text and enable presenter notes.
2. Choose a wrist, paper size, text size and position. By default, notes use the opposite wrist from the recording controls. Notes also work with the recording panel off.
3. Leave **Thumb rest: tap to show / hide** checked for supported Touch controllers, then save and close.
4. Launch the game. The sheet starts hidden. Briefly touch the flat thumb rest beside the face buttons on the notes controller, then lift your thumb to show it. Tap and lift again to hide it. This is the physical thumb rest, not the thumbstick or a button press.
5. While the sheet is visible, hold that rest for **0.5 seconds** to turn one page. The last page wraps to the first. Lift before turning another page. Releasing a hold does not hide the notes; holding while hidden does nothing.

Lift your thumb once after startup or a focus/tracking interruption. Enable notes and thumb control before launching an OpenXR game; restart the game if you enabled them afterward.

## Head-aiming alternative

If your controller/runtime does not provide thumb-rest input, uncheck the thumb-rest option. Raise the notes wrist and look at the sheet. Aim your head at **Previous** or **Next** for about **0.35 seconds** to change pages. This navigation is also available on a visible thumb-controlled sheet while your thumb is lifted. The controls use head direction, not eye tracking.

## What appears in the recording

With the **OpenXR source**, presenter notes stay out of the saved video, including supported D3D11, D3D12, OpenGL and Vulkan games. This also applies when SteamVR runs the OpenXR game. The recording wrist panel has its own separate inclusion setting.

With the **SteamVR / OpenVR compositor source**, visible notes can appear in the saved mirror image. Independent exclusion is unavailable for that source. Make a short test before recording a presentation.

## Save and update

Text is saved locally in `presenter-notes.txt` beside the recorder; preferences and the current page are in `capture-settings.ini`. Keep both when updating. Neither personal file is included in the release ZIP. Notes support multiple pages, line breaks and up to 16,384 UTF-16 text units. Edit on the desktop; there is no in-headset text editor.

Extract the entire update, including the `input` folder and both `layers` folders. Close the game and recorder before replacing files. If notes are missing, check enablement, the chosen wrist, controller tracking and the desktop status. Try head aiming if thumb input is unavailable. See [troubleshooting](troubleshooting.md) and [recording wrist controls](wrist-panel.md).
