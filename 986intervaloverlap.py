class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        left=0
        right=0
        result=[]
        for inter in firstList:
            for secinter in secondList:
                if max(inter[0],secinter[0])<=min(inter[1],secinter[1]):
                    result.append([max(inter[0],secinter[0]),min(inter[1],secinter[1])])
        return result

