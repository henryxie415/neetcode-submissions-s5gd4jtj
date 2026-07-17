"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #using a hashmap make two passes
        copyNodes = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            copyNodes[curr] = copy
            curr = curr.next

        curr = head 
        while curr:
            copy = copyNodes[curr]
            copy.next = copyNodes[curr.next]
            copy.random = copyNodes[curr.random]
            curr = curr.next

        return copyNodes[head]



        #the first pass will establish the copies of the nodes in the hashmap 
        #the second pass will allow the pointers to be established





