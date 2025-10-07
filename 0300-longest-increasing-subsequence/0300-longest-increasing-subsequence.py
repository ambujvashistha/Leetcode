class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # n = len(nums)
        # l=[[-1]*n for i in range(len(nums))]
        # def helper(index,prev_index):
        #     if index==len(nums):
        #         return 0
            
        #     if l[index][prev_index] != -1:
        #         return l[index][prev_index]

        #     not_take=helper(index+1,prev_index)
        #     take=0

        #     if prev_index==-1 or nums[index]>nums[prev_index] :
        #         take= 1+ helper(index+1,index)
        #     l[index][prev_index]=max(take,not_take)
        #     return l[index][prev_index]
        # return helper(0,-1)

        arr=[-1 for _ in range(len(nums))]
        # print(arr)
        for i in range(len(nums)):
            if i==0:
                arr[i]=1
            maxi=0
            for j in range(i):
                if nums[j]<nums[i]:
                    if arr[j]>maxi:
                        maxi=arr[j]
            arr[i]=maxi+1
        # print(arr)
        return max(arr)
        