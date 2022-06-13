#!/bin/bash

if [ $# -eq 0 ];
then
python solver.py
elif [ $# -eq 3 ];
then
python solver.py $1 $2 $3  # [csv_subdir_name] [generations] [time_limit]
else
python solver.py $1 $2 $3 $4    # [csv_subdir_name] [generations] [time_limit] [population_size]
fi