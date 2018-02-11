#!/usr/bin/env bash


# The folder where the PubMed XML files are located.
# These files will be parsed and imported into the specified database.
INPUT_XMLS=tmp/pubmed-2018-updatefiles/

# The name of the database where the PubMed XML files will be imported.
TARGET_DB=import_using_pubmedportable

# How many XML files are parsed concurrently.
PROCESSES=4

# How to get help:
#python PubMedParser.py -h

# Keep the content of the database, do not truncate it:
#python PubMedParser.py -i $INPUT_XMLS -d $TARGET_DB -p $PROCESSES --no-cleaning

# Truncate the database, delete its content:
python PubMedParser.py -i $INPUT_XMLS -d $TARGET_DB -p $PROCESSES -c
