class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)>1:
            lis=[0 for i in range(len(nums))]
            return lis
        if len(set(nums))==1 and nums[0]==0:
            lis=[0 for i in range(len(nums))]
            return lis
            
        prod=1
        arr=[]
        flag=False
        for i in nums:
            if i==0:
                flag=True
            else:
                prod*=i
        
        for i in nums:
            if i==0:
                arr.append(prod)
            else:
                if flag:
                    ele=0
                else:
                    ele=prod//i
                arr.append(ele)
        
        return arr
        