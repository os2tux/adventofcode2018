#!/bin/bash

aocInput=/home/joseph/development/work_projects/advent_of_code/2018/day1/frequencies.csv

if [[ -f $aocInput ]]; then {
	export AOC_INPUT_FILE=$aocInput
}
fi
