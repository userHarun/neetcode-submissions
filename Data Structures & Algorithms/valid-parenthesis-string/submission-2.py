
class Solution:
    def checkValidString(self, s: str) -> bool:
        opens = []
        stars = []
        for i in range(len(s)):
            if s[i] == "*":
                stars.append(i)
            elif s[i] == '(':
                opens.append(i)
            else:
                if opens:
                    opens.pop()
                elif stars:
                    
                    stars.pop()
                else:
                    return False
        while opens and stars:
            if stars:
                if stars[-1] > opens[-1]:
                    opens.pop()
                    stars.pop()
                else:
                    return False
        
        
        return len(opens) == 0
    
        


'''

s="*(*)(" 
we must store the positions of the stars and right parenthesis because if a star appeared before an open parenthesis we cant just always treat it as a closing one


'''