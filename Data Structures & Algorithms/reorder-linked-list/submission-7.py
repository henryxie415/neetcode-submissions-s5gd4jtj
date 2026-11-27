# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle node
        slow = head
        fast = head.next 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next

        #separate into two linked lists 
        slow.next = None

        #rearrange the second half of the list
        prev = None
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle 
            middle = temp

        #merge the two lists
        #prev is the head of the second half 
        curr = head

        while prev:
            tmp1 = curr.next
            tmp2 = prev.next
            curr.next = prev
            curr = tmp1
            prev.next = curr
            prev = tmp2




            








