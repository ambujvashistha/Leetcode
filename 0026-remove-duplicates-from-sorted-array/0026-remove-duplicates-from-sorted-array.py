class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        c=1
        prev=nums[0]
        prev_index=1
        for i in range(1,len(nums)):
            if nums[i]!=prev:
                nums[prev_index]=nums[i]
                prev_index+=1
                c+=1
                prev=nums[i]
        # for i in range(prev_index,len(nums)):
        #     nums[i]
        # print(c)
        return c
        