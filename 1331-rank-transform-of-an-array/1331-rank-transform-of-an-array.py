class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a=set(arr)
        a=list(a)
        a.sort()
        ans=[]
        memo={}
        pos=1
        for i in a:
            memo[i]=pos
            pos+=1
        
        for i in arr:
            ans.append(memo[i])
        return ans
        


        