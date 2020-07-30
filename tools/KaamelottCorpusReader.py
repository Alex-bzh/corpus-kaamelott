#!/usr/bin/python
#-*- coding: utf-8 -*-

"""Custom tagged corpus reader class to manipulate the Kaamelott corpus."""

#
#   Modules to import
#
import csv
import re
from nltk.tag import str2tuple, tuple2str
from nltk.corpus.reader import CorpusReader

class KaamelottCorpusReader(CorpusReader):
    """KaamelottCorpusReader is based on the CorpusReader
    from NLTK.
    """

    #
    #   Constructor
    #

    def __init__(self, root, fileids):
        """Constructs a reader for the Kaamelott corpus,
        based on a tagged version.

        Keyword arguments:
        root -- the root directory for the Kaamelott corpus.
        fileids -- A list or regexp specifying the fileids in this corpus.
        """
        CorpusReader.__init__(self, root, fileids)

    #
    #   Private methods
    #

    def _clean_spaces(self, text):
        """Removes, in a string, spaces around a punctuation mark,
        if needed.
        """

        # Spaces before a double quote, a comma or a full stop
        # are eliminated.
        text = re.sub('\s([",\.…])', '\g<1>', text)
        # Same fate for spaces around a dash or a single quote
        text = re.sub('\s?([’-])\s', '\g<1>', text)

        return text

    def _reader(self, fileid):
        """Loads a reader for the file as a list of tuples,
        containing two elements: the speaker and its cue.
        """

        data = list()

        # Opens the file as a CSV dictionary with two keys:
        # "speaker": the name of the character
        # "cue": the utterances of the speaker
        with open(fileid, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter='\t',
                fieldnames=['speaker', 'cue'])

            # Each line is stored as a tuple
            [
                data.append((row['speaker'], row['cue']))
                for row in reader
            ]

        return data

    def _tokens_to_raw(self, tokens):
        """Transforms a list of tokens into raw text"""

        # The raw string to return
        raw = str()

        # Tokens are tuples of (word, tag).
        # The goal is to merge the tuples with a blank space,
        # by keeping only the first element (the word).
        raw += ' '.join(
            [
                re.search(r'(.*)/.+', tuple2str(token)).group(1)
                for token in tokens
            ])

        # Clean spaces around punctuation marks
        raw = self._clean_spaces(raw)

        return raw

    def _tokenize(self, string):
        """Transforms a tagged string (format word/tag)
        into a list of tuples: (word, tag)
        """
        tokens = [ str2tuple(pair) for pair in string.split() ]

        return tokens

    #
    #   Public methods
    #

    def raw(self, fileids=None):
        """Returns the content of the file as raw text"""

        text = str()

        for (fileid, enc) in self.abspaths(fileids, True):

            # List of tuples: (speaker, cue)
            reader = self._reader(fileid)

            # Each entry is analysed to delete the tag from the words
            for row in reader:
                tokens = self._tokenize(row[1])
                cue = self._tokens_to_raw(tokens)
                text += f'{row[0]}\t{cue}\n'

        # The text, minus the last blank line
        return text[:-1]

    def words(self, fileids=None):
        """Returns a simple list of words."""

        # The list to return
        words = list()

        for (fileid, enc) in self.abspaths(fileids, True):
            # Fetches a list of lines filled with tuples: (speaker, cue)
            reader = self._reader(fileid)

            # Each line is tokenized into tuples (word, tag).
            # Then only the word is added to the list.
            [
                [
                    words.append(token[0])
                    for token in self._tokenize(row[1])
                ]
                for row in reader
            ]

        return words

    def sents(self, fileids=None):
        """Returns a simple list of sentences."""

        # Strong punctuation marks.
        marks = ['…', '.', '!', '?']

        # The list of sentences to return
        sentences = list()

        for (fileid, enc) in self.abspaths(fileids, True):
            # Fetches a list of lines filled with tuples: (speaker, cue)
            reader = self._reader(fileid)

            for row in reader:
                # A fresh sentence
                sentence = str()
                # Tags are removed from the utterances
                utterances = re.sub(r'/[\+\w]+', '', row[1])
                # Spaces around the punctuation marks are cleaned
                utterances = self._clean_spaces(utterances)
                # Each character is added to the sentence
                for c in utterances:
                    sentence += c
                    # And if a strong punctuation mark is found,
                    # the sentence is closed and a new one opened.
                    if c in marks:
                        sentences.append(sentence.strip())
                        sentence = str()

        return sentences

    def tagged_corpus(self, fileids=None):
        """
        Returns the corpus as a list of cues indexed by the fileid.
        All the cues are word-tokenized.
        """

        # The object returned is a dictionary
        corpus = dict()

        for (fileid, enc) in self.abspaths(fileids, True):

            # Each file given is a distinct entry in the dictionary
            corpus.update({ fileid: list() })

            # Opens the file as csv
            reader = self._reader(fileid)

            for row in reader:
                # Each cue is tokenized, e.g. splitted into tuples.
                # Originally a cue is a string of pairs: word/tag.
                tokens = self._tokenize(row[1])
                # (speaker, [(word, tag), …])
                corpus[fileid].append((row[0], tokens))

        return corpus

    def tagged_words(self, fileids=None):
        """Returns a simple list of tokens as tuples (word, tag)."""

        # A collection of tagged words
        tagged_words = list()

        for (fileid, enc) in self.abspaths(fileids, True):

            # Fetches a list of lines filled with tuples: (speaker, cue)
            reader = self._reader(fileid)

            # Transforms each cue into a list of tuples (word, tag)
            # that is added to the collection.
            [
                [
                    tagged_words.append(token)
                    for token in self._tokenize(row[1])
                ]
                for row in reader
            ]

        return tagged_words


    def tagged_sents(self, fileids=None):
        """Returns a simple list of sentences where
        each word-form is tagged.
        """

        # Strong punctuation marks.
        marks = [
                    ('…', 'PONCT'), ('.', 'PONCT'),
                    ('!', 'PONCT'), ('?', 'PONCT')
                ]

        # List of sentences in a file
        sentences = list()

        for (fileid, enc) in self.abspaths(fileids, True):

            # Fetches a list of lines filled with tuples: (speaker, cue)
            reader = self._reader(fileid)

            for row in reader:

                # Each cue is at least composed of one sentence
                sentence = list()

                # Cue is tokenized
                tokens = self._tokenize(row[1])

                for token in tokens:

                    # The token is added to the current sentence.
                    sentence.append(token)

                    # If the token is somewhat close to a
                    # strong punctuation mark…
                    if token in marks:

                        # … the sentence is considered as stopped
                        # and a fresh one starts.
                        sentences.append(sentence)
                        sentence = list()

        return sentences
