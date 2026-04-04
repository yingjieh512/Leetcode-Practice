class Solution(object):
    def checkPossibility(self, nums):
        changed = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                changed += 1
                if changed > 1:
                    return False
                if i >= 2 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
        return True

        