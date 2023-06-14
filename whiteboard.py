# Write a function that takes in a list of integers and returns the second largest number in the list. 
# This must be done without removing any items from lists (using pop, remove, etc) or using sort. 
# You can assume the list will always have 3 or more items. 

#Example 1
# Input = [5, 10, 2, 8, 3]
# Output = 8
# Explanation: the function should return 8 is the second largest number

#Example 2
#Input = [1, 2, 3, 4]
#Output = 3
#Explanation: 3 is the second largest number in the list

#Example 3 
#Input = [10, 1, 11]
#Ouput = 10
#Explanation: 10 is the second largest number in the list

# input: list
# output: integer (second largest)
# loop through the list
# set a variable = max(nums)
# set another variable that is a very small number
# compare each num in the list with the max number and the smallest number
# if the next_largest is smaller than num and less than the max, then reassign next_largest to num
# the loop keeps on going, reassigning next_largest to each number 

def second_largest(nums):
    max_num = max(nums)
    next_largest = -float("inf")
    for num in nums:
        if num < max_num and num > next_largest:
            next_largest = num
    return next_largest

nums = [5, 10, 2, 8, 3]
print(second_largest(nums))
            