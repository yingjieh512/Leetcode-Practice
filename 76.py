class Solution(object):
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""
        
        tLetter = {}
        for c in t:
            tLetter[c] = tLetter.get(c, 0) + 1
        
        curr = {}
        for key in tLetter:
            curr[key] = 0
        
        l = 0
        start = 0
        min_len = float('inf')
        
        def check():
            for key in tLetter:
                if curr[key] < tLetter[key]:
                    return False
            return True
        
        for r in range(len(s)):
            if s[r] in tLetter:
                curr[s[r]] += 1
            
            while check():
                if r - l + 1 < min_len:
                    start = l
                    min_len = r - l + 1
                
                removedchar = s[l]
                l += 1
                if removedchar in tLetter:
                    curr[removedchar] -= 1
        return "" if min_len == float('inf') else s[start:start + min_len]