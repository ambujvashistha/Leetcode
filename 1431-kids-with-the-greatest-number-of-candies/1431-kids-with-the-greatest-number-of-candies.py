class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=max(candies)
        arr=[]
        for i in candies:
            if i+extraCandies>=maxi:
                arr.append(True)
            else:
                arr.append(False)
        return arr
        