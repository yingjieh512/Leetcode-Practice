class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num_array=nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return sum(self.num_array[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)