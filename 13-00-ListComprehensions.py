#General List Comprehensions
'''
List Comprehensions
===================

nums = [1,2,3]
[x*10 for x in nums]
return: [10,20,30]

name = 'colt'
[char.upper() for char in name]
return: ['C','O','L','T']

'''
nums = [1,2,3]
nums = [x*5 for x in nums]
print(nums)
print([x*10 for x in nums])


#List Comprehensions With Logics
'''
numbers = [1,2,3,4,5,6]
even_numbers = [num for num in numbers if num %2 == 0]
odd_numbers = [num for num in numbers if num %2 != 0]
tests = [num*2 if num % 2 == 0 else num/2 for num in numbers]


'''
nums = [1,2,3]
tests = [num*2 if num % 2 == 0 else num/2 for num in nums]
print(tests)
nums = [x*5 for x in nums]
print(nums)
print([x*10 for x in nums])

#Nested List
'''
nested_list = [[1,2],[3,4]]
nested_list[0][1] -> return: 2

board = [[num for num in range(1,4)] for val in range(1,4)]
return: [[1,2,3],[1,2,3],[1,2,3]]

board2 = [["X" if num%2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]
return: [['X','O','X'],['X','O','X'],['X','O','X']]

'''