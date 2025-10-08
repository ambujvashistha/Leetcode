class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        gb=[]
        def helper(i,arr):
            if i==len(nums):
                gb.append(arr.copy())
                return 
            arr.append(nums[i])
            helper(i+1,arr)
            arr.pop()
            helper(i+1,arr)
            return gb
        return helper(0,[])

        