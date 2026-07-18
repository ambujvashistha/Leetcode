class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=max(nums)
        b=min(nums)

        while b:
            a, b = b, a % b
            # print(a,b)
        return a
        