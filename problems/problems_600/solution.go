package problem600

import (
	"encoding/json"
	"log"
	"strings"
)

func findIntegers(n int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return findIntegers(n)
}