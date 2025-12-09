class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        hash={}

        for i in arr:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        c=k
        for i in hash:
            if hash[i]==1:
                c-=1
            if c==0:
                return i
        return ""
            

