#!/bin/bash

cd ~/TransE
git pull origin Authority
cd WN
python ./WN_parse.py
python ./WN_TransE.py
python ./WN_evaluation.py
python ./WN_test.py