class Solution:
    def minimumSum(self, num: int) -> int:
        temp=list(str(num))
        temp.sort()
        return int(temp[0]+temp[3])+int(temp[1]+temp[2])

        