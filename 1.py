class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        have_seen={}
        for i,num in enumerate(nums):
            need=target-num
            if need in have_seen:
                return [have_seen[need],i]
            have_seen[num]=i
