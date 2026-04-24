class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        hashmap={}

        for i in range(len(matrix)):
            for j in range (len(matrix[i])):
                if matrix[i][j]==0:
                    hashmap[("i",i)]=1
                    hashmap[("j",j)]=1
        
        print(hashmap)
        for i in range(len(matrix)):
            for j in range (len(matrix[i])):
                if ("i",i) in hashmap or ("j",j) in hashmap:
                    matrix[i][j]=0



        