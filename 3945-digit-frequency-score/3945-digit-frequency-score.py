class Solution:
    def digitFrequencyScore(self, n: int) -> int:

        hashmap={}
        temp=str(n)
        ans=0
        for i in temp:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        
        for i in hashmap:
            ans+=int(i)*hashmap[i]
        return ans
        