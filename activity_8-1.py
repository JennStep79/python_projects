def bubble_sort(lst):
    for i in range(len(lst)-1):
        swapped = False
        print(f'Iteration {i}')
        for j in range(len(lst)-1):
            print(f'Comparing {lst[j]} and {lst[j+1]}')
            if lst[j] > lst[j+1]:
                swapped = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
        if not swapped:
            return
    return lst

sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")