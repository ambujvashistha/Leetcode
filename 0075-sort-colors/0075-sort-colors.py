class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def helper(nums,start,end):
            if start>=end:
                return
            pivot=nums[end]
            pos=start
            for i in range(start,end+1):
                if nums[i]>pivot:
                    pass
                else:
                    nums[i],nums[pos]=nums[pos],nums[i]
                    pos+=1
            pos-=1
            helper(nums,start,pos-1)
            helper(nums,pos+1,end)
            return nums
        return helper(nums,0,len(nums)-1)