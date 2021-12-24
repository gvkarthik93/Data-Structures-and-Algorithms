def bubbleSort(nums):
	for i in range(len(nums)):
		for j in range(len(nums)-1):
			if nums[j] > nums[j+1]:
				temp = nums[j+1]
				nums[j+1] = nums[j]
				nums[j] = temp
	return


def modifiedBubbleSort(nums):
	for i in range(len(nums)):
		flag = 0
		for j in range(len(nums)-1):
			if nums[j] > nums[j+1]:
				temp = nums[j+1]
				nums[j+1] = nums[j]
				nums[j] = temp
				flag = 1

		if flag == 0:
			break
	return

def selectionSort(nums):
	for i in range(len(nums)):
		min_index = i
		for j in range(i, len(nums)):
			 if nums[j] < nums[min_index]:
			 	min_index = j
		temp = nums[i]
		nums[i] = nums[min_index]
		nums[min_index] = temp
	return

def insertionSort(nums):

	for i in range(1, len(nums)):

		j = i

		while j > 0 and nums[j] < nums[j-1]:
			temp = nums[j-1]
			nums[j-1] = nums[j]
			nums[j] = temp
			j -= 1

	return


nums = [2,1,3,5,4]
insertionSort(nums)
print (nums)

