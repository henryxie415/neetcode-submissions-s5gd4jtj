
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pointers
        dummy = ListNode(0, head)
        slow = dummy
        #fast needs to have a gap of n 
        fast = head
        start = n
        while start > 0:
            #move slow every n times fast moves
            fast = fast.next
            start -= 1
        #move through the node 
        while fast:
            slow = slow.next
            fast = fast.next 
        #once the fast.next reaches None 
        #slow.next should reach the node to terminate
        slow.next = slow.next.next
        return dummy.next
        #create mechanism to delete node
        #slow and fast should still be used 

