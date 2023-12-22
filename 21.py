# Logic: 
# I like this one. We've got two sorted lists and were going to merge the two into one sorted list. 
# This problem exposes a nice technique of using a dummy node and tail pointer to track the end of dummy node list.
# All the steps are written below.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node technique to avoid inserting into an empty list
        # also dont need to sever current mode links so we can just have a tail pointer
        # to where we put L1 and L2 nodes
        dummy = ListNode()
        tail = dummy

        # While we have values in L1 and L2, go through and compare list nodes to find smallest
        while list1 and list2:
            # If L1 is smaller, point tail to L1 and shift L1 
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            # If L2 is smaller or equal, point tail to L2 and shift L2     
            else:
                tail.next = list2
                list2 = list2.next
            # Update our tail in either case so do this outside of the loop
            tail = tail.next
        # Finally, if there's only one list left, we can point our tail at remaining list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        # Finally finally, return our dummy node list
        return dummy.next