# VRCapture

**PCVR recording, built for creators.** By thefreemike.

Arm on your desktop, put on your headset, and launch your game. VRCapture records supported VR images and your commentary, then saves when you leave the game. No OBS setup required.

![VRCapture desktop interface](images/recorder.jpg)

**0.1.0-beta.9 · Windows x64 · Closed source**

**New in beta.9:** **headless OpenXR recording** for agents and automation, persistent sessions that change the next clip's resolution without restarting or manually rearming, and a **resizable borderless preview** with Windowed / F10. See [headless setup and commands](docs/headless.md) and [preview controls](docs/quick-start.md#fullscreen-live-preview).

Flat panel recording also handles menu panels explicitly marked by a compatible mod, even when the game submits a 3D scene alongside them. This requires support in the mod; ordinary gameplay HUDs and headset composition are unchanged.

[Download the beta](https://github.com/thefreemike31/VRCapture/releases) · [Start here](docs/quick-start.md) · [Audio & editing](docs/audio-and-editing.md) · [Wrist controls](docs/wrist-panel.md) · [Troubleshooting](docs/troubleshooting.md)

## What you can do

- Record at 1080p, 1440p, 4K or 2560×1080 ultrawide, targeting 60 fps, with H.264, HEVC or AV1 hardware encoding where supported by your GPU.
- Choose **Full view (keep hands visible)** to retain the complete submitted eye image with bars where needed, or **Fill** for a widescreen crop. Quest 3 and Native source always use Full view.
- Capture 32-bit and 64-bit OpenXR games using D3D11/D3D12/OpenGL/Vulkan, or use the SteamVR compositor source.
- Adjust microphone and game volume independently. Save a mixed track plus separate microphone and game tracks for editing.
- Pause and resume from the desktop or wrist panel, keeping one video file with paused picture and sound excluded.
- Open a resizable borderless preview with **Windowed / F10**, or use **Fullscreen / F11**. Drag the picture to move, drag edges to resize, and use **Escape** to return. Preview sizing leaves the recording unchanged.
- Let an agent record OpenXR clips without a window or audible cues. Keep one recorder process running between clips and switch the next take between half-native, native or preset resolutions.
- See the selected microphone on a wrist panel and change it before or during recording. Use head aiming and dwell controls to arm, pause, resume, stop and confirm.
- Read multi-page talking points on another wrist, with Touch thumb-rest tap/hold controls or head-aimed navigation. OpenXR notes stay out of your recording.
- See desktop/wrist warnings during recording, hear setup and post-capture failure alarms, and recover saved components after an interruption.

## Your first take

**Also included from beta.5 — pause/resume, remembered camera settings and further performance improvements:** Skip a break or an unwanted section with **Pause**, then **Resume** into the same MP4. Smoothing and edge margin survive restart and upgrades that retain your settings file. OpenGL capture avoids a redundant image copy, and desktop preview presentation runs independently of recording, including during window resizing. Resolution, bitrate and audio-track choices stay the same.

Beta.9 automated checks cover 32-bit and 64-bit D3D11 sources, including resolution changes across clips in one headless recorder session. Preview tests checked unchanged recording pixels and a 4K60 AV1 take while resizing and delaying presentation. These are automated checks, not headset-performance claims.

The earlier beta.8 owner test completed roughly 55 minutes of Fallout: New Vegas VR using a modified OpenXR/Vulkan build through VDXR, recording at 4K60 AV1 and stopping from the wrist panel. The owner reported that it worked perfectly. Its reports show no encoder queue drops or audio faults, with two missed output slots and some repeated source images. This validates that reported setup; other games, engines, drivers and runtimes still need testing.

To update, close your game and VRCapture, then extract the complete ZIP over your existing installation. Keep your `capture-settings.ini`, `presenter-notes.txt` and recordings; the ZIP contains none of them. If you move to a new folder, follow the relocation steps in the [quick-start guide](docs/quick-start.md).

1. Download the release ZIP and **extract everything** to a permanent, writable folder.
2. Close other copies of VRCapture and run **Test recording.cmd**. Play its generated demo to check encoding and saving.
3. Connect your headset, open **VRCapture.exe**, choose **Auto (recommended)** for VR source, and select your microphone. Start with **H.264 / 1080p60 / Auto bitrate**.
4. Click **Arm recording**, wait for **ARMED**, then launch your game. The first OpenXR setup may request Windows administrator approval.
5. Make a short take with speech, gameplay and a menu. Exit the game, let saving finish, and check the MP4 before a longer session.

Auto prefers the OpenXR capture path for supported games such as F.E.A.R. VR, including when SteamVR is their runtime. It uses the SteamVR compositor when that is the available capture source. Manual source choices remain available. See the [source guide](docs/quick-start.md#choose-your-capture-source) for detection and overlay limits.

## Compatibility and beta limits

Requires Windows 10/11 x64, a working PCVR setup, Windows Media Foundation and a compatible hardware encoder. Windows N editions may need the Media Feature Pack. The recorder and game must use the same GPU. No separate OBS, FFmpeg or C++ runtime installation is needed. The optional `headless-client.py` helper needs Python 3; agents can also use the file-command interface without Python.

Headless mode currently captures OpenXR only. It does not provide SteamVR/OpenVR compositor capture, pause/resume, wrist controls or presenter notes. It needs a normal Windows user session; Windows service/session-0 operation is not validated. Audio defaults to Off and must be selected explicitly. Headless mode does not register capture layers or switch your runtime.

OpenXR capture supports D3D11, D3D12, OpenGL and Vulkan, including wrist controls and presenter notes. It captures 8-bit SDR RGBA/BGRA game images; HDR/10-bit/float capture and native Oculus SDK capture are not implemented. OpenGL needs compatible `WGL_NV_DX_interop2` support. Vulkan needs Vulkan 1.1+ with Windows external texture/fence sharing on the same GPU. SteamVR capture uses its compositor mirror and has different framing/overlay limits. Standalone Quest games and Quest/Virtual Desktop system UI are outside this PC capture path.

This beta has been used for real gameplay recordings, but hardware, games and runtimes vary. Test your own setup. Recovery can preserve media already saved; it cannot reconstruct unsaved footage or guarantee against recording loss. Check desktop/wrist warnings promptly; alerts stay silent while recording to keep them out of your audio. The app is currently unsigned.

## Downloads, feedback and source

This repository hosts **release downloads, user guides and issue reports**. VRCapture's application source is not published. You can use the beta to make personal or monetized videos; see [the license](LICENSE.txt).

For a problem, include your version, GPU, headset connection, game, capture source, settings and a short reproduction. Review diagnostic text before attaching it: it can contain local paths and audio-device names. Do not upload full recordings unless you intend to share them.

VRCapture bundles a separate [FFmpeg](https://ffmpeg.org/) helper under LGPL 2.1 or later. Its corresponding source and build instructions are included in each [release ZIP](https://github.com/thefreemike31/VRCapture/releases), under `tools/source`. OpenVR, OpenXR and Vulkan notices are also included. These components retain their own licenses; see [third-party notices](THIRD-PARTY-NOTICES.txt).
