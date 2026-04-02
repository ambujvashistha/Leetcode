class Solution:
    def tribonacci(self, n: int) -> int:
        
        memo={}
        def helper(i):
            if i<=0:
                return 0
            if i==1:
                return 1
            if i in memo:
                return memo[i]

            memo[i]= helper(i-1)+helper(i-2)+helper(i-3)

            return memo[i]
        return helper(n)