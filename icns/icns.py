from icnsutil import IcnsFile

def convert_png_to_icns(png_path, icns_path):
    try:
        icns = IcnsFile()
        icns.add_media(file=png_path)
        icns.write(icns_path)
        print(f"成功将 {png_path} 转换为 {icns_path}")
    except Exception as e:
        print(f"转换失败：{e}")

png_file = "icon.png"  # 替换为希望的 PNG 文件路径
icns_file = "icon.icns" 
convert_png_to_icns(png_file, icns_file)

