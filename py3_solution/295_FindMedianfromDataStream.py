import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxh = []
        self.minh = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.length += 1
        if self.length == 1:
            heapq.heappush(self.minh, num)
            return
        
        if num >= self.minh[0]:
            heapq.heappush(self.minh, num)
            if len(self.minh) > len(self.maxh) + 1:
                heapq.heappush(self.maxh, -heapq.heappop(self.minh))
        else:
            heapq.heappush(self.maxh, -num)
            if len(self.minh) < len(self.maxh):
                heapq.heappush(self.minh, -heapq.heappop(self.maxh))
        

    def findMedian(self) -> float:
        if self.length % 2:
            return self.minh[0]
        else:
            return (self.minh[0] + -self.maxh[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
