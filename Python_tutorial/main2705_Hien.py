# # Name: Tran Quang Hien
# # Student ID: GCS210109
# # Class: GCS1003A

# # Exercise 4:
# import random
# # a. Slice 1st half and 2nd half of the list
# # create a list of 20 random integers
# my_list = random.sample(range(1, 30), 20)

# # slice the list into two halves
# first_half = my_list[:10]
# second_half = my_list[10:]

# print("Original list:", my_list)
# print("First half of the list:", first_half)
# print("Second half of the list:", second_half)

# # b. Slice list to get a sublist that removes n elements at begin and n elements at end of list
# def return_list_b_c():
#     print("-----------------------------------------")
#     n = int(input("Enter the number of elements to remove (n): "))

#     sublist = my_list[n:len(my_list)-n]
    
#     print(f"Sublist without {n} elements at the beginning and end:", sublist)
# # c. With n from keyboard, get n first elements and n last elements, join them to make a new list of 2n elements
#     first_elements = my_list[:n]
#     last_elements = my_list[-n:]

#     new_list = first_elements + last_elements
    
#     print(f"New list of elements:", new_list)

# return_list_b_c()

# Exercise 5:
# Create a 5x5 list of integers
num_list = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# a) Get 3 middle rows in as many ways as you can
middle = num_list[1:4]
print("The 3 middle rows is: ")
for subaray in middle:
    print (subaray) 
# b) Get 2 last rows in as many ways as you can
last = num_list[3:5]
print("The 2 last rows is: ", last)
# c) Enter n from keyboard, get max, min of nth row and print them
n = int(input("Enter the row number (0-4): "))
if n >= 0 and n < len(num_list):
    row = num_list[n]
    max_value = max(row)
    min_value = min(row)
    print(f"Max value in the {n}th row: {max_value}")
    print(f"Min value in the {n}th row: {min_value}")
else:
    print("Invalid input for n!")
