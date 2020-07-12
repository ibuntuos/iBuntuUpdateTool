#!/usr/bin/env python
import os
WorkPath=os.path.dirname(os.path.realpath(__file__))
result = os.system("python3 "+os.path.join(WorkPath, "iBuntu_Update_Tool.py"))
if 0 == result:
    print(" iBuntu Update Tool started")
else:
    print("Error occured, try to install missing dependencies")
    os.system("gnome-terminal -- sh "+os.path.join(WorkPath, "dependencies.sh"))
    result2 = os.system("python3" +os.path.join(WorkPath, "iBuntu_Update_Tool.py"))
    if 0 == result2:
        print(" iBuntu Update Tool started")
    else:
        print("Error occured, nothing else we can do, sorry.")
