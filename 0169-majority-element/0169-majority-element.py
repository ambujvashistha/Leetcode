class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1

        maximum=0
        curr=0
        for i in (d):
            if d[i]>maximum:
                maximum=d[i]
                curr=i
        return curr
        