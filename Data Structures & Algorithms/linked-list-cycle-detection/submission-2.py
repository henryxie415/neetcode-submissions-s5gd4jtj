# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #use the slow pointer vs fast pointer 
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                return True
        return False
        

        #if there is a cycle return True else return False 