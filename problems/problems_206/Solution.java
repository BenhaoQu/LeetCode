package problems.problems_206;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
import qubhjava.models.ListNode;

public class Solution extends BaseSolution {
    public ListNode reverseList(ListNode head) {

    }

    @Override
    public Object solve(String[] values) {
        ListNode head = jsonArrayToListNode(values[0]);
        return JSON.toJSON(ListNode.LinkedListToIntArray(reverseList(head)));
    }
}
