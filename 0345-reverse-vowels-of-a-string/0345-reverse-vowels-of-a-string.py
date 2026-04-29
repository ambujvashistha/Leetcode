class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels={"a":1,"e":1,"i":1,"o":1,"u":1,"A":1,"E":1,"I":1,"O":1,"U":1}

        arr=[]
        ans=""
        for i in s:
            if i in vowels:
                arr.append(i)
        j=len(arr)-1
        for i in range(len(s)):
            ele=s[i]
            if ele in vowels:
                ans+=arr[j]
                j-=1
            else:
                ans+=ele

                



        return ans
