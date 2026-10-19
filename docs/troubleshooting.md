# Troubleshooting and recovery

## Armed, but no recording

Wait for **ARMED** before launching the game, and choose a source matching its API. F.E.A.R. VR uses OpenXR, including through SteamVR. Native OpenVR requires the SteamVR compositor source. OpenXR capture must be registered before the game starts. Desktop launchers are not VR frames. SteamVR Home does not start a take.

Check the status message. D3D12/Vulkan OpenXR and native Oculus SDK capture are not supported by the OpenXR layer. Game and recorder must use the same GPU. Do not replace game DLLs to fix recorder setup.

## Encoder unavailable or the demo fails

Try H.264, 1080p60, Auto bitrate and current GPU drivers. HEVC/AV1 hardware support varies. Keep the entire extracted package together and use a writable local folder. On Windows N, check that the Media Feature Pack is installed. Keep the generated diagnostics if the bundled demo fails.

## Stutter or uneven recording

Update to beta.4 or newer using the complete ZIP. Beta.4 fixes recording-clock pacing, removes runtime compilation of capture shaders and reuses encoder GPU surfaces. Close the game and recorder before replacing the files, and keep your settings and recordings.

Note whether the hitch occurs in the headset, the saved MP4, or both, and keep a rough video timestamp. A 60 fps file can still contain repeated source images when fresh game frames arrive late. Neither a repeated image nor a long VR runtime call alone proves which component caused a hitch.

For a useful comparison, play the same short section with the recorder fully closed, then with recording enabled, keeping game and headset settings consistent. Minimize the desktop preview during the recording test. Lower output resolution can reduce recorder work, but does not reduce the game's own rendering resolution or guarantee that all capture work becomes cheaper. Avoid adding live monitoring tools during the comparison.

After exiting normally, preserve the reports beside the MP4 and the OpenXR layer logs under `%LOCALAPPDATA%/VRCapture`. Reports include missed recording output slots, queue drops, encoder pool occupancy and bounded CPU timing history. CPU timings do not measure GPU execution or headset delivery. Check reports for private paths and device names before sharing.

## Voice missing, quiet or doubled

Select the microphone for your current connection and confirm its armed meter responds when you speak. A Virtual Desktop microphone may still be listed while using Steam Link; its presence does not prove it is carrying your voice. Check routing and listen to a short take. Lower game volume if it masks speech. When editing separate streams, mute Mix. See [audio and editing](audio-and-editing.md).

## Missing edges, menus or overlays

Select **Framing: Full view (keep hands visible)** to preserve the complete submitted eye image at 1080p, 1440p, 4K or 2560 x 1080. Bars preserve its proportions where needed. This bypasses smoothing and edge margin, but cannot recover hands or scenery absent from the source image. **Fill** crops the eye image. **Quest 3** and **Native source** always use Full view. **Menus: VR perspective** shows supported game panels spatially. Unsupported layers or modifiers produce diagnostics. Quest/system UI added after PC composition is not captured. SteamVR mirror capture includes overlays to the extent SteamVR exposes them, while OpenXR captures supported game-submitted layers.

## An alarm sounds

Warnings stay silent during recording so VRCapture's tones cannot enter your footage or microphone. Check the desktop or enable the wrist panel in Settings before recording. A long loading screen can trigger the source-stale warning; 15 seconds without game sound triggers the game-audio warning. Warnings and fatal errors are displayed separately. Test/arming tones remain audible before capture; fatal alarms can sound after capture stops. **Silence alarm** acknowledges the sound; it does not repair the underlying problem. The saved-time counter is more useful than a moving preview for checking progress.

## Saving takes time, or a take was interrupted

Final assembly joins saved video and audio without re-encoding the video. Large takes need time and free disk space. Keep the recorder open while saving and watch its progress. If it reports a failure, preserve all files for that take.

**Do not delete `.video.mp4`, `.video.ts`, `.mix.aac`, `.mic.aac` or `.game.aac` components.** Keep them together. Click **Recover files** and select the `.video.mp4` or `.video.ts` component. Recovery writes a new `.recovered.mp4` and preserves originals. It cannot restore frames never saved, or guarantee survival of disk/power failures.

## Move or remove the recorder

Close VR games, then use **Settings > Disable OpenXR capture** from the old copy before moving/removing it. If its UI cannot open, the included `disable-layer.ps1` can disable that folder's registrations from an administrator PowerShell. It targets this recorder's manifests, not other layers. After moving, check Save folder and arm again.

## Report a problem

Include BUILD.txt version, Windows version, GPU, headset connection, game/mod, source, codec/resolution and steps to reproduce. Attach relevant small `.txt`/`.log` reports if useful, after checking for private paths/device names. OpenXR layer logs are under `%LOCALAPPDATA%/VRCapture`; recording reports are next to the MP4. Never share credentials or recordings you do not intend to publish.

This beta is unsigned. Obtain it from the creator's release page and compare the supplied SHA-256 checksum if needed. Do not disable security software to make it run.
