class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        count_s1={}
        count={}
        for i in range(len(s1)):
            count_s1[s1[i]]=count_s1.get(s1[i], 0) + 1
        left=0
        for right in range(len(s2)):
            count[s2[right]]=count.get(s2[right], 0) + 1
            while (right - left + 1) > len(s1):
                count[s2[left]] -= 1
                if count[s2[left]]==0:
                    del count[s2[left]]
                left+=1
            if count==count_s1:
                return True
        return False
