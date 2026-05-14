class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        ele=0
        for i in t:
            if i==s[ele]:
                ele+=1
            if ele==len(s):
                return True
        
        
        return False
