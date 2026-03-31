class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        result=[1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i+1]>ratings[i]:
                result[i+1]=result[i]+1
        for i in range(len(ratings)-1):
            right=len(ratings)-1-i
            left=right-1
            if ratings[right]<ratings[left]and result[left]<=result[right]:
                result[left]=result[right]+1
        return sum(result)
