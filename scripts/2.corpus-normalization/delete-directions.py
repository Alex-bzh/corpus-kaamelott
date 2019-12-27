#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Deletes the stage directions"""

# Modules to import
import os, re

# Main
if __name__ == '__main__':
    
    path = '../../sample'
    screenplays = os.listdir(path)

    # A collection of the lines after cleaning
    new_lines = []

    for screenplay in screenplays:
        
        # Gets a list of lines
        with open(f'{path}/{screenplay}') as src:
            lines = src.readlines()
        
        # For each line…
        for line in lines:
            # … if there is no tabulation…
            if '\t' in line:
                # … it is doubtless a stage direction
                new_lines.append(line)

        # Rewrites the screenplay accordingly
        with open(f'{path}/{screenplay}', 'w') as dest:
            for line in new_lines:
                dest.write(line)