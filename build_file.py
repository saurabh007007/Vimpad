from setuptools import setup

APP = ['main.py']
DATA_FILES = ['icons2']  # include your icons folder
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icons2/s.icns',  # macOS app icon (must be .icns)
    'packages': ['tkinter'],
    'resources': ['icons2'],
    'plist': {
        'CFBundleName': 'VimPad',
        'CFBundleDisplayName': 'VimPad',
        'CFBundleIdentifier': 'com.saurabh.vimpad',
        'CFBundleVersion': '1.0',
        'CFBundleShortVersionString': '1.0',
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
