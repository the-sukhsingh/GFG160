from collections import Counter
class Solution:
    def nonRepeatingChar(self,s):
        #code here
        counts = Counter(s)
        
        for char in s:
            if counts[char] == 1:
                return char
        return '$'
    