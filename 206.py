# Logic: 
# Big boy. Gotta go over this one a few times to lock in the logic, BUT we're traversing a linked list and reversing the list. 
# We're really going to be using THREE pointers here, a current pointer, a previous and a temp pointer.
# We start all traversals defining our current pointer to the head of our linked list. Then we define our previous pointer
# as null. As we step through our linked list we need to remember the next pointer bc we're severing the link to our next node
# in the reversal step. More notes down below for each step.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Need to define pointers, one for current node and one for previous so that we can do reversal
        curr = head
        prev = None

        # Set up our loop, while curr pointer is pointing at another node (while not null)
        while curr:
            # Need to set up another pointer / temp variable to remember current nodes pointer
            temp = curr.next
            curr.next = prev

            # Update our pointers to the next iteration
            prev = curr # We have a pointer to our current node, so we go back to front and move previous node up 
            curr = temp # Then we take our pointer to the previous node and move our current node up to that next node
            
        # We return previous pointer, bc that's now pointing to the linked list
        return prev