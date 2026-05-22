class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[0 for i in range (len(nums))]
        pos=0
        for i in range(0,len(nums),2):
            ans[i]=nums[pos]
            pos+=1

        pos=n
        for i in range(1,len(nums),2):
            ans[i]=nums[pos]
            pos+=1
        return ans
        