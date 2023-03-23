# Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.
# Unsorted list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] Sorted list of tuples: 
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

grades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_tuples = sorted(grades, key = lambda x: x[1])
# print(sorted_tuples)

# Write a lambda function to cube every element of a list.
#Original list: [3,6,9,2] List after lambda function: [27,216,729,8]

cubes = lambda list: [num ** 3 for num in list]
# print(cubes([3, 6, 9, 2]))

# Write a lambda function to determine whether a number is even or odd (the function should return True or False), 
# and then use the function and a list comprehension to create a new list of booleans, where even numbers are 
# True and odd numbers are False.
# Input list: [3,6,9,2] List after lambda function and list comprehension: [False, True, False, True]

is_even = lambda num: num % 2 == 0
bool_lst = [is_even(num) for num in [0, 1, 2, 3, 4]]
# print(bool_lst)

# Use a list comprehension to create a list of the numbers from 1 to 100 (including 100).

num_lst = [num for num in range(1, 101)]
# print(num_lst)

# Use a dictionary comprehension to count the length of each word in a sentence.
# Input: "The quick brown fox jumped over the fence." otuput: 
# {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}

word_length = {word: len(word) for word in "The quick brown fox jumped over the fence.".split()}
# print(word_length)

