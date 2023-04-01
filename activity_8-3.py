def binary_search(data, el):
    first = 0
    last = len(data)-1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if data[mid] == el:
            found = True
        else:
            if el < data[mid]:
                last = mid-1
            else:
                first = mid+1

    return found

test_lst = [1, 3, 5, 6, 9, 12, 13, 16, 21, 982]
print(binary_search(test_lst, 2))