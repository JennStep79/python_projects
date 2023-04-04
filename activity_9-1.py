# Remember that when working with recursive algorithms, it is helpful to determine the base case before starting to code the solution.

# 1. Write an algorithm that checks if a string contains another string.
# If it does, return True; otherwise, return False.
# Example: When checking if string "Hello world" contains "Hello", the function should return True. If checking if 
# the same string contains "Bye", the function should return False.

# function check_string(base, search)
# return boolean expression for if search is found in base
# def check_string(base, search):
#     return search in base



check_string = lambda base, search: search in base

print(check_string("Hello world", "Bye"))
# 2. Write a recursive function that takes in a number and returns the sum of the numbers from 0 to the number.
# Example: if the input is 5, the expected output would be 15 (5+4+3+2+1 = 15).

# function recursive_add(int)
# base case int is 1, return 1
# recursive case return int + recursive_add(int-1)

def recursive_add(num):
    if num == 1:
        return 1
    elif num > 1:
        return num + recursive_add(num-1)
    else:
        return num + recursive_add(num +1)
    
print(recursive_add(5))

# 3. Write a function that takes in a string and returns the string reversed.
# Example: if the input is "hello", the expected output would be "olleh".

def reverse_string(string):
    return string[::-1]

print(reverse_string("Hello"))
# 4. Write a recursive function that takes in a list of strings and returns the words capitalized.
# Example: if the input is ['pandas', 'monkeys', 'koalas', 'kangaroos'], then the expected 
# output would be PANDAS MONKEYS KOALAS KANGAROOS.

def recursive_caps(lst):
    if not lst:
        return []
    else:
        return [lst[0].upper()] + recursive_caps(lst[1:])
    
# def recursive_capitalize(test_list):
#     if len(test_list) == 0:
#         return ""
#     else:
#         return (f"{test_list[0].upper()} {recursive_capitalize(test_list[1:])}")
    
print(recursive_caps(['pandas', 'monkeys', 'koalas', 'kangaroos']))



# 5. Write a function that takes in a list of numbers and returns the product of the numbers in the list.
# Example: if this input is [4, 3, 5], then the expected output would be 60 (4*3*5=60).

def num_product(list):
    result = 1
    for num in list:
        result*=num
    return result

print(num_product([4, 3, 5]))
# 6. Write an algorithm that prints the non-repeating integers in a list.
# Example: in a list of [1, 5, 1, 6, 8, 5], the expected output would be 6, 8.
def non_repeating(lst):
    result = {}
    for i in range(len(lst)):
        if lst[i] not in result:
            result[lst[i]]=0
        result[lst[i]]+=1

    for key in result:
        if result[key] == 1:
            print(key)

non_repeating([1, 5, 1, 6, 8, 5])

# What is a data structure and why are they important for programmers to know?
# A data structure is a method for organizing data in a computer. It is important to know 
# about data structures to be able to choose the most efficient data structure for a situation.

# What is a linear data structure?
# A linear data structure is a structure in which the elements are arranged in a 
# linear order (in a sequence). Array, stack, queue, and linked list are examples of linear data structures.

# What is a linked list?
# A linked list is a linear data structure. The nodes/elements are linked. Each node contains a data 
# field and a pointer field to the next node. The first node is called the head. If the list is empty, 
# the head node points to null. A linked list has the ability to grow and shrink/change size. There are singly and doubly-linked lists.

# Compare use of a linked list versus an array.
# A linked list is a dynamic data structure in languages where the arrays are fixed sizes. Insertion and deletion of elements is more efficient when using linked lists than arrays.  
#   Arrays have random accessing, which means it is more efficient to access an element at any index in an 
# array than in a linked list. 

# What is an algorithm?
# An algorithm is a step-by-step procedure (a set of instructions to be executed by the computer).

# Define recursion.
# Recursion is when a problem is defined in terms of itself. It is when a function calls itself over and over. 
# There is a base case and recursive case. 
# Recursion makes use of the stack data structure.

# What is algorithm analysis and why it is important?
# Big O Notation is the mathematical notation used to describe the time and space complexities of algorithms. 
# There are many ways to write an algorithm, so algorithm analysis determines the efficiency of the algorithm. 
# Time complexity refers to the amount of time an algorithm runs based on the size of 
# the input. Space complexity refers to the amount of memory taken by an algorithm based on the size of the input.

# Compare linear search and binary search.
# Binary search is more efficient than linear search as fewer comparisons are made. 
# Binary search has O(logn) time complexity, while linear search has O(n) time complexity.
# Binary search is an efficient way to find an item in a sorted list, as it repeatedly divides the list in 
# half in order to find the item in question. 
# Linear search is where each item is checked in order from the start of the list.

# What is merge sort and how does it work?
# Merge sort is a common sorting algorithm known as a divide-and-conquer algorithm. 
# It creates smaller lists of data and then merges and sorts adjacent data to make larger sorted lists. 
# These lists are merged repeatedly until there is one large sorted list.

# What is selection sort and how does it work?
# Selection sort is a common sorting algorithm. It repeatedly picks the smallest number from the 
# list and puts it at the beginning. This process continues until the list is sorted.
