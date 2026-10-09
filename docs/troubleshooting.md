# Troubleshooting and recovery

## Armed, but no recording

Wait for **ARMED** before launching the game, and choose a source matching its API. F.E.A.R. VR uses OpenXR, including through SteamVR. Native OpenVR requires the SteamVR compositor source. OpenXR capture must be registered before the game starts. Desktop launchers are not VR frames. SteamVR Home does not start a take.

Check the status message. D3D12/Vulkan OpenXR and native Oculus SDK capture are not supported by the OpenXR layer. Game and recorder must use the same GPU. Do not replace game DLLs to fix recorder setup.

## Encoder unavailable or the demo fails

Try H.264, 1080p60, Auto bitrate and current GPU drivers. HEVC/AV1 hardware support varies. Keep the entire extracted package together and use a writable local folder. On Windows N, check that the Media Feature Pack is installed. Keep the generated diagnostics if the bundled demo fails.

## Voice missing, quiet or doubled

Select the microphone for your current connection and confirm its armed meter responds when you speak. A Virtual Desktop microphone may still be listed while using Steam Link; its presence does not prove it is carrying your voice. Check routing and listen to a short take. Lower game volume if it masks speech. When editing separate streams, mute Mix. See [audio and editing](audio-and-editing.md).

## Missing edges, menus or overlays

Widescreen crops the eye image. Try **Native source** to distinguish cropping from missing content. **Menus: VR perspective** shows supported game panels spatially. Unsupported layers or modifiers produce diagnostics. Quest/system UI added after PC composition is not captured. SteamVR mirror capture includes overlays to the extent SteamVR exposes them, while OpenXR captures supported game-submitted layers.

## An alarm sounds

Check the recorder promptly. A long loading screen can trigger the source-stale warning; a silent menu can trigger the game-audio warning. Warnings and fatal errors are displayed separately. **Silence alarm** acknowledges the sound; it does not repair the underlying problem. The saved-time counter is more useful than a moving preview for checking progress.

## Saving takes time, or a take was interrupted

Final assembly joins saved video and audio without re-encoding the video. Large takes need time and free disk space. Keep the recorder open while saving and watch its progress. If it reports a failure, preserve all files for that take.

**Do not delete `.video.mp4`, `.video.ts`, `.mix.aac`, `.mic.aac` or `.game.aac` components.** Keep them together. Click **Recover files** and select the `.video.mp4` or `.video.ts` component. Recovery writes a new `.recovered.mp4` and preserves originals. It cannot restore frames never saved, or guarantee survival of disk/power failures.

## Move or remove the recorder

Close VR games, then use **Settings > Disable OpenXR capture** from the old copy before moving/removing it. If its UI cannot open, the included `disable-layer.ps1` can disable that folder's registrations from an administrator PowerShell. It targets this recorder's manifests, not other layers. After moving, check Save folder and arm again.

## Report a problem

Include BUILD.txt version, Windows version, GPU, headset connection, game/mod, source, codec/resolution and steps to reproduce. Attach relevant small `.txt`/`.log` reports if useful, after checking for private paths/device names. OpenXR layer logs are under `%LOCALAPPDATA%/VRCapture`; recording reports are next to the MP4. Never share credentials or recordings you do not intend to publish.

This beta is unsigned. Obtain it from the creator's release page and compare the supplied SHA-256 checksum if needed. Do not disable security software to make it run.
