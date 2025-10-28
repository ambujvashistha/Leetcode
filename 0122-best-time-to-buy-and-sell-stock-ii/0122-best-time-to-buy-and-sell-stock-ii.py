class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        ans=0

        for i in range(len(prices)):
            if prices[i]-mini>0:
                ans+=prices[i]-mini
                mini=prices[i]
            else:
                mini=prices[i]
        return ans