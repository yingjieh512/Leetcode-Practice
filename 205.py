class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map={}
        for S,T in zip(s,t):
            if S not in s_map:
                s_map[S]=T
            elif T!=s_map[S]:
                return False
        seen=set()
        for key in s_map:
            val=s_map[key]
            if val in seen:
                return False
            seen.add(val)
        return True
        
        