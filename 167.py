class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        leftPointer=0
        rightPointer=len(numbers)-1
        while True:
            if numbers[leftPointer]+numbers[rightPointer]==target:
                return [leftPointer+1,rightPointer+1]
            elif numbers[leftPointer]+numbers[rightPointer]<target:
                leftPointer+=1
            else:
                rightPointer-=1
