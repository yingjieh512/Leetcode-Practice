class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        result={}
        for i in range(3):
            result[i]=0
        for i in range(len(nums)):
            if nums[i]==0:
                result[0]+=1
            if nums[i]==1:
                result[1]+=1
            if nums[i]==2:
                result[2]+=1
        final=result[0]*[0]+result[1]*[1]+result[2]*[2]
        nums[:]=final