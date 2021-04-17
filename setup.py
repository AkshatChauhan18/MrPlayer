import PyInstaller.__main__ as py
py.run([
    "MrPlayer.py",
    "--noconsole",
    "--icon=icon.ico",
    "--exclude-module=tkinter,pandas,tcl,tcl8,jedi,numpy,PyQt5,ipython,pygame,cryptography",
    "--hidden-import=sys"
])
