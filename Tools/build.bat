pyinstaller -F ..\main.py --window
move .\__init__.py ..\Build
move .\main.spec ..\Build
move .\build ..\Build
move .\dist ..\Build
mkdir ..\Build\dist\AppData
xcopy ..\AppData ..\Build\dist\AppData /s /e /y
echo success