class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo={}
        def helper(i,j):
            if i==len(word1) and j==len(word2):
                return 0
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            
            if (i,j) in memo:
                return memo[(i,j)]
            ans1=float("inf")
            ans2=float("inf")

            if word1[i]==word2[j]:
                ans1=helper(i+1,j+1)
            else:
                ans2=min(1+helper(i+1,j),1+helper(i,j+1),1+helper(i+1,j+1))
            memo[(i,j)]=min(ans1,ans2)
            return memo[(i,j)]
        return helper(0,0)