class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def helper(i):
            if i==0:
                return 1
            if i in memo:
                return memo[i]
            choice1=helper(i-1)
            choice2=0
            if i-2>=0:
                choice2=helper(i-2)
            memo[i]=choice1+choice2
            return memo[i]
        return helper(n)

        