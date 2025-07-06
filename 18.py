def searcch(pat,txt):
    output = []
    n = len(txt)
    m = len(pat)
    
    for i in range(n - m + 1):
        print(txt[i: i + m ])
        if txt[i: i+ m] == pat:
            output.append(i)
        
    return output
            
            
print(searcch("aaba", "aabaacaadaabaaba"))  # Output: [0, 2]