#!/bin/sh

set -v -e -x

wget https://index.taskcluster.net/v1/task/project.socorro.mac-update-symbols.latest/artifacts/public/build/target.crashreporter-symbols.zip
python upload_symbols.py target.crashreporter-symbols.zip
