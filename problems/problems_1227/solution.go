package problem1227

import (
	"encoding/json"
	"log"
	"strings"
)

func nthPersonGetsNthSeat(n int) float64 {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return nthPersonGetsNthSeat(n)
}
