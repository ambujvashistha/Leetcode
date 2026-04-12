class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        pos=0

        for i in range(len(nums)):
            ele=nums[i]
            if ele%2==0:
                ele=0
                if i==pos:
                    nums[i]=ele
                else:
                    nums[pos],nums[i]=ele,nums[pos]
                pos+=1
            else:
                ele=1
                nums[i]=ele
        return nums