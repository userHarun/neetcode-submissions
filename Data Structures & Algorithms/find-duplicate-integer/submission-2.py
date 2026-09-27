class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                break
        return slow2 


'''
Let each val point to its index in the nums arr.
Then, eventually we will find two vals pointing to the same index.
We can do this because we know the vals we will be in the range [1,n]
Thus, the val that points to the same index. that index is the duplicate

Floyd detection algo in a linkedlist


so first, find where they intersect
then, start another loop with a new slow ptr to find where the new slow intersects FROM where the original


'''