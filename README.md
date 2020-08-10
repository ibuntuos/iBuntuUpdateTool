# iBuntu Update Tool

This tool helps you updating your iBuntu System from one Version to another. It comes with a Point-by-Point Instruction, a detailed Tutorial and automatically saving and restoring of your manually installed software (if you did get them without external PPAs or by installing .deb Files)


From iBuntu Version 1.3 the iBuntu Update Tool will be fully integrated within the System so all settings are already done and you can launch it directly from the Launchpad.

If you have a Version lower than 1.3 you first need to download it from here.

just click on “Code” and than “Download ZIP”.
After that you just extract the folder to your desktop.

Than, just open the downloaded folder and run the script

```
iBuntu_Update_Tool_start.sh
```

It's very likely a Terminal will Pop-up and tells you

```
iBuntu Update Tool could not load we try to install missing dependencies
After this window closes just open the app again."
========================================================================
Installing: python3-tk, python3-pip and PySimpleGui:
```

This will install the neccessary dependencies and after that you just restart the Program and it should come up.


If you like to install the needed dependencies by yourself, enter follwoing commands to your terminal:

```
sudo apt install python3-pip python3-tk -y
pip3 install pysimplegui
```


Important:
Of course you can use this tool on any other Ubuntu-Version as well but than I give no guarantee or support for it since this Software was especially designed for iBuntu.
