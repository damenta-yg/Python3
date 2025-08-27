def list_manipulation(list,method,position,value=0):
    if method == "remove":
        if position == "beginning":
            list.sort(reverse=True)
            return list.pop()
        else:
            return list.pop()
    elif method == "add":
        if position == "beginning":
            list.insert(0,value)
            return list
        else:
            list.append(value)
            return list


#print(list(list_manipulation([1,2,3],"a","b")))


x = [1,2,3,4,5]
#x.sort(reverse=True)
#print(x)
print(list_manipulation(x,"add","end",7))
