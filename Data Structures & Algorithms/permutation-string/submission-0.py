class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        k = len(s1)
        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1
        
        l = 0

        for r in range(len(s2)):

            freq2[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) > k:
                # remove left size count
                freq2[ord(s2[l]) - ord("a")] -= 1
                l += 1




            # if its size l
            if (r - l + 1) == k and freq1 == freq2:
                return True
        

        return False
