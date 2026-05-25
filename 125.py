class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= ''.join(ch for ch in s.lower() if ch.isalnum())
        if len(s)<=1:
            return True
        left=0
        right=len(s)-1
        while True:
            if left>=right:
                break
            if s[left]!=s[right]:
                return False
            else:
                left+=1
                right-=1
        return True
            