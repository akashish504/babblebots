def flip(arr,id):
    id_range = id//2
    if id % 2 != 0:
        id_range  = id//2 + 1
        
    for j in range(id_range):
        # print(j," ",id)
        arr[j], arr[id-j] = arr[id-j], arr[j]
    return arr

arr = [2,3,9,10,24,13,67,34,5,2,2]
n = len(arr)
for i in range(n-1, -1, -1):
    # print(i)
    # to find pos of min element
    # print(arr)
    min_el = 2147483647
    lowest_index = 0
    for j in range(i+1):
        if arr[j] < min_el:
            lowest_index = j
            min_el = arr[j]
    print(lowest_index)
    arr = flip(arr,lowest_index)
    # print(arr)
    # print(i)
    arr = flip(arr,i)
# arr = flip(arr,1)
# one last flip
arr1 = flip(arr, len(arr)-1)
print(arr1)
    