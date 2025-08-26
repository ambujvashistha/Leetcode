class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        d={}
        ans={}
        for i in range(len(nums)):
            d[i]=True
        gb=[]
        arr=[]
        def helper(nums,arr,i):
            if len(arr)==len(nums):
                if str(arr.copy()) in ans:
                    return
                gb.append(arr.copy())
                ans[str(arr.copy())]=True
                return 
            for i in range (len(nums)):
                if d[i]:
                    arr.append(nums[i])
                    d[i]=False
                    helper(nums,arr,i+1)
                    d[i]=True
                    arr.pop()
            return (gb)
        return helper(nums,arr,0)
        