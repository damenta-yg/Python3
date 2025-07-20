#Lists
"""
List is a collection or grouping of items.
Can contains more than 1 data types.
"""

#LengthOfLists
"""
drama = [1,2,3,4,5]
len(drama)
"""
drama = [1,2,3,4,5]
print(len(drama))


#Creating List With Range
"""
drama2 = list(range(1,10)) -> creating list from 1 to 9
print(drama2)
"""
drama2 = list(range(1,10))
print(drama2)


#Accessing List in Python
"""
List ALWAYS start counting at zero like Ranges. First element index is 0.
List is ordered data type, so order is matters.

drama3 = [1,2,3,4,5,6,7,8,9]
to access 9 in list is drama3[8]

Accesing values from the end is by using negative number
drama3 = [1,2,3,4,5,6,7,8,9]
to access 9 in list is drama3[-1]
"""
drama3 = [1,2,3,4,5,6,7,8,9]
print(drama3[len(drama3)-1])
print(drama3[-1])


#Check Values in List
"""
USING IN for the easiest ways!
friends = [1,2,3,4,5]
x = 2 in friends

returning True/False values

"""
friends = [1,2,3,4,5]
x = 2 in friends
print(x)


#List Methods: Append, Insert, and Extend
"""
.append() -> to add new data to the end of the list -> only can have 1 value per transaction
example: listmethodexample.append(1)

.extend() -> to add new data more than 1 data in list, by using list type.
example: listmethodexample.extend([1,2,3,4,5])

.insert() -> to add new data in the middle or elsewhere beside latest index
example: list.insert(index_want_to_insert,data_that_want_tobe_inserted)

"""
list_methods_example = [1,2,3,4,5,6]
list_methods_example.append(7)
print(list_methods_example)

list_methods_example.extend([8,9,10,12,"purple"])
print(list_methods_example)

list_methods_example.insert(-8,"New Items")
print(list_methods_example)


#List Methods: Clear, Pop, Remove
"""
.clear() -> remove all items from the list, no needed additional parameter
example: list_a.clear() -> results: []

.pop() -> remove the item at give position but if no index specified, remove and returns last items in the list
example: list_a.pop(4) // list_a.pop() 

.remove() -> remove the first item from the list whose value is specified on parameters.
and will throw a valueError if the item is not found.
example: list_a.remove(3)

"""

#list_methods_example.clear()
list_methods_example.pop(3)
print(list_methods_example)


#List Methods: Index, Count, Sort, Reverse, and Join
"""
.index() -> return the index of the specified item in the list
list_a = [1,2,3,4,5,4]
example: list_a.index(2) -> results: 1 ; list_a.index(4,2) -> results: 5 ; list_a.index(4,1) -> results: 3

.count() -> return the number of times x appears in the list
list_a = [1,2,3,4,5,4]
example: list_a.count(1) -> results: 1 ; list_a.count(4) -> results: 2

.reverse() -> reversing the items on the list from index 0 to end, vice versa.
example: list_a.reverse()

.sort() -> sorting the items of the list (ascending orders)
example: list_a.sort() -> [1,2,3,4,4,5]

.join() -> joining items on the list. but the connector is in front not like javascript.
example: list_a = ["Yohanes","Damenta"] -> ' '.join(list_a) -> "Yohanes Damenta"
example: list_a = ["Yohanes","Damenta"] -> '-'.join(list_a) -> "Yohanes-Damenta"

"""

#list_methods_example.clear()
item_index = list_methods_example.index('purple')
print(item_index)
print(list_methods_example)


#List Methods: Slicing
"""
Slicing is a proces making a new list using slices of the old list.

example: some_list[start:end:step]

first_list = [1,2,3,4]
first_list[1:] -> results: [2,3,4]
first_list[3:] -> results: [4]
first_list[-1:] -> results: [4]
first_list[-3:] -> results: [2,3,4]

"""
new_list_to_slice = [1,2,3,4,5,6,7,8,9,0]
slice_results = new_list_to_slice[1::2]
print(slice_results)

#Swapping Values
"""
names = ['A','B']
names[0], names[1] = names[1], names[0]
results = ['B','A']
"""