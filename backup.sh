#!/bin/bash
BASEDIR=$(dirname "$0")
if [ ! -d "$BASEDIR/Backup" ]; then
echo "We try now to backup your packages, sourcelists and snaps"

sudo mkdir $BASEDIR/Backup
sudo mkdir $BASEDIR/Backup/Snaps
sudo mkdir $BASEDIR/Backup/Applications
sudo mkdir $BASEDIR/Backup/sources

sudo cp -R /var/lib/snapd/*  $BASEDIR/Backup/Snaps/
echo "sudo cp -R /usr/share/applications/*.desktop  ./Backup/Applications/"
sudo cp -R /usr/share/applications/*.desktop  $BASEDIR/Backup/Applications/
echo "sudo cp -R /etc/apt/sources.list.d/*  .R/Backup/sources/"
sudo cp -R /etc/apt/sources.list.d/*  $BASEDIR/Backup/sources/
echo "--------------------------------------------------------------------"
echo "Backup done. This window should close automatically"
fi
