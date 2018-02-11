#!/usr/bin/env bash

# The location of this script.
LOCATION=$(dirname $0)

psql -h localhost -d import_using_pubmedportable -U parser -f $LOCATION/truncate-tables.sql
