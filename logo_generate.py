# if you want to use form terminal 
# make sure you already have  Pillow  and  icnsutil
# if you do not have , please run " pip install Pillow " and " pip install icnsutil "

# the code that runs it in the terminal is " python logo_generate.py {path-to-your-png} "

import argparse
from PIL import Image
from icnsutil import IcnsFile

# logo PNG targe
png_sizes = [
    (512, 512, "icon.png"),
    (50, 50, "StoreLogo.png"),
    (310, 310, "Square310x310Logo.png"),
    (284, 284, "Square284x284Logo.png"),
    (150, 150, "Square150x150Logo.png"),
    (142, 142, "Square142x142Logo.png"),
    (107, 107, "Square107x107Logo.png"),
    (89, 89, "Square89x89Logo.png"),
    (71, 71, "Square71x71Logo.png"),
    (44, 44, "Square44x44Logo.png"),
    (30, 30, "Square30x30Logo.png"),
    (256, 256, "128x128@2x.png"),
    (128, 128, "128x128.png"),
    (32, 32, "32x32.png")
]

# logo ICO targe
ico_sizes = [
    (128, 128, "icon.ico")
]

def generate_png(input_image_path):
    original_image = Image.open(input_image_path)
    for size in png_sizes:
        width, height, output_path = size
        resized_image = original_image.resize((width, height))
        resized_image.save(output_path)
        print(f"Saved {output_path} ({width}x{height})")

def generate_ico(input_image_path):
    original_image = Image.open(input_image_path)
    for size in ico_sizes:
        width, height, output_path = size
        resized_image = original_image.resize((width, height))
        resized_image.save(output_path, format="ICO")
        print(f"Saved {output_path} ({width}x{height})")

def generate_icns(input_image_path):
    try:
        icns = IcnsFile()
        icns.add_media(file=input_image_path)
        icns.write("icon.icns") # if you want to revise ,do not forget the file name
        print("Saved icon.icns") # 512*512
    except Exception as e:
        print(f"Failed to generate ICNS file: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_image', type=str)
    args = parser.parse_args()
    input_image_path = args.input_image

    generate_png(input_image_path)
    generate_ico(input_image_path)
    generate_icns("icon.png")# icon.png comes from  generate_png_icons  just generated


if __name__ == "__main__":
    main()
