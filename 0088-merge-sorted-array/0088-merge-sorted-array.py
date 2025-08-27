class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)-m):
            nums1.pop()
        for i in range(len(nums2)-n):
            nums2.pop()

        for i in nums2:
            
            nums1.append(i)
        
        def helper(nums1,start,end):
            if start>=end:
                return 
            pivot=nums1[end]
            pos=start
           
            for i in range(start,end+1):
                if nums1[i]>pivot:
                    pass
                else:
                    nums1[pos],nums1[i]=nums1[i],nums1[pos]
                    pos+=1
            pos-=1
            helper(nums1,start,pos-1)
            helper(nums1,pos+1,end)

            return nums1
        
        return helper(nums1,0,len(nums1)-1)

        