class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==0:
            return []
        result=[[nums[0],nums[0]]]
        left=0
        seen=set()
        for right in range(len(nums)):
            seen.add(nums[right])
        for right in range(len(nums)):
            if nums[right]>result[-1][1]:
                can_change=True
                # for s in range(result[-1][1],nums[right]):
                #     if s not in seen:
                #         can_change=False
                s=result[-1][1]+1
                if s not in seen:
                    can_change=False
                if can_change:
                    result[-1][1]=nums[right]
                else:
                    result.append([nums[right],nums[right]])
        final_res=[]
        for pair in result:
            if pair[0]==pair[1]:
                final_res.append(str(pair[0]))
            else:
                final_res.append(str(pair[0])+"->"+str(pair[1]))
        return final_res


