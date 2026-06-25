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
    public ListNode mergeKLists(ListNode[] lists) {
        //check if lists is empty
        if (lists.length == 0) {return null;}
        //create a minHeap using PriorityQueue
        PriorityQueue<ListNode> minHeap = new PriorityQueue<>((a, b) -> a.val - b.val);
        //push head of every non-empty linked list into heap
        for (ListNode list: lists) {
            if (list != null) {
                minHeap.offer(list);
            }
        }
        //create our new linked list
        ListNode res = new ListNode(0);
        ListNode curr = res;
        //when heap isnt empty pop smallest value into linked list
        while (!minHeap.isEmpty()) {
            //pop smallest value from heap into linked list
            ListNode node = minHeap.poll();
            //make curr point to the node and move curr up one
            curr.next = node;
            curr = curr.next;
            //the "node" is equal to whatever it pointed to in its original linked list
            node = node.next;
            //if our new node isn't null then add it to the min heap and repeat process
            if (node != null) {
                minHeap.offer(node);
            }
        }
        return res.next;
    }
}
