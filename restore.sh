#!/bin/bash
BASEDIR=$(dirname "$0")
if [ -d "$BASEDIR/Backup" ]; then
xargs -a $BASEDIR/packages.list.save sudo apt install -y
sudo cp -R $BASEDIR/Backup/Snaps/* /var/lib/snapd/
sudo cp -R $BASEDIR/Backup/Applications/* /usr/share/applications/
sudo cp -R $BASEDIR/Backup/sources/* /etc/apt/sources.list.d/
sudo rm -R $BASEDIR/Backup
fi
