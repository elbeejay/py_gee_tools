#!/usr/bin/env python

# This script is used to write the GEE API key (available as GEE_API_KEY environment variable in the travis machine via the travis variable encription mechanism) to a file

# script from https://github.com/loicdtx/landsat-extract-gee/blob/c40318760af5d9f712e4d6ad51ffac345607c574/travis_setup.py

import os

# Get key
key = os.environ['GEE_API_KEY']

# Build line
line = '{"refresh_token": "%s"}' % key

# Create directory
os.makedirs(os.path.expanduser('~/.config/earthengine/'))

# Write line to file
with open(os.path.expanduser('~/.config/earthengine/credentials'), 'w') as dst:
   dst.write(line)
