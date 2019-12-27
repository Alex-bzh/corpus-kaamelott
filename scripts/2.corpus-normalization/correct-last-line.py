#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Deletes the last line of a script if it a metadata"""

# Modules to import
import os

# Main
if __name__ == '__main__':

    path = '../../sample'
    # List of screenplays
    screenplays = os.listdir(path)

    # For each screenplay
    for screenplay in screenplays:
        # Fetching lines of a screenplay
        with open(f'{path}/{screenplay}') as src:
            lines = src.readlines()
        # If the last line begins with "Rédigé par", delete it
        if lines[-1].startswith('Rédigé par'):
            lines = lines[:-1]
            with open(f'{path}/{screenplay}', 'w') as dest:
                for line in lines:
                    dest.write(line)