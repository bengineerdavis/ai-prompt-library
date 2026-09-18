#!/bin/sh
# Needs: cmake >= 3.20, a C compiler, git, network.
set -eu

cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build

printf 'built build/cmake-demo\n'
