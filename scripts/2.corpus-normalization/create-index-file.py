#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Modules to import
import tools, os

# Main
if __name__ == '__main__':

    screenplays = os.listdir('../../raw')   # List of screenplays
    metadata = []                           # Empty list of metadata

    # For each screenplay
    for index, screenplay in enumerate(screenplays):
        # Fetches metadata
        metadata.append(tools.get_metadata(screenplay))
        # Opens the screenplay
        with open(f'../../raw/{screenplay}') as file:
            # Focus on the last line
            last_line = file.readlines()[-1]
            # Gets the alias
            alias = tools.get_alias(last_line)
            # Adds the alias in the metadata array
            tools.add_meta(alias, index, metadata)
        # Finally, adds the owner of the script
        tools.add_meta('Hypnoweb', index, metadata)

    # Writes the index.txt file
    with open('../../static/index.txt', 'a') as file:
        # For each block of metadata…
        for block in metadata:
            # … same treatment for each metadata
            for i, meta in enumerate(block):
                # with comma between each, except for the last one
                file.write(f'{meta},') if i < (len(block) - 1) else file.write(meta)
            # Line break
            file.write('\n')