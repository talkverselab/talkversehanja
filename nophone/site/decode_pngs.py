#!/usr/bin/env python3
import base64
import os
import glob

# Decode base64 encoded PNG files in the current directory
for b64_file in glob.glob("*.png"):
    with open(b64_file, "r") as f:
        data = f.read().strip()
    try:
        binary = base64.b64decode(data)
        with open(b64_file, "wb") as out:
            out.write(binary)
        print(f"Decoded {b64_file}")
    except Exception as e:
        print(f"Failed {b64_file}: {e}")
