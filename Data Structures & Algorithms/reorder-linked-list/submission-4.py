# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle node (will always be last)
        slow = head 
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next

        #separates the two lists 
        slow.next = None 


        #reverse the second half of the list 
        #use the middle as the end point by having it point to None 
        #and then reverse the list 
        prev = None
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        
        #merge with first half of the list 

        #the beginning of the first half is head
        #beginning of second half is prev.next
        curr1 = head
        curr2 = prev
        while curr2:
            tmp1 = curr1.next
            tmp2 = curr2.next
            curr1.next = curr2
            curr2.next = tmp1
            curr1 = tmp1
            curr2 = tmp2
        


            








