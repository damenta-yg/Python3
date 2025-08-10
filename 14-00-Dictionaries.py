#Dictionaries
"""
1. Dictionary is a data structure that consist key value pairs
2. Structure:
    dictionaries = {
        "key": value,
    }
3. Can create dictionaries using dict function. Example: variables = dict(key="value", key2="value2")
"""

my_self = {
    "name": "Yohanes Damenta",
    "age" : 31,
    "jobs": "Software Engineer",
    "hobby": ["play","music","sports"],
    "isMarried": False
}

print(my_self)


#Iterating Dictionaries
for key, value in my_self.items():
    print(f"The key is {key} and the value is {value}")

results_test_key = "girlfriend" in my_self
print(results_test_key)

#Dictionary Methods
"""
clear -> removing all the keys and values from a dictionary
example: d = {a:1,b:2,c:3} -> d.clear() -> d= {}

copy -> copy object from 1 variables to other variables.
example: a= {a: 1, b:2} -> clone = a.copy() -> clone = {a: 1, b:2}

fromkeys -> creates key-value pairs from comma separated values
example = {}.fromkeys("a","b")

get -> retrieves a key in an object and return None instead of a KeyError if the key does not exist
example = dict.get(key) -> if there is no key in dictionary then returning None

pop -> takes a single argument corresponding to a key and remove the key-value pair from dictionary
    -> will return value to the key that was removed
example: d = dict(a=1,b=2,c=3) -> d.pop('a')

popitem -> removes a random key in a dictionary
example: d.popitem() -> will remove random key from dictionaries d.

update -> update key and values in a dictioonary with another set of key value pairs.
example -> first = dict(a=1,b=2) -> second = {} -> second.update(first) -> second = {a:1, b:2}

"""

clone_a = {}.fromkeys(["a","b"],2)
print(clone_a)


#Dictionary Comprehensions
"""
General Form: { _____:_____ for _____ in _____ }

Conditional Logic With Dictionaries
num_list = [1,2,3,4,5]
new_dict = {num : ("even" if num % 2 == 0 else "odd") for num in num_list}

"""

dict_result = {num : num ** 2 for num in [1,2,3,4,5,6]}
print(dict_result)

num_list = [1,2,3,4,5,6]
new_dict = {num : ("even" if num % 2 == 0 else "odd") for num in num_list}
print(new_dict)