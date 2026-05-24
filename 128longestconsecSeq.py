class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        max_sofar=0
        for num in num_set:
            if num-1 not in num_set:
                k=1
                while True:
                    if num+k in num_set:
                        k+=1
                    else:
                        break
                max_sofar=max(k,max_sofar)
        return max_sofar
