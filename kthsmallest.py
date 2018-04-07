def partition(arr, low, high):
    i = low
    pivot = arr[low]
    for j in range(low+1, high+1):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[low], arr[i] = arr[i], arr[low]
    return i

def quickselect(arr, low, high, k):
    index = partition(arr,low,high)
    length = index + 1
    if k == length:
        return arr[index]
    if k < length:
        return quickselect(arr, low, length-1,k)
    else:
        return quickselect(arr,length+1, high, k-length)
if len(nums) == 1:
    return nums[0]
if len(nums) < k:
    return
return quickselect(nums, 0, len(nums)-1, k)