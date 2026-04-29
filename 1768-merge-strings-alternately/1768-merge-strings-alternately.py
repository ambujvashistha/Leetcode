class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ans=""
        i=0
        if len(word1)<len(word2):
            rest=word2[len(word1):]
        else:
            rest=word1[len(word2):]
        while i<len(word1) and i<len(word2):
            ans+=word1[i]
            ans+=word2[i]
            i+=1
        return ans+rest