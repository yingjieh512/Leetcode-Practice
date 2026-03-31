class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        child=0
        cookies=0
        while child<len(g) and cookies<len(s):
            if g[child]<=s[cookies]:
                child+=1
            cookies+=1 
        return child