class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        low = 0
        high = N - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] >nums[high]:
                low = mid + 1
            else:
                high = mid
        
        return nums[low]


'''
O(N) is simple ,so for a log N solution it usually involves binary search

well, we need to know where the arry was rotated, then the problem becomes simple
if we find out it was rotated 4 times we know ever number to the right of the 4th will be smaller
 

how to check where its rotated:
if nums[mid] > nums[h]: the rotated area is on the left and move boundary to the  right
else:
    move the boundary to the left
at the end nums[left] will have your min
 

nums = [3,4,5,6,1,2]
        l    m    h
nums = [3,4,5,6,1,2]
        l    m    h
               l
                 m
              l
              m h
                l
              

'''