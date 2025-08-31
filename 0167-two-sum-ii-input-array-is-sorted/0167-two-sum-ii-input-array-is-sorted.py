class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr=[]
        low=0
        high=len(numbers)-1
        while low<=high:
            add = numbers[low]+numbers[high]
            if add > target:
                high-=1
            elif add<target:
                low+=1
            else:
                arr.append(low+1)
                arr.append(high+1)
                return arr
        return arr