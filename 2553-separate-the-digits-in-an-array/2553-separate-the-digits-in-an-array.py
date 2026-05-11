class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s=""

        for i in nums:
            s+=str(i)
        
        arr=[]
        for i in s:
            arr.append(int(i))
        
        return arr
        