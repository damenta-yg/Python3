def isEven(num):
    return num % 2 == 0


def partition(list,func_name):
    truthy_return=[]
    falsy_return=[]
    for i in list:
        if func_name(i):
            truthy_return.append(i)
        else:
            falsy_return.append(i)
    return [truthy_return,falsy_return]
    

print(partition([1,2,3,4],isEven))