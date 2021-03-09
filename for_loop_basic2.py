#1. Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big"
#define a function that accepts a list as parameters
# use a loop to go through the list to see if the values are positive or negative
# use an if condition to change positive numbers to "big"
def biggie_size(num_list):
    for idx in range(len(num_list)):
        if num_list[idx] > 0:
            num_list[idx] = "big"
    return num_list
# print(biggie_size([-1, 3, 5, -5]))

#2.Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
#define a function that accepts a list as parameters
# create a variable to store positive number count
# use a for loop to check if int is greater than o
# if it is greater than 0 count it in pos_count
# create a variable called last index and set it equal to the length of the last index of any list given
# set list of the last index to equal how many positive values were counted during the for loop
# evaluate the list of positive numbers and put the total count at the last index of the list
#print the function call
def count_positives(num_list):
    pos_count = 0
    for i in num_list:
        if i > 0:
            pos_count += i
    last_idx = len(num_list)-1
    num_list[last_idx] = pos_count
    return num_list
# print(count_positives([-1, 1, 1, 1]))

#3. Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7
# define a function
# use a variable to store integers added together
# use a for loop
# set count equal to count + iterable (i)
# return sum of integers in list
# print total 
def sum_total(nums_list):
    count = 0
    for i in nums_list:
        count += i
    return count
# print(sum_total([1,2,3,4]))

#4. Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5
# define a function that takes a list of integers
# create a variable to count up int
# use a for loop to loop through integers and put them in the variable
def average(nums_list):
    sum = 0
    for i in range(len(nums_list)):
        sum += nums_list[i]
    return sum / len(nums_list)
# print(average([1,2,3,4]))

#5. Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0
def length(nums_list):
    return len(nums_list)
# print(length([37,2,1,-9]))

#6. Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False
# define a function that accepts a list
# create a variable that contains min value
# use a for loop 

# def minimum(nums_list):
#     min = nums_list[0]
#     for idx in range(len(nums_list)):
#         if nums_list[idx] < min:
#             min = nums_list[idx]
#     return min
# print(minimum([37,2,1,-9]))

#7.Maximum - Create a function that takes a list and returns the maximum value in the array. 
# If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False
# def maximum(nums_list):
#     max = nums_list[0]
#     if len(nums_list) == 0:
#         return False
#     for idx in range(len(nums_list)):
#         if nums_list[idx] > max:
#             max = nums_list[idx]
#     return max
# print(maximum([37,2,1,-9]))

#8.Ultimate Analysis - Create a function that takes a list and returns a dictionary 
# that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should 
# return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
# define a function and pass a list
# def ultimate_analysis(nums_list):
#create variables for sumTotal, average, min, max, and length
    # sumTotal = 0
    # max = nums_list[0]
    # min = nums_list[0]
    # for idx in range(len(nums_list)):
    #     sumTotal += nums_list[idx]
    #     if nums_list[idx] > max:
    #         max = nums_list[idx]
    #     elif nums_list[idx] < min:
    #         min = nums_list[idx]
    # return {'max': max, 'min': min, 'sumTotal': sumTotal, 'len': len(nums_list)} 
# print(ultimate_analysis([37,2,1,-9]))

# 9. Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. # Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(nums_list):
    list_len = len(nums_list)
    for idx in range(int(len(nums_list)/2)):
        temp = nums_list[list_len-1-idx]
        nums_list[list_len-1-idx] = nums_list[idx]
        nums_list[idx] = temp
    return nums_list
# print(reverse_list([3,1,8,10,-5,6]))