package problem724

import (
	"encoding/json"
	"log"
	"strings"
)

func pivotIndex(nums []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return pivotIndex(nums)
}