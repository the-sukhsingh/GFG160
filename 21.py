def sort012(arr):
    # code here
    n = len(arr)
    for i in range(len(arr)):
        if arr[i] == 0:
            arr.pop(i)
            arr.insert(0,0)
    
    for i in range(len(arr)):
        if arr[i] == 2:
            arr.pop(i)
            arr.insert(len(arr),2)

        
    return arr
    
print(sort012([0, 1, 2, 0, 1, 2]))