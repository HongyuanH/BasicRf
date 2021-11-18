#!/bin/bash
python3 -m venv venv
cd venv
. bin/activate
pip3 install -r ../requirements.txt
cd ..