def getMinDiff(arr,k):
    n = len(arr)
    arr.sort()
    
    res = arr[n-1] - arr[0]
    
    for i in range(1,len(arr)):
        if(arr[i] - k < 0):
            continue
        minH = min(arr[0]+k, arr[i] - k)
        maxH = max(arr[i - 1] , arr[n - 1] - k)
        res = min(res, maxH - minH)
        
    return res
    
k = 7
arr = [1, 8, 10, 6, 4, 6, 9, 1]

print(getMinDiff(arr,k))