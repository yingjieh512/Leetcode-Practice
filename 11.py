class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxsofar=0
        left=0
        right=len(height)-1
        while left < right:
            calc_volume=(right-left)*min(height[left],height[right])
            maxsofar=max(maxsofar,calc_volume)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return maxsofar