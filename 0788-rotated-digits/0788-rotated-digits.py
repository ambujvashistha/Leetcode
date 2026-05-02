class Solution:
    def rotatedDigits(self, n: int) -> int:
        c=0
        for i in range (1,n+1):
            s=set(str(i))

            if "7" in s or "3" in s or "4" in s:
                pass
            elif "2" in s or "5" in s or "6" in s or "9" in s:
                c+=1
            # print(s,i)
        return c
        