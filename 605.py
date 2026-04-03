class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count=n
        if len(flowerbed)==1:
            if (n==1 and flowerbed[0]==0) or (n==0):
                return True
            else:
                return False
        for i in range(len(flowerbed)):
            if i ==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                count-=1
                flowerbed[i]=1
            elif i == len(flowerbed)-1:
                if flowerbed[i]==0 and flowerbed[i-1]==0:
                    count-=1
                    flowerbed[i]=1
            else:
                if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    count-=1
        if count<=0:
            return True
        else:
            return False


