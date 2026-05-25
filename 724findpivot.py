class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum=[0]*len(nums)
        right_sum=[0]*len(nums)
        left_sums=0
        right_sums=0
        for i in range(len(nums)):
            left_sum[i]=left_sums
            left_sums+=nums[i]
        for j in range(len(nums)):
            right_sum[len(nums)-j-1]=right_sums
            right_sums+=nums[len(nums)-j-1]
        for i in range(len(nums)):
            if left_sum[i]==right_sum[i]:
                return i
        return -1