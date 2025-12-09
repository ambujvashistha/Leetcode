class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini=len(strs[0])
        for i in strs:
            if len(i)<mini:
                mini=len(i)
        def helper(i):
            if i==mini:
                return ""
            c=0
            ans=""
            temp=strs[0][i]
            for x in strs:
                if x[i]==temp:
                    c+=1
            
            if c==len(strs):
                ans=temp+helper(i+1)
            
            return ans
        return helper(0)