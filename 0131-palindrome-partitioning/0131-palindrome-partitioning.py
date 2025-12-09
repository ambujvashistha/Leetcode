class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(l):
            t=len(l)
            c=0
            for i in l:
                low=0
                high=len(i)-1
                while low<=high:
                    if i[low]==i[high]:
                        low+=1
                        high-=1
                    else:
                        return False
                c+=1
            if c!=t:
                return False
            return True
        gb=[]
        arr=[]
        def helper(i,arr):
            if i==len(s):
                if check(arr):
                    gb.append(arr.copy())
                    arr=[]
                return 
            
            arr.append(s[i])
            helper(i+1,arr)
            arr.pop()
            if len(arr)>0:
                arr[-1]+=s[i]
                helper(i+1,arr)
            return gb
        return helper(0,[])

            