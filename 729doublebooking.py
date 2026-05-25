class MyCalendar(object):

    def __init__(self):
        self.list=[]
        

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        if not self.list:
            self.list.append([startTime,endTime])
            return True
        for i in range(len(self.list)):
            if max(startTime,self.list[i][0])<min(endTime,self.list[i][1]):
                return False
        else:
            self.list.append([startTime,endTime])
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)