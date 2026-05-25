class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        i_longest={}
        for i in range(len(s)):
            i_longest[i]=[s[i]]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[j] in i_longest[i]:
                    break
                i_longest[i].append(s[j])
        result=[len(i_longest[key]) for key in i_longest]
        return max(result)
