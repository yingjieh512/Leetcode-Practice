class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i_left_prod=1
        i_right_prod=1
        i_store_left_right={}
        for i in range(len(nums)):
            i_store_left_right[i]=[i_left_prod]
            i_left_prod*=nums[i]
        for i in range(len(nums)):
            i_store_left_right[len(nums)-i-1].append(i_right_prod)
            i_right_prod*=nums[len(nums)-i-1]
        result=[]
        for j in range(len(nums)):
            result.append(i_store_left_right[j][0]*i_store_left_right[j][1])
        return result
