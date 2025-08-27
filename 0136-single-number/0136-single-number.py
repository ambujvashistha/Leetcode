class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
            
        for i in d:
            if d[i]==1:
                return i