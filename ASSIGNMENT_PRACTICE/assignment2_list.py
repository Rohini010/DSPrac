# 1) Create a list of the first 20 positive integers. Print the listrtlist= .
list=[]
for i in range(1,21):
  list.append(i)
print(list)


# 2) Print the first, middle, and last elements of the list created in Assignment 1.
print(list[0])
print(list[len(list)//2])
print(list[-1])

# 3) Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.
print(list[:5])
print(list[-5:])
print(list[5:15])

# 4) Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.
sqlist= [x**2 for x in range(1,11)]
print(sqlist)

# 5) Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list.
evnsqlist=[x**2 for x in range(1,21) if x%2==0]
print(evnsqlist)

# 6) Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list.
import random
random_list=[random.randint(1,14) for x in range(1,14)]
sort_list=sorted(random_list)
print("Sorted list " ,sort_list)
rev_list=sorted(sort_list, reverse=True)
print("Reverse list ",rev_list)

# 7) Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for x in matrix:
  print(matrix)
print(f"Element at second row and third column: {matrix[1][2]}")

# 11) Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. 
# Print the modified list.

list= [x for x in range(1,11)]
print(list)
del list[2]
list.pop(4)
del list[6]
print("updated list :",list)

# 12) Create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.
# list1=[1,2,3,4,5]
# list2=[6,7,8,9,8]
# zipped = list(zip(list1, list2))
# print(zipped)


# 13) Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.
def reverse_list(lst):
    return sorted(lst,reverse=True)

original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print(f"Original list: {original_list}")
print(f"Reversed list: {reversed_list}")