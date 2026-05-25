class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        min_len=len(nums)+1
        prefix_sum_upto={}
        for right in range(len(nums)+1):
            if right==0:
                prefix_sum_upto[right]=0
            else:
                prefix_sum_upto[right]=prefix_sum_upto[right-1]+nums[right-1]
            while prefix_sum_upto[right]-prefix_sum_upto[left]>=target and left<right:
                min_len=min(right-left,min_len)
                left+=1
        if min_len==len(nums)+1:
            return 0
        return min_len

            