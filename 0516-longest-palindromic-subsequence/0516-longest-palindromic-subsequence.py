class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo={}
        def helper(start,end):
            if start>=end:
                if start==end:
                    return 1
                return 0
            
            if (start,end) in memo:
                return memo[(start,end)]
            
            if s[start]==s[end]:
                memo[(start,end)]= 2+ helper(start+1,end-1)
            else:
                memo[(start,end)]= max(helper(start+1,end),helper(start,end-1))

            return memo[(start,end)]
        return helper(0,len(s)-1)

        