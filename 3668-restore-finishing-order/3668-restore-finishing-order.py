class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        
        # arr=[0 for i in range(len(order))]
        # print(arr)

        # for i in range(len(friends)):
        #     arr[order[i]-1]=friends[i]
        # print(arr)

        res=[]

        for i in order:
            if i in friends:
                res.append(i)
        return res
