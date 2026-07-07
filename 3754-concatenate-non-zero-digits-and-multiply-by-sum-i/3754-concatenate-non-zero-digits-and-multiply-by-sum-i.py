class Solution:
    def sumAndMultiply(self, n: int) -> int:
        temp=str(n)
        x=""
        sum=0
        for i in temp:
            if i!="0":
                sum+=int(i)
                x+=i
        if x:
            return int(x)*sum
        return 0
        