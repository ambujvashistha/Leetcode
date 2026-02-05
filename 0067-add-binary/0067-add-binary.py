class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        num1=0
        num2=0
        a=a[::-1]
        b=b[::-1]
        pow=0
        for i in a:
            num1+= (2**pow)*int(i)
            pow+=1
        pow=0
        for i in b:
            num2+= (2**pow)*int(i)
            pow+=1
        
        result= num1+num2

        if result==0:
            return "0"
        final=""
        while result>0:
            final+=str(result%2)
            result=result//2
        
        return final[::-1]



