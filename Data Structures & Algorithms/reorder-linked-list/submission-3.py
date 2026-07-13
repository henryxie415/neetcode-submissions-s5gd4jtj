# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle ListNode
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        
        #reverse the second half
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        #merge with the first half
        first = head 
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1 
            first = tmp1 
            second = tmp2







