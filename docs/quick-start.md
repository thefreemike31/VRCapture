# Record your first VR video

## Install once

Extract the entire release ZIP into a permanent, writable folder. Open `VRCapture.exe` from that folder. Keep `layers`, `input` and `tools` alongside it. You can create a Windows shortcut to the executable.

Before playing, close other copies and run **Test recording.cmd**. It creates ten seconds of generated video and audio in a new `diagnostics` folder. A PASS checks encoding and saving on your computer, not headset capture or microphone routing. Play the saved demo.

## Choose your capture source

Choose **Auto (recommended)** to detect the capture source when your game starts. New settings default to Auto; an upgrade preserves your previous manual choice, so select Auto once if needed. The choice is saved for future launches.

Auto prefers a valid OpenXR game image. It gives OpenXR a short opportunity to arrive before using SteamVR's game mirror, and ignores SteamVR Home. Once selected, the source stays fixed through recording, pause/resume and loading screens. The app displays **Auto -> OpenXR** or **Auto -> SteamVR**. Manual choices remain available:

| Game/setup | Recorder source | What to expect |
| --- | --- | --- |
| F.E.A.R. VR with Virtual Desktop, Link or SteamVR | OpenXR (DX / GL / Vulkan) | Captures supported game layers; wrist panel can stay out of the video. |
| Another supported D3D11/D3D12/OpenGL/Vulkan OpenXR game | OpenXR (DX / GL / Vulkan) | Flat or VR-perspective menus, optional rotational smoothing. |
| Native OpenVR game, or a game running through SteamVR whose graphics API our OpenXR path does not support | SteamVR / OpenVR | Captures SteamVR's composited eye mirror, including visible overlays. No recorder smoothing or flat-menu mode. |

**SteamVR can run OpenXR games.** Using Steam Link does not automatically mean you need the recorder's SteamVR compositor source. VRCapture does not change your runtime or install a game-specific DLL.

For Auto or OpenXR, click **Arm recording** and approve the Windows setup prompt if requested. This registers capture for both 32-bit and 64-bit applications. Canceling setup leaves it unarmed. Launch games afterward; games already open need restarting.

Beta.8 adds native Vulkan capture and wrist support alongside D3D11, D3D12 and OpenGL. This covers 8-bit SDR RGBA/BGRA images; HDR/10-bit/float and native Oculus SDK capture are not implemented. Vulkan requires version 1.1+ and Windows external texture/fence sharing on the same GPU. The owner tested a modified OpenXR/Vulkan Fallout: New Vegas VR build through VDXR; this does not add OpenXR to the upstream mod.

Auto chooses the capture method without changing resolution, bitrate or your VR runtime. SteamVR capture still includes visible overlays and bypasses recorder smoothing. When no supported game image is available, VRCapture stays armed rather than starting an empty take.

## Fullscreen live preview

In beta.9, click **Windowed** or press **F10** to open a resizable borderless preview. Drag the picture to move it and drag edges or corners to resize it. **Escape**, **Alt+F4**, or right-click > **Return to recorder** closes the preview without stopping a take. Size and position are remembered within the app session, not across restarts.

Click **Fullscreen**, press **F11** while VRCapture has keyboard focus, or double-click the live preview to toggle fullscreen. From a windowed preview, fullscreen uses that window's monitor and **Escape** restores its prior size and position. From the embedded preview, fullscreen uses the controller's monitor and Escape returns to the controls. These actions do not stop, pause or start a take. The separate preview remains active while recording is paused or the main controls are minimized. Use **Stop recording** or wrist controls to finish a take.

For a live mirror without saving video, open VRCapture, choose your source, use **Windowed** or **Fullscreen**, then launch the game without arming. First-use OpenXR setup may request Windows administrator approval; a game already running must restart after registration. This mode does not open recording audio or start the encoder. If you want a recording too, arm normally before launching the game.

Both modes scale the existing **1280×720 live preview**, fitting the available area and keeping its proportions. Differently shaped windows can show bars; the image is not stretched or newly cropped. This does not change recording resolution, bitrate, framing or the saved file, and is not a native 4K preview. Presentation runs on the independent preview worker; the display still uses some GPU resources.

## Headless recording for agents

Use `--headless` for unattended OpenXR capture without a recorder window, preview or audible cues. Persistent sessions can start/stop several clips and set the next clip's resolution without restarting or manually rearming. Audio defaults to Off; the GUI settings are not loaded. See [headless setup, commands and results](headless.md) before using an agent.

## Prepare before putting on the headset

1. Connect the headset. Refresh audio devices if needed, choose your microphone, and leave game output on Automatic unless you need a particular device.
2. Start with H.264 / GPU, 1080p60 and Auto bitrate. Newer GPUs may support HEVC/AV1. An unsupported encoder produces an error; there is no silent software-encoding fallback.
3. Choose your save folder. Final assembly temporarily needs room for both recording components and the finished video.
4. Test the alarm and confirm you can hear it in your headset.
5. Click **Arm recording**, wait for **ARMED**, then launch the game normally. Audio meters are live while armed.

Recording starts when the game supplies supported VR images. Desktop launchers and splash screens before VR initialization are not captured. A preview is not proof that a take is recording: check the recording status and saved-time counter.

During a take, use **Pause** on the desktop or [wrist panel](wrist-panel.md) to leave an unwanted section out. **Resume** continues the same MP4, excluding the paused picture and sound from every audio track. The recording timer freezes while the preview and input meters stay live. Recording quality settings remain unchanged.

Exit the game or use **Stop recording** to save, including while paused. Pause does not keep a take open after the game exits. Wait for saving to complete before closing the recorder. Open **Recordings** and inspect picture, voice, game sound, menus and duration. Repeat this short check when changing hardware, runtime or codec.

## Presenter notes

Before launching the game, open **Settings > Presenter notes...**, enter your talking points and enable the notes sheet. Choose its wrist, size and position. Supported Touch controllers can tap the physical thumb rest to show/hide and hold for half a second to turn a page. Head-aimed navigation is available too. OpenXR keeps notes out of recordings; SteamVR/OpenVR mirror capture can include them. See [the presenter guide](presenter-notes.md).

## Framing and quality

- **1080p / 1440p / 4K:** 16:9, targeting 60 fps. Choose Fill for a cropped single eye or Full view to retain the complete image with bars where needed. They do not stitch both eyes. Higher output resolution cannot create missing source detail.
- **2560 x 1080:** ultrawide output, targeting 60 fps. Full view preserves the complete submitted eye image, including hands when present, with bars where needed; Fill crops more vertically than 16:9 for a typical tall eye image.
- **Framing: Full view:** preserves every part of the submitted eye image and its proportions at the selected resolution. Smoothing and edge margin are disabled. Quest 3 and Native source always use full view.
- **Quest 3:** 2064 x 2208 output, preserving source aspect ratio with padding when needed.
- **Native source:** output dimensions follow the first source image, aligned for encoding. SteamVR native means its mirror dimensions, which may differ from the game's eye render target.
- **Menus: Flat panel:** makes supported panel-only menus easier to read. Beta.9 also recognizes a menu explicitly marked by a compatible mod when a 3D scene is submitted alongside it. Older/unmodified mods do not gain that mixed-scene detection automatically. **VR perspective** preserves the panel's placement relative to your view.
- **Smoothing:** OpenXR rotational smoothing. More edge margin trades field of view for room at the edges; neither can recover scenery the game did not render.

Smoothing and edge margin are saved when you finish adjusting them. Full view bypasses both, and SteamVR compositor capture bypasses smoothing, without erasing your chosen values. Older versions did not store these two settings; adjust them once in beta.5 or newer if their previous values were lost.

Your Left/Right eye selection is remembered after restart in beta.7 and newer, alongside your other camera settings.

60 fps is an output target. Slow sources repeat frames; overloaded recording can drop frames. Test performance in the games and settings you intend to use.

## Update or move

To update in the same folder, close the game, finish saving and close VRCapture. Extract the complete new ZIP over the old installation. Keep recordings, `capture-settings.ini` and `presenter-notes.txt` backed up; none is included in the download. Open the updated recorder, check **Save folder**, and make a short test. Only run one copy at a time.

To move to a different folder, close games and use **Settings > Disable OpenXR capture** in the old copy before moving it. Extract the new version fully, copy your preferences and presenter notes if wanted, and check **Save folder** because retained preferences may refer to the old path. Arm to register the new layers before launching the game.
