# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def helper(root,flag):
            if root==None:
                return 0

            ans=0
            if root.left==None and root.right==None and flag:
                ans+=root.val
            
            ans+=helper(root.left,True)
            ans+=helper(root.right,False)

            return ans
        
        # a=helper(root.left,True)
        # b=0
        # if root.right!=None:
        #     b=helper(root.right.left,True)

        return helper(root,False)
        