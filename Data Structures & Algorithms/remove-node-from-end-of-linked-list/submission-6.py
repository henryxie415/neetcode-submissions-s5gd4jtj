# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #start the two pointers 
        #the fast pointer will start n spots away from the slow
        #that way the slow pointer will end on the node right before the destructred node
        #start with a dummy node that points to the beginning of the list 
        dummy = ListNode(0, head)
        slow = dummy
        fast = head 
        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next