class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curr=nums[0]
        ans=1
        currseq=1
        
        for i in range(1,len(nums)):
            if nums[i]>curr:
                currseq+=1
                if ans<currseq:
                    ans=currseq
            else:
                currseq=1
            
            curr=nums[i]
        return ans
