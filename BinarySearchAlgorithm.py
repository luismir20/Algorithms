arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

result = binary_search(arr, 4)
print(result)  
