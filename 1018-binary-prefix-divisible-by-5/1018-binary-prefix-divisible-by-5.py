class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        arr=[False for _ in range(len(nums))]
        binary=""
        ans=0

        for i in range(len(nums)):
            binary+=str(nums[i])
            div=int(binary,2)%5
            if div==0:
                arr[i]=True
            else:
                arr[i]=False            
        return arr