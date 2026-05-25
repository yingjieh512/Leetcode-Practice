class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result=[]
        left=0
        window_count={}
        p_count={}
        for i in range(len(p)):
            p_count[p[i]]=p_count.get(p[i],0)+1
        for right in range(len(s)):
            window_count[s[right]]=window_count.get(s[right],0)+1
            while right-left+1>len(p):
                window_count[s[left]]-=1
                if window_count[s[left]]==0:
                    del window_count[s[left]]
                left+=1
            if window_count==p_count:
                result.append(left)
        return result