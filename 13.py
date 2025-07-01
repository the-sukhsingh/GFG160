def findMissing(arr):
    n = len(arr)
    for i in range(n):
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[temp - 1] = temp            
    for i in range(1,n + 1):
        if i != arr[i - 1]:
            return i
    return n + 1   
print(findMissing([-3, 5, 4, 5, 8, 7, 0, 9]))