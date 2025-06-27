def second_largest(arr):
    print(sorted(arr))
    print(set(arr))
    arr = sorted(list(set(arr)))
    if len(arr) > 1:
        return arr[-2]
    return -1


arr = [12, 35, 1, 10, 34, 1]
print(second_largest(arr))