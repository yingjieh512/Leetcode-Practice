class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        oneP=0
        twoP=0
        result=[]
        while m > 0 and n > 0:
            if nums1[oneP] <= nums2[twoP]:
                result.append(nums1[oneP])
                oneP += 1
                m -= 1
            else:
                result.append(nums2[twoP])
                twoP += 1
                n -= 1
        while m > 0:
            result.append(nums1[oneP])
            oneP += 1
            m -= 1
        while n > 0:
            result.append(nums2[twoP])
            twoP += 1
            n -= 1
        nums1[:] = result
        