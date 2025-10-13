class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        memo={}
        def helper(i,j):
            if i==n-1:
                return matrix[i][j]

            if (i,j) in memo:
                return memo[(i,j)]

            choice1=float("inf")
            choice2=float("inf")
            choice3=float("inf")
            if i+1<n:
                choice1=matrix[i][j] + helper(i+1,j)
            if i+1<n and j+1<n:
                choice2=matrix[i][j] + helper(i+1,j+1)
            if i+1<n and j-1>=0:
                choice3=matrix[i][j] + helper(i+1,j-1)
            memo[(i,j)]=min(choice1,choice2,choice3)
            return memo[(i,j)]
        ans=[]
        for j in range(n):
            a=helper(0,j)
            ans.append(a)
        return min(ans)
        