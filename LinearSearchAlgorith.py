arr = [3, 2, 5, 1, 4]

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

result = linear_search(arr, 5)
print(result)