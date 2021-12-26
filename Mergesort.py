# Time Complexity: O(nlogn)
# Space Complexity: O(n) on arrays and constant on linked lists.

def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break 

    return result

def mergesort(list):
    if len(list) < 2:
        return list

    middle = len(list)//2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)

if __name__ == "__main__":
    nums = [3,4,5,1,2,8,3,7,6,0]
    print (mergesort(nums))