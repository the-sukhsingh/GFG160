def reverseArray( arr):
    length = len(arr)
    for i in range(len(arr) // 2):
        arr[i], arr[-i-1] = arr[-i-1], arr[i]
            

arr = [1, 4, 3, 2, 6, 5]

print(reverseArray(arr))