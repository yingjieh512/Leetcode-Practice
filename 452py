class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sorted_Interval = sorted(points, key=lambda x: x[1])
        count=0
        prev=0
        for i in range(1,len(sorted_Interval)):
            if  sorted_Interval[i][0]<=sorted_Interval[prev][1]:
                count+=1
            else:
                prev=i
        return len(points)-count

