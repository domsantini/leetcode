# Logic:
# This is a LL problem. Need to return if the LL has a cycle, or if some node.next references another node in the list
# Using fast and slow pointers, if the fast ever catches up to the slow, then theres a cycle, but if the fast
# gets to the end of the LL w/o matching up, there's no cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Define our fast and slow pointers
        slow = head
        fast = head
        
        # Check while theres a fast, and if fast is the last node (fast.next will be null IF fast is last node)
        while fast and fast.next:
            # Iterate slow once per loop
            slow = slow.next
            # Iterate fast twice per loop
            fast = fast.next.next
            
            # If they ever meet, return true
            if fast == slow:
                return True
                
        return False