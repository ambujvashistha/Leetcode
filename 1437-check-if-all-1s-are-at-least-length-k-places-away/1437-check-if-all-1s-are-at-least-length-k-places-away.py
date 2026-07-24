class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        c=0
        flag=True
        ans=True

        for i in nums:
            if i==1:
                if c>=k or flag:
                    c=0
                    flag=False 
                # elif flag:
                #     c=0
                #     flag=False
                else:
                    ans=False
            else:
                c+=1
        
        return ans


        
            

        