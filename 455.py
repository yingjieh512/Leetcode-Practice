class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sorted_Interval = sorted(intervals, key=lambda x: x[1])
        count=0
        prev=0
        for i in range(1,len(sorted_Interval)):
            if  sorted_Interval[i][0]<sorted_Interval[prev][1]:
                count+=1
            else:
                prev=i
        return count