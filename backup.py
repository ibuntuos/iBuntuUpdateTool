import subprocess
import os
import glob
import tarfile
import time


#path=os.path.dirname(os.path.realpath(__file__))
path=os.environ['HOME']
print("============================================================================")
os.system("echo 'We try now to backup your packages, sourcelists and snaps'")
os.system("echo for this we need Access to your File-System.")
os.system("sudo echo 'Granted. We beginn.'")
    #path = WorkPath
os.system("sudo rm -R "+path+"/Backup/")
time.sleep(5)
os.system("sudo mkdir "+path+"/Backup")
os.system("sudo mkdir "+path+"/Backup/Snaps")
os.system("sudo mkdir "+path+"/Backup/apt-clone")
os.system("sudo mkdir "+path+"/Backup/debs")
os.system("sudo mkdir "+path+"/Backup/sources")
print("============================================================================")

#Backup Snaps
print("Backup snaps")
time.sleep(2)
os.system("sudo snap list > "+path+"/snappackage.save.list")

#Backup .debs and sources
print("=========================================================================")
print("Backup debs and sources")
print("Be patient, this will take a while")
print("First we create a backup with apt-clone")
time.sleep(2)
os.system("sudo apt-clone clone --with-dpkg-repack  "+path+"/Backup/")
print("=========================================================================")
#Extract sources list
print("Now we extract your additional package-sources and your manual installed .deb files")
time.sleep(2)
for file in glob.glob(path+"/Backup/apt-clone-*"):
    print(file)
    os.system("sudo chmod -R 777 "+path+"/Backup")
    time.sleep(2)
    with tarfile.open(file) as tar:
        subdir_and_files_sources = [
        tarinfo for tarinfo in tar.getmembers()
            if tarinfo.name.startswith("./etc/apt/sources.list.d")
        ]

        subdir_and_files_debs = [
        tarinfo for tarinfo in tar.getmembers()
            if tarinfo.name.startswith("./var/lib/apt-clone/debs")
        ]

        subdir_and_files_keys = [
        tarinfo for tarinfo in tar.getmembers()
            if tarinfo.name.startswith("./etc/apt/trusted.gpg.d")
        ]

        tar.extractall(path=path+"/Backup/apt-clone/", members=subdir_and_files_sources)
        tar.extractall(path=path+"/Backup/apt-clone/", members=subdir_and_files_debs)
        tar.extractall(path=path+"/Backup/apt-clone/", members=subdir_and_files_keys)


debs=os.listdir(path+"/Backup/apt-clone/var/lib/apt-clone/debs/")

#Find Matches
packagelist=[]
filepath = path+"/packages.list.save"
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       line=line.split("\n")
       packagelist.append(line[0])
       line = fp.readline()
       cnt += 1

for debfile in debs:
    for package in packagelist:
        if  debfile.split("_")[0] == package:
            os.system("sudo cp -R "+path+"/Backup/apt-clone/var/lib/apt-clone/debs/"+debfile+" "+path+"/Backup/debs/")

os.system("sudo cp -R "+path+"/Backup/apt-clone/etc/apt/sources.list.d/ "+path+"/Backup/sources/")
os.system("sudo cp -R "+path+"/Backup/apt-clone/etc/apt/trusted.gpg.d/ "+path+"/Backup/sources/")
os.system("sudo rm -R "+path+"/Backup/apt-clone-*")
os.system("sudo rm -R "+path+"/Backup/apt-clone/")
print("============================================================================")
print("Backup of your programs complete. Please press any key to close this window")
programPause = input("and return to the iBuntu Update Tool")
