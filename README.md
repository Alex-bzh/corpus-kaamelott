# Corpus Kaamelott

## Presentation

This corpus is a collection of screenplays (400) from the French TV show [*Kaamelott*](https://fr.wikipedia.org/wiki/Kaamelott). The transcriptions are not official. Originally, they have been automatically scraped from a French website: [Hypnoweb](https://www.hypnoweb.net/); then, they have been normalized by automatic procedures to produce a text version.

Ultimately, *Corpus Kaamelott* intends to be an NLP-ready annotated resource, available in multiple formats.

## Distribution

At this time, only a text version is available, in the folder `txt/`. As things progress, you can evaluate the result of the most recent developments in the `sample/` folder, where a list of screenplays are gradually formatted in text mode.

## Resources

- `sample/` folder is a set of 40 screenplays selected by sampling. By nature, they should not be considered as stable, but as a work in progress.
- `static/characters.txt`: directory of characters in Kaamelott.
- `static/episodes.txt` lists all the episodes transcribed on *Hypnoweb*. To consult the detailed sheet of an episode, just prefix the title of an episode with this string: `https://kaamelott.hypnoweb.net/kaamelott/episode.119.2/`. Example: [https://kaamelott.hypnoweb.net/kaamelott/episode.119.2/S01E02-la-tarte-aux-myrtilles-2957.html](https://kaamelott.hypnoweb.net/kaamelott/episode.119.2/S01E02-la-tarte-aux-myrtilles-2957.html).
- `static/index.txt` is a collection of metadata about the original screenplays scraped from Hypnoweb. In order, the metadata are: title, season number, episode number in the season, alias of the transcriber and, finally, the source.
- `static/ne.txt` lists the named entities.
- `static/slang.txt` is a lexicon of slang expressions in tabulated format. The columns are, in order: the word-form, the lemma, the POS and a brief description.
- The `tagged/` folder contains the 400 screenplays in tagged format (e.g. : token/tag). Each line lists, in tabulated format, the speaker and his cue, tagged.
- The `txt/` folder contains the 400 screenplays in text format. As for the tagged version, each line lists, in tabulated format, the speaker and his cue.

## Credits

Transcribed screenplays come from [Hypnoweb.net](https://www.hypnoweb.net/).

The reference lexicon for spellchecking comes from *Lexique 3* (v3.83) :
- New, Boris, Pallier, Christophe, Ferrand, Ludovic, Matos, Rafael (2001) Une base de données lexicales du français contemporain sur internet: LEXIQUE, *L’Année Psychologique*, 101, 447-462. <http://www.lexique.org>
- New, Boris, Pallier, Christophe, Brysbaert, Marc, Ferrand, Ludovic (2004) Lexique 2 : A New French Lexical Database. *Behavior Research Methods, Instruments, & Computers*, 36 (3), 516-524.

French slang lexicon was created thanks to [Bob](https://www.languefrancaise.net/Bob/Introduction).

The POS-tagger has been trained with the [*French Treebank*](http://ftb.linguist.univ-paris-diderot.fr) :
- Abeillé, Anne, Clément, L., Toussenel, F. – "Building a treebank for French". In Abeillé, Anne (ed.) *Treebanks*. – Dordrecht : Kluwer, 2003. – p. 165-187.
