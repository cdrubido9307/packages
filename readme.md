# Installing Python Packages with a Python Script

## Overview
The process of packages instalation can be very anoying while setting up a python developer enviorment.
This simple program will take care of the task of installing all your desire python packages.

## Usage
Add all your favorite packages to the `packages.txt`.
If you a pip user simply run `python install_packages.py pip`. If you are a conda user uncoment line 4 and rum `python install_packages.py conda`. Recall that for using conda, anaconda must be installed.
In the case that a package is not installed correctly and error message will be display to console and the program will jump to the next packages in the installation packages queue.
 
