#!/bin/bash

set -e

export LD_PRELOAD=/lib/x86_64-linux-gnu/libSegFault.so
export SEGFAULT_SIGNALS=all
ls /lib/x86_64-linux-gnu/

#export ADDITION_LIB="addition_backend.o"
#
#g++ addition.cpp -o $ADDITION_LIB
#ls
#python --version

python_major=$(python -c 'import sys; import __future__; print(sys.version_info.major)')
echo MAJOR $python_major

cd $SRC_DIR/src
git clone https://github.com/bigartm/bigartm.git
cd bigartm
mkdir build && cd build

# installs by default under /usr/local. To manipulate this use -DCMAKE_INSTALL_PREFIX=xxx flag in cmake
if [[ "$python_major" == "2" ]]; then
    cmake ..
elif [[ "$python_major" == "3" ]]; then
    cmake -DPYTHON=python3 ..
fi
echo DONE cmake
printenv
sudo apt-get --yes install build-essential libboost-all-dev gfortran libblas-dev liblapack-dev

make
echo DONE make

sudo make install
echo DONE make install

export ARTM_SHARED_LIBRARY=/usr/local/lib/libartm.so
ls $ARTM_SHARED_LIBRARY

which bigartm


export COLLECTIONS_DIR="$SRC_DIR/collections"
mkdir $COLLECTIONS_DIR

pip install .
