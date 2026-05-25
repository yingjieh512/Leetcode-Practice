class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        newnums=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==val:
                count+=1
                continue
            else:
                newnums.append(nums[i])
        nums[:]=newnums
        return len(newnums)