import base64
import glob
import os

for b64_file in glob.glob("*.png.b64"):
    png_file = b64_file.replace(".b64", "")
    with open(b64_file, "r") as f:
        b64_data = f.read().strip()
    png_data = base64.b64decode(b64_data)
    with open(png_file, "wb") as f:
        f.write(png_data)
    print(f"Decoded {b64_file} to {png_file}")
