
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = []
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next
        
        index = len(temp) - n
        temp.pop(index)

        dummy = ListNode()
        top = dummy

        for num in temp:
            top.next = ListNode(num)
            top = top.next
        return dummy.next






        #go through the linked list 
        #based on n, remove node from end of the list

        #how do we traverse with the number n 

        #deletion part is when you have current node equal to the next next node 
        #return the modified linked list 


