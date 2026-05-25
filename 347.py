class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count={}
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
        result=sorted(count.items(),key=lambda x:x[1],reverse=True)
        final=[]
        counted=0
        for key,value in result:
            final.append(key)
            counted+=1
            if counted>=k:
                break
        return final
