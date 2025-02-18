@echo off
echo Generating PNG , ICO files...

rem 生成 logo
./ffmpeg.exe -i logo.png -vf "scale=512:512" icon.png
./ffmpeg.exe -i logo.png -vf "scale=50:50" StoreLogo.png
./ffmpeg.exe -i logo.png -vf "scale=310:310" Square310x310Logo.png
./ffmpeg.exe -i logo.png -vf "scale=284:284" Square284x284Logo.png
./ffmpeg.exe -i logo.png -vf "scale=150:150" Square150x150Logo.png
./ffmpeg.exe -i logo.png -vf "scale=142:142" Square142x142Logo.png
./ffmpeg.exe -i logo.png -vf "scale=107:107" Square107x107Logo.png
./ffmpeg.exe -i logo.png -vf "scale=89:89" Square89x89Logo.png
./ffmpeg.exe -i logo.png -vf "scale=71:71" Square71x71Logo.png
./ffmpeg.exe -i logo.png -vf "scale=44:44" Square44x44Logo.png
./ffmpeg.exe -i logo.png -vf "scale=30:30" Square30x30Logo.png
./ffmpeg.exe -i logo.png -vf "scale=256:256" 128x128@2x.png
./ffmpeg.exe -i logo.png -vf "scale=128:128" 128x128.png
./ffmpeg.exe -i logo.png -vf "scale=32:32" 32x32.png
./ffmpeg.exe -i logo.png -vf "scale=128:128" icon.ico

echo PNG and ICO generation complete.

icns.exe icon.png icon.icns

echo ICNS generation complete.
pause
