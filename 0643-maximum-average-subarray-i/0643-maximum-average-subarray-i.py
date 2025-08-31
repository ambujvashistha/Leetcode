class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        c=sum(nums[:k])
        maxavg=c/k
        for i in range(k,len(nums)):
            c=c+nums[i]-nums[i-k]
            g=c/k
            if g>maxavg:
                maxavg=g
        return round(maxavg,5)
            