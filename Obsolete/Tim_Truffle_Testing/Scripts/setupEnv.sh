#!/bin/bash

# Script to interface between python / solidity deployment
# Tim Tscheppe, Marquette University

# Ensure we are running on a working OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # This is what I'm working on, and can only promise code will work on this platform
        echo "OS Found : Linux-GNU"
fi
if [[ "$OSTYPE" == "darwin"* ]]; then
        # MacOS
        echo "Error: OS not supported"
        exit
fi
if [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
        echo "OS found : POSIX compatibility layer and Linux environment emulation for Windows"
fi 
if [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
        echo "OS found : Lightweight shell and GNU utilities compiled for Windows (part of MinGW)"
fi
if [[ "$OSTYPE" == "win32" ]]; then
        # TODO: Look into adding support for this
        echo "Error: OS not supported"
        exit
fi

# Store location of file path for python executable
PYTHON_FILE_PATH = export PATH=$PATH:$(pwd):/python/DatabaseInterfactTest.py

# Run python executable
echo python PYTHON_FILE_PATH

# TODO: Capture python output

