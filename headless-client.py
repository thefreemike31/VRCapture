"""Send one command to a running VRCapture persistent headless session.

This acknowledges command acceptance, not completion of the recording. Poll
status.json / the clip's result JSON for completion before using its MP4.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import time
import uuid


def send(directory, words, timeout=20, request_id=None):
    directory = Path(directory)
    identity = request_id or uuid.uuid4().hex
    if not identity or len(identity) > 80 or any(c not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_" for c in identity):
        raise ValueError("Request ID must use 1-80 ASCII letters, digits, hyphens or underscores")
    if not words or any("\n" in word or "\r" in word or "\0" in word for word in words):
        raise ValueError("Expected one command line")
    target = directory / "commands" / (identity + ".cmd")
    temporary = directory / "commands" / (identity + ".tmp")
    response = directory / "responses" / (identity + ".json")
    if target.exists() or response.exists() or (directory / "processed" / target.name).exists():
        raise FileExistsError("Use a new request ID")
    # CREATE_NEW + same-directory rename prevents partial command reads.
    with temporary.open("x", encoding="utf-8", newline="") as stream:
        stream.write(subprocess.list2cmdline(words))
        stream.flush()
        os.fsync(stream.fileno())
    temporary.rename(target)
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            return json.loads(response.read_text(encoding="utf-8"))
        except (FileNotFoundError, PermissionError, json.JSONDecodeError):
            time.sleep(.05)
    raise TimeoutError(f"No response for {identity}; command may still be pending. Inspect {response} before retrying")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--control-dir", type=Path, required=True)
    parser.add_argument("--timeout", type=float, default=20)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    options = parser.parse_args()
    try:
        reply = send(options.control_dir, options.command, options.timeout)
        print(json.dumps(reply))
        return 0 if reply["accepted"] else 2
    except (OSError, ValueError, TimeoutError) as error:
        print(json.dumps({"accepted": False, "error": str(error)}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
