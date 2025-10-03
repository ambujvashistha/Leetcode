class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo={}
        n=len(text2)
        m=len(text1)
        def helper(i,j):
            if i==m or j==n:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            if text1[i]==text2[j]:
                memo[(i,j)]=1+ helper(i+1,j+1)
                return memo[(i,j)]
        
            memo[(i,j)]=max(helper(i+1,j),helper(i,j+1))
            return memo[(i,j)]
        return helper(0,0)