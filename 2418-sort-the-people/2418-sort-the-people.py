class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap={}
        for i in range(len(heights)):
            hashmap[heights[i]]=names[i]
        heights.sort()
        heights=heights[::-1]
        arr=[]
        for i in heights:
            arr.append(hashmap[i])
        
        return arr


        