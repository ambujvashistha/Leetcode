class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in s:
            if i.isalnum():
                x+=i.lower()
        print(x)
        low=0
        high=len(x)-1
        while low<=high:
            if x[low]==x[high]:
                low+=1
                high-=1
            else:
                return False
        return True
             
        