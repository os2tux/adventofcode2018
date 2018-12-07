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

	return contents
}

func sumTotalFrequencyChanges(frequencies [][]string) {
	var sum int

	for _, f := range frequencies {
		fc, _ := strconv.Atoi(f[0])

		sum += fc
	}

	fmt.Println(sum)
}

func main() {
	filepath := os.Getenv("AOC_INPUT_FILE")
	fmt.Println(filepath)

	sumTotalFrequencyChanges(retrieveFrequencies(filepath))
}
