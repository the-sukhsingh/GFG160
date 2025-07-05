class Solution:
    def areAnagrams(self, s1, s2):
       # code here
        n = len(s1)
        m = len(s2)
        if n != m:
           return False
        n1 = [0] * 26
        n2 = [0] * 26
        for char in s1:
            n1[ord(char) - ord('a')] += 1
        for char in s2:
            n2[ord(char) - ord('a')] += 1
        if n1 == n2:
            return True
        return False