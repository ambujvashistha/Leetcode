class Solution:
    def pivotInteger(self, n: int) -> int:
        pref=[]
        suff=[]
        c=0
        for i in range(1,n+1):
            c+=i
            pref.append(c)
        c=0
        for i in range(n,0,-1):
            c+=i
            suff.append(c)

        print(pref,suff)

        for i in range(len(pref)):
            if pref[i]==suff[len(pref)-i-1]:
                return i+1
        
        return -1
        
        

        