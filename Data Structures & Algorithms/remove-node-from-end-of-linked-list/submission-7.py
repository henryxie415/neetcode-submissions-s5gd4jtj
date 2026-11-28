
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_arr = []
        curr = head

        while curr:
            temp_arr.append(curr.val)
            curr = curr.next
        

        index = len(temp_arr) - n
        temp_arr.pop(index)

        res = ListNode()
        final = res 
        
        for num in temp_arr:
            final.next = ListNode(num)
            final = final.next
        return res.next

        #go through the linked list 
        #based on n, remove node from end of the list

        #how do we traverse with the number n 

        #deletion part is when you have current node equal to the next next node 
        #return the modified linked list 


