#!/bin/bash

aocInput=/home/joseph/development/work_projects/advent_of_code/2018/day2/boxIDs.csv

if [[ -f $aocInput ]]; then {
	export AOC_INPUT_FILE=$aocInput
}
fi

echo "Input file:" $AOC_INPUT_FILE
