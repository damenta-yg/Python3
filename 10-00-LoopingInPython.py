# for i in range(0,10):
#     print(i)

#for loops
"""
iterable object -> collections of items like list, strings, or range
if want to use index in for, use enumerate in the range / loop objects
enumerate is use for pythonic, clean, secure for indexerror, and can be started for special index start

"""


#range
"""
when create range do not forget using list.
after that range is start from zero if you do not initialize the first value
example : range(7) -> 0 to 6
range(1,8) -> 1 to 7
range(1,10,2) -> is 1 to 10, stepping up by 2
range(7,0,-1) -> is 7 to 1, stepping down by 1
"""

str = "Hello"
for index,character in enumerate(str):
    print(index, character)

x = list(range(7,-3,-2))
print(x)

for num in range(10,20):
    if(num % 2 != 0):
        print(num)