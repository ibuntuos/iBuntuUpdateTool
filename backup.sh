#!/bin/bash
BASEDIR=$(dirname "$0")
if [ ! -d "$BASEDIR/Backup" ]; then
#if [ ! -d $BASEDIR/Backup]; then
sudo mkdir $BASEDIR/Backup
sudo mkdir $BASEDIR/Backup/Snaps
sudo mkdir $BASEDIR/Backup/Applications
sudo mkdir $BASEDIR/Backup/sources

sudo cp -R /var/lib/snapd/*  $BASEDIR/Backup/Snaps/
sudo cp -R /usr/share/applications/*.desktop  $BASEDIR/Backup/Applications/
sudo cp -R /etc/apt/sources.list.d/*  $BASEDIR/Backup/sources/
fi
