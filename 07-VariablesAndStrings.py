#variables assignment -> no data type, data type is shown when assigning value

#variable naming restrictions and conventions
"""
1. variables must start with a letter or underscore, cant start by number!
2. cannot use special characters in the middle!
3. variables are case sensitives

"""


#variable naming conventions
"""
1. using snake case (ex: first_letter)
2. using lowercase, CAPITAL_CASE is just for constants!
3. UpperCamelCase refers to class
4. dunder -> double underscore are suppose to be private method (ex: __not_touch__)
"""

#DataTypes
"""
1. bool -> True or False values (ex: is_toggle_on = True)
2. int -> number without point of decimal (ex: 1,2,3,etc) (ex: num_of_chars =  3)
3. str -> sequence of unicode characters (Ex: "robin") (ex: first_name = "damenta")
4. list -> naming of array in Python (ex: collections_number = [1,2,3])
5. dictionary / dict -> naming of object in Python (key and value pairs) (ex: {"first_name" : "damenta"})
"""

#Dynamic Typing
"""
1. No strict rules to a variable, can switch into another data type just with reassign value of variables.
"""

#Special Value in Python -> NONE
"""
1. Similar to NULL in Javascript, to define emptyness on a variable.
2. When declaring variable explicitly must with value, so use None if still not knowing what value want to be assigned.
"""

#String Concatenation
"""
1. Combining multiple string together
2. adding string and number will causing error
"""

first_name = 'damenta'
last_name = 'ginting'

print('hello my name is',first_name,'and also',last_name)

#String Interpolation -> using f function
balls = 2
new_string = f"{first_name} and {last_name} have {2*3**3+5} balls"
print(new_string)

#Uppercase and Lowercase
"""
1. variables.upper() or variables.lower() -> only works on strings
"""

#Convert Data Types
"""
1. type(variables) -> return class of data type. using __name__ to return the name of data types.
2. str(8) -> to convert into string
3. int(99.3) -> to convert into integer
4. float(1) -> to convert into float
5. dont use reserve/built in function become variable names. (ex: str, int, float), it will overwrite the function
"""