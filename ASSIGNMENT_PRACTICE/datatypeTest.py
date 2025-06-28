# def sum_list(numbers):
#     total=0
#     if numbers==[]:
#         return 0
#     else:
#         for i in numbers:
#             total=total+i
#         print(total)

# numbers = [10, -5, 7, 8, -2]
# sum_list(numbers)


def find_largest(numbers):
    
    sort_list= numbers.sort()
    print(sort_list)
    
numbers = [3, 8, 2, 10, 5]
find_largest(numbers)