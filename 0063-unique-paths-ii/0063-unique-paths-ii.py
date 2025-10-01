class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        memo={}
        def helper(i,j):
            if i==m-1 and j==n-1:
                if obstacleGrid[i][j]==1:
                    return 0
                return 1
            if obstacleGrid[i][j]==1:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            ch1=0
            ch2=0
            if i+1<m:
                ch1=helper(i+1,j)
            if j+1<n:
                ch2=helper(i,j+1)
            memo[(i,j)]=ch1+ch2
            return memo[(i,j)]
        return helper(0,0)