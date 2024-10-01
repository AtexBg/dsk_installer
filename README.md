------------------------
      Description
------------------------

dsk.exe (or DeSKtop) is a program thats allows you to have multiple desktops layouts simpely, all you need is to launch the DeSKtop_installer.exe AS ADMINISTRATOR and run the "dsk" command from anywhere you can (on Windows menu, cmd, from a batch file, Win+R menu, etc...) and it will swap your Desktop with the desktop_alt folder, if you want to go back to your original desktop you can just execute the command again.

If you want you can simpely extract the dsk.exe file from your system32 folder.

------------------------
      Compilation
------------------------

You need to use this command to compile the code : 

"pyinstaller --icon=icon.ico --noconsole --onefile --add-data "dsk.exe;." --manifest manifest.xml installer.py"