def pushZerosToEnd(arr):
    count = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
        
arr = [1, 2, 0, 4, 3, 0, 5, 0]
pushZerosToEnd(arr)