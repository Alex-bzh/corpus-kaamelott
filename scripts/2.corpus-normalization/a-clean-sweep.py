#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Roughly cleans the screenplay: deleting stage directions…"""

# Modules to import
import os, re

# Main
if __name__ == '__main__':
    
    path = '../../sample'
    screenplays = os.listdir(path)

    for screenplay in screenplays:
        with open(f'{path}/{screenplay}') as src:
            # Reads the screenplay
            text = src.read()
            # Removes text between parenthesis
            text = re.sub('\n?\(\n?.*\n?\)\n?', '', text)
            # Substitutes ":" + newline by a tabulation
            text = text.replace(':\n', '\t')
            # Substitutes newline + ":" by a tabulation
            text = text.replace('\n:', '\t')
            # Substitutes ":" by a tabulation
            text = text.replace(':', '\t')
            # Deletes extra spaces around a tabulation
            text = re.sub('\s?\t\s?', '\t', text)

        with open(f'{path}/{screenplay}', 'w') as dest:
            dest.write(text)