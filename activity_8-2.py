# sort an unsorted numerical list

# def sort_list(lst):
#     lst.sort()
#     return lst

# print(sort_list([2, 5, 6, 1, 9]))

# sort function acts on the existing list and does not return anything

a = [2, 5, 6, 1, 9]
a.sort()
print(a)

# create a new sorted list from an unsorted list
# sorted function returns a new list 

unsorted = [2, 5, 6, 1, 9]
new_list = sorted(unsorted)
# print(new_list)

# create a new sorted list in descending order from an unsorted list

descending_list = sorted(unsorted, reverse=True)
print(descending_list)

