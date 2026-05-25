class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newnums=sorted(nums,key=lambda x: x*x)
        return [newnums[i]*newnums[i] for i in range(len(newnums))]