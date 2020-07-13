#!/bin/bash
BASEDIR=$(dirname "$0")
if [ ! -d "$BASEDIR/Backup" ]; then
sudo mkdir $BASEDIR/Backup
sudo mkdir $BASEDIR/Backup/Snaps
sudo mkdir $BASEDIR/Backup/Applications
sudo mkdir $BASEDIR/Backup/sources
fi
sudo rm -R $BASEDIR/Backup/Snaps/*
sudo rm -R $BASEDIR/Backup/Applicationsps/*
sudo rm -R $BASEDIR/Backup/sources/*
echo "We try now to backup your packages, sourcelists and snaps"
sudo cp -R /var/lib/snapd/*  $BASEDIR/Backup/Snaps/
echo "sudo cp -R /usr/share/applications/*.desktop  ./Backup/Applications/"
sudo cp -R /usr/share/applications/*.desktop  $BASEDIR/Backup/Applications/
echo "sudo cp -R /etc/apt/sources.list.d/*  .R/Backup/sources/"
sudo cp -R /etc/apt/sources.list.d/*  $BASEDIR/Backup/sources/
echo "--------------------------------------------------------------------"
echo "Backup done. This window should close automatically"
