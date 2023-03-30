'''
Problem 1: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
returns {'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
'''

def flatten_dict(dictionary):
    flattened = {}
    for key in dictionary.keys():
        if isinstance(dictionary[key], dict):
            for inner_key, inner_value in dictionary[key].items():
                flattened.update({key + "." + inner_key: inner_value})
        else:
            flattened.update({key: dictionary[key]})
    return flattened

print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))




'''
Problem 2: Write a function unflatten_dict to do reverse of flatten_dict.

unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
returns {'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
'''
def unflatten_dict(dictionary):
    unflattened = {}
    for key in dictionary.keys():
        if "." in key:
            split_key = key.split('.')
            outer_key = split_key[0]
            inner_dict = {}
            for inner_key in split_key[1:]:
                inner_dict.update({inner_key: split_key[inner_key]})
            unflattened.update({outer_key: {dictionary[key]}})
    else:
        unflattened.update({key: dictionary[key]})
    return unflattened




'''
Problem 3: Write a function treemap to map a function over nested list.

>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]
'''


