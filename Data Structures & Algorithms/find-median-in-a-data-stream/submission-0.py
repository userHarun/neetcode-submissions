class MedianFinder:

    def __init__(self):
        self.small = [] # min heap
        self.large = [] # max heap


    def addNum(self, num: int) -> None:
        n = len(self.small)
        m = len(self.large)
        # add to small orginally(which we need the largest value at the front)
        heapq.heappush(self.small, -1 * num)
        # make sure every elem in left half is < than every elem in right half
        if self.small and self.large and self.small[0] * -1 > self.large[0]:
            # append it to right since its bigger
            largest = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, largest)


        # check if lengths are uneven
        # one can be greater than other, but by at most 1
        if len(self.small) > len(self.large) + 1:
            # push to large
            largest =  -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, largest)

        if len(self.large) > len(self.small) + 1:
            # push to small
            smallest =  heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * smallest)


       

    def findMedian(self) -> float:
        # if our final length is odd, median is in small heap

        # if even we take root of small and large and / 2. 

        if len(self.small) > len(self.large):
            return self.small[0] * -1
        
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2



'''
For the median, we need access to:

largest number in the smaller half
smallest number in the larger half

use use 2 heaps and append to them accordingly

when the total number of elements is odd, keep the extra element in one specific heap
(commonly left) so you always know where the median is.

3 cases because of our invariant that abs(len(large) - len(small)) <= 1:
small bigger by 1
large bigger by 1
same size

'''