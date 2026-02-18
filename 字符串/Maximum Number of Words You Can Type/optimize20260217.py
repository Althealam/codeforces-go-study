class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        can_type = True
        res = 0
        for ch in text+ ' ': # iterate all the charcter in text
            if ch == ' ': # means that we have already iterate one word
                if can_type == True:
                    res+=1
                can_type = True # start with a new word
            else:
                if ch in broken:
                    can_type = False
        return res