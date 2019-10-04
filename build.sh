#!/bin/bash

export ADDITION_LIB="addition_backend.o"

g++ addition.cpp -o $ADDITION_LIB
ls
pip install .