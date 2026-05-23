class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        newint=sorted(intervals,key=lambda x:x[0])
        result=[newint[0]]
        for i in range(1,len(newint)):
            if result[-1][1]>=newint[i][0]:
                if result[-1][1]<=newint[i][1]:
                    result[-1][1]=newint[i][1]
                continue
            else:
                result.append(newint[i])
        return result
