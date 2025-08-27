class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        d={}
        x=[]
        l=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in d:
                    x.append(grid[i][j])
                else:
                    l.append(grid[i][j])
                    d[grid[i][j]]=1
        l.sort()
        gg=True
        for i in range(len(l)-1):
            if l[i+1]-l[i]!=1:
                x.append(l[i]+1)
                gg=False
            
        if gg:
            if l[0]==1:
                x.append(l[-1]+1)
            else:
                x.append(l[0]-1)
        return x
                