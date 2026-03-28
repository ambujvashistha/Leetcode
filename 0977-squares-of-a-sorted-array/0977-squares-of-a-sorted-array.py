class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[]
        low=0
        high=len(nums)-1
        while low<=high:
            x=nums[low]**2
            y=nums[high]**2
            if x>y:
                arr.append(x)
                low+=1
            elif y>x:
                arr.append(y)
                high-=1
            else:
                if low!=high:
                    arr.append(x)
                    low+=1
                    arr.append(y)
                    high-=1
                else:
                    arr.append(x)
                    low+=1
                    high-=1
        return arr[::-1]

        