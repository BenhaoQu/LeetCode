package problem142

import (
	"encoding/json"
	. "leetCode/golang/models"
	"log"
	"strings"
)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var head *ListNode

	var headIntArray []int
	if err := json.Unmarshal([]byte(inputValues[0]), &headIntArray); err != nil {
		log.Fatal(err)
	}
	head = IntArrayToLinkedList(headIntArray)

	return detectCycle(head).LinkedListToIntArray()
}