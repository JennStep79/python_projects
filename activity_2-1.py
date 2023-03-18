def arb_args(*args):
    for arg in args:
        print(arg)

# arb_args(1, False, "Jenn", 2)

def inner_func(int_1, int_2):
    def divide():
        return int_1 / int_2
    def modulus():
        return int_1 % int_2
    print(divide() + modulus())

# inner_func(5, 17)

def lunch_lady(str_1, str_2="Mystery Meat"):
    print(str_1, str_2)

# lunch_lady("Jeff", "Pizza")
# lunch_lady("Megan")

def sum_n_product(int_1, int_2):
    return int_1 + int_2, int_1 * int_2

# print(sum_n_product(1, 2))

alias_arb_args = arb_args

# alias_arb_args("test", 0)

def arb_mean(*args):
    if len(args) == 0:
        print("No arguments provided")
    else:
        total = 0
        for arg in args:
            total += arg
        print(total/len(args))

# arb_mean(10, 20)

def arb_longest_string(*args):
    longest = ""
    for arg in args:
        if len(arg) > len(longest):
            longest = arg
    return longest

# print(arb_longest_string("test", "really long test", "really super long test", "t", "really super ultra long test"))



