#!/usr/bin/env python
import os
import desk_environment

WorkPath=os.path.dirname(os.path.realpath(__file__))
konsolecommand="gnome-terminal"
print(desk_environment.detect_desktop_environment())
#set konsole command according to system
if not desk_environment.detect_desktop_environment() == "gnome":
	konsolecommand="konsole"
	
result = os.system("python3 "+os.path.join(WorkPath, "iBuntu_Update_Tool.py"))
if 0 == result:
    print(" iBuntu Update Tool started")
else:
    print("Error occured, try to install missing dependencies")
    os.system(konsolecommand+" -e "+os.path.join(WorkPath, "dependencies.sh"))
    result2 = os.system("python3" +os.path.join(WorkPath, "iBuntu_Update_Tool.py"))
    if 0 == result2:
        print(" iBuntu Update Tool started")
    else:
        print("Error occured, nothing else we can do, sorry.")
