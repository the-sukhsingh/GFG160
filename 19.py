class Solution:
    def minChar(self, s):
        #Write your code here
        n = len(s)
        rev = s[::-1]
        s = s + '$' + rev
        lps = computeLPSArray(s)
        
        
        return n - lps[-1]


        
def computeLPSArray(pat):
    n = len(pat)
    lps = [0] * n
    len_lps = 0
    i = 1
    while i < n:
        if pat[i] == pat[len_lps]:
            len_lps += 1
            lps[i] = len_lps
            i += 1
        else:
            if len_lps != 0:
                len_lps = lps[len_lps - 1]
            else:
                lps[i] = 0
                i += 1
    return lps