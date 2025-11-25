class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo={}

        def helper(i,last):
            if i==len(nums):
                return 0
            if (i,last) in memo:
                return memo[(i,last)]

            ans=helper(i+1,False)
            if not(last):
                ans=max(ans,nums[i]+helper(i+1,True))
            memo[(i,last)]=ans
            return memo[(i,last)]
        return helper(0,False)