class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap={}
        for i in jewels:
            if i not in hashmap:
                hashmap[i]=True
        result=0
        for i in stones:
            if i in hashmap:
                result+=1
        return result
        