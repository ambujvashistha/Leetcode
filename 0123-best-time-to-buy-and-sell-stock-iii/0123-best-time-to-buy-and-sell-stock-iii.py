class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy=[0 for _ in range(len(prices))]
        sell=[0 for _ in range(len(prices))]
        mini=prices[0]
        for i in range(len(prices)):
            if prices[i]-mini>0:
                sell[i]=prices[i]-mini
            
            else:
                mini=prices[i]
        maxi=prices[-1]
        for i in range(len(prices)-1,-1,-1):
            if prices[i]-maxi<0:
                buy[i]=maxi-prices[i]
            else:
                maxi=prices[i]

        # print(sell,buy)

        newmaxi=sell[0]
        profit=0
        for i in range(1,len(prices)):
            # print(profit)
            # x=sell[:i+1]
            if sell[i]>=newmaxi:
                newmaxi=sell[i]
            if buy[i]+newmaxi>profit:
                # print(i,maxi)
                profit=buy[i]+newmaxi
        
        return profit
