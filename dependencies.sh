#!/bin/bash
echo "iBuntu Update Tool could not load we try to install missing dependencies"
echo "After this window closes just open the app again."
echo "========================================================================"
echo "Installing: python3-tk, python3-pip and PySimpleGui:"
sudo apt update
sudo apt install python3-tk python3-pip -y
pip3 install pysimplegui
