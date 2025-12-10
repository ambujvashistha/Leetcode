class Solution:
    def countTriples(self, n: int) -> int:
        dic={}
        for i in range(1,n+1):
            dic [i**2]=True
        
        c=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if (i**2)+(j**2) in dic:
                    # print(i,j)
                    c+=1
        
        return c