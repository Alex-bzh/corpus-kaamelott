#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Builds the Kaamelott corpus"""

#
# Modules to import
#
import tools, re

# Main
if __name__ == '__main__':

    # Scrap hypnoweb file on Kaamelott
    url = 'https://kaamelott.hypnoweb.net/kaamelott/guide.119.2/'
    html = tools.get_html_from_url(url, 'ISO-8859-1')
    episodes = tools.parse_html_by_class(html,
        '.tabs-content .content tr td a')

    # For each episode, get the href and put it on a file
    for episode in episodes:
        with open('../../static/episodes.txt', 'a') as file:
            link = episode.get('href')
            link = link.replace('/kaamelott/episode.119.2/', '')
            file.write(link + '\n')

    # Reads the file in which the links to episodes are stored
    with open('../../static/episodes.txt') as file:
        lines = file.readlines()

    """
    For each line in the file:
        - builds the url to scrap
        - gets the content of the script
        - stores the content in a text file
    """
    pattern = '(?P<episode>[0-9ES]{6}-[a-z0-9-]*)-[0-9]*\.html'

    for line in lines:
        url = f'https://kaamelott.hypnoweb.net/kaamelott/episode.119.2/{line}'
        html = tools.get_html_from_url(url, 'ISO-8859-1')
        scripts = tools.parse_html_by_class(html, '#script_vo div')

        m = re.match(pattern, line)

        if len(scripts) != 0:
            with open(f"../../raw/{m.group('episode')}.txt", 'w') as file:
                for text in scripts[0].stripped_strings:
                    file.write(text)
                    file.write('\n')
