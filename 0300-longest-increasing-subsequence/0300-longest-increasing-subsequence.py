class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[-1 for _ in range(len(nums))]
        lis[0]=1
        for i in range(1,len(nums)):
            maxi=0
            for j in range(i+1):
                if nums[j]<nums[i]:
                    if lis[j]>maxi:
                        maxi=lis[j]
            lis[i]=maxi+1
        return max(lis)
