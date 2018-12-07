package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"strings"
)

var (
	filepath = os.Getenv("AOC_INPUT_FILE")
)

type charcount struct {
	id      string
	trcount bool
	twcount bool
}

func retrieveBoxIDs(filepath string) [][]string {
	var (
		file, _   = os.Open(filepath)
		csvreader = csv.NewReader(file)
	)

	contents, err := csvreader.ReadAll()

	if err != nil {
		fmt.Println(err)
	}

	return contents
}

func findCounts() {
	var (
		evalstr []charcount
		trcount []string
		twcount []string

		boxIDs = retrieveBoxIDs(filepath)

	)

	for _, boxid := range boxIDs {
		for _, c := range boxid[0] {
			var (
				cc charcount

				count = strings.Count(boxid[0], string(c))
			)
		
			cc.id = boxid[0]

			if count == 2 {
				cc.twcount = true
				evalstr = append(evalstr, cc)		
			} else if count == 3 {
				cc.trcount = true
				evalstr = append(evalstr, cc)
			}
		}
	}

	for _, c := range evalstr {
		if c.twcount == true {
			twcount = append(twcount, c.id)
		} else if c.trcount == true {
			trcount = append(trcount, c.id)
		}
	}

	ans := len(twcount) * len(trcount)
	fmt.Println(ans)
}

func main() {
	findCounts()
}
