package problems.problems_LCR_022;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
import qubhjava.models.ListNode;

public class Solution extends BaseSolution {
    public ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                break;
            }
        }
        if (slow != fast) {
            return null;
        }
        slow = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
		int pos = Integer.parseInt(inputJsonValues[1]);
		ListNode head = ListNode.IntArrayToLinkedListCycle(arr, pos);
        ListNode res = detectCycle(head);
        return JSON.toJSON(res == null ? null : res.val);
    }
}
