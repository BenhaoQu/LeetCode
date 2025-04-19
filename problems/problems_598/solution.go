package problem598

import (
	"encoding/json"
	"log"
	"strings"
)

func maxCount(m int, n int, ops [][]int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var m int
	var n int
	var ops [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &ops); err != nil {
		log.Fatal(err)
	}

	return maxCount(m, n, ops)
}
