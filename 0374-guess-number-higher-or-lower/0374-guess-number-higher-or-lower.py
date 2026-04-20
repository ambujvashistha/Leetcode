# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        

        low=1
        high=n

        while low<=high:
            guessed=(low+high)//2
            flag=guess(guessed)

            if flag>0:
                low=guessed+1
            elif flag<0:
                high=guessed-1
            else:
                return guessed

