#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Selects a random sample of screenplays"""

#
# Modules to import
#
import os, shutil

# Main
if __name__ == '__main__':

    raw = '../../raw/'              # Path to raw files
    sample = '../../sample/'        # Path to sample files
    screenplays = os.listdir(raw)   # List of screenplays

    """
    For each screenplay, if its index number is a multiple of 10,
    make a copy!
    """
    for index, screenplay in enumerate(screenplays):
        if not(index % 10):
            shutil.copy(raw + screenplay, sample)