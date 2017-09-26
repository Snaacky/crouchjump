@RD /S /Q "dist"
cd %~p0
python %localappdata%\Programs\Python\Python35\Scripts\pyinstaller-script.py src/crouchjump.py --onefile --clean --icon=img/logo.ico --key=zfDzwOwIUvnQemip
@RD /S /Q "build"
del /s /q "crouchjump.spec"
cd %~p0/utils/
verpatch.exe ../dist/crouchjump.exe 1.0.0.0 /va /pv 1.0.0.0 /s description "A crouch-jump hotkey script for PUBG." /s product "Crouchjump" /s copyright "No copyright applied." /s company "https://github.com/snaacky"
cd %~p0/src/
@RD /S /Q "__pycache__"