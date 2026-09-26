class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charsInS = {}

        for char in s:
            if char in charsInS:
                charsInS[char] = charsInS.get(char) + 1
            else:
                charsInS[char] = 1

        for char in t:
            if char in charsInS:
                amount = charsInS.get(char)
                if amount == 1:
                    del charsInS[char]
                else:
                    charsInS[char] = amount - 1
            else:
                return False
        if len(charsInS) == 0:
            return True
        return False