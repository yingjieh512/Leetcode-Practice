class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        result=[intervals[0]]
        for i in range(1,len(intervals)):
            added_i_in_inter=False
            for j in range(len(result)):
                if result[j][1]>=intervals[i][0]:
                    if result[j][1]<=intervals[i][1]:
                        result[j][1]=intervals[i][1]
                    added_i_in_inter=True
                    break
            if not added_i_in_inter:
                result.append(intervals[i])
        return result
            

