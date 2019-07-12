#!/bin/sh

set -v -e -x

git clone https://github.com/marco-c/breakpad-mac-update-symbols
cd breakpad-mac-update-symbols
./run.sh
