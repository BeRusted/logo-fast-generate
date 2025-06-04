# Some uesless information ( maybe not all people use venv? )
# if you want to use form terminal 
# make sure you already have  Pillow , icnsutil and cairosvg installed
# if you do not have , please run " pip install Pillow " , " pip install icnsutil " and " pip install cairosvg "

# the code that runs it in the terminal is " python logo_generate.py {path-to-your-png} "

import argparse
import os
import platform
import subprocess
from PIL import Image
from icnsutil import IcnsFile
import cairosvg
import io

# logo PNG targe
png_sizes = [
    (512, 512, "512x512.png"),
    (256, 256, "256x256.png"),
    (128, 128, "128x128.png"),
    (64, 64, "64x64.png"),
    (32, 32, "32x32.png"),
    (16, 16, "16x16.png"),
]

# logo ICO targe
ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256),(512, 512)]

# PNG or SVG input image
def load_input_image(input_path):
    ext = os.path.splitext(input_path)[1].lower()
    if ext == ".png":
        return Image.open(input_path)
    elif ext == ".svg":
        # SVG → PNG 
        png_data = cairosvg.svg2png(url=input_path, output_width=512, output_height=512)
        return Image.open(io.BytesIO(png_data))
    else:
        raise ValueError("Only .png and .svg files are supported")
    
def generate_png(input_image_path):
    original_image = Image.open(input_image_path)
    for size in png_sizes:
        width, height, output_path = size
        resized_image = original_image.resize((width, height))
        resized_image.save(output_path)
        print(f"Saved {output_path} ({width}x{height})")

def generate_ico(input_image_path):
    original_image = Image.open(input_image_path)
    images = [original_image.resize(size, Image.LANCZOS) for size in ico_sizes]
    images[0].save("icon.ico", format="ICO",sizes=ico_sizes)
    print("Saved icon.ico")

def generate_icns():
    system_name = platform.system()

    if system_name == "Darwin":
        # macOS - use iconutil
        iconset_dir = "icon.iconset"
        os.makedirs(iconset_dir, exist_ok=True)

        mapping = [
            ("16x16.png", "icon_16x16.png"),
            ("32x32.png", "icon_16x16@2x.png"),
            ("32x32.png", "icon_32x32.png"),
            ("64x64.png", "icon_32x32@2x.png"),
            ("128x128.png", "icon_128x128.png"),
            ("256x256.png", "icon_128x128@2x.png"),
            ("256x256.png", "icon_256x256.png"),
            ("512x512.png", "icon_256x256@2x.png"),
            ("512x512.png", "icon_512x512.png"),
            ("512x512.png", "icon_512x512@2x.png"),
        ]

        for src, dest in mapping:
            if os.path.exists(src):
                Image.open(src).save(os.path.join(iconset_dir, dest))
                print(f"Added to iconset: {dest}")
            else:
                print(f"Warning: {src} not found, skipping {dest}")

        result = subprocess.run(["iconutil", "-c", "icns", iconset_dir], capture_output=True)
        if result.returncode == 0:
            print("Saved icon.icns")
        else:
            print("Failed to generate icon.icns:", result.stderr.decode())

    else:
        # no macOS - use icnsutil
        try:
            icns = IcnsFile()
            # defult to the 512*512 PNG found in png_sizes
            source_path = None
            for (_, _, fname) in png_sizes:
                if os.path.exists(fname):
                    source_path = fname
                    break
            if not source_path:
                print("No PNG found to create .icns")
                return
            icns.add_media(file=source_path)
            icns.write("icon.icns")
            print("Saved icon.icns (fallback via icnsutil)")
        except Exception as e:
            print(f"Failed to generate ICNS file: {e}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_image", type=str)
    args = parser.parse_args()

    try:
        original_image = load_input_image(args.input_image)
    except Exception as e:
        print(f"Error loading input image: {e}")
        return

    generate_png(original_image)
    generate_ico(original_image)
    generate_icns()


if __name__ == "__main__":
    main()
