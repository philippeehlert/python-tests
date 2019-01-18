#!/bin/bash

set -ex

cd "$(dirname ${BASH_SOURCE[0]})"
[ -e venv ] || virtualenv -p python2.7 venv
source venv/bin/activate

pip install -U -r dev-requirements.txt

pytest
