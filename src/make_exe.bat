@echo off

set Args= --noupx  --add-data res\wxPomoTimer.ico;res --add-data res\blank.ico;res --add-data res\Clear-icon-64.png;res --add-data res\Pause-icon-64.png;res --add-data res\Settings-icon-64.png;res --add-data res\Start-icon-64.png;res --add-data res\Stop-icon-64.png;res --add-data res\sound\beep0.wav;res\sound --add-data res\sound\beep1.wav;res\sound
set ExtraArgs=--noconsole
@echo on
pyinstaller -F -i res\wxPomoTimer.ico %Args% %ExtraArgs% wxPomoTimer.pyw
