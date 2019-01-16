#!/bin/sh

set -v -e -x

# TODO: We shouldn't install these at runtime, but in the docker image.
pip install redo
pip install requests

URL=https://queue.taskcluster.net/v1/task/${ARTIFACT_TASKID}/artifacts/public/build/target.crashreporter-symbols.zip
wget -q --method HEAD "${URL}" && python upload_symbols.py ${URL}
