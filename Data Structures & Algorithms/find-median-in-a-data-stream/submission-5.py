class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.length = 0
        

    def addNum(self, num: int) -> None:
        self.length += 1
        if not self.minHeap:
            heapq.heappush(self.minHeap, num)
            return

        ## Push to the correct heap
        if num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)
        
        ## Balance heaps so that median is in first position
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)
        elif len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        return 
            

        
        

    def findMedian(self) -> float:

        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        elif len(self.minHeap) == len(self.maxHeap):
            print(self.minHeap)
            print(self.maxHeap)
            print("-----")
            return float((-(self.maxHeap[0]) + self.minHeap[0]))/2
        else:
            return -self.maxHeap[0]
        
        