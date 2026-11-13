# Headless OpenXR recording for agents

Beta.9 can record without a recorder window, desktop preview or audible cues. Use one invocation per clip, or keep a persistent recorder available across clips and change the next clip's resolution without restarting or manually rearming.

Headless mode supports OpenXR capture only. It does not provide SteamVR/OpenVR compositor capture, pause/resume, wrist controls or presenter notes. Use a normal Windows user session with a supported GPU encoder; Windows service/session-0 operation is not validated. The regular desktop app still opens when launched without `--headless`.

## Prepare once

Extract the complete package to a permanent writable folder. Keep its helpers, `layers`, `input` and `tools` together. Close other VRCapture instances before starting a headless process; only one recorder can own the capture connection.

The capture layer must already be enabled for the OpenXR application. Use the desktop app's capture setup once before unattended use: click **Windowed** with Auto/OpenXR selected, approve setup if prompted, then close the recorder. Launch games after registration. Headless mode does not register layers, request elevation or change the runtime. An agent may instead supply the matching package layer through the source application's own OpenXR loader environment. Do not change the system runtime just to record.

Audio is **Off by default**. `--game-audio auto` captures the game's playback endpoint when identifiable, otherwise the Windows default output. Other applications playing through that endpoint can also be recorded. A microphone is opened only when explicitly selected. GUI preferences are neither loaded nor saved by headless mode.

Examples below run from the extracted package folder and use `C:\Videos` as an example destination. Choose your own writable folder and new filenames. This is a Windows GUI executable: use a child-process API or `Start-Process -PassThru` to wait reliably.

## One clip

```powershell
$recorder = Start-Process -FilePath '.\VRCapture.exe' -WindowStyle Hidden -PassThru -ArgumentList '--headless --output "C:\Videos\clip-001.mp4" --seconds 30 --game-audio auto'
```

Poll `C:\Videos\clip-001.mp4.result.json` until `phase` is `waiting`, then start the OpenXR application. Recording begins with a fresh source image. The duration starts with encoding, not the initial source wait. Source exit also finishes the take after the existing grace interval. A timeout defaults to 60 seconds while waiting for a source; `--wait-timeout 0` waits indefinitely.

For an indefinite take, omit `--seconds` and use `--stop-file "C:\Videos\clip-001.stop"`. Create that initially absent file to finish the MP4. Do not kill the recorder as a normal stop mechanism. After it exits, check both its exit code and the final result:

```powershell
$recorder.WaitForExit()
$recorder.Refresh()
$result = Get-Content -Raw 'C:\Videos\clip-001.mp4.result.json' | ConvertFrom-Json
if ($recorder.ExitCode -ne 0 -or $result.phase -ne 'complete') {
    throw "Recording failed: $($result.error)"
}
```

## Keep the recorder available between clips

Start a persistent session with a **new** control directory:

```powershell
$recorder = Start-Process -FilePath '.\VRCapture.exe' -WindowStyle Hidden -PassThru -ArgumentList '--headless --persistent --control-dir "C:\Videos\agent-session-001" --resolution half-native --game-audio auto'
```

Poll the control directory's `status.json` until `phase` is `ready`. The same recorder keeps the GPU connection across clips; capture is disabled while ready so it does not keep copying or encoding images between takes. Do not supply startup `--output` or `--result` in persistent mode: each Start supplies those paths.

The optional bundled helper needs Python 3:

```powershell
py -3 headless-client.py --control-dir 'C:\Videos\agent-session-001' start --output 'C:\Videos\clip-001.mp4' --seconds 10
py -3 headless-client.py --control-dir 'C:\Videos\agent-session-001' set --resolution native
```

The first clip retains its half-native size even if Set arrives during recording. Wait for `status.json` to return to `ready`, then request the next take:

```powershell
py -3 headless-client.py --control-dir 'C:\Videos\agent-session-001' start --output 'C:\Videos\clip-002.mp4' --seconds 10
```

`half-native` means half the source width and half the source height, rounded to even dimensions: approximately one quarter of the pixels. Both native modes keep the full eye image. There is no separate Arm command. Source exit finishes the current take and returns the session to ready; a later source can be recorded by the same process.

| Command | Effect |
| --- | --- |
| `set --resolution VALUE` | Change the next-clip default, including while a take is active. Never resizes the current take. |
| `start --output NEW.mp4` | Request one clip using a snapshot of the current defaults. |
| `start --output NEW.mp4 --resolution VALUE` | Override the size for that clip only. |
| `start ... --seconds N --wait-timeout N --result NEW.json` | Optional per-clip duration, source timeout and result location. |
| `stop` | Save the active take or cancel its source wait; harmless when ready. |
| `status` | Return the current session state. |
| `shutdown` | Save the active take if any, then exit. |

Only resolution can be changed with Set in this version. Other settings stay fixed for the session. Start is rejected while another take is queued, waiting, recording or saving. Wait for ready before starting another. A command acknowledgement means the request was accepted, **not that the MP4 was saved**.

## Direct commands without Python

Agents can use the file interface directly. The control directory contains `commands`, `responses`, `processed` and an atomically updated `status.json`.

