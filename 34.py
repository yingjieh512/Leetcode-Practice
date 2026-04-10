class Solution(object):
    def searchRange(self, nums, target):
        def lowerbound(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l

        def upperbound(nums, target):
            l = 0
            r = len(nums)
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l

        lower = lowerbound(nums, target)
        upper = upperbound(nums, target) - 1

        if lower == len(nums) or nums[lower] != target:
            return [-1, -1]
        return [lower, upper]