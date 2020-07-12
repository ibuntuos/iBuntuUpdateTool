#!/bin/bash
BASEDIR=$(dirname "$0")

if [ -d "$BASEDIR/Backup" ]; then
echo "We try now to restore your previously saved programs and settings"
echo "sudo cp -R ./Backup/Snaps/* /var/lib/snapd/"
sudo cp -R $BASEDIR/Backup/Snaps/* /var/lib/snapd/
echo "sudo cp -R ./Backup/Applications/* /usr/share/applications/"
sudo cp -R $BASEDIR/Backup/Applications/* /usr/share/applications/
echo "sudo cp -R ./Backup/sources/* /etc/apt/sources.list.d/"
sudo cp -R $BASEDIR/Backup/sources/* /etc/apt/sources.list.d/
echo "-----------------------------------------------------------------"
echo "Updating Package-Sources:"
sudo apt update
echo "-----------------------------------------------------------------"
echo "Reinstall Packages:"
xargs -a $BASEDIR/packages.list.save sudo apt install -y
echo "-----------------------------------------------------------------"
echo "Remove Backup:"
sudo rm -R $BASEDIR/Backup
fi