Write one UTF-8 command to `commands/<unique-id>.tmp`, close it, then rename it to `commands/<unique-id>.cmd` in the same directory. For example, the file content can be `start --output "C:\Videos\clip-003.mp4" --seconds 10`. IDs contain 1–80 ASCII letters, digits, hyphens or underscores. Commands use Windows argument quoting and are limited to 16 KiB. Files with other extensions are ignored.

Read `responses/<unique-id>.json` for `accepted`, `error` and a status snapshot. Wait for this response before sending a dependent command. Use a unique ID each time; replaying an acknowledged ID retains its original response and does not start a new take. Commands are consumed in filename order, so concurrent clients must coordinate. On timeout, inspect that response and session state before retrying. Never reuse a control directory across launches.

Session status includes `schemaVersion`, `mode`, `recorderPid`, `phase`, `closing`, `nextResolution`, `activeCommandId`, `completedClips`, `currentClip`, `lastClip` and `error`. Clip phases progress through queued/initializing/waiting/starting/recording/finalizing and briefly complete/failed/cancelled before ready. Shutdown ends at stopped; a fatal session failure ends at failed. Associate results with the requested output or command ID.

Each take also has a result file, defaulting to `<output>.result.json`. Read it to determine whether that take succeeded. CompletedClips counts successful saves. Ordinary clip failures, source timeouts and cancellations leave the session available. A failure to maintain the session's status/control channel is fatal. If a clip's own result cannot be updated, its final failure is retained in session `lastClip` and stderr.

Use Shutdown for normal session completion. An optional startup `--stop-file` provides graceful whole-session shutdown; it must start absent and be outside the control directory. Recording outputs/results must also be outside that directory. Persistent process exit 0 means graceful session shutdown, even if an earlier clip failed; inspect each clip's result.

## Options and results

| Option | Values / default |
| --- | --- |
| `--output`, `--result` | New MP4 path; optional new JSON path, default `<output>.result.json` |
| `--seconds` | 0–86400, fractional allowed; default 0 runs until source exit or Stop |
| `--wait-timeout` | 0–86400 seconds; default 60, 0 waits indefinitely for the requested clip's source |
| `--codec` | `h264` (default), `hevc`, `av1`; GPU support required |
| `--resolution` | `1080` (default), `1440`, `2160`, `2560x1080`, `quest3`, `native`, `half-native` |
| `--framing` | `fill` (default), `full`; quest3/native/half-native always use Full |
| `--eye` | `right` (default), `left` |
| `--menu-view` | `flat` (default), `vr` |
| `--bitrate` | 0 for Auto (default), or integer 4–100 Mbps |
| `--smoothing`, `--margin` | 0–100 (default 25), 0–30 (default 4); Fill only |
| `--mic` | `off` (default), `default`, or endpoint ID |
| `--game-audio` | `off` (default), `default`, `auto`, or endpoint ID |
| `--audio-mode` | `mixed` (default), `editing` for Mix / Microphone / Game tracks |
| `--mic-volume`, `--game-volume` | Integer 0–200%; default 100 and 65 |
| `--list-audio` | Print microphone/playback endpoint IDs as JSON and exit |
| `--help` | Print command help and exit |

Pass `--headless` with these options. `--source openxr` is the only supported explicit source. All recordings use the existing 60 Hz output timeline. Disabled audio sources remain silent tracks. Native dimensions follow the first source image, aligned for encoding; a later source-size change does not resize the MP4.

Clip result JSON is atomically updated at transitions and approximately once per second. It reports phase, exitCode, output, source/sourcePid/producerBits, dimensions, frame rate, frame/drop/repeat counters, audio-device names, stopReason and error. ExitCode is null while active. Transitions also go to redirected stdout and errors to stderr.

| Clip exit code | Meaning |
| --- | --- |
| 0 | Completed MP4 saved |
| 1 | Runtime, device, helper, output or save failure |
| 2 | Invalid arguments or conflicting paths |
| 3 | Timed out waiting for a source |
| 4 | Stop requested before recording began |

## Troubleshooting

- **Waiting forever or timing out:** confirm the source is OpenXR, its capture layer is enabled, it was launched after setup, and recorder/game use the same GPU. The source must actually submit frames. Headless does not capture the Windows desktop.
- **No audio:** audio defaults to Off. Select `--game-audio auto` and/or a microphone explicitly. GUI preferences do not apply.
- **No result file:** invalid arguments or inability to reserve that path can fail before JSON exists. Inspect redirected stderr and the process exit code.
- **Output already exists:** use a new MP4/result path. Existing recordings and protected sidecars are preserved.
- **Command accepted but video not ready:** wait for final clip results and ready/stopped state. Do not treat an acknowledgement as completion.
- **Failed take:** preserve its media components for the bundled recovery tool. A complete result means normal saving/packet verification finished, not that every source frame was captured; inspect frame counters.

Automated D3D11 tests cover 32-bit and 64-bit sources, several codecs/resolutions, same-process multi-clip operation, resolution changes, source exit, cancellation and failure recovery. Other games/backends and headset performance still need setup-specific testing. Real microphone routing is not established by generated or silent test audio.
