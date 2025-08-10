#Tuple
"""
definition: an ordered collection or grouping items -> immutable -> cannot be changed the value
numbers = (1,2,3,4)
2 in numbers -> return True
numbers[0] = "a" -> error  object does not support item assignment.

why using tuples?
-> faster than list, lighter weight for memory
-> it makes code safer because of cannot change the values
-> valid keys to use in dictionary

how to create tuples?
var_name = tuple(1,2,3,4,5)

looping in tuples is similar to list

Tuple Methods:
1. count -> x = (1,2,3,3,3) -> x.count(3) -> return 3
2. index -> returns the index at which a value is found in a tuple -> x.index(1) -> return 0


"""

numbers = (1,2,3,4)
#numbers[0] = 9
print(numbers)


#Sets
"""
sets are like formal mathematical sets.
sets do not have duplicate values
elements in sets are not ordered
cannot access items in a set by index
can be useful if you need to keep track of a collection of elements, but do not care about ordering, keys or values and duplicates

Set Methods:
Add -> adding new data into the set -> s = set([1,2,3,4]) -> a.add(5) -> return : s={1,2,3,4,5}
Remove -> removing value from the set -> s.remove(3) -> print(s) -> s={1,2,4,5} -> return error when there is no key that can be deleted
Discard -> removing value but theres is no error notifications -> s.discard(3)
Copy -> to copy a set onto another set -> s = set([1,2,3]) -> another_s = s.copy()
Clear -> To remove all elements on the set -> s.clear() -> return {}

Set Math
math_students = {"a","b","c","d","e","f"}
bio_students = {"d","e","g","h","i","f"}

| -> union -> returning element from set 1 and 2 and remove duplicates
& -> intersect -> returning the same element from 2 sets

math_students = {"a","b","c","d","e","f"}
bio_students = {"d","e","g","h","i","f"}

report_students = math_students | bio_students
report_students2 = math_students & bio_students
print(report_students2)

Set Comprehensions
==================

{x**2 for x in range(10)} -> return : {0,1,64,4,36,9,16,49,81,25} -> not in order


"""

new_sets = {(1,2),1,2,(1,2),3,4,1,2}
print(len(new_sets))


