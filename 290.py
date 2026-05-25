class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_map={}
        words=s.split()
        if len(pattern)!=len(words):
            return False
        for p,w in zip(pattern,words):
            if p not in pattern_map:
                pattern_map[p]=w
            elif pattern_map[p]!=w:
                return False
        
        seen=set()
        for key in pattern_map:
            val=pattern_map[key]
            if val in seen:
                return False
            seen.add(val)
        return True
        