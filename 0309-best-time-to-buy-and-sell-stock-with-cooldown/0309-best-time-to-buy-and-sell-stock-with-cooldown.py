class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo={}
        def helper(i,flag):
            if i==len(prices):
                return 0
            t=(i,flag)

            if t in memo:
                return memo[t]

            if flag==1:
                ans=max(prices[i]+helper(i+1,-1),helper(i+1,1))
            elif flag==0:
                ans=max(-prices[i]+helper(i+1,1),helper(i+1,0))
            elif flag==-1:
                ans=helper(i+1,0)
            
            memo[t]=ans
            return memo[t]
        return helper(0,0)