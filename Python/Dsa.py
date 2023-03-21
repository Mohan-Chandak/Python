from LinkedList import ListNode

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n): 
            fast = fast.next
            if not fast: 
                return head.next
            while fast.next: 
                fast, slow = fast.next, slow.next
            slow.next = slow.next.next
        return head