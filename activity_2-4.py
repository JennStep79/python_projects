# write a function called max_num() to find the maximum of three numbers

def max_num(int_1, int_2, int_3):
    list = [int_1, int_2, int_3]
    return max(list)

# print(max_num(10, 2, 14))


# write a function called mult_list() to multiply all the numbers in a list

def mult_list(list):
    result = 1
    for x in list:
        result *= x
    return result

list1 = [2, 4, 6]
list2 = [1, 2, 3]
# print(mult_list(list1))
# print(mult_list(list2))


# write a function called rev_string() to reverse a string

def rev_string(string):
    string = string[::-1]
    return string

# print(rev_string("Hello World!"))


# write a function called num_within() to check whether a number falls in a given range. 
# Accepts the number, beginning of range, and end of range as args. 
# Example: num_within(3, 2, 4) returns True, num_within(10, 2, 5) returns False.

def num_within(int_1, int_2, int_3):
    if int_1 >= int_2 and int_1 <= int_3:
        return True
    else:
        return False

# print(num_within(3, 2, 4))
# print(num_within(10, 2, 5))


# write a function called pascal() that prints out the first n rows of Pascal's triangle.
# Accepts number n and the number of rows to print.

def pascal(n):
    for i in range(n):
        print(' '.join(map(str, str(11**i))))

# pascal(1)
# pascal(5)