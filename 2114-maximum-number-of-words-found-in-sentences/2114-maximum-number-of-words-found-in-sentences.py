class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxx=0

        for i in sentences:
            arr=list(i.split())
            maxx=max(maxx,len(arr))
        return maxx