# Record your first VR video

## Install once

Extract the entire release ZIP into a permanent, writable folder. Open `VRCapture.exe` from that folder. Keep `layers` and `tools` alongside it. You can create a Windows shortcut to the executable.

Before playing, close other copies and run **Test recording.cmd**. It creates ten seconds of generated video and audio in a new `diagnostics` folder. A PASS checks encoding and saving on your computer, not headset capture or microphone routing. Play the saved demo.

## Choose your capture source

| Game/setup | Recorder source | What to expect |
| --- | --- | --- |
| F.E.A.R. VR with Virtual Desktop, Link or SteamVR | OpenXR (D3D11 / OpenGL) | Captures supported game layers; wrist panel can stay out of the video. |
| Another supported D3D11/OpenGL OpenXR game | OpenXR (D3D11 / OpenGL) | Flat or VR-perspective menus, optional rotational smoothing. |
| Native OpenVR game, or a game running through SteamVR whose graphics API our OpenXR path does not support | SteamVR / OpenVR | Captures SteamVR's composited eye mirror, including visible overlays. No recorder smoothing or flat-menu mode. |

**SteamVR can run OpenXR games.** Using Steam Link does not automatically mean you need the recorder's SteamVR compositor source. VRCapture does not change your runtime or install a game-specific DLL.

For OpenXR, click **Arm recording** and approve the Windows setup prompt if requested. This registers capture for both 32-bit and 64-bit applications. Canceling setup leaves it unarmed. Launch games afterward; games already open need restarting.

## Prepare before putting on the headset

1. Connect the headset. Refresh audio devices if needed, choose your microphone, and leave game output on Automatic unless you need a particular device.
2. Start with H.264 / GPU, 1080p60 and Auto bitrate. Newer GPUs may support HEVC/AV1. An unsupported encoder produces an error; there is no silent software-encoding fallback.
3. Choose your save folder. Final assembly temporarily needs room for both recording components and the finished video.
4. Test the alarm and confirm you can hear it in your headset.
5. Click **Arm recording**, wait for **ARMED**, then launch the game normally. Audio meters are live while armed.

Recording starts when the game supplies supported VR images. Desktop launchers and splash screens before VR initialization are not captured. A preview is not proof that a take is recording: check the recording status and saved-time counter.

Exit the game or use Stop recording. Wait for saving to complete before closing the recorder. Open **Recordings** and inspect picture, voice, game sound, menus and duration. Repeat this short check when changing hardware, runtime or codec.

## Framing and quality

- **1080p / 1440p / 4K:** 16:9, targeting 60 fps. Choose Fill for a cropped single eye or Full view to retain the complete image with bars where needed. They do not stitch both eyes. Higher output resolution cannot create missing source detail.
- **2560 x 1080:** ultrawide output, targeting 60 fps. Full view preserves the complete submitted eye image, including hands when present, with bars where needed; Fill crops more vertically than 16:9 for a typical tall eye image.
- **Framing: Full view:** preserves every part of the submitted eye image and its proportions at the selected resolution. Smoothing and edge margin are disabled. Quest 3 and Native source always use full view.
- **Quest 3:** 2064 x 2208 output, preserving source aspect ratio with padding when needed.
- **Native source:** output dimensions follow the first source image, aligned for encoding. SteamVR native means its mirror dimensions, which may differ from the game's eye render target.
- **Menus: Flat panel:** makes supported panel-only menus easier to read. **VR perspective** preserves their placement relative to your view.
- **Smoothing:** OpenXR rotational smoothing. More edge margin trades field of view for room at the edges; neither can recover scenery the game did not render.

60 fps is an output target. Slow sources repeat frames; overloaded recording can drop frames. Test performance in the games and settings you intend to use.

## Update or move

To update in the same folder, close the game, finish saving and close VRCapture. Extract the complete new ZIP over the old installation. Keep recordings and `capture-settings.ini` backed up; neither is included in the download. Open the updated recorder, check **Save folder**, and make a short test. Only run one copy at a time.

To move to a different folder, close games and use **Settings > Disable OpenXR capture** in the old copy before moving it. Extract the new version fully, copy your preferences if wanted, and check **Save folder** because retained preferences may refer to the old path. Arm to register the new layers before launching the game.
