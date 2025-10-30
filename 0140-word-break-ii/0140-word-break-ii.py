class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        gb=[]
        arr=[]
        def helper(i):
            if i==len(s):
                c=0
                for i in arr:
                    if i in wordDict:
                        c+=1
                if c==len(arr):
                    # gb.append(arr.copy())
                    gb.append(" ".join(arr))
                return 

            if len(arr)==0:
                arr.append(s[i])
                helper(i+1)
            else:
                arr.append(s[i])
                helper(i+1)
                arr.pop()
                arr[-1]+=s[i]
                helper(i+1)
            return gb
        return helper(0)

            

