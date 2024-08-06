#!/bin/bash

set -eu
set -o pipefail

module use /g/data/hh5/public/modules
module load conda/analysis3

set -x

python example_async.py

python example_multiprocessing.py

mpirun python example_mpi4py.py

