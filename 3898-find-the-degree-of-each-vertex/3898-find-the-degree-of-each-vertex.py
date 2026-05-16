class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        arr=[]

        for i in matrix:
            arr.append(sum(i))
        
        return arr