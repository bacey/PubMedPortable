#!/usr/bin/env bash


# The folder where the PubMed XML files are located.
# These files will be parsed and imported into the specified database.
INPUT_XMLS=tmp/pubmed-baseline-files/

# The name of the database where the PubMed XML files will be imported.
TARGET_DB=import_using_pubmedportable

# How many XML files are parsed concurrently.
PROCESSES=3

# How to get help:
#python PubMedParser.py -h

# Keep the content of the database, do not truncate it:
python PubMedParser.py -i $INPUT_XMLS -d $TARGET_DB -p $PROCESSES -c False

# Truncate the database, delete its content:
#python PubMedParser.py -i $INPUT_XMLS -d $TARGET_DB -p $PROCESSES -c
