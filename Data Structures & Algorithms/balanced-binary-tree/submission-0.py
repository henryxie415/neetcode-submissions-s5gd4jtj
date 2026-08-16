# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #do bfs 
        #keep root node in the deque until you reach level three 
        #add level two and kick out level 1 
        def getHeight(node):
            # Base case: empty tree has height 0
            if not node:
                return 0
            
            # Get heights of left and right subtrees
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            
            # If either subtree is unbalanced, return -1 (signal)
            if left_height == -1 or right_height == -1:
                return -1
            
            # If height difference > 1, this tree is unbalanced
            if abs(left_height - right_height) > 1:
                return -1
            
            # Otherwise, return the height of this node
            return 1 + max(left_height, right_height)
        
        # If getHeight returns -1, tree is unbalanced. Otherwise balanced.
        return getHeight(root) != -1