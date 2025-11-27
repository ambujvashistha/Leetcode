class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        def helper(i,flag,count):
            if i==len(prices):
                return 0
            if (i,flag,count) in memo:
                return memo[(i,flag,count)]

            ans=helper(i+1,flag,count)

            if flag and count>0:
                ans=max(ans,helper(i+1,not(flag),count-1)-prices[i])
            elif not(flag):
                ans=max(ans,helper(i+1,not(flag),count)+prices[i])
            memo[(i,flag,count)]=ans
            return memo[(i,flag,count)]
        return helper(0,True,2)

