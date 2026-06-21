class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        temp=coins
        c=0
        for i in costs:
            if i<=temp:
                temp-=i
                c+=1
            else:
                return c

        return c
            

        