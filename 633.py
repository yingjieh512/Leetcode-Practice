class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c==0 or c==1:
            return True
        l=0
        r=int(c**0.5)
        while l<=r:
            result=l*l+r*r
            if result>c:
                r-=1
            if result<c:
                l+=1
            if result==c:
                return True
        return False