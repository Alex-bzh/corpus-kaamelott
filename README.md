# Corpus Kaamelott

## Presentation

This corpus is a collection of screenplays (400) from the French TV show [*Kaamelott*](https://fr.wikipedia.org/wiki/Kaamelott). The transcriptions are not official. Originally, they have been automatically scraped from a French website: [Hypnoweb](https://www.hypnoweb.net/); then, they have been normalized by automatic procedures to produce the text version.

Ultimately, *Corpus Kaamelott* intends to be an NLP-ready annotated resource, available in multiple formats.

## Distribution

At this time, only a text version is available, in the folder `txt`. As things progress, you can evaluate the result of the most recent developments in the `sample` folder, where a list of screenplays are gradually formatted in text mode.

## Resources

- `static/characters.txt`: directory of characters in Kaamelott.
- `static/episodes.txt` lists all the episodes transcribed. To consult the detailed sheet of an episode, just prefix the title of an episode with this string: `https://kaamelott.hypnoweb.net/kaamelott/episode.119.2/`. Example: [https://kaamelott.hypnoweb.net/kaamelott/episode.119.2/S01E02-la-tarte-aux-myrtilles-2957.html](https://kaamelott.hypnoweb.net/kaamelott/episode.119.2/S01E02-la-tarte-aux-myrtilles-2957.html).
- `static/index.txt` is a collection of metadata about the original screenplays scraped from *Hypnoweb*. In order, the metadata are: title, season number, episode number in the season, alias of the transcriber and, finally, the source.
- The `txt` folder contains the 400 screenplays in text format. Each line lists, in tabulated format, the speaker and his cue.

## Credits

Transcribed screenplays come from [Hypnoweb.net](https://www.hypnoweb.net/).
