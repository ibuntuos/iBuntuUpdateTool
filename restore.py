import subprocess
import os
import glob
import tarfile
import time

path=os.path.dirname(os.path.realpath(__file__))
print("============================================================================")
os.system("echo 'We try now to restore your previously saved programs and settings'")
os.system("echo for this we need Access to your File-System.")
os.system("sudo echo 'Granted. We beginn.'")
print("============================================================================")
#Restore Snaps
print("Restore Snaps")
time.sleep(2)
os.system("sudo chmod -R 777 "+path+"/Backup")
snapversion=os.listdir(path+"/Backup/Snaps")
#snapversion=snapversion.sort()
snapversion=snapversion[-1].split("_")[0]
os.system("sudo cp -R "+path+"/Backup/Snaps/* /var/lib/snapd/snapshots/")
os.system("sudo snap restore " +snapversion)
print("============================================================================")
#Restore Manual installed .deb Files
print("Restore manual installed .deb Files")
time.sleep(2)
debs=os.listdir(path+"/Backup/debs")
os.chdir(path+"/Backup/debs")
for files in debs:
    os.system("sudo dpkg -i "+files)

print("============================================================================")
#Restore sources
print("Restore Sources")
time.sleep(2)
os.system("sudo cp -R "+path+"/Backup/sources/sources.list.d/* /etc/apt/sources.list.d/")
os.system("sudo apt clean")
os.system("sudo apt update")


print("============================================================================")
#Restore Rest
print("Restore Packages")
time.sleep(2)
os.system("sudo xargs -a '"+os.path.join(path, "packages.list.save")+"' sudo apt install")
print("============================================================================")
print("Restore complete. Please press any key to close this window")
programPause = input("and return to the iBuntu Update Tool")
