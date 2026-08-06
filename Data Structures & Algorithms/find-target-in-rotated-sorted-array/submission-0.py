class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[high]:
                # check if your target is in the sorted part
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # check if youre target is in this rotated part
                if nums[mid] < target <= nums[high]:
                    low  = mid + 1
                else:
                    high = mid - 1
                
                
        return -1



'''
Input: nums = [3,4,5,6,1,2], target = 1 
                l  m     h

we do the binary approach and move our boundaries based on certain conditions

for ex, if nums[m] > nums[h] we know every value to the right is in the rotated part

so we use the information that nums[l]... nums[mid] is for sure rotated and we can just check if our target is in the sorted half
else
we know its in the rotated half.






'''