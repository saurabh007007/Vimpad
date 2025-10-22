import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',                   # your main file
    '--name=VimPad',             # name of the app/executable
    '--windowed',                # GUI app, no console
    '--onefile',                 # bundle into a single executable
    '--add-data=icons2:icons2',
    '--icon=s.ico'
])
