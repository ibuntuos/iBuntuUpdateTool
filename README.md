# iBuntu Update Tool

This tool helps you updating your iBuntu System from one Version to another. It comes with a Point-by-Point Instruction, a detailed Tutorial and automatically saving and restoring of your manually installed software (if you did get them without external PPAs or by installing .deb Files)


From iBuntu Version 1.3 the iBuntu Update Tool will be fully integrated within the System so all settings are already done and you can launch it directly from the Launchpad.

If you have a Version lower than 1.3 you first need to download it from here.

just click on “Code” and than “Download ZIP”.
After that you just extract the folder to your desktop and than press

```
ALT + CTRL + T
```
to open a new Terminal Console. There you enter follwoing command (you can copy it here and insert it in the terminal with a right click and selecting “paste”):
```
sudo apt install python3-pip python3-tk -y
pip3 install pysimplegui
```

This will install the necessarry dependencies for the program. After that, just open the downloaded folder and run the script
```
iBuntu_Update_Tool_start.sh
```
Than the program should come up.

Of course you can use this tool on any other Ubuntu-Version as well but than I give no guarantee or support for it since this Software was especially designed for iBuntu.
