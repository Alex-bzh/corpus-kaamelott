# Normalizing the corpus

The scripts must be run in this order:
1. create-index.py
2. correct-last-line.py
3. a-clean-sweep.py
4. delete-directions.py

## Warning

We are concern that the scripts erase some replies (especially `delete-directions.py`), mainly due to lack of transciption directives, but the loss is tiny compared to the gain.