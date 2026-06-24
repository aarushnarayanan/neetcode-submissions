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

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        //left pointer
        ListNode dummy = new ListNode(0, head);
        ListNode left = dummy;
        //right pointer
        ListNode right = head;

        //move right pointer n steps ahead
        while (n > 0) {
            right = right.next;
            n--;
        }
        //move left and right pointer til right reaches end of list
        while (right != null) {
            left = left.next;
            right = right.next;
        }

        left.next = left.next.next;
        return dummy.next;


    }
}
