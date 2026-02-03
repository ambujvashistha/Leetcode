class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low=0
        high=len(nums)-1
        last=0
        while low<=high:
            mid = (low+high)//2
            last=mid
            if nums[mid]<target:
                low+=1
            elif nums[mid]>target:
                high-=1
            else:
                return mid
        if nums[last]<target:
            return last+1
        return last