def kadane(arr):
    totalSum = 0    
    currMaxSum = 0
    currMinSum = 0
    maxSum = arr[0]
    minSum = arr[0]
    
    for i in range(len(arr)):
        currMaxSum = max(currMaxSum + arr[i], arr[i])
        maxSum = max(maxSum, currMaxSum) 
        currMinSum = min(currMinSum + arr[i], arr[i])
        minSum = min(minSum, currMinSum)
        totalSum += arr[i]
    normalSum = maxSum
    circularSum = totalSum - minSum
    if minSum == totalSum:
        return normalSum
    return max(normalSum, circularSum)


arr = [8, -8, 9, -9, 10, -11, 12]

print(kadane(arr))