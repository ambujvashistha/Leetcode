# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        gb=[]
        def helper(root):
            if root==None:
                return 
            
            helper(root.left)
            gb.append(root.val)
            helper(root.right)

            return gb
        
        lis=helper(root)
        for i in range(1,len(lis)):
            if lis[i]<=lis[i-1]:
                return False
        
        return True