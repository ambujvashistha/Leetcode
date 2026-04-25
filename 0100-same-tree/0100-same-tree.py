# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        def helper(root,arr):
            if root==None:
                arr.append("None")
                return 
            
            arr.append(root.val)
            helper(root.left,arr)
            helper(root.right,arr)

            return arr
        
        arr1=helper(p,[])
        arr2=helper(q,[])
        print(arr1,arr2,p,q)
    
        if len(arr1)!=len(arr2):
            return False

        i=0
        while i<len(arr1):
            if arr1[i]!=arr2[i]:
                return False
            i+=1
        return True
       

        