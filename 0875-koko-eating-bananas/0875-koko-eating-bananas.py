class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def apple_eater(arr,guard):
            low=0
            high=max(arr)
            ans=0
            while low<=high:
                mid=(low+high)//2
                hour=0
                if mid==0:
                    low=mid+1
                else:
                    for i in arr:
                        if i%mid==0:
                            hour+=i//mid
                        else:
                            hour+=i//mid
                            hour+=1
                # if mid==guard:
                #     ans=mid
                # ans=mid
                    print("low",low,"high",high,"mid",mid,"hour",hour)
                    if hour<=guard:
                        ans=mid
                        high=mid-1
                    else:
                        low=mid+1
            
            return ans
        return apple_eater(piles,h)
        