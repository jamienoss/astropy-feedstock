#!/bin/bash

if [[ `uname` == Linux ]]; then
    export CFLAGS="$CFLAGS -std=c99"
    export CC=gcc
elif [[ `uname` == Darwin ]]; then
    export CFLAGS="$CFLAGS -std=c99 -m64"
    export CC=clang
fi

$PYTHON setup.py install --offline --old-and-unmanageable
