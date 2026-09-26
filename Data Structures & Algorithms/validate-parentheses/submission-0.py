class Solution:
    def isValid(self, s: str) -> bool:
        cache = []
        closing = {
            ")":"(",
            "]":"[",
            "}":"{",
        }

        opening = ["(","[","{"]

        for p in s:
            if not bool(cache):
                cache.append(p)
            else:
                if p in closing:
                    if cache[-1] == closing.get(p):
                        cache.pop()
                    else:
                        return False
                elif p in opening:
                    cache.append(p)
                else:
                    return False
        
        if not bool(cache):
            return True
        else:
            return False