# Logic:
# This is a LL problem. We want the middle node, so using fast and slow pointers, once the fast reaches the end, 
# slow pointer will be at the middle node

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow