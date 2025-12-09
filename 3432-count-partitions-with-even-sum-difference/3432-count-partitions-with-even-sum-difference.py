class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left=nums[0]
        right=sum(nums[1:])
        c=0
        for i in range(1,len(nums)):
            l=left%2
            r=right%2
            if (left-right)%2==0:
                # print(nums[:l+1],nums[r:])
                c+=1
            left+=nums[i]
            right-=nums[i]
        
        return c