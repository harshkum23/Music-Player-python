from cx_Freeze import*
includefiles=['browse.png','d.ico','music.png','pause.png','play-button.png','stop.png','volume.png','volume-down.png']
excludes=[]
packages=[]
base=None
if sys.platform=="Win32":
    base='Win32GUI'

shortcut_table=[
    ('DesktopShortcut',#Shortcut
     'DesktopFolder',#Directory_
     'HK Music Player',#Name
     'TARGETDIR',#Component_
     '[TARGETDIR]\Hkmuusicplayer.exe',#Target
      None, #Arguments
      None, #Description
      None, #Hotkey
      None, #icon
      None, #Iconindex
      None, #Showccmd
      'TARGETDIR',#Wkdir
     )
]

msi_data={'Shortcut':shortcut_table}

bdist_msi_option={'data':msi:data}
setup(
    versiom='0.1',
    desciption="Hk Music Player",
    author='Harsh Kumrawat',
    name="Hk Music Player",
    options={'build_exe':{'includefiles':includefiles},'bdist_msi':bdist_msi_option,},
    executable={
        Executable(
            script='Hkmusicplayer.py',
            base=base,
            icon=d.ico,
        )
    }
)


