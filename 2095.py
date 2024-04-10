# Logic: 
# Back w/ a BANG. One shot this in just a couple minutes.
# We want to find the middle node, then delete it. We can use slow / fast pointers to find middle
# and also use a prev pointer to keep track of node before middle.
# We iterate our pointers, then point prev to slow.next (middle node) and remove connection 
# of the middle node to next (slow.next = None)


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        slow = fast = head
        prev = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            prev = prev.next

        prev.next = slow.next
        slow.next = None

        return dummy.next
        