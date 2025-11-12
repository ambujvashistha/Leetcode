class RandomizedSet:
    import math

    def __init__(self):
        self.dic={}
        self.arr=[]
        

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        else:
            self.arr.append(val)
            self.dic[val]=len(self.arr)-1
            return True

        

    def remove(self, val: int) -> bool:
        if val in self.dic:
            indox=self.dic[val]
            if indox==len(self.arr)-1:
                del self.dic[val]
                self.arr.pop()
            else:
                self.arr[indox],self.arr[-1]=self.arr[-1],self.arr[indox]
                self.dic[self.arr[indox]]=indox
                del self.dic[self.arr[-1]]
                self.arr.pop()

            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return self.arr[random.randint(0,len(self.arr)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()