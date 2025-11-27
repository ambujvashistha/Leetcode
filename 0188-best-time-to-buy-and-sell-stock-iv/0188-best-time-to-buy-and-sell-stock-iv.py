class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        memo={}
        def helper(i,flag,count):
            if i==len(prices):
                return 0
            t=(i,flag,count)
            if t in memo:
                return memo[t]
            ans=helper(i+1,flag,count)

            if flag and count>0:
                ans=max(ans,helper(i+1,not(flag),count-1)-prices[i])
            elif not(flag):
                ans=max(ans,helper(i+1,not(flag),count)+prices[i])
            memo[t]=ans
            return memo[t]
        return helper(0,True,k)