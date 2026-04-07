class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels={'a':0,'e':0,'i':0,'o':0,'u':0}
        consonants={}

        for i in s:
            if i in vowels:
                vowels[i]+=1
            elif i in consonants:
                consonants[i]+=1
            else:
                consonants[i]=1
        max_vowel=0
        for i in vowels:
            if vowels[i]>max_vowel:
                max_vowel=vowels[i]

        max_consonant=0
        for i in consonants:
            if consonants[i]>max_consonant:
                max_consonant=consonants[i]
        # print(max_vowel,max_consonant)
        return max_vowel+max_consonant
