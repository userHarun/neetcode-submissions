class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        for word in strs:
            size = str(len(word))
            encoded += (size + '#' + word)
        return encoded
            
            

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_length = int(s[i:j])
            curr_word = s[j + 1: j + 1 + word_length]
            decoded.append(curr_word)
            i = j + 1 + word_length
        return decoded
             

'''
basically create a consistent format for the encode
then decode remoes that consistent format

store size of string at the beginning and then the delimiter
'''