import subprocess
import os
import glob
import tarfile
import time
import copy


#path=os.path.dirname(os.path.realpath(__file__))
path=os.environ['HOME']
current_user=os.environ.get('USER')
print("============================================================================")
os.system("echo 'We try now to restore your previously saved programs and settings'")
os.system("echo for this we need Access to your File-System.")
os.system("sudo echo 'Granted. We beginn.'")
print("============================================================================")
#Restore Snaps
print("Restore Home Folder")
time.sleep(2)
os.system("sudo mkdir /tmp/homesync")
os.system("sudo chown "+current_user+":"+current_user+" "+path+"/Migrator_Backup.7z")
os.system("sudo 7z x "+path+"/Migrator_Backup.7z -o/tmp/homesync/ -aoa")
os.system("sudo chmod 777 -R /tmp/homesync")
os.system("sudo chown -R "+current_user+":"+current_user+" /tmp/homesync")


#rsync files from live system to home
print("rsync files from live system to home")
os.system("sudo rsync --archive --update --progress /tmp/homesync/ "+path+"/")
os.system("sudo chown -R "+current_user+":"+current_user+" "+path)


#delete sync
os.system("sudo rm -R /tmp/homesync")
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
print("Restore Sources and perform update")
time.sleep(2)
os.system("sudo cp -R "+path+"/Backup/sources/sources.list.d/* /etc/apt/sources.list.d/")
os.system("sudo cp -R "+path+"/Backup/sources/trusted.gpg.d/* /etc/apt/trusted.gpg.d/")
os.system("sudo apt clean")
os.system("sudo apt autoclean")
os.system("sudo apt update")
os.system("sudo apt upgrade -y")
print("============================================================================")
#Restore Snaps
print("Restore Snaps")
time.sleep(2)
os.system("sudo snap list > "+path+"/snappackage_new.save.list")
snaplist=[]
snaplist2=[]
snaplist3=[]
with open(path+"/snappackage.save.list") as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line=line.split("    ")
       snaplist.append(line[0])
       line = fp.readline()
snaplist.pop(0)

#Restorelist
with open(path+"/snappackage_new.save.list") as fp2:
   line2 = fp2.readline()
   cnt2 = 1
   while line2:
       line2=line2.split("    ")
       snaplist2.append(line2[0])
       line2 = fp2.readline()
snaplist2.pop(0)

snaplist3=copy.copy(snaplist)
for snappy in snaplist:
    for newsnap in snaplist2:
        if snappy == newsnap:
            snaplist3.remove(snappy)

#Restoring
for snapprog in snaplist3:
    os.system("sudo snap install " +snapprog)

print("============================================================================")
#Restore Packaes
print("Restore Packages")
time.sleep(2)
os.system("sudo xargs -a '"+os.path.join(path, "packages.list.save")+"' sudo apt install -y")
print("============================================================================")
print("Restore complete. Please press any key to close this window")
programPause = input("and return to the iBuntu Update Tool")
