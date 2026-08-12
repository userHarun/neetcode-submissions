class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1, nums2
        if len(A) > len(B):
            A , B = B, A
        
        total = len(A) + len(B)
        low = 0
        high = len(A)

        half = (total+ 1) // 2

        while low <= high:
            # take i elements from A and take j eements from B for the left partition
            i = (low + high) // 2
            j = (half) - i

            # actual values from boundaries
            l1 = A[i - 1] if i > 0 else float('-inf')
            r1 = A[i] if i < len(A) else float('inf')
            l2 = B[j - 1] if j > 0 else float('-inf')
            r2 = B[j] if j < len(B) else float('inf')
            # check if its valid part
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)


            #move boundaries otherwise 
            if l1 > r2:
                # left values too big
                high = i - 1
            else:
                low = i + 1
    

'''


'''
