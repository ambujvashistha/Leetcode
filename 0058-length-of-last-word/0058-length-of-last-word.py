class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # arr=list(s.split())
        # print(len(arr[-1]))

        # return len(arr[-1])
        
        word_start=0
        ans=0
        for i in range(len(s)-1,-1,-1):
            if word_start:
                if s[i]!=" ":
                    ans+=1
                else:
                    return ans
            else:
                if s[i]!=" ":
                    ans+=1
                    word_start+=1
        return ans


        