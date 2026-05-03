class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1={}
        num2={}
        answer=[]

        for i in nums1:
            num1[i]=True

        for i in nums2:
            num2[i]=True
        
        arr=[]
        for i in num1:
            if i not in num2:
                arr.append(i)
        
        answer.append(arr)
    
        brr=[]
        for i in num2:
            if i not in num1:
                brr.append(i)
        
        answer.append(brr)
        
        return answer
        
        