package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"strconv"
)

var sampleInput = []int{1, -2, 3, 1,}

func retrieveFrequencies(filepath string) [][]string {
	var (
		file, _   = os.Open(filepath)
		csvreader = csv.NewReader(file)
	)

	contents, _ := csvreader.ReadAll()

	fmt.Println(contents)
	return contents
}

//func compareFrequencies(frequencies []int) {
func compareFrequencies(frequencies[][]string) {
	var (
		dup       bool
		lastValue int

		sum =  make(map[int]string)
	)

	for dup != true {
		for _, f := range frequencies {

			fc, _ := strconv.Atoi(f[0])
			lastValue += fc

			if  _, ok := sum[lastValue]; ok == false {
				sum[lastValue] = ""
				continue
			}

			fmt.Println(lastValue)
			dup = true
			break
		}
	}
}

func main() {
	filepath := os.Getenv("AOC_INPUT_FILE")
	compareFrequencies(retrieveFrequencies(filepath))

	//compareFrequencies(sampleInput)
}
