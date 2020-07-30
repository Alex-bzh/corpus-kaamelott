# Corpus Kaamelott

## Presentation

This corpus is a collection of screenplays (400) from the French TV show [*Kaamelott*](https://fr.wikipedia.org/wiki/Kaamelott). The transcriptions are not official. Originally, they have been automatically scraped from a French website: [Hypnoweb](https://www.hypnoweb.net/); then, they have been normalized by automatic procedures to produce a text version.

Ultimately, *Corpus Kaamelott* intends to be an NLP-ready annotated resource, available in multiple formats.

See the [documentation](https://github.com/Alex-bzh/corpus-kaamelott/wiki) for more informations.

## Distribution

At this time, two formats are available:
- text version;
- POS tagged version (word/tag).

As things progress, you can evaluate the result of the most recent developments in the `sample/` folder.

## Resources

- `sample/` folder is a set of some screenplays selected by sampling. By nature, they should not be considered as stable, but as a work in progress.
- `static/cast.txt`: makes the link between characters and the actors who interpret them.
- `static/characters.txt`: directory of characters in Kaamelott.
- `static/episodes.txt` lists all the episodes transcribed on *Hypnoweb*.
- `static/index.txt` is a collection of metadata about the original screenplays scraped from Hypnoweb.
- `static/ne.txt` lists the named entities.
- `static/slang.txt` is a lexicon of slang expressions in tabulated format.
- The `tagged/` folder contains the 400 screenplays in tagged format (e.g. : token/tag). Each line lists, in tabulated format, the speaker and his cue, tagged.
- The `tools/` folder presents some useful scripts to manipulate the corpus.
- The `txt/` folder contains the 400 screenplays in text format. As for the tagged version, each line lists, in tabulated format, the speaker and his cue.

## Credits

Transcribed screenplays come from [Hypnoweb.net](https://www.hypnoweb.net/).

The reference lexicon for spellchecking comes from *Lexique 3* (v3.83) :
- New, Boris, Pallier, Christophe, Ferrand, Ludovic, Matos, Rafael (2001) Une base de données lexicales du français contemporain sur internet: LEXIQUE, *L’Année Psychologique*, 101, 447-462. <http://www.lexique.org>
- New, Boris, Pallier, Christophe, Brysbaert, Marc, Ferrand, Ludovic (2004) Lexique 2 : A New French Lexical Database. *Behavior Research Methods, Instruments, & Computers*, 36 (3), 516-524.

French slang lexicon was created thanks to [Bob](https://www.languefrancaise.net/Bob/Introduction).

The POS-tagger has been trained with the [*French Treebank*](http://ftb.linguist.univ-paris-diderot.fr) :
- Abeillé, Anne, Clément, L., Toussenel, F. – "Building a treebank for French". In Abeillé, Anne (ed.) *Treebanks*. – Dordrecht : Kluwer, 2003. – p. 165-187.
