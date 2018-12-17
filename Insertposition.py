# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2

        
nums = [1,3,5,6]
target = 0

low = 0
high = len(nums)-1
found = False

while(low <= high and found == False):
	mid = (low + high ) // 2
	if nums[mid] == target:
		found = True
	else:
		if target < nums[mid]:
			high = mid - 1
		else:
			low = mid + 1

if target in nums:
	print(mid)

else:
	if target < nums[mid]:
		nums.insert(mid,target)
	else:
		nums.insert(mid+1,target)
				
print(nums)
		

