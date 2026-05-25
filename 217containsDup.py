class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count={}
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
            if count[nums[i]]>=2:
                return True
        return False