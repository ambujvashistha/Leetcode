class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd=[]
        maxx=0
        for i in nums:
            
            maxx=max(i,maxx)
            a = maxx
            b = i

            while b:
                a, b = b, a % b
            prefixGcd.append(a)
        
        # arr=set(prefixGcd)
        # arr=list(arr)
        
        # arr.sort()
        prefixGcd.sort()

        print(prefixGcd)

        low=0
        high=len(prefixGcd)-1
        ans=0
        while low<high:
            a,b=prefixGcd[low],prefixGcd[high]
            while b:
                a, b = b, a % b
            
            ans+=a
            low+=1
            high-=1
        
        return ans

        