def hello():
    print("Hi")

hello()


def pack(a, b, c):
    return [a, b, c]

print(pack("pickles", "wolves", "beer"))


def eat_lunch(food_items):
    if not food_items:
        print("My lunch box is empty!")
    else:
        print(f"First I eat {food_items[0]}")
        for item in food_items[1:]:
            print(f"Next I eat {item}")

food_items = ["apple", "sandwich", "chips"]
eat_lunch(food_items)

empty_luchbox = []
eat_lunch(empty_luchbox)
