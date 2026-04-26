class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n):
            x=str(n)
            x=x[::-1]
            return int(x)
        return abs(n - reverse(n))