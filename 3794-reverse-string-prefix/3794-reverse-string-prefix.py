class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        result=""

        for i in range(k-1,-1,-1):
            result+=s[i]

        for i in range(k,len(s)):
            result+=s[i]
        return result