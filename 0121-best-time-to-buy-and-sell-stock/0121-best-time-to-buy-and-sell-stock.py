class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        max_answer=0

        for i in range(len(prices)):
            if prices[i]-mini>max_answer:
                max_answer=prices[i]-mini
            if prices[i]<mini:
                mini=prices[i]
        return max_answer                